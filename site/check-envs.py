#!/usr/bin/env python3
"""Audit LaTeX environment boundaries in a course source.

A clean compile proves nothing about whether environments close where the author
meant them to. If a `\\begin{proof}` is never closed, LaTeX will happily consume
whatever follows until some later `\\end{proof}` — one intended for a different
result — balances the count. The document compiles, and ten pages of definitions
and examples are silently typeset inside a proof.

This is not hypothetical. The Elements of Functional Analysis source had
thirteen of them; the largest swallowed 331 lines, including the Banach-space
definition and a worked example.

Two checks:

1. NESTING — `\\end{x}` must close the innermost open environment. Catches
   crossed pairs that a compile may still survive.

2. OVER-REACH — a result environment (proof, thm, defn, exa, ...) must not
   contain a sectioning command or another result declaration. That is the
   signature of a missing closer. `\\subhead` inside a proof or solution is
   deliberate house style and is not reported.

Usage:  site/check-envs.py courses/<course>/source/<file>.tex [...]
        site/check-envs.py courses/*/source/*.tex
"""

import re
import sys
from pathlib import Path

RESULT_ENVS = {"proof", "solution", "thm", "defn", "exa", "prop",
               "coro", "lem", "result", "exe", "note", "remark"}
# A declaration inside a result environment is the reliable signal. Sectioning
# commands are reported too, but \subhead is excluded: it is used inside proofs
# and solutions on purpose, to head the steps of an argument.
DECL_RE = re.compile(r"\\begin\{(thm|defn|exa|prop|coro|lem|result|exe)\}")
SECT_RE = re.compile(r"\\(?:sub)*section\*?\{")
ENV_RE = re.compile(r"\\(begin|end)\{([a-zA-Z*]+)\}")
# Everything from an unescaped % to end of line is a comment. Without stripping
# it, a commented-out \end{enumerate} is counted as real — which reported the
# whole of Introduction to Statistics as broken when it was not.
COMMENT_RE = re.compile(r"(?<!\\)%.*$")


def audit(path: Path) -> int:
    lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
    stack: list[list] = []
    problems: list[str] = []

    for n, raw in enumerate(lines, 1):
        line = COMMENT_RE.sub("", raw)
        for m in ENV_RE.finditer(line):
            name = m.group(2)
            if m.group(1) == "begin":
                stack.append([name, n, []])
            elif not stack:
                problems.append(f"  {n}: stray \\end{{{name}}} — nothing is open")
            elif stack[-1][0] != name:
                open_name, open_line, _ = stack[-1]
                problems.append(
                    f"  {n}: \\end{{{name}}} closes \\begin{{{open_name}}} "
                    f"opened at line {open_line}")
                stack.pop()
            else:
                frame = stack.pop()
                # A result declaration inside another result environment is the
                # reliable signal of a missing closer. A bare sectioning command
                # is not: Introduction to Probability heads the steps of its
                # worked solutions with \subsubsection, which renders as an
                # unnumbered heading and never reaches the sidebar. Flagging
                # those buried the one real defect in noise.
                decls = [(ln, w) for ln, w in frame[2] if w != "sectioning"]
                if decls:
                    where = ", ".join(f"{ln} ({what})" for ln, what in decls[:4])
                    more = "" if len(decls) <= 4 else f" and {len(decls) - 4} more"
                    problems.append(
                        f"  {frame[1]}-{n}: {frame[0]} spans {n - frame[1]} lines and "
                        f"contains {where}{more} — missing closer?")

        # Attribute intrusions to every enclosing result environment, skipping
        # the frame opened on this very line.
        hit = DECL_RE.search(line) or SECT_RE.search(line)
        if hit and stack:
            what = hit.group(1) if hit.re is DECL_RE else "sectioning"
            for frame in stack:
                if frame[0] in RESULT_ENVS and frame[1] != n:
                    frame[2].append((n, what))

    for name, line, _ in stack:
        if name != "document":
            problems.append(f"  {line}: \\begin{{{name}}} is never closed")

    if problems:
        print(f"{path}: {len(problems)} problem(s)")
        for p in problems:
            print(p)
    else:
        print(f"{path}: clean")
    return len(problems)


def main() -> int:
    paths = [Path(a) for a in sys.argv[1:]]
    if not paths:
        print(__doc__.strip().split("Usage:")[-1].strip(), file=sys.stderr)
        return 2
    return 1 if sum(audit(p) for p in paths) else 0


if __name__ == "__main__":
    sys.exit(main())
