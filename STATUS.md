# Interactive Notes Web App — Project Status

**This file is the resumable state of this project.** If a session gets cut off (power cut,
closed terminal, anything), load this file first — it is the record of what has actually
happened, not the conversation history. Read top to bottom, then jump to the most recent
entry in the Status Log at the bottom.

This is a **separate project** from the Zambia climate-extremes work
(`Zambia_Climate_Extremes` / `Zambia_Temperature_Extremes` / `Zambia_CMIP6_Evaluation` /
the portfolio site). Nothing here should be mixed into those repos.

**Folder name is provisional.** `/home/corban/LaTeX_WebApp` — rename any time, nothing
depends on this exact path yet.

---

## What this is

Turning the user's own LaTeX teaching materials into an interactive web app. Source
material lives at `/home/corban/LaTeX_Projects` — NOT inside this project folder, and not
copied yet. That directory holds:

- **61 authored `.tex` documents** — the user's own lecture notes and course material,
  spanning most of the pure-maths/statistics curriculum: Real Analysis, Linear Algebra,
  Topology, Probability Theory, Non-Parametric Methods, Design of Experiments, Time Series,
  Functional Analysis, Stochastic Processes, and more. Many topics have a paired "Notes"
  folder and an "Exam Questions" folder.
- **Reference material that is NOT the user's own work**, sitting in some of the same
  folders — downloaded textbooks (e.g. Casella & Berger) and other people's notes (MIT OCW
  slides, a PDF titled "Dr Nawas", a file literally named "Document from Jeshurun Mwanza").

## Scope rule — settled, refined 2026-07-30 (see log)

**Only the user's own authored content goes on the platform** — but "authored" now means
*originally written or reconciled by the user*, not necessarily identical to the existing
61 `.tex` files verbatim. See "Content reconciliation process" below: some course notes
need to be rewritten/simplified from multiple existing sources, not just converted as-is.
The reference PDFs from other authors (Dr Nawa, textbooks, MIT OCW, etc.) are **never
republished directly** — they are read for coverage/correctness only, never copied.

## Current phase

**BUILDING — started 2026-07-30.** User confirmed: start now with the two probability
courses (Introduction to Probability, Probability Theory); Mat1110 and Introduction to
Statistics material expected from the user "by next week." First technical step is
testing LaTeX-to-web conversion on real content (Introduction to Probability, the
no-conflict course) before committing to a tech stack — see log for findings.

## Decisions (settled 2026-07-30)

1. **Audience: local Zambian system** — UNZA and other Zambian institutions specifically.
   Not international, not a generic public resource. This is a deliberate narrowing.
2. **Interactivity: both**, not either/or —
   - a clean **searchable/browsable notes** side, AND
   - a **quiz/problem engine** built from solved exam questions.
3. **Rollout: free first, paid is the actual goal.** Launch free while the mechanism is
   being built and while students discover it exists; convert to paid once it has traction.
   The user has said the paid model is "something we will go over and over" — i.e. do not
   over-plan monetisation mechanics now, but do not architect anything that would make
   adding payment/gating later gratuitously hard.
4. **Scope is broader than the 2 current courses, and the timeline is relaxed.** User
   wants more courses showcased at launch to help build an audience, not just Mat1110 and
   Introduction to Statistics — draw on the wider ~30-topic library already in
   `LaTeX_Projects` (Real Analysis, Linear Algebra, Probability Theory, Time Series,
   Design of Experiments, etc.), reconciled per the process above. **No rush: the user
   explicitly said it is fine to go live at the end of the semester.** This supersedes the
   earlier Monday-deadline framing — Monday matters for the user's own teaching, not for
   the platform.

## Content reconciliation process — the standing rule for EVERY course, not a one-off

**Confirmed 2026-07-30: this applies uniformly as more courses are added over time, not
just to Probability Theory.** The user's own framing: "combine so that at the same time we
own the material as we [keep] adding more and more." Read as: growth in course count must
not outpace ownership — every course added, however many there eventually are, goes
through the same combine-and-own step before publishing, never a shortcut conversion of
someone else's material. This is a deliberate constraint on the pace of growth: a course
is not "added" until it has been synthesised into original material, however long that
takes for that particular course.

**Why this matters.** In the Zambian university system, lecturers/tutors teaching
different sections of the *same* course are expected to teach broadly the *same* content,
for fairness across sections. That is why the user's folders contain other people's
material (e.g. "Dr Nawas.pdf") alongside his own — those are the shared/departmental
reference notes for courses he also teaches, not random downloads.

**The risk this creates for the platform:** if the site's notes for a course omit
something another section's students are taught, or present it differently, that is a
real conflict for a student comparing the site against their own lecturer — not just a
copyright problem.

**The process going forward, per course, before writing any web content:**
1. Treat the user's own `.tex` notes as the primary draft.
2. Treat the departmental/shared material (Dr Nawa or equivalent) as a **coverage
   checklist** — what must be included so no section's student is missing something —
   never as text to copy.
3. Where the user's own notes are thin against that checklist, **write new original
   material** to close the gap (textbooks like Casella & Berger may be consulted for
   correctness, never copied).
4. The result per course is **one clean, simplified, original synthesis** — a superset of
   what any section teaches, in the user's own words, so no student is contradicted by it.

This is materially more work than "convert existing tex to html" for courses where the
user's own notes are not already the most complete version. Budget for it accordingly when
picking the first course.

## Course reference — corrected 2026-07-30, do not re-guess this

**UNZA's foundation maths courses are three separate courses by faculty, not variants of
one thing** (an earlier guess in this file wrongly conflated them — corrected):
- **MAT1100** — Engineering and Natural Sciences
- **MAT1110** — Humanities (= "Foundation Mathematics and Statistics for Social Sciences",
  the one the user tutors). **The "Foundation Mathematics" folder in `LaTeX_Projects` is a
  DIFFERENT course for different learners — do not use it for Mat1110.**
- **MAT1120** — Health Sciences

**Mat1110 content is on hold until the user supplies this semester's actual material** —
do not build from the existing `Mat1110.tex` (Jan 2026) without checking with the user
first, since he is writing fresh notes for this course this semester.

**Two courses inspected in detail as worked examples of the reconciliation problem, while
Mat1110/Intro Stats material is pending:**

- **Introduction to Probability — LOW CONFLICT, good candidate to start on now.**
  `Introduction To Probability.tex` (Jan 2026) is the user's own, complete, well-structured
  notes (2 chapters seen in the ToC: probability axioms/Bayes/counting; random variables
  and distributions incl. PGFs/MGFs). A matching `Introduction To Probability Exam
  Questions.tex` (2020) exists as the question-bank half. User's comment: this 2026
  version "is what was done last semester... often the notes they don't even change them"
  — i.e. treat as current/usable, not stale. **No competing departmental version found for
  this course** — unlike the cases below, this one may not need the reconciliation process,
  only conversion.

- **Probability Theory (MAT 3902) — HIGH CONFLICT, a second Dr-Nawa-style case.** Two
  versions exist:
  - the user's own `PROBABILITY THEORY` (2020, in `LaTeX_Projects`) — his authored notes.
  - `Probality_Theory_Notes/MAT 3902 Probability theory.ver6.pdf` (Dec 2025) plus three
    2024 tutorial sheets — reads as the **departmental/currently-used version** ("ver6"
    versioning, recent tutorial sheets attached). User's own words: "there is that I did
    and the one they be using this time" — confirming the ver6 PDF is what is actually
    taught now, not his 2020 version. **This is exactly the reconciliation-process case**:
    his notes as draft base, the ver6 PDF as the coverage checklist, original synthesis as
    the output — never copy the ver6 PDF directly.

## Technical decision — CONFIRMED by testing on real content, 2026-07-30

**LaTeX-to-HTML conversion tool: `make4ht`, in `mathjax` build mode** (i.e.
`make4ht -u -a debug file.tex "mathjax"`), NOT the default `svg` mode.

**Why `svg` mode was rejected:** it rasterises every math expression into a separate image
(948 images for one document), with meaningless alt text (e.g. `"M(ME)-"` for a fraction).
That would make the notes unsearchable and inaccessible — directly against the searchable-
notes requirement.

**Why `mathjax` mode was chosen, and how it was verified — not assumed:** run on the real
Introduction to Probability document (195 KB source, 64 real TikZ diagrams, 182 theorem/
definition/example/remark blocks) rather than a toy file. Result: only 33 images (the real
diagrams), all other math left as live text for MathJax to render client-side. Manually
inspected several full content pages (rendered in headless Chrome, screenshotted, read):
- Tree diagrams and set-mapping diagrams (TikZ/xy-pic) render correctly as images.
- Dense multi-line derivations (variance proofs, PGF/MGF work, integrals, sums) render
  correctly throughout — this was checked over several pages of continuous content, not
  a single cherry-picked example.
- Tables (probability distributions, comparison tables) render cleanly as HTML tables.
- Chapter/section navigation and the linked table of contents work.

**UPDATE 2026-07-30, later: both suspected "issues" above were mis-diagnosed on first
pass — root-caused and FIXED properly, not worked around:**
1. **The `\includegraphics` call is commented out in the source** (`%\includegraphics...`,
   a logo, never active) — there was never a missing external image. False alarm.
2. **The "garbled math" was actually a broken diagram, not math**, and the real cause was
   found: three `tikzpicture`s use `pattern=dots` fills
   (`\path[pattern=dots,...]`/`\draw[pattern=dots...]`), which `tex4ht` silently fails to
   convert to SVG even though the figure compiles to PDF without any LaTeX error — a
   narrow tex4ht limitation on that one fill style, not a math-rendering problem. **Fixed
   by replacing the dot-pattern fills with a plain light solid fill** (`fill=blue!12`) at
   all three locations in the working copy — a legitimate style call, not a workaround,
   and arguably clearer for students than a dot pattern anyway. Also corrected a real typo
   found while in there: `\begin{tikzpicture}[=>stealth]` (invalid option syntax) →
   `[->,>=stealth]`, six occurrences.
- **Result: the full document now converts and renders with zero remaining defects.**
  36 diagrams (up from 33 once the three fixed ones were included), all visually verified;
  the previously-broken shaded-region figure (Example 2.3.4) now renders as a correct,
  clean trapezoid with proper axis labels. Working copy with both fixes lives at
  `courses/introduction-to-probability/source/intro_prob.tex`; converted output at
  `courses/introduction-to-probability/build/intro_prob.html` — **open that file in a
  browser to see the actual result.**
- **Practical consequence, revised:** the earlier conclusion that "every document needs a
  manual proofreading pass" still stands as good practice, but the specific defect found
  here was a fixable authoring bug (an unsupported fill style), not an inherent tool
  limitation to work around forever. Worth checking new documents for the same
  `pattern=...` fill styles specifically.

**This resolves half of what was open question 6.** The conversion/content pipeline is now
proven. The site-framework/hosting half (Hugo+PaperMod+Fuse.js vs something else) is still
undecided and not urgent — it can wrap around this HTML output regardless of which
framework is chosen.

## Project folder structure (established 2026-07-30)

```
LaTeX_WebApp/
  STATUS.md
  courses/
    introduction-to-probability/
      source/   the working .tex (with fixes applied) + original .pdf/.toc — NOT the
                 pristine original, which stays untouched in LaTeX_Projects
      build/    make4ht output: intro_prob.html + 36 svg diagrams + css
```
One `courses/<slug>/{source,build}` pair per course going forward.

## User instructions on approach (recorded 2026-07-30, apply to all future content work)

- **Build first, then react** — the user explicitly prefers seeing a concrete result over
  more up-front planning: "I would rather build then from there it easy to see."
- **Editorial licence granted**: free to rearrange, add clarifying examples, and simplify
  — not a mechanical conversion. Also free to look at how the department structures its
  own material (e.g. the ver6 Probability Theory PDF) and follow that where it works well
  — they have more institutional experience with what Zambian students need.
- **Voice/approach: write as an experienced educator**, prioritising clarity for the
  learner over fidelity to the original wording.
- **A "window to ask questions"** — a Q&A/discussion feature — was raised as a possible
  addition. Not scoped or committed; logged here so it isn't lost, revisit once there is
  real usage to design it around.
- **User will observe real student behaviour once this is live** and feed that back —
  i.e. this is explicitly expected to be iterated on after launch, not perfected upfront.

## Design research — real precedents, checked 2026-07-30

The user asked to look at how strong online maths courses do this rather than invent it.
Three findings, all now driving concrete decisions:

**1. Paul's Online Notes (`tutorial.math.lamar.edu`)** — the closest precedent that exists:
one professor's own LaTeX lecture notes turned into a widely-used free maths site. Its
structure is being copied deliberately:
- **A dedicated page per section**, not one long scrolling document.
- A persistent expandable sidebar showing the whole course tree, so a learner can jump
  anywhere.
- **"Notes" and "Practice Problems" kept as separate parallel sections** — which maps
  exactly onto the notes + quiz-engine split already decided here.
- Next/previous navigation at the foot of each page; download options.

**2. Brilliant.org** — for the quiz interaction pattern specifically:
- **Progressive reveal**: answers/steps hidden behind a click rather than shown alongside.
- Practice sets are deliberately **low-stakes**, and scaffolding (hints, worked steps) is
  progressively removed as the learner is tested on independent ability.
- This is directly relevant to open question 5 and suggests the answer is "both": a
  searchable bank of solved problems, where the solution is behind a reveal rather than
  visible by default.

**3. giscus (`giscus.app`)** — answers the user's "window to ask questions" request:
- A commenting/discussion widget backed by **GitHub Discussions**. Free, open source, no
  ads, no tracking, actively maintained (the older `utterances` is largely unmaintained).
- **No backend, no database, no accounts to build** — it fits the free-phase constraint
  exactly, and can sit at the foot of every section page so questions attach to the
  specific topic rather than a general forum.
- Caveat to confirm with the user later: commenters need a GitHub account, which is a real
  barrier for Zambian students. Fine for the free/early phase; revisit when the paid phase
  brings real user accounts.

## MIT OpenCourseWare — catalogue/index design, reviewed 2026-07-30

User pointed at `ocw.mit.edu/search/?t=Mathematics`. Rendered and inspected it (the page is
JS-driven, so it needs a real browser, not a plain fetch). It is the best available model
for the **course index / catalogue page** — the thing this project does not have yet.

**Worth copying now:**
- **Course cards**, one per course, each carrying: course code + level on one line in a
  coloured small-caps style (`18.900 | UNDERGRADUATE`), bold title, instructor, **topic
  tags as pill chips**, and a **thumbnail image** on the right.
- **Level as a first-class label.** Maps naturally onto UNZA numbering, where the first
  digit already encodes year: MAT1110 → first year, MAT2901 → second year, MAT3902 →
  third year. Free structure, already present in the course codes.
- **Topic tags** (`Mathematics`, `Probability and Statistics`, `Algebra and Number
  Theory`), with a `+3 more` overflow rather than an unbounded row.
- **Thumbnails.** MIT uses a small figure per course. **This project can generate these
  free** — the converted notes already contain 36 SVG diagrams; one good figure per course
  makes an honest, subject-specific thumbnail at zero cost.
- **Prominent search at the top**, above the results, not tucked in a corner.

**Deliberately NOT copying yet, and why:**
- **The faceted filter sidebar** (Departments / Level / Topics / Features, each with result
  counts). MIT is filtering **330 courses**; this project has **one**. Filters over one to
  three items are noise, not navigation. Revisit at roughly 10+ courses.
- **COURSES / RESOURCES tabs** and the list/grid view toggle — same reason, premature.
- **Sort-by-relevance dropdown** — meaningless until there are enough courses to sort.

**Tension worth resolving with the user (raised, not yet decided).** The user asked to drop
the course code from the title page, reasoning that going online means not tying the
material to one university. That is right for the *title*. But Zambian students very
likely **search by course code** — "MAT1110" is exactly what a UNZA student types. MIT
keeps the code visible on every card for precisely that reason. Suggested resolution: keep
the code **out of the title/heading** but **in the searchable metadata and card label**
(e.g. a tag, or an "also known as" line), so the page stays a general resource while still
being findable by the students it is for. Cheap to do, and it protects discoverability
without undoing the depersonalisation.

## Multi-page output — SOLVED, no custom build needed

`make4ht` splits automatically by depth: `make4ht -u -a debug file.tex "mathjax,3"`.
Verified on the real document: **22 pages** — one per numbered section, plus chapter pages
and a contents page. Confirmed working: the table of contents links each entry straight to
its own page, and every section page carries automatic `next / prev / up` navigation. This
is exactly the Paul's-Notes structure, for free, out of the tool.
- `,2` = split at chapter level (3 pages) — too coarse.
- `,3` = split at section level (22 pages) — **chosen**.

## Open questions

5. **Exact quiz interaction model.** User said: "solve the questions and put them in the
   engine where learners have to search for themselves" — read as: worked solutions exist
   in the system, but the interaction requires the learner to search/attempt rather than
   being handed the answer passively. Needs confirming whether that means (a) an
   attempt-first-then-reveal quiz flow, (b) a searchable bank of solved problems the
   learner browses/searches directly, or (c) both.
6. **Site framework/hosting** (separate from the now-proven conversion tool above). Leaning
   towards reusing the pattern already proven on the climate portfolio site — Hugo +
   PaperMod with its client-side Fuse.js search — for the notes side, plus a lightweight
   client-side quiz component (question/answer data in JSON, no backend) for the engine
   side. Not committed — worth confirming before building the real site shell.

## How to resume this project cold

1. Read this file top to bottom.
2. Check the Status Log below — the most recent entry is where things actually left off.
3. Once there is code: check `git log` in this directory for the detailed history.
4. Do not assume anything happened that isn't recorded here or in git — if it's not
   written down, treat it as not done yet.

---

## Status Log

*(most recent first — append new entries, never rewrite old ones)*

### 2026-07-30 (latest) — Book-quality presentation: build pipeline, house diagram style, self-hosted maths

User's brief: *"make things look beautiful, you free to change things work diagrams make
them uniform, like a proper book… you can use also those from the department to fill in.
Have not yet gone live. We are looking at things so be free."*

**The build is now one command.** `site/make-course.sh <course-dir>` converts the LaTeX and
post-processes it in a single step:

```
site/make-course.sh courses/introduction-to-probability
```

It wipes `build/`, runs the same stock `make4ht -u -a debug <file>.tex "mathjax,3"` as
before, fails loudly on LaTeX errors, then runs `site/build.py`. **The two halves must
always run together** — `build.py` rewrites pages in place and is *not* idempotent. It now
refuses to run twice (marker comment + non-zero exit) and warns on unbalanced `<div>`s.

**`site/build.py` — what the post-processor does.**
1. **Tags theorem blocks by type.** This was the single biggest win. tex4ht marks
   Definition, Theorem, Lemma, Example and Remark all as `class='newtheorem'`, so they
   render identically. The type is only recoverable from the bold label text, so the
   script reads it and adds `nt-definition`, `nt-theorem`, … Colour-coding follows in CSS.
2. **Injects a persistent sidebar** (course tree parsed from the generated contents page,
   current page highlighted) into all 22 pages — the Paul's Online Notes pattern.
3. **Wraps content** in the `.layout` / `.content .inner` shell.
4. **Replaces** tex4ht's bare `[next][prev][up]` row with a styled footer nav.
5. **Adds a Q&A block** — *section pages only*; the title/chapter/contents pages have no
   topic to ask about and an empty thread on each would look abandoned.
6. **Repoints MathJax at a local copy** (see below).

**`site/assets/notes.css`** — serif body at a 36rem measure, sans chrome, colour-coded
theorem blocks, quiet proofs, styled contents page, mobile drawer, full dark mode.
One trick worth remembering: several theorems carry their proofs *inside* the environment,
which turned the tinted panel into a page-long field of colour. `.newtheorem:has(.proof)`
drops the fill and keeps only the coloured rule and label — statement then proof, the way
a book sets it.

**Self-hosted MathJax — this one matters for the actual audience.** tex4ht hardcodes
`cdn.jsdelivr.net`. A headless screenshot caught the consequence: with a short load budget
the page renders *upright, mis-spaced* maths until ~1MB of third-party JS and fonts
arrive. That is exactly what a student on slow Zambian mobile data would stare at.
MathJax 3.2.2 (`tex-chtml-full.js` + all woff-v2 fonts, **1.7MB total**) now lives in
`site/assets/mathjax/`. Verified by re-rendering with *every external host blocked*
(`--host-resolver-rules="MAP * 0.0.0.0, EXCLUDE 127.0.0.1"`): output was byte-identical to
the online render. The site now works offline once visited.

**House diagram style — uniformity without touching 41 pictures.** The diagrams had drifted
apart over the years: five different blues, arrow tips from two libraries, label sizes from
`\tiny` to `\large`, weights from `thin` to `ultra thick`. Rather than edit each one, one
preamble block in `intro_prob.tex` redefines the names they *already share*:
- the named colours (`blue`, `red`, `green`, `orange`, `gray`, …) are repointed at a single
  palette that matches the theorem-box colours in the stylesheet;
- the built-in weight keywords are flattened to a narrow range (`thin` 0.5pt →
  `ultra thick` 1.3pt), so no diagram shouts next to its neighbour;
- `every picture` sets one arrow tip (`>=Stealth`), line join/cap and label size;
- `every axis` (pgfplots) unifies axis lines, tick/grid/label/legend styling.

Every diagram keeps its own structure and picks up one consistent look. 36 SVGs, clean
compile, no LaTeX errors. Note the ordering constraint: the `\pgfplotsset` half must sit
*after* `\usepackage{pgfplots}`, not with the rest of the block.

**Source corrections applied** (user: *"you are free to rearrange"*):
- Section 1.4 title: "Condition Probability and Bayes Theorem" → "Conditional Probability
  and Bayes' Theorem".
- **18 lines of quote damage fixed.** `"word"` compiles to `”word”` — *both glyphs are
  closing quotes*. Converted to proper `` ``word'' `` pairs, and moved one pair out of
  math mode. Script kept at `scratchpad/fixquotes.py`; it skips comments and refuses
  ambiguous odd-quote lines, and every change was reviewed before applying.
- Contents page was listing *itself* as a chapter (`\addcontentsline` on line 260) —
  removed. `\contentsname` changed from shouty `TABLE OF CONTENTS` to `Contents`.
- "we focus on…" → "We focus on…"; "Not that" → "Note that"; "manger" → "manager".

**Two of my own mistakes, caught and fixed:**
- `build.py` originally wrapped proofs in `<div class='proof'>` — but **tex4ht already
  emits that div**. The result was a duplicate opening div plus a stray `</div>` at the
  QED: unbalanced DOM that browsers silently repaired. Removed; CSS targets tex4ht's own
  class. A div-balance check now runs after every build.
- I then ran `build.py` twice over the same files and misread the resulting imbalance as a
  new bug. Hence the idempotence guard.

**Verification.** Screenshotted at 1400px and at a *true* 390px viewport. Note the trap
hit before on the climate site: **headless Chrome clamps windows to ~500px**, so
`--window-size=390,…` produces a *cropped* 500px render that looks like a mobile overflow
bug. `.viewport/m390.html` iframes the page at exactly 390px to get a real narrow viewport;
use it rather than trusting a small `--window-size`. Sidebar collapses to a "Contents"
drawer, no horizontal overflow, wide aligned displays scroll rather than clip.

**Equation numbering — a defect the split created.** MathJax numbers equations *per page*,
restarting at 1; LaTeX numbers them *per chapter*, continuing across the sections a chapter
is split into. So the display LaTeX calls (2.2) rendered as (2), while the `\eqref` pointing
at it — which tex4ht resolves from LaTeX's numbering — said 2.2. Two numbers for one
equation on the same page. `build.py` now counts numbered environments per chapter in
document order and injects a per-page MathJax `tagformat` with the right prefix and offset
(section 2.5 correctly continues at 2.3). The proof that surfaced this had `(2.1) and (2.2)`
as hardcoded text matching nothing — now real `\label`/`\eqref`.

**Overflow checking.** `.viewport/overflow-check.html` loads all 22 pages and reports
anything a reader would have to scroll to see. It filters two benign cases: a display that
scrolls inside its own box, and an equation tag positioned in the right margin (where a book
puts it). **Currently reports none.** Two things it caught: display maths had no
`max-width`, so a wide formula dragged its enclosing proof box out with it; and the text
measure at 36rem clipped `cases` blocks — now 41rem.

**Still open from this round:**
- Departmental material (MAT 3902 ver6 PDF) not yet used to fill gaps — the reconciliation
  process above still applies, and nothing from it has been copied.
- giscus is stubbed, not live: `GISCUS_READY = False` in `build.py` renders a placeholder
  line. Needs a GitHub repo with Discussions enabled, then the four IDs filled in.
- Quiz interaction model still undecided (open question 5).

### 2026-07-30 — Catalogue page built, following the MIT OCW card pattern
- User pointed at MIT OpenCourseWare's maths search page. Rendered and analysed it (see
  the new section above), then **built the first real site page**: `site/index.html`.
- Follows MIT's course-card pattern: subject + level line, bold title, short description,
  topic tag chips, and a thumbnail. **The thumbnail is one of the converted SVG diagrams**
  from the notes themselves (the probability-density trapezoid) — subject-specific
  artwork at zero cost, which MIT pays illustrators for.
- **Deliberately omitted MIT's faceted filter sidebar** — they filter 330 courses, this
  filters one. Noted in the design section to revisit at ~10+ courses.
- **Planned courses are shown as visible "in preparation" placeholders** rather than
  hidden. A catalogue that visibly grows is a better signal to students than one that
  looks finished and then stalls — and the user explicitly liked the "building up over
  time" idea earlier.
- **Resolved the course-code tension** flagged above without undoing the depersonalisation:
  codes stay out of titles and headings, but appear as a small "also listed as MAT2901"
  tag and in the searchable metadata. **Verified by test:** searching `mat1110` finds the
  right course.
- **Verified, not assumed:** automated probe confirms the live search filters correctly
  (4 → 1 on "bayes", 1 on "mat1110", 0 + no-results message on nonsense, back to 4 when
  cleared) and that the page has **no horizontal overflow at 390px**.
- Dark mode supported via `prefers-color-scheme`.
- **Next step:** wire the notes pages themselves into this shell — a persistent sidebar
  showing the course tree (the Paul's Notes pattern), consistent styling with this
  catalogue page, and giscus at the foot of each section page.

### 2026-07-30 — Depersonalised; multi-page navigation working; design research done
- **Removed all personal and institutional identifiers from the title page** per the user's
  instruction (going online, so no name, no university, no course code). Replaced with a
  clean professional title block: "Introduction to Probability / Course Notes /
  Foundations, random variables, and distributions / 2026". Verified: zero occurrences of
  the name, university or course code in any generated page.
- **Solved the user's table-of-contents request**: switched to `make4ht ... "mathjax,3"`,
  which splits the document into **22 pages — one per section** — with the contents page
  linking directly to each, and automatic next/prev/up navigation on every page. No custom
  code needed; this is built into the tool. Visually verified both the new contents page
  and a section page (1.4 Bayes/Independent Events — definitions, lemma, theorem and full
  proofs all rendering correctly).
- **Did the design research the user asked for** (see the new section above): Paul's Online
  Notes as the structural model (page-per-section, persistent tree sidebar, Notes and
  Practice Problems as separate parallel tracks); Brilliant.org for the quiz pattern
  (progressive reveal, low-stakes practice, scaffolding removed over time); and **giscus**
  as the answer to the "window to ask questions" request — a free, no-backend discussion
  widget backed by GitHub Discussions that can attach to each section page individually.
- **One cosmetic defect noted, not yet fixed:** the contents page shows the heading "TABLE
  OF CONTENTS" twice (once from the document's own `\chapter*` heading, once from tex4ht's
  generated list). Trivial to remove; left for the next pass.
- **Next step:** fix the duplicate heading, then build the actual site shell around this
  output — sidebar navigation, styling, and giscus at the foot of each section page — so
  the user has something concrete to react to, per the build-first instruction.

### 2026-07-30 — Real build started; both conversion defects root-caused and fixed
- User gave clear direction: build first rather than keep planning, with editorial
  licence to rearrange/simplify/add examples, following departmental structure where
  useful, writing as an experienced educator, and expecting real iteration once students
  are actually using it. A "Q&A window" idea was raised and logged as a future
  possibility, not scoped now. All recorded above as standing instructions for future
  content work, not just for this document.
- Set up the real project structure: `courses/introduction-to-probability/{source,build}`.
  Copied the full original source folder (not just the `.tex`) into `source/`.
- **Went back and properly root-caused the two "issues" logged in the previous entry —
  both were mis-diagnosed on first pass.** The missing-image concern was a false alarm
  (the `\includegraphics` call is commented out, never active). The "garbled math" was
  actually a broken diagram: three TikZ figures use `pattern=dots` fills that `tex4ht`
  silently fails to convert to SVG despite the LaTeX compiling without error. Fixed by
  switching those three fills to a plain solid colour — a legitimate style choice, not a
  workaround. Also fixed a real syntax typo found in passing
  (`[=>stealth]` → `[->,>=stealth]`, six occurrences).
- **Reran the full conversion: zero remaining defects.** 36 diagrams, all visually
  verified including the previously-broken one (now a clean, correctly-labelled
  trapezoid). Output sits at `courses/introduction-to-probability/build/intro_prob.html`
  — openable in a browser right now.
- **Next step:** get the user to actually look at this converted output, then move into
  the real educator-pass work (reorganising/simplifying/adding examples) on a first
  section, per the build-first-then-react instruction above.

### 2026-07-30 — Conversion tool CONFIRMED by testing; two known issues documented
- Finished the content-page verification left over from before the power cut. Checked
  several full pages of dense mathematical content (variance proofs, PGF/MGF derivations,
  probability tables, tree and set-mapping diagrams) rendered in an actual browser, not
  just inspected as raw HTML. All render correctly via `make4ht ... mathjax` mode.
- Found and documented two real, minor issues (external images need the full source folder
  copied, not just the `.tex`; rare garbled inline-math expressions need a manual
  proofreading pass) — both written up in the Technical decision section above, with the
  practical consequence: every converted document needs a manual QA pass before
  publishing, not just an automated conversion.
- **The conversion/content half of the technical stack is now settled and evidence-based,
  not assumed.** Site framework/hosting remains open (question 6) but is decoupled from
  this and not urgent.
- **Next step:** do the real conversion of Introduction to Probability (copying the full
  source folder this time, then a manual QA pass), and decide the quiz-interaction model
  (question 5) — both can proceed without waiting on Mat1110/Intro Stats material.

### 2026-07-30 — Power cut mid-session; resumed cleanly from this file
- A power cut interrupted the session mid-way through testing LaTeX-to-HTML conversion.
  On resume, this file (read fresh from disk, not from conversation memory) had every
  decision through "combine-and-own is the standing rule" intact and committed, plus the
  in-progress conversion test findings below as uncommitted edits that also survived on
  disk. **The mechanism worked as intended.**
- In-progress technical finding, carried over: tested `make4ht` on the real Introduction
  to Probability document (64 real TikZ diagrams confirmed present, not just imported
  packages; 182 theorem/definition/example/remark blocks). First attempt used SVG mode,
  which rasterised **every math expression** into an image (948 images, garbage alt text
  like `"M(ME)-"` for a fraction) — this would make notes unsearchable and inaccessible,
  directly against the "searchable notes" requirement. **Switched to `make4ht ... mathjax`
  mode**: down to 33 images (real diagrams only) plus live MathJax for all math notation.
  Title page rendered and visually checked — clean, correct metadata (confirms course code
  MAT2901 for Introduction to Probability). Was mid-way through checking a content page
  with actual diagrams/equations (anchor-based screenshot navigation was not working
  reliably in headless Chrome) when the cut happened.
- `scratch/` added to `.gitignore` — it holds this throwaway conversion test output,
  regenerable, not final content, not meant to be committed.
- **Next step:** finish visually verifying a content page (math + a real diagram) from the
  mathjax-mode conversion, then report the technical recommendation and get it confirmed
  before writing the real Introduction to Probability content.

### 2026-07-30 — Confirmed: combine-and-own is the rule for every course
- User confirmed the reconciliation ("combine so we own the material") process is not a
  one-off for Probability Theory but the standing rule as more courses are added over
  time. Generalised in the section above rather than left implicit. Practical
  consequence: the rate at which courses are added is paced by how much original
  synthesis each needs, not by conversion speed — which is fine given the relaxed,
  end-of-semester timeline already agreed.
- No new open question raised by this; it tightens an existing rule rather than adding
  a new decision to make.

### 2026-07-30 — Narrowed to 2 courses; corrected Mat1110; found a clean starter
- User clarified the "showcase more courses" comment: the real driver is that **students
  repeat courses often**, not that many different topics are needed for launch. Confirmed
  going with **two courses this semester** (Mat1110, Introduction to Statistics), with
  wider-catalogue growth as a later, visible "building up over time" phase — which the
  user explicitly said he likes.
- **Corrected a wrong assumption:** MAT1100/1110/1120 are three separate UNZA foundation
  courses split by faculty (Engineering/NS, Humanities, Health Sciences respectively), not
  variants of one course. Mat1110 = Humanities = "Foundation Mathematics and Statistics
  for Social Sciences." The "Foundation Mathematics" folder in `LaTeX_Projects` is for a
  *different* course entirely — must not be used as a Mat1110 source. Mat1110 build is on
  hold until the user delivers this semester's real material.
- Per the user's redirect, inspected two courses as worked examples while waiting on
  Mat1110/Intro Stats content: **Introduction to Probability** (clean, recent, complete,
  no conflicting version — a strong immediate starting candidate) and **Probability
  Theory / MAT 3902** (a second real reconciliation case: the user's 2020 notes vs a
  "ver6" departmental PDF that is what's actually taught now). Both documented in detail
  above.
- **Proposed, not yet confirmed:** start real building on Introduction to Probability now,
  since it has no blocker, while Mat1110/Intro Stats material is pending this week.
- **Next step:** get the user's go-ahead on that proposal.

### 2026-07-30 (earlier) — Scope widened, timeline relaxed
- User wants **more than the 2 current courses** showcased at launch — breadth helps
  build an audience. The other ~28 topics already sitting in `LaTeX_Projects` (as authored
  `.tex`, needing the same reconciliation treatment) are back in scope for the launch
  version, not deferred to "later."
- User explicitly relaxed the timeline: **"don't worry about time even at the end of the
  semester we can go live."** The earlier Monday framing was about the user's own teaching
  prep, not a platform deadline. Full semester is available as build time.
- Recommended approach (given in this turn, not yet confirmed by user): prove the
  notes+quiz pipeline on 1-2 courses first — Mat1110 and Introduction to Statistics remain
  the natural pilots since they are being actively (re)written this semester anyway — then
  use the reconciliation process to progressively add the remaining ~28 topics through the
  semester, prioritising by likely enrolment/how foundational a course is, ending with a
  broader-catalogue launch at semester end.
- **Not yet answered:** whether the user agrees with that prioritisation heuristic, or has
  a specific order in mind for which of the ~28 other topics matter most.

### 2026-07-30 (later still) — Timeline constraint: semester starts Monday
- User will personally write **new** notes and exam questions for Mat1110 and
  Introduction to Statistics **this semester** — not simply reuse the archived
  2020/2026 `.tex` files as-is. Those old files remain useful as style/coverage
  reference (per the reconciliation process above) but are not the content going live.
- **Classes start Monday.** This is a hard, near-term deadline that changes what "which
  course first" means — see revised open question 4. Realistic framing: content will
  arrive incrementally, week by week, as the user teaches, for both courses at once,
  rather than one course being fully built up front.
- **Not yet answered:** whether anything needs to be visible/live to students by Monday
  itself, or whether it's acceptable to start building the pipeline now and publish the
  first real content whenever the user's first batch of new material is ready.
- **Next step:** resolve that scheduling question with the user, then decide the
  lightest-weight pipeline that can take "user writes a new note/question set" to
  "published on the site" repeatedly, starting this week.

### 2026-07-30 (later same day) — Audience, interactivity and rollout decided
- User confirmed: local Zambian system (UNZA + others), both notes-site and quiz-engine
  (not either/or), free-first-then-paid rollout with paid as the real long-term goal.
- User explained why some folders hold other authors' PDFs (e.g. Dr Nawas.pdf): Zambian
  departments expect lecturers teaching the same course to teach the same content, so
  these are shared/departmental reference notes, not arbitrary downloads.
- This changes the scope rule: notes need active *reconciliation* against that shared
  material (as a coverage checklist, never copied) plus original writing to fill gaps —
  not a simple tex-to-html conversion. Documented as its own section above.
- Checked the two courses the user is tutoring this semester (Introduction to Statistics,
  Mat1110) as first-course candidates. Introduction to Statistics has both a notes and an
  exam-questions `.tex` file (2020, dated but complete); Mat1110 has recent notes
  (Jan 2026) but no confirmed matching exam-question source yet.
- Three new open questions raised (4-6 above): which course to start with, the exact quiz
  interaction model, and the technical approach for the free phase. **None answered yet.**
- **Next step:** get the user's advice request answered — recommendation given in the same
  conversation turn this log entry was written; awaiting the user's response to it.

### 2026-07-30 — Project opened, not yet scoped
- User asked to build an interactive web app from the LaTeX teaching materials, as a
  project separate from the climate work.
- Checked for a prior discussion of this (user believed it had been discussed before):
  not found in saved memory, and not in the `Career_Strategy` folder inside
  `LaTeX_Projects` (that folder only holds the climate-project planning docs already
  known). Confirmed nothing was lost — this is a fresh start.
- Surveyed `/home/corban/LaTeX_Projects`: 63 folders, ~273 MB, 61 authored `.tex` files
  plus a separate layer of downloaded reference PDFs in some of the same folders.
- Agreed the scope rule above: authored `.tex` only, reference PDFs excluded.
- Three open questions raised (audience, interactivity type, free/paid) — **not yet
  answered.**
- **Next step:** user to answer the three open questions, then brainstorm format and
  technical approach together.
