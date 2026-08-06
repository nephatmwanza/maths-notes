#!/usr/bin/env bash
# Build one course from LaTeX source to finished web pages.
#
# The two halves must always run together on a clean directory: build.py
# rewrites the conversion output in place and is not idempotent, so running it
# over already-built pages would nest a second layout inside the first.
# Doing both here removes the chance of running one without the other.
#
# Usage: site/make-course.sh courses/introduction-to-probability

set -euo pipefail

course="${1:?usage: make-course.sh <course-dir>}"
course="$(cd "$course" && pwd)"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tex="$(ls "$course"/source/*.tex | head -1)"
name="$(basename "$tex")"

echo "==> converting $name"
rm -rf "$course/build"
mkdir -p "$course/build"
cp -r "$course"/source/. "$course/build/"

cd "$course/build"
# mathjax mode keeps maths as real text (selectable, searchable, screen-readable).
# The default SVG mode rasterises every formula - ~950 images with useless alt
# text on this document. "3" is the split level: one page per section.
# -interaction=nonstopmode matters more than it looks. Without it, a missing
# .sty leaves htlatex sitting at an interactive prompt and the build hangs until
# something kills it - ten minutes of apparently "still converting" for what is
# really a one-line error. The timeout is the backstop for anything else that
# blocks. The 5th positional argument is passed through to latex.
#
# 600s was too tight and silently truncated real builds. The probability notes
# run to ~300 pages and take around seven minutes alone; on a loaded machine, or
# straight after another course has been built, they went past ten minutes and
# were killed mid-conversion. Nothing was wrong with them. The timeout is meant
# to catch a hang, so it is set well clear of any legitimate build.
timeout 1800 make4ht -u -a debug "$name" "mathjax,3" "" "" "-interaction=nonstopmode" \
  > "$course/build/make4ht.log" 2>&1
status=$?
if [ $status -eq 124 ]; then
  echo "conversion timed out after 30 minutes - see $course/build/make4ht.log" >&2
  exit 1
fi

# A missing package is reported as an error but nonstopmode carries on, so the
# log has to be checked explicitly rather than trusting the exit code.
if grep -qE "^! LaTeX Error: File .* not found" "$course/build/make4ht.log"; then
  echo "missing LaTeX package:" >&2
  grep -E "^! LaTeX Error: File .* not found" "$course/build/make4ht.log" | sort -u >&2
  exit 1
fi

if grep -qE '^! ' "$course/build/make4ht.log"; then
  echo "LaTeX errors - see $course/build/make4ht.log" >&2
  grep -E '^! ' "$course/build/make4ht.log" | sort -u >&2
  exit 1
fi

echo "==> post-processing"
cd "$root"
python3 site/build.py "$course"

# A diagram that fails to convert leaves an <img> pointing at an .svg that was
# never written, so the page shows a broken image and nothing else complains.
# Counting the files produced does not catch it - the count simply comes out
# lower, and looks like a smaller document. Compare against what the HTML asks
# for instead. (Two F-distribution figures were missing this way for some time:
# tex4ht cannot convert TikZ `pattern=` fills, and those two still used one.)
python3 - "$course" <<'PYCHK'
import glob, os, re, sys
b = os.path.join(sys.argv[1], "build")
refs = set()
for f in glob.glob(os.path.join(b, "*.html")):
    refs |= set(re.findall(r"src=['\"]([^'\"]+\.svg)['\"]",
                           open(f, encoding="utf-8").read()))
have = {os.path.basename(x) for x in glob.glob(os.path.join(b, "*.svg"))}
missing = sorted(refs - have)
for m in missing:
    print(f"    WARNING missing diagram {m} - referenced by the HTML but never "
          f"produced. A TikZ `pattern=` fill is the usual cause.")
print(f"==> {len(glob.glob(os.path.join(b,'*.html')))} pages, "
      f"{len(have)} diagrams" + (f", {len(missing)} MISSING" if missing else ""))
PYCHK
