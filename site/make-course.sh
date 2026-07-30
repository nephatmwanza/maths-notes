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
make4ht -u -a debug "$name" "mathjax,3" > "$course/build/make4ht.log" 2>&1

if grep -qE '^! ' "$course/build/make4ht.log"; then
  echo "LaTeX errors - see $course/build/make4ht.log" >&2
  grep -E '^! ' "$course/build/make4ht.log" | sort -u >&2
  exit 1
fi

echo "==> post-processing"
cd "$root"
python3 site/build.py "$course"

echo "==> $(ls "$course"/build/*.html | wc -l) pages, $(ls "$course"/build/*.svg 2>/dev/null | wc -l) diagrams"
