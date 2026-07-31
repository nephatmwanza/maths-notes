# maths-notes

University mathematics and statistics course notes and worked past-paper problems,
written for Zambian students. Free to read.

**Not live yet.** This repository is the working source. The public name of the site is
still undecided — nothing here depends on it, and the repository can be renamed at any
time.

## Where the state lives

**[`STATUS.md`](STATUS.md) is the resumable record of this project.** Read it first —
what has been decided, what has been built, what is still open, and a reverse-chronological
log. It exists because power cuts here interrupt sessions; the conversation is lost, the
file is not.

## Layout

```
courses/<course>/source/   the LaTeX source - the thing that is actually edited
courses/<course>/build/    generated web pages (committed, so the site can be served)
site/index.html            course catalogue
site/assets/notes.css      the stylesheet for the notes
site/build.py              post-processor: theorem tagging, sidebar, nav, solutions
site/make-course.sh        build one course, end to end
site/assets/mathjax/       vendored MathJax 3.2.2 (Apache-2.0) - see its README
.viewport/                 screenshot harnesses for layout and overflow checking
```

## Building a course

```sh
site/make-course.sh courses/introduction-to-probability
```

That converts the LaTeX with `make4ht` and post-processes the result. **Both halves must
run together** — `build.py` rewrites pages in place and is not idempotent. It refuses to
run twice rather than nesting a second layout inside the first.

To preview, serve the repository root and open `site/index.html`:

```sh
python3 -m http.server 8000
```

## Checking a build

`.viewport/overflow-check.html` loads every generated page and reports anything a reader
would have to scroll sideways to see. It distinguishes real clipping from the two benign
cases — a display that scrolls in its own box, and an equation tag set in the right margin.

`.viewport/m390.html` renders a page in a 390px iframe. Use it rather than a small
`--window-size`: headless Chrome clamps its window to about 500px, so a narrow
`--window-size` produces a *cropped* wide render that looks like a mobile bug that is not
there.

## Content

The notes are the author's own. Reference material by other authors is read for coverage
and correctness only, never republished. Practice problems come from past papers and each
records where it came from.

Every numerical answer added is verified computationally — by exhaustive enumeration where
that is feasible — rather than by re-deriving it. Doing this has already turned up several
errors in the original notes; see the table in `STATUS.md`.
