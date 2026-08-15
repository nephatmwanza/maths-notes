#!/usr/bin/env python3
"""Convert hand-typed bold pseudo-headings into real theorem environments.

The older course sources declare no `\\newtheorem` at all. Every definition,
theorem and example is set as `\\textbf{Definition 2.3.1}\\\\` with the number
typed by hand, so LaTeX numbers nothing, nothing can be cross-referenced, and
inserting a result means renumbering the rest of the section by hand.

This rewrites those into `\\begin{defn} ... \\end{defn}` and lets LaTeX number
them. The hand-typed numbers are DISCARDED: the sources contain numbering
errors that only a real counter fixes (Linear Algebra numbers an example in
section 2 as "1.2.1", and skips 4.1.7-4.1.8 outright).

Why this is not a regex over the whole file. The heading tells you where a
result STARTS; nothing in the source says where it ends. The end has to be
inferred as "just before the next heading", and that inference is only safe at
a point where the file is structurally neutral -- not inside an `align*`, not
inside an `enumerate`, not inside a `$$...$$`, not inside an unclosed brace.
Closing an environment at a non-neutral point produces LaTeX that still
compiles surprisingly often and is silently wrong.

So the scanner tracks three things at once and refuses to act where any of them
is non-neutral:

  * environment depth  -- \\begin{...} / \\end{...}
  * brace balance      -- { } outside verbatim, ignoring \\{ \\}
  * math state         -- $ $$ \\[ \\] \\( \\)

and it asserts that every \\section / \\subsection line is reached at neutral
state. That assertion is the real safety net: if the tracker has drifted, a
sectioning command is where it shows, because those are unambiguously
top-level. Drift is reported and the file is left alone rather than half
converted.

Usage:
    python3 site/tex_env.py courses/linear-algebra/source/linear_algebra.tex
    python3 site/tex_env.py --dry-run <file>      # report only
"""

import re
import sys
from pathlib import Path

# Bold word -> environment name. Plurals appear in the sources ("Theorems
# 1.3.9", "Examples") and mean the same thing.
ENVS = {
    "Definition": "defn",
    "Definitions": "defn",
    "Theorem": "thm",
    "Theorems": "thm",
    "Example": "exa",
    "Examples": "exa",
    "Lemma": "lem",
    "Lemmas": "lem",
    "Proposition": "prop",
    "Propositions": "prop",
    "Corollary": "coro",
    "Corollaries": "coro",
    "Result": "result",
    "Remark": "remark",
    "Remarks": "remark",
    "Note": "note",
    "Notes": "note",
    "Proof": "proof",
    "Solution": "solution",
    "Solutions": "solution",
    # Complex Variables declares \newtheorem{exe}{Exercise}; the default is
    # only a fallback, since env_map_from_source() reads the real name.
    "Exercise": "exe",
    "Exercises": "exe",
}

# Environments that take no optional title and are not numbered.
UNTITLED = {"proof", "solution"}

# A heading line: nothing but \textbf{Word ...} and optional trailing \\ or \\\\.
# The number is matched so it can be thrown away; a parenthetical name is
# captured so it can become the optional argument of the environment.
#
# Two shapes occur across the sources and both are accepted:
#
#     \textbf{Definition 2.3.1}                 -- Linear Algebra, Linear Models
#     \textbf{\textcolor{red}{Example}}         -- Complex Variables
#
# The colour is discarded: it was carrying the meaning that the environment
# will carry properly once converted, and a red word is not a heading to a
# screen reader. A trailing colon is allowed and dropped, since
# `\textbf{\textcolor{blue}{Note:}}` and `\textbf{Note}` mean the same thing.
HEADING_RE = re.compile(
    r"""^\s*\\textbf\{\s*
        (?:\\textcolor\{[A-Za-z!0-9]+\}\{\s*)?   # optional colour wrapper
        (?P<word>[A-Za-z]+)          # Definition, Theorem, Proof, ...
        \s*
        (?P<num>[\d.]*)              # 2.3.1  -- discarded
        \s*:?\s*
        (?:\((?P<title>[^()]*)\))?   # (De Morgan's theorem) -- kept
        \s*:?\s*
        \}?                          # closes the colour wrapper, if present
        \s*\}
        \s*:?                        # a colon written outside the braces
        (?P<tail>(?:\s*\\\\)*)       # trailing \\ or \\\\
        \s*$""",
    re.VERBOSE,
)

NEWTHEOREM_RE = re.compile(
    r"\\newtheorem\*?\{(?P<env>[A-Za-z]+)\}(?:\[[A-Za-z]+\])?\{(?P<label>[^}]+)\}")


def env_map_from_source(text):
    """Map marker words to the environment names *this document* declares.

    The courses do not agree on names: Linear Algebra calls it `exa`, Complex
    Variables calls it `example`, and one of them also has `exe`. Hard-coding
    either produces \\begin{exa} in a document where only `example` exists,
    which fails at the far end of a ten-minute build.

    So the mapping is read from the file's own \\newtheorem declarations, whose
    second argument is the word actually printed. Anything the document does
    not declare falls back to the defaults, and `proof` is always available
    from amsthm.
    """
    declared = {}
    for m in NEWTHEOREM_RE.finditer(text):
        declared[m.group("label").strip().lower()] = m.group("env")
    out = {}
    for word, default in ENVS.items():
        key = word.rstrip("s").lower()
        out[word] = declared.get(key, declared.get(word.lower(), default))
    out["Proof"] = "proof"            # amsthm's, never redeclared
    return out


# NOT anchored to the start of the line, and that is the whole point. Complex
# Variables writes every one of its 82 sectioning commands as
# `{\color[wave]{485}\section{...}}`, so an anchored pattern matched none of
# them: the assertion below silently never fired, and no section acted as a stop
# for an environment. A conversion run under that pattern produced a `\section`
# nested inside a `proof`. Search the whole line.
SECTIONING_RE = re.compile(r"\\(?:sub)*section\*?\{")

# The last heading in a file has no following heading to stop it, so without
# this its \end lands after \end{document} and the document is reported as
# "ended by \end{document}" -- which reads like an unbalanced brace somewhere in
# 4,500 lines rather than what it is.
DOC_END_RE = re.compile(r"^\s*\\end\s*\{document\}")

# A line that is nothing but a bold phrase is a heading of SOME kind, even when
# it is not one of the marker words -- "Properties of Exponential Functions",
# "Laurent Series", "Poles". It therefore ends whatever block precedes it.
#
# Leaving these out is not a cosmetic slip. Complex Variables uses bold for its
# ordinary subheadings as well as for its Examples, so without this rule a
# converted Example ran on until the next *marker* word and swallowed entire
# subsections of exposition -- one block reached 200 lines and absorbed a
# heading, its prose and its displays.
BOLD_HEADING_RE = re.compile(
    r"^\s*\\textbf\{(?:\\textcolor\{[A-Za-z!0-9]+\}\{)?[^{}]*\}?\}\s*(?:\\\\)*\s*$")

# Lines the scanner must not read as content: the preamble defines \subhead
# with a \textbf inside it, and comments can contain anything.
VERBATIM_ENVS = {"verbatim", "lstlisting"}

# Environments that only affect alignment. A course may wrap its headings in
# one -- Functional Analysis writes every section as
#
#     \begin{center}\section{...}\end{center}
#
# -- and being inside one says nothing about whether the document is
# structurally at top level. Counting them made the drift assertion fire on all
# five sections of a perfectly balanced file and refuse to convert it. They are
# transparent for that check only; they still count when deciding where an
# environment may be closed.
FORMATTING_ENVS = {"center", "flushleft", "flushright"}


class State:
    """Structural state of the file at a line boundary."""

    def __init__(self):
        self.envs = []       # stack of open environment names
        self.braces = 0
        self.math = []       # stack of open math delimiters

    @property
    def neutral(self):
        return not self.envs and self.braces == 0 and not self.math

    def describe(self):
        bits = []
        if self.envs:
            bits.append("open environments: " + ", ".join(self.envs))
        if self.braces:
            bits.append(f"brace balance {self.braces:+d}")
        if self.math:
            bits.append("open math: " + ", ".join(self.math))
        return "; ".join(bits) or "neutral"


def strip_comments(line):
    """Drop a trailing LaTeX comment, respecting \\%."""
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i : i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def advance(state, line):
    """Update `state` for one line of LaTeX."""
    line = strip_comments(line)
    i = 0
    while i < len(line):
        c = line[i]

        if c == "\\":
            m = re.match(r"\\(begin|end)\s*\{([^}]*)\}", line[i:])
            if m:
                kind, name = m.group(1), m.group(2)
                if kind == "begin":
                    state.envs.append(name)
                elif state.envs and state.envs[-1] == name:
                    state.envs.pop()
                elif name in state.envs:
                    # Crossed nesting. Pop to it and keep going, but this is
                    # already a sign the file is not what we think it is.
                    while state.envs and state.envs.pop() != name:
                        pass
                i += m.end()
                continue
            if line[i : i + 2] == r"\[":
                state.math.append(r"\[")
                i += 2
                continue
            if line[i : i + 2] == r"\]":
                if state.math and state.math[-1] == r"\[":
                    state.math.pop()
                i += 2
                continue
            if line[i : i + 2] == r"\(":
                state.math.append(r"\(")
                i += 2
                continue
            if line[i : i + 2] == r"\)":
                if state.math and state.math[-1] == r"\(":
                    state.math.pop()
                i += 2
                continue
            # \{ \} \$ \\ and every other escape: consume both characters so
            # the brace and math counters never see an escaped delimiter.
            i += 2
            continue

        if state.envs and state.envs[-1] in VERBATIM_ENVS:
            i += 1
            continue

        if c == "$":
            tok = "$$" if line[i : i + 2] == "$$" else "$"
            if state.math and state.math[-1] == tok:
                state.math.pop()
            elif tok == "$" and state.math and state.math[-1] == "$$":
                # A single $ inside $$...$$ is content, not a delimiter.
                pass
            else:
                state.math.append(tok)
            i += len(tok)
            continue

        if not state.math:
            if c == "{":
                state.braces += 1
            elif c == "}":
                state.braces -= 1
        i += 1
    return state


def convert(text, path_label="<file>"):
    lines = text.split("\n")
    envmap = env_map_from_source(text)

    # ---- pass 1: structural state at the start of every line ---------------
    # The preamble is skipped: it legitimately contains \textbf inside a macro
    # definition, and its brace state is not the body's business.
    try:
        body_start = next(
            i for i, l in enumerate(lines) if l.strip() == r"\begin{document}"
        ) + 1
    except StopIteration:
        body_start = 0

    state = State()
    at = [None] * len(lines)
    problems = []
    for i in range(body_start, len(lines)):
        at[i] = (list(state.envs), state.braces, list(state.math))
        structural = [e for e in state.envs if e not in FORMATTING_ENVS]
        if SECTIONING_RE.search(lines[i]) and (
            structural or state.braces or state.math
        ):
            problems.append(
                f"{path_label}:{i+1}: sectioning command reached at non-neutral "
                f"state ({state.describe()}) -- the scanner has drifted, or the "
                f"source is unbalanced. Nothing was converted."
            )
        advance(state, lines[i])

    if problems:
        return None, problems, {}

    def neutral_at(i):
        envs, braces, math = at[i]
        return not envs and braces == 0 and not math

    # ---- pass 2: find headings --------------------------------------------
    heads = []
    for i in range(body_start, len(lines)):
        m = HEADING_RE.match(lines[i])
        if not m:
            continue
        word = m.group("word")
        if word not in ENVS:
            continue
        if not neutral_at(i):
            # A bold word inside a table cell or a list is a label, not a
            # heading. Leave it alone and say so.
            envs, braces, math = at[i]
            problems.append(
                f"{path_label}:{i+1}: '{word}' looks like a heading but sits "
                f"inside {envs or 'braces/math'} -- left as bold text."
            )
            continue
        heads.append((i, envmap[word], m.group("title")))

    if not heads:
        return None, problems + ["no headings found"], {}

    # ---- pass 3: choose an end line for each heading ------------------------
    # The body runs to just before the next heading or sectioning command.
    # Trailing blank lines are excluded so the \end lands against the content
    # rather than several blank lines below it.
    stops = sorted(
        {i for i, _, _ in heads}
        | {
            i
            for i in range(body_start, len(lines))
            if SECTIONING_RE.search(lines[i])
            or DOC_END_RE.match(lines[i])
            or BOLD_HEADING_RE.match(lines[i])
        }
        | {len(lines)}
    )

    inserts = {}   # line index -> text to insert BEFORE that line
    replace = {}   # line index -> replacement text
    counts = {}
    for n, (i, env, title) in enumerate(heads):
        stop = next(s for s in stops if s > i)
        end = stop
        while end - 1 > i and not lines[end - 1].strip():
            end -= 1
        # The end must land at a neutral boundary. If it does not, the body
        # runs into something unbalanced and the environment is not closed
        # here; report it rather than emitting broken LaTeX.
        if end < len(lines) and not neutral_at(end):
            problems.append(
                f"{path_label}:{i+1}: body of {env} does not end at a neutral "
                f"boundary (line {end+1}) -- left unconverted."
            )
            continue
        if env in UNTITLED:
            open_tag = f"\\begin{{{env}}}"
        elif title:
            open_tag = f"\\begin{{{env}}}[{title.strip()}]"
        else:
            open_tag = f"\\begin{{{env}}}"
        replace[i] = open_tag
        inserts.setdefault(end, []).append(f"\\end{{{env}}}")
        counts[env] = counts.get(env, 0) + 1

    # ---- pass 4: emit ------------------------------------------------------
    out = []
    for i, line in enumerate(lines):
        for tag in inserts.get(i, []):
            out.append(tag)
        out.append(replace.get(i, line))
    for tag in inserts.get(len(lines), []):
        out.append(tag)

    return "\n".join(out), problems, counts


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    path = Path(args[0])
    text = path.read_text()
    result, problems, counts = convert(text, path.name)

    for p in problems:
        print("  " + p)
    if result is None:
        print("REFUSED: nothing written.")
        return 1

    for env, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:4d}  {env}")
    print(f"  {sum(counts.values()):4d}  total")

    if dry:
        print("dry run -- nothing written.")
        return 0

    path.write_text(result)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
