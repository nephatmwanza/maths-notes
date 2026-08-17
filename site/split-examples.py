#!/usr/bin/env python3
"""Split multi-part examples whose solutions are interleaved inside the list.

Several of these sources write a multi-part example as

    \\textbf{Example}
    Evaluate the integrals
    \\begin{enumerate}
    \\item  <question 1>
    \\textbf{Solution}
    <working 1>
    \\item  <question 2>
    \\textbf{Solution}
    <working 2>
    \\end{enumerate}

so a reader meets the answer to part 1 before reaching the question for part 2.
This rewrites each such block as a numbered example holding the whole question,
followed by one solution holding the whole working, with each part labelled.

It also unblocks `tex_env.py`, which refuses these blocks: the example cannot be
closed at a neutral point because the closing brace of the list sits between the
heading and the end of its body.

Refusal is the feature. Any block whose shape does not match is reported and
left alone rather than guessed at.

Two heading conventions appear across the courses and both are accepted:

    \\textbf{Example}                      (Analytic Geometry)
    \\textbf{\\textcolor{red}{Example}}     (Advanced Calculus)

Verify afterwards that nothing was lost. The transform only ever moves lines, so
the multiset of non-empty lines, ignoring the markers it removes and the
environment delimiters it adds, must be identical before and after.

Usage:
    python3 site/split-examples.py <file.tex>            # report only
    python3 site/split-examples.py <file.tex> --write
"""
import re
import sys
from pathlib import Path

# The optional colour wrapper, and the brace that closes it.
_C = r"(?:\\textcolor\{[A-Za-z!0-9]+\}\{)?"
_E = r"\}?"

HEAD = re.compile(r"\\textbf\{" + _C + r"Examples?" + _E + r"\}\s*(?:\\\\)*\s*$")
SOL = re.compile(r"^\s*\\textbf\{" + _C + r"Solutions?" + _E + r"\}\s*[.:]?\s*(?:\\\\)*\s*$")
STOP = re.compile(r"\\(sub)*section\*?\{|^\s*\{?\\?\w*\\?textbf\{" + _C +
                  r"(Example|Definition|Theorem|Exercise|Proof|Note)")

OPEN = ("\\begin{enumerate}", "\\begin{itemize}")
CLOSE = ("\\end{enumerate}", "\\end{itemize}")


def depth_delta(line):
    return sum(line.count(o) for o in OPEN) - sum(line.count(c) for c in CLOSE)


def top_level_items(body):
    """Split an enumerate body into chunks at depth-0 \\item."""
    chunks, cur, depth = [], [], 0
    for line in body:
        if re.match(r"\s*\\item\b", line) and depth == 0:
            if cur:
                chunks.append(cur)
            cur = [line]
        else:
            if not cur:
                cur = []
            cur.append(line)
        depth += depth_delta(line)
    if cur:
        chunks.append(cur)
    return chunks


def convert(path, write=False):
    lines = Path(path).read_text().split("\n")
    heads = [i for i, l in enumerate(lines) if HEAD.search(l.strip())]
    edits, refused = [], []

    for h in heads:
        # The block ends at the next stop that is itself at depth 0. A bold
        # heading inside a list belongs to this example, not the next one.
        j, d = h + 1, 0
        while j < len(lines):
            if d == 0 and STOP.search(lines[j]):
                break
            d += depth_delta(lines[j])
            j += 1
        span = j

        b, d = None, 0
        for k in range(h + 1, span):
            if d == 0 and lines[k].strip().startswith(OPEN):
                b = k
                break
            d += depth_delta(lines[k])
        if b is None:
            continue

        depth, e = 0, None
        for k in range(b, span):
            depth += depth_delta(lines[k])
            if depth == 0:
                e = k
                break
        if e is None:
            refused.append((h + 1, "list is not closed inside the block"))
            continue

        inner = lines[b + 1:e]
        if not any(SOL.match(l) for l in inner):
            continue

        stem = lines[h + 1:b]
        chunks = top_level_items(inner)
        if not chunks or not chunks[0][0].lstrip().startswith("\\item"):
            refused.append((h + 1, "list does not begin with an item"))
            continue

        questions, solutions = [], []
        for n, chunk in enumerate(chunks, 1):
            cut = next((x for x, l in enumerate(chunk) if SOL.match(l)), None)
            if cut is None:
                questions.append(chunk)
                continue
            questions.append(chunk[:cut])
            work = list(chunk[cut + 1:])
            while work and not work[0].strip():
                work.pop(0)
            while work and not work[-1].strip():
                work.pop()
            if work:
                solutions.append((n, work))
        if not solutions:
            refused.append((h + 1, "no solution body recovered"))
            continue

        new = ["\\begin{exa}"]
        new += [l for l in stem if l.strip()]
        new.append("\\begin{enumerate}")
        for q in questions:
            qq = list(q)
            while qq and not qq[-1].strip():
                qq.pop()
            new += qq
        new += ["\\end{enumerate}", "\\end{exa}", "", "\\begin{solution}"]
        multi = len(solutions) > 1
        for n, work in solutions:
            if multi:
                new.append("\\subhead{Part %d}" % n)
            new += work
            new.append("")
        while new and not new[-1].strip():
            new.pop()
        new.append("\\end{solution}")
        edits.append((h, e + 1, new, len(questions), len(solutions)))

    print("convertible blocks: %d   refused: %d" % (len(edits), len(refused)))
    for ln, why in refused:
        print("   line %d: %s" % (ln, why))
    for h, e, new, nq, ns in edits:
        print("   line %d: %d questions, %d solutions" % (h + 1, nq, ns))

    if write:
        for h, e, new, nq, ns in sorted(edits, key=lambda z: -z[0]):
            lines[h:e] = new
        Path(path).write_text("\n".join(lines))
        print("written.")
    else:
        print("dry run -- nothing written.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        sys.exit(__doc__)
    convert(args[0], write="--write" in sys.argv)
