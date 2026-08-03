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

## Identity and hosting — settled 2026-07-31

**Positioning: free, community, not commercial — settled 2026-07-31.** The paid tier is
dropped. The user's reasoning: *"it will be enough for me to contribute to the community,
so I don't want to sound like a try-hard, like a lot of people who sell past papers and
solved sheets."* This is a deliberate strategic choice, not an unfinished plan — do not
reintroduce payment mechanics without asking.

Consequences already applied, and worth preserving:
- The front page states the pledge plainly: **"No sign-up. No adverts. Nothing to pay."**
  That single line is what distinguishes the site from the people selling past papers, so
  it sits in the hero, not buried in About.
- The word "past-paper" is gone from the lead. It is "worked problems".
- **The past-paper and tutorial-sheet source extracts were deleted from the repository and
  purged from git history** (`git filter-branch` + reflog expire + gc, then a force-push;
  verified zero recoverable objects). The originals remain in `~/LaTeX_Projects`, outside
  the repo. The problems themselves live on in the `.tex` as the user's own transcriptions
  with original solutions — that is authored work, not republished material.
- No author name on the site. The user's portfolio site covers attribution, and the
  repository URL carries the name for anyone who wants it.
- No "new courses are added through the semester" — the "In preparation" status on each
  card says it without making a promise about timing.
- Footer colophon credits LaTeX, tex4ht, MathJax and Claude.

**No course codes anywhere on the site — settled 2026-07-31.** Not MAT2901, not MAT1110,
not in the hidden search keywords. They are a local UNZA label and would confuse a learner
from another school. Courses are identified by name only: "Introduction to Probability".
The same reasoning removed "written for the Zambian curriculum" from the front page — the
audience starts Zambian but the material is not Zambia-specific, and nothing on the site
should imply otherwise.

**Site name: WJ Maths.** Display form `WJ Maths`, handle/email/domain form `wjmaths`. The
initials are the user's parents'; **do not publish what they stand for** — in a small
community that is an identifying detail, and the name works without the story.

**Authorship is open.** A pseudonymous build was considered and rejected: "what we've built
is too big to hide." The existing GitHub account and commit identity stay as they are, so
there is no history rewrite and nothing is blocked. WJ Maths is a brand name over open
authorship, not a disguise.

**Hosting: GitHub Pages from `main`, folder `/` (root).** Every path in the project is
already relative and correct when served from the root, so the only addition is a root
`index.html` that redirects to `site/index.html`. Verified locally by serving the repo
root: catalogue, course pages, stylesheet and MathJax all resolve.

*Superseded 2026-08-01:* this section originally said "no Actions workflow". There is one
now — `.github/workflows/pages.yml`. The branch option runs jekyll-build-pages over the
repository and failed on every push; the workflow skips the build step and uploads the
repo as static files instead. Its own header comment carries the full reasoning.

**Still gated on the user (three clicks in GitHub settings):**
1. Make the repo **public** — required for both Pages on a free account and for giscus.
2. **Settings → Pages** → Source: Deploy from a branch → `main` / `/ (root)`.
3. **Settings → General → Features → Discussions** on, with a **Q&A** category, then
   install the giscus app and read the two IDs off giscus.app into `site/build.py`.

**Analytics:** `GOATCOUNTER_CODE` in `site/build.py`. Empty by default, and when empty **no
script tag is emitted at all** — no third-party request, nothing to disclose. Set it to the
subdomain chosen at goatcounter.com to switch it on.

**Note before making the repo public:** it contains past-paper questions and tutorial
sheets (2020 exams, Feb–March 2026 tutorial sheets — last semester's). Worth a final check
that none are current assessed coursework.

## Custom domain — prepared 2026-08-03, not yet bought

The user intends to buy a domain (`wjmaths.com` or similar, roughly $10–15/yr). Everything
on this side is ready; three things to do when it exists, in this order:

1. **A `CNAME` file at the repository root** containing the bare domain and nothing else
   (e.g. `wjmaths.com`). The workflow uploads the repo root as the artifact, so a root
   `CNAME` is picked up with no other change. Committing it also sets the domain in
   Settings → Pages, so do not type it there as well — GitHub will fight itself.
2. **DNS at the registrar.** Apex domain: four `A` records to `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (and the matching `AAAA`
   records if the registrar supports them). A `www` subdomain: one `CNAME` to
   `nephatmwanza.github.io`. Propagation is usually minutes, occasionally a day.
3. **Enforce HTTPS** in Settings → Pages once the certificate is issued. The box is greyed
   out until GitHub has provisioned it; that can take up to an hour after DNS resolves.

Two things that do *not* need changing: every internal path is relative, so nothing breaks
on a domain move, and the giscus thread keys are keyed to course directory and section
title, not to URL — so no discussion orphans when the address changes. GoatCounter will
start a fresh path history under the new host; the old one stays readable in its dashboard.

**Do not retire the `github.io` address.** GitHub redirects it automatically, and links
handed to learners this year keep working.

## Introduction to Statistics — started 2026-08-01

**Second-year course** (the user corrected this; the departmental code MAT2602 agrees).
Course codes still do not appear on the site.

**Sources**, in `~/LaTeX_Projects/Introduction to Statistics/`:
- `Introduction To Statistics.tex` — the user's own notes, dated 2013. **This is the draft.**
- `Dept/Lecturer_Notes.pdf` (89 pp) — departmental notes, the **coverage checklist**, never
  copied.
- `Dept/Introduction_to_Statistics_Course_Content.pdf` — the syllabus.
- `Dept/Tutorial_Sheet_1.pdf` (May 2026), `Tutorial_Sheet_2.pdf` (June 2026) — last
  semester's, so the same status as the probability sheets. Transcribe problems with
  original solutions; do not republish the sheets.

**The user's notes match the syllabus exactly** — five chapters, five syllabus topics, same
order, and every named sub-topic present. So the draft needs filling out, not restructuring.

**Four topics appear only once in the .tex** and may be mentioned rather than taught. Check
these against the departmental notes for depth: goodness of fit, tests of independence,
completely randomised design, ratio of variances.

**Done:** converted (19 pages, 43 diagrams), title page depersonalised, headings set in
title case, tally marks reimplemented, sidebar fixed, first editorial pass.

**Not done:** practice problems (none yet, against 77 in probability), the depth check
above, and a full editorial read. **The catalogue still lists it as "In preparation" and
should stay that way until it has problems** — publishing a course with none, next to one
with 77, sets the wrong expectation.

**Two things this course taught the pipeline:**

1. **`\StrokeOne`..`\StrokeFive` come from `ifsym`**, which is not installed here. They are
   tally marks, and they carry the frequency-table teaching — how raw observations become
   counts. Reimplemented in TikZ rather than adding a dependency. *I removed the package
   first without checking what it provided, having only grepped for `circledR`.*
2. **An `article`-class document gives subsections their own pages.** `read_toc` matched
   only `chN`/`seN`, so ten of nineteen pages were missing from the sidebar. Fixed, and
   sections are promoted to headings when a document has no chapters.

**Build hardening, prompted by a ten-minute hang:** a missing `.sty` leaves `htlatex` at an
interactive prompt, so the build does not fail — it waits, looking like a slow conversion.
`make-course.sh` now runs `-interaction=nonstopmode` under a `timeout`, and greps for
missing packages explicitly. The same fault now reports itself in seconds.

## Introduction to Statistics — published 2026-08-01

**Live.** 26 pages, 59 diagrams, 14 worked problems across all five chapters.

**Source:** the user's own 2013 `.tex`, which maps onto the departmental syllabus exactly —
five chapters, same five topics, same order. Departmental material
(`~/LaTeX_Projects/Introduction to Statistics/Dept/`) used strictly as a coverage checklist
per the standing rule; nothing copied.

**Fourteen mathematical errors found and corrected.** These were real, not typographical,
and several would have changed a student's answer:

| Where | What |
|---|---|
| Confidence intervals | `t` used when σ is *known*; `t` used for a proportion; `z` used for the pooled two-sample case |
| Hypothesis testing | "H₀ is true" / "H₁ is true"; P-value compared with α/2 |
| Chi-square | statistic printed as `(O−E)¹`; df given as `n−1` |
| ANOVA | MS_W divided by `n−1` against its own `n−k`; SS_B built from the grand total; the sum-of-squares identity false three ways |
| Regression | least squares described as minimising the sum of errors, not squares |

**A pattern worth remembering about this author's writing:** the notes repeatedly state
something loosely and then correctly a few lines later — the χ² statistic, the ANOVA
identity, and the least-squares description all do this. The loose version is what a reader
meets first. When auditing the remaining courses, **read the first statement of every
result, not the derivation.**

**Three sections written** (missing entirely, all on the syllabus):
1. **The four sampling distributions** — the largest gap. The notes *used* Z, t, χ² and F
   throughout without ever introducing them. This is almost certainly why the z/t rule was
   backwards: the rule had nothing to attach to.
2. **P-values** — defined, decision rule, one- vs two-tailed, and what a P-value is *not*.
3. **Inference for regression** — ANOVA table, R², t-test for slope, F-test, intervals for
   slope and intercept. The chapter previously stopped after least squares.

**Diagrams: 43 → 59.** Same defects as the probability notes — 22 TikZ `pattern=` fills
tex4ht cannot convert (those figures rendered blank) and 39 pictures opened with
`[=>stealth]`, which is invalid and silently produces no arrowheads. Both fixed, and the
course now shares the probability house style.

**Editorial pass** with `aspell --mode=tex`: 13 misspellings, grammar fixes, abbreviation
stops regularised, and the `+ve`/`-ve` handwriting shorthand spelled out (11 instances — it
was marked up as maths, so it rendered italic mid-sentence).

**Verification method, worth repeating on the next course:** every numerical answer was
computed before being written — exact rational arithmetic, symbolic integration, or
`scipy` — and the ANOVA errors were caught by working a four-group example and finding the
two sides of the identity did not balance.

## Status Log

*(most recent first — append new entries, never rewrite old ones)*

### 2026-08-03 (later) — Mathematical Statistics published; the question box was
### missing from 97 of the site's content pages

**Mathematical Statistics is live** and listed in the catalogue, taking the count
to four. It was deliberately held back until chapter 3 had practice problems, so
it would not launch with two chapters equipped and one bare.

Sources: the user's own `Mathematical Statistics.tex`, with *questions only* taken
from the `Mathematical Statistics Notes` folder — Assignment 2 and 2.2
(estimation), Assignment 3 (hypothesis testing), and the MAT3601 2013 final
examination, all worked in full.

**A defect found during the clean-up pass, worth reading before touching
`build.py`.** The giscus question box was gated on the page *filename* matching
tex4ht's `se\d+` stem. That silently assumed every course splits at section
level. Two do not: Foundation Maths and Introduction to Statistics use `\section`
for what a reader calls a chapter, so their content pages carry the `su` stem and
were shipping with **nowhere to ask a question** — 97 pages of the 117 in those
two courses, and precisely the pages a learner is stuck on. The ten boxes that did
exist sat on chapter landing pages, which have nothing to ask about.

Now gated on whether the page *carries* a section or subsection heading, so it
cannot drift again when a course is structured differently. The thread key was
extended the same way (`(?:sub){0,2}sectionHead`); a section head always precedes
its own subsections, so `re.search` still finds it first and **every key minted
before the change still points at the same thread** — verified against a snapshot
of all 46, none lost, none renamed.

**Lesson, same shape as several earlier ones:** ask what a page *contains*, not
what it is *called*. The filename test looked precise and was wrong in a way that
produced no error, no warning and no visible difference — only silence where a
learner should have been able to ask.

**Two source misprints corrected in place**, both flagged to the reader:
- Assignment 3 is clean, but the 2013 paper's Q3(c) gives the geometric support as
  $x=0,1,2,\ldots$ against $\theta(1-\theta)^{x-1}$, which sums to
  $\frac{1}{1-\theta}$. Intended support is $x=1,2,3,\ldots$
- Sizes that look wrong and are not: the $n=1$ test in Assignment 3 Q1 has power
  0.0975 against size 0.05, and it *is* the most powerful test at that size.

Every stated number was recomputed in sympy before being written, as before. The negative
binomial closure in the 2013 paper's Q1(c) was checked by direct convolution as well as by
moment generating function — the two agree to 1.4e-17.

**Build after all four courses were rebuilt:**

| Course | Pages | Diagrams | Question boxes |
|---|---|---|---|
| Foundation Maths and Statistics for the Social Sciences | 75 | 122 | 10 → **73** |
| Introduction to Probability | 22 | 41 | 17 |
| Introduction to Statistics | 42 | 61 | 5 → **39** |
| Mathematical Statistics | 26 | 9 | **20** |

Site total 46 → 149 question boxes, all 149 keys unique, no LaTeX errors, no missing
diagrams, no empty titles. `scratchpad/verify_site.py` runs the whole check in one go and
compares against a snapshot of the keys taken before the change.

### 2026-08-03 — Every "sketch" tutorial question now has its curve drawn

Diagrams went 39 -> 122. Every tutorial question that tells a learner to sketch,
draw or illustrate now shows the answer, including the Venn diagram for Sheet 1
Q1(b) (which said "draw a Venn diagram" and got a table) and De Morgan's laws on
the number line.

**Panels are generated, not hand-written** — `scratchpad/panel2.py`, from the same
sympy expressions the solutions were checked against, so a curve cannot drift from
the answer printed beside it. The generator refuses to emit a panel whose curve
leaves its own box; that caught five bad domains.

**Three TikZ traps, all worth remembering:**
- Do **not** use `xscale`/`yscale` anisotropically. It turns circle markers into
  ellipses and lets bounding boxes wander — eleven panels meant to be identical
  came out between 109pt and 729pt tall. Normalise the *data* into a fixed
  centimetre box and leave the canvas alone.
- A y-range of a few hundred drives `yscale` to ~0.008 and **overflows pgf**:
  the build dies with `Dimension too large`. Normalising removes the cause.
- **pgfmath computes `a^b` as `exp(b ln a)`**, which is wrong for negative `a`, so
  `\t^4` misbehaves silently once a domain crosses zero. Expand powers into
  repeated multiplication.

**Two process lessons:**
- When splitting generated blocks apart, anchor on the opening token
  (`\begin{tikzpicture}`), not on a separator. Anchoring on the separator left
  the generator's group names (`S8A`, `S4Q3`, ...) printed as literal text in
  five figures — and that shipped in one commit before being noticed.
- **Counting `\begin`/`\end` pairs is not a structural check.** A bad repair left
  273/273 notes with the structure still wrong. The stack-based nesting checker
  caught it ("end solution closes begin note"); a separate check that no figure
  sits inside a note is now run too.

Current build: 75 pages, 122 diagrams, none missing, no LaTeX errors.

### 2026-08-02 (later) — All eleven MAT1110 tutorial sheets worked

**Course identity settled.** This is MAT1110, *Foundation Mathematics and Statistics for
Social Sciences*. There is a **separate MAT1100, Foundation Mathematics, for Natural
Sciences** — its material is in `LaTeX_Projects/Foundation Mathematics`, a past-papers
document (tests and exams by year, 2013–2020). Do not confuse them. The web-app
directory was therefore renamed `courses/foundation-mathematics` →
`courses/foundation-maths-social-sciences`, free to do because the course was not yet on
the catalogue. Title page now reads "Foundation Mathematics and Statistics for the
Social Sciences".

**All 11 tutorial sheets are done**, mapped to chapters as: 1 → ch 1 and 2; 2 → ch 3;
3, 4, 5 → ch 4; 6 → ch 6; 7 → ch 5; 8, 9, 10 → ch 7; 11 → ch 8. Each sits in a
`\subsection{Practice problems}` block at the end of its chapter, matching the
statistics course. There are no tutorial sheets for chapters 9 or 10.

**Sheet 5 is an earlier version of Sheets 3 and 4** (April 2023). Its Q3, Q4(a)-(e),
Q6, Q7(b)-(e) and Q8 duplicate them word for word. The overlap is stated as a map at
the top and only the new material worked — chiefly Q9, eleven partial fractions.

**Misprints found in the sheets**, all confirmed by reading the rendered page:
- Sheet 3 Q6(c)(vi) / Sheet 5 Q3(f): `x^4-6x^3-11x^2+24x-28` does not factorise; should
  be `+28`, which is the same polynomial as Sheet 3 Q7(e).
- Sheet 3 Q7(c) / Sheet 5 Q4(c): `x^3+6x^2+5x-2=0` has no rational roots; likely `-12`.
- Sheet 3 Q2(a): empty — "solve by completing the square" then nothing.
- Sheet 7 Q9(e): `2cos^2x + cos x = sin^2 x` gives `cos x = (-1±√13)/6`, not doable
  without a calculator; likely `2cos^2x + cos x - 1 = 0`.
- Sheet 11 Q5(f): denominator printed `(3x+2x)(2-x)^2`; should be `(3x+2)`. The part is
  also labelled "(b)" a second time.
- Sheet 11 Q6: carries a stray "using by parts formular" left over from Q4.
- Sheet 11 Q1: skips from (b) to (d).

Every one is worked as printed *and* in its intended form where that is clear.

**Method that must not be skipped: read these PDFs as images.** `pdftotext` mangles
fractions, overlines and conjugate bars. Use `pdftoppm -r 130 -png`, and higher with
`-x -y -W -H` to crop when a symbol is doubtful.

**Verification**: every numerical answer was computed independently in Python/sympy
before being written — set operations with real Python sets, inclusion–exclusion checked
by reconstructing all eight Venn regions, every division checked by multiplying
`Q(x)D(x)+R(x)` back, every partial fraction against `apart`, every identity simplified
to zero, every integral differentiated back.

Current build: **74 pages, 39 diagrams, none missing.**

**Still to do**: add the course to the site catalogue (deliberately withheld so far);
the probability course has still never had the systematic recompute-every-answer audit.

### 2026-08-02 — MAT1110 finished at ten chapters, not nine; Tutorial Sheet 1 worked

**The course is ten chapters, not nine.** The contents page of Dr Mbaale's notes lists
Chapter 10 Probability after Descriptive Statistics. Earlier sessions had planned for
nine. All of 8 (Integral Calculus), 9 (Descriptive Statistics) and 10 (Probability) are
now written, so the syllabus is covered end to end.

**Chapter 7 had real gaps.** Section 7.2 Continuity is on the departmental contents
page and had been skipped outright. Cross-checking the eleven tutorial sheets against
the notes showed students could not attempt sheets 8, 9 or 10 from what was written.
Added: the properties of limits, piecewise limits and existence, indeterminate forms,
limits at infinity, Continuity as its own section, the second derivative as a topic,
the normal to a curve, critical values with a sign table, points of inflexion, greatest
and least values on a closed interval, and optimisation.

**Five worked examples were tutorial questions verbatim.** (2x+1)/(2x-1), sin^3(2x+5),
x^2 e^(-2x) and 2x+3y^2+3x^2y+12=0 are sheet 10 Q1(c), Q1(b), Q1(f) and Q2(f); the
limit of (x^2-x-2)/(x-2) is sheet 9 Q1(f). Two more found later: the second derivative
of (x+1)/(x-1) is sheet 8 Q1(a)(iv), and 2x^3-3x^2-12x is the departmental notes' own
example 7.6.2. All seven replaced. **A worked example must not be an unsolved tutorial
question with the answer attached** — check new examples against the sheets before
writing them.

**Read tutorial-sheet PDFs as images, not text.** `pdftotext` mangles fractions,
overlines and conjugate bars in these files. On sheet 1 alone the text layer hid that
three of the Q8(a) decimals are recurring rather than terminating, that Q8(b)(vi) is
3sqrt(28)/(2sqrt(175)) and not its reverse, and that all three parts of Q9(c) contain a
conjugate. Use `pdftoppm -r 130 -png` and read the page.

**Tutorial sheets: 1 of 11 done.** Sheet 1 is complete, split across chapters 1 and 2 as
`\subsection{Practice problems}` blocks, matching how the statistics course does it.
Roughly 430 leaf questions remain across sheets 2-11. Mapping: 2 and 3 to Functions,
3-5 to Polynomial Functions, 6 to Exponential and Logarithmic, 7 to Trigonometry, 8-10
to Differentiation, 11 to Integral Calculus. There are no tutorial sheets for chapters
9 or 10.

**Foundation Mathematics is still not on the site catalogue.** Deliberate — add it once
the tutorial sheets are further along.

Current build: 69 pages, 25 diagrams, none missing.

### 2026-08-02 (late) — Two diagrams were never being produced, and the build said fine

User: Figures 31 and 32 are not showing. Both were missing entirely.

**Cause.** Both used `\path[pattern = north west lines, …]` to shade the $F$
distribution's tail. tex4ht cannot convert TikZ pattern fills; it emits no SVG at
all, so the HTML pointed at `intro_stats49x.svg` and `intro_stats50x.svg` which
were never written. Every other shaded tail in these notes uses `fill=blue!25` ---
22 were converted in an earlier pass and these two survived it. Neither course now
contains a `pattern=` fill.

**Why I never noticed, which is the part worth keeping.** `make-course.sh` printed
`59 diagrams` --- a count of SVG files *produced*. The HTML referenced **61**. A
failed diagram does not raise that number or colour it red; it just makes it
smaller, which reads like a shorter document. I quoted "59 diagrams" as evidence of
a clean build for an entire session, and it was two short throughout.

The build now compares produced against referenced and names anything missing.
Verified by deleting a third SVG deliberately --- it reported all three:

    WARNING missing diagram intro_stats10x.svg - referenced by the HTML but never produced…
    ==> 42 pages, 58 diagrams, 3 MISSING

> **A count of what succeeded is not a check.** It has to be measured against what
> was required. This is the third time the same lesson has come up here --- the
> overflow checker that reported clean after dumping early, the marker checker that
> matched nothing and said nothing, and now a diagram count that could only ever go
> down. Each time the fix was the same: compare against the requirement, and prove
> the check fails on a known-bad input before trusting it.

Both courses now report referenced == present: statistics 61, probability 41.


### 2026-08-02 (later) — Choosing the number of classes: a section neither source had

User pointed out a real gap: neither these notes nor the departmental notes say how
to decide the **number of class intervals** when $N$ gets large. They cited
ISBN 978-81-317-3403-2 — verified as **J.K. Sharma, *Business Statistics*,
Pearson** — and asked for a section with an example or two.

Now §1.2.2, "How many classes? The $2^k$ rule and Sturges' formula".

**The point worth making, and the reason the section is short.** The two rules are
the *same* rule. $3.322$ is not an arbitrary constant:
$$\frac{1}{\log_{10}2}=3.3219\ldots$$
so $3.322\log_{10}N=\log_2 N$, making Sturges $k=1+\log_2 N$ while the $2^k$ rule
is $k=\lceil\log_2 N\rceil$. They differ by about one class, always. Taught as two
competing formulas they look like something to memorise; shown as one idea there is
nothing to memorise.

Second point: $k$ grows like $\log_2 N$, so **doubling the data adds one class**.
From $50$ observations to $5000$ takes $k$ only from $6$ to $13$.

Two worked examples, every figure checked:
- $N=50$ antibody concentrations — data already in the notes, so it connects to
  existing content. The division comes out exactly, putting the maximum on the
  final boundary, so the last class must be closed at both ends. Shown rather than
  dodged by choosing friendlier numbers.
- $N=850$ household incomes, where range$/k = 940$ and rounding **down** to $900$
  would leave the highest earner outside every class. That is what makes "round the
  width up" bite.

One caveat included briefly: Sturges' formula is derived by matching a histogram to
binomial coefficients of a normal distribution, so it assumes roughly normal,
moderate-sized data and is known to give too few classes for large or skewed
samples. Framed as "the rule saves you an arbitrary choice; it does not excuse you
from looking at the result".

> **Checked the rules against independent sources rather than writing them from
> memory**, and confirmed the ISBN before attributing anything to it. Both were
> things I could have got approximately right and been wrong about in detail.


### 2026-08-02 — Every tutorial and exam question added: 85 problems

User: add the exam questions, and make sure all the tutorial questions are in —
"those are the ones students will be looking for". Both are now complete.

**Tutorial sheets: 22 of 22.** Sheet 1 had 3 of 6; Sheet 2 had none of its 16.
Sheet 2 now forms a new practice section at the end of Estimation and Sampling
Distributions.

**Exam file: 66 of 66**, across all eleven sections. Statistics went from 14
problems to **85**, every one with a collapsed worked solution.

Every numerical answer was computed and checked before being written, using table
values so the arithmetic matches what a student gets from their own tables.

**Six defects in the source questions**, each stated in the solution rather than
quietly patched:

| Question | Defect |
|---|---|
| Lamp lives | says 50 lamps, lists 49 values |
| Two mark distributions | totals printed 34 and 34; rows sum to 40 and 45 |
| Smoking | 200 women in one copy, 230 in another — see below |
| Mosi consumption | 2000 value reads 3.5 among values of 35–62 |
| Training/performance | gives `sum(y-ybar) = 62`, which is identically zero |
| Training/performance | never supplies ybar, so the intercept has no number |

> **The smoking question reversed a published conclusion.** It appears twice. The
> Exercises copy reads 200 women; the Test 2 copy reads 230, and 270+230 = 500
> matches the stated total. With 200 the test gives Z = 0.92 and fails to reject;
> with 230 it gives Z = 2.56 and rejects. I had shipped the wrong verdict.
>
> The failure was not missing the inconsistency — I flagged it — but resolving it
> by assuming the counts were right and the total wrong. **When a source
> contradicts itself, check whether the question appears elsewhere in the same
> document before deciding which figure to trust.**

Two overlaps proved useful rather than redundant: the smoking duplicate settled
that typo, and the Final's spring data (32.5, 37.1, 35.5, …) is essentially the
Mosi series, independently confirming the dropped digit.

**Three arithmetic slips of my own**, all caught by recomputing before building,
none of which changed an answer: the Latin square counterfactual (53.1 and 3.93,
not 47.4 and 4.4), the heights sum of squares (6866.7, not 6866.2), and the
employee times (40,272.4, not 40,268.7). All three were numbers written from an
intermediate step rather than read off the final calculation.

**Teaching points the questions turn on, now made explicit.** Pairing is the big
one and appears twice. For the typists, paired t = 1.75 against unpaired 0.62 —
same verdict, different reasoning. For the car tune-ups, **paired t = 2.89 rejects
while unpaired t = 0.61 does not**: there the mistake reverses the conclusion,
because car-to-car consumption runs 7 to 31 km/l and buries an effect of 1.9.

Others: frequency density when class widths differ (the tyre data's last class
stands at 12 on frequency and 6 on density); the finite population correction,
which halves a variance in one question and cuts a standard error by 17% in
another; sample sizes always rounded up; interval **width** being twice the margin
(misreading it gives n = 62 instead of 246); and pooling the standard error for a
two-proportion *test* but not for a confidence interval.

**Also this session**: all 246 `\dfrac` replaced with `\frac` across both courses
at the user's request. `\tfrac` left alone, not having been mentioned.

Build clean: 42 pages, 59 diagrams, 85 problems, 85 collapsed solutions, no
warnings, no overflow, zero `\dfrac` in either built site.


### 2026-08-01 (late) — Two centred headings; the P_s section rewritten

User: 2.1.7 Properties of Estimation and 2.1.8 An Unbiased Estimation of
Population Proportion sit centred instead of left like every other heading; put
$P_s=X/n$ in a fraction; the $E(P_s)$ computation should be one line.

Both headings were wrapped in `\begin{center}` — the only two in the file, which
is why they alone looked different. Unwrapped. The first also carried stray double
braces, `{{Properties of Estimation}}`.

$P_s=\dfrac{X}{n}$ now, and the same in the estimators table where `\hat{P}=X/n`
and `Pq/n` were set with slashes while the rows directly below them used `\dfrac`
— inconsistent inside one table.

$E(P_s)$ was three `align*` lines for a single chain; now one line, and
$\operatorname{var}(P_s)$ collapsed to match.

**Two real errors in the sentence that followed**, which is what the tidy-up
exposed. It read that the sampling distribution of $P_s$ "tends to $N(0,1)$ with
mean $X/n$". $N(0,1)$ is the *standardised* version, not the distribution of
$P_s$; and the mean is $P$, not the estimate $X/n$. Now
$P_s\ \dot\sim\ N(P, P(1-P)/n)$, with the standardising step added so the
$N(0,1)$ a student expects still appears, in its right place.

One more in the same table: the symbol row read $\theta \mid n \mid
\hat{\theta} \mid \hat{\theta} \mid \hat{\theta}$ — the same $\hat{\theta}$ under
both *Expected value* and *Variance*, saying nothing. Now $E(\hat{\theta})$ and
$\operatorname{var}(\hat{\theta})$.

**Tooling note.** A Monitor watching for build completion fired early because its
pattern included `rror`, which matched the phrase "standard error" in the source
being echoed. **Watch patterns need to be anchored to the tool's own output**, not
to substrings that can occur in the content passing through it.

### 2026-08-01 (night, after) — \hat for single symbols, \widehat only when wide

User, on Estimation and Sampling Distributions: "we still have the `\widehat`."

Checked first whether it was failing to render — it was not; all 89 occurrences
on that page sit inside `\(...\)` and display correctly. The complaint is the
notation itself, and it is right.

**`\widehat` stretches the accent to fit its argument.** Over a single letter that
is the wrong accent and it is exactly what makes `\widehat{S}` look drawn out.
`\hat` is for one symbol; `\widehat` for anything wider.

An earlier pass had standardised everything onto `\widehat` on the grounds that
115 beat 7 — **counting which form was more common, instead of asking which was
correct.** The majority was simply wrong more often.

Converted 232: $S$ (55), $b$ (73), $a$ (36), $\theta$ (29), $Y$ (22), $P$ (16),
$p$ (1). Kept the 7 `\widehat{\overline{X}}`, where the argument genuinely is
wide and the stretched accent is correct.

Also closed an unmatched bracket found in the same section,
`E(\widehat{\overline{X}} &= …`, and verified every `E(` in the file now balances.

> **A house style settled by frequency is not a house style.** When two forms
> disagree, the question is which is right, not which is winning.

### 2026-08-01 (night, final) — Transposed too many tables; reverted

User pointed at Example 1.45's table, then Table 2 and Table 3. I transposed
those **and six more of the same shape** — Table 4, Table 5, Table 6, the
travel-time distribution (5 copies), the heights problem, the nine-samples table.
User: "no, i only wanted the transpose for the tables i request, the others where
okay without transposing them."

Reverted all six. Only the three requested are laid across.

> **A named example is a scope, not a sample.** When a user points at a specific
> table, figure or example, the request is that one. Finding others that share
> the trait is not evidence they want the trait changed everywhere — a tall table
> is a judgement call about that table, and the author is making it. Ask, or do
> the named ones and *say* what else matches.
>
> This is distinct from the sweeps that were right today: a wrong caption, a
> broken formula, a marker that renders unstyled are all defects, and finding
> more of a defect is a reason to fix them all. Layout is a preference. **Fix
> defects broadly; apply preferences narrowly.**

One note worth keeping from the episode: Table 3 was already transposed locally
when the user reported it as still tall — they were reading the deployed site,
which was behind. **When a report does not match what is on disk, check whether
the fix has shipped before re-investigating it.**

### 2026-08-01 (night, end) — Central Limit Theorem stated properly; wide tables

User asked whether the Central Limit Theorem had been stated. It had, in both
courses, and badly in both.

- **Probability** had one clause: "the sample mean has a normal distribution if
  the sample size is large." No finite-variance condition, no statement of the
  mean and variance, never a theorem — for the result the whole normal
  distribution section rests on.
- **Statistics** had prose under a subsubsection, writing
  $Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$ — the *exact*
  distribution symbol for a relation that is approximate and only in the limit.
  The finite-variance condition was missing there too.

Both are now `\begin{thm}[\textbf{Central Limit Theorem}]`, numbered, with the
condition stated and the convergence written as convergence. Statistics renders
it as **Theorem 2.1**. Each is followed by the points a student actually needs:
the population's shape is irrelevant, the variance must be finite, and the
conclusion is about $\overline{X}$ and not about the observations.

**Tall narrow tables laid across.** User: Example 1.45's table leaves a lot of
space. It was 3 columns by 7 rows; transposed it is 8 by 3 and uses the width.
Applied to three more of the same shape (the median example's grouped table and
cumulative-frequency table, the nine-samples table). The distributions reference
table was left alone — its first column is long text, which does not transpose.
Overflow checked afterwards, since wider tables are exactly what would break the
mobile layout: 41 pages, none overflowing.

That sweep turned up **another right-answer-wrong-working**: the sampling
distribution mean printed $(2+3+4+3+5+5+4+6)/9$ — eight terms for nine samples,
totalling $32$, which gives $3.56$. The printed answer $4$ requires the correct
sum $36$.

**Build timeout raised, 600s to 1800s.** The probability notes run to ~300 pages
and take about seven minutes alone; built straight after the statistics course
they went past ten minutes and `timeout` killed make4ht mid-conversion, leaving
zero HTML files and a log with no errors in it. Nothing was wrong with the
document. A backstop meant to catch a hang should not be tight enough to cut off
a legitimate build — and when it does, the failure looks like a mystery rather
than a timeout.

### 2026-08-01 (night, last) — Ellipses typed as literal dots

User: replace the manually typed dots with `\cdots`. Seven in the statistics
notes, run lengths from 7 to 15 dots — `+.............+`, `+...............+`.
A literal run sets at the baseline with no spacing around it, so it sits low and
crowds whatever it joins.

Applied the standard distinction rather than one command everywhere:

- **`\cdots`** between operators or terms — `X_1 + X_2 + \cdots + X_n`;
- **`\ldots`** after a comma — `\mu_1, \mu_2, \ldots, \mu_k`.

`\cdots` in a comma list would sit the dots too high, which is the same kind of
fault as the literal ones.

**Probability's 7 were deliberately left alone.** They are `samples at={0,1,...,15}`
in pgfplots options and one code comment — not maths, and rewriting them would
break the plots. Worth remembering before running this as a blanket substitution.

One error surfaced while checking a converted line: "The $k$ parent population …
with respective means $\mu_1, \mu_2, \ldots, \mu_n$" — with $k$ populations the
last mean is $\mu_k$. Fixed, and "population" made plural.

### 2026-08-01 (night, later) — Tables with columns nobody filled in

Continuing the sweep for the presentation faults the user has been naming.
Wrote a check that reports any `tabular` column empty in every data row.

**One real hit**, and it is the "tables without the missing values filled in"
complaint exactly: the goodness-of-fit table for the coin data had **both**
right-hand columns — $(O-e)^2$ and $(O-e)^2/e$ — blank on all five rows, while the
total row confidently printed $\chi^2=4.625$. The total is correct; the work
behind it was simply never written down. All five rows are now filled
($25, 36, 36, 25, 0$ and $2.500, 0.900, 0.600, 0.625, 0$), the $e$ column made
consistent (three rows read `= 60` with no $160\times P(x)$ prefix), and a proper
total row added.

**One more missing square**, of the same family as the $\mu_2$ and ANOVA ones:
$$\sigma=\sqrt{\frac{\sum f(X-\overline{X})}{\sum f}}$$
with no square on the deviation. As printed the numerator is identically zero.
Its own table column is headed $f(X-\overline{X})^2$ and sums to $8.90$, which the
line then uses — so again the answer came from the right quantity and the printed
formula from the wrong one.

The one other flagged column was a false positive: a stem-and-leaf plot has
ragged rows by nature. Checked its 23 leaves against the source data; correct.

> **Column-completeness is worth checking mechanically.** A blank column reads as
> deliberate white space, and the total underneath makes the table look finished.

### 2026-08-01 (night) — Headings that were not headings; a broken chi-square test

Following the same thread as the variance formulas: swept both courses for the
rest of the "typed to look like structure" pattern.

**Twelve bold pseudo-headings** in the statistics notes — `\textbf{Quartiles}`,
`\textbf{Chi-Square Tests}`, `\textbf{Stem-and-Leaf Plots}` and so on. None was
numbered, none appeared in the sidebar, so a reader could not navigate to any of
them. Ten are now `\subsubsection`. The two left are genuine labels, not headings.

**Three of them could not be promoted until a structural fault was fixed.**
`\subsection{Measures Of Central Tendencies}` wrapped Mean, Median and Mode as
three `\item`s of a **614-line enumerate**. That is why they were bold text
instead of headings: a section cannot open inside a list item. They are now
`\subsubsection`s and the enumerate is gone. Neither course now has any list
longer than 150 lines.

`\textbf{Quartiles}` was renamed to "Quartiles for grouped data" — promoting it
verbatim would have put two identical entries in the sidebar, since a full
`\subsection{Quartiles}` follows later.

**The contingency-table test was wrong in every number.** It was loose exposition
with no example or solution wrapper, and:

| printed | correct |
|---|---|
| Kabwata row total 2556 | 2558 ($703+994+861$) |
| $\chi^2 = 33.48$ | $\chi^2 = 103.96$ |
| $\chi^2_{4,0.05}=$ *(blank)* | $9.488$ |
| "F Value = 0.01" | there is no $F$ here; it is a $\chi^2$ test |
| "P-value of 0.01" | $\approx 1.4\times 10^{-21}$ |

The conclusion — reject $H_0$ — was right, and every number supporting it was
wrong. Now an example with a full solution: expected-frequency table, the
statistic, the critical value, and a closing paragraph reading off *where* the
association lies (three cells contribute $82.9$ of the $103.96$; the compounds
differ in the balance of detached houses against flats, not across the board).

> **A right conclusion is not evidence of right working.** This block would pass
> any reading that checks only whether the verdict looks sensible.

### 2026-08-01 (evening, later) — The five variance forms, presented properly

User: the formulas after "…and it is exactly why the coded method exists" are
unprofessionally presented. They were on the **Percentiles** page.

Five alternative forms for the variance were typed as display maths hand-numbered
`(1). (2). (3). (4). (5).` with `\hspace{2cm}` faking the alignment, and form (2)
was not a formula at all but a five-line derivation wedged into the same list. So
the list read as four formulas and one lump of algebra.

Now a real `enumerate`, each form with a sentence saying **when you would use it**
rather than just what it is, and the derivation lifted out into a `proof`
environment after the list. A closing note points at the two steps that are
usually got wrong: $\overline{X}$ is constant so it comes out of the sum, and
$\sum X = n\overline{X}$ is what turns the middle term into $2n\overline{X}^2$.

Searching for the same hand-numbering pattern across both courses found exactly
one more instance, and it carried two real errors:

- `\widehat{S}=\sqrt{\dfrac{\sum(X-\overline{X})^2}{n=1}}` — **`n=1` for `n-1`**;
- `S=\dfrac{\sqrt{\sum(X-\overline{X})^2}}{n}` — the root covered only the
  numerator, so it was not a standard deviation at all;
- and it was labelled **(2)** while its own data ($n=13$) is part **(3)** of the
  question, the thirteen ball bearings.

That block had also spilled outside its `solution` environment; it now closes
around the whole answer.

> **Hand-numbered display maths is worth grepping for as a class.** `$$(1).` and
> friends are a reliable marker for "this list was never really a list", and in
> both instances found here the presentation problem sat on top of a maths error.

### 2026-08-01 (evening) — Median Example 1 rebuilt; two more boundary errors

User flagged the median / interquartile-range Example 1 as poorly done. It was,
and not only in presentation.

**The question** asked "Find the medians" over three parts, but only (b) and (c)
were labelled — part (a) was an `\item` rendering as "1.", and (b) and (c) were
literal text wedged into a single table float with `\hspace`, side by side.

**The solution** was worse:
- part (a) listed the sorted data as **seven** values when the question gives
  **eight** — a 15 was dropped. The printed answer 20 is the eight-value answer,
  so the working contradicted its own result;
- part (b) printed `n=1` where $n=\sum f=15$;
- **part (c) was never answered at all**;
- and the block then ran on into two unrelated sections of new exposition.

All three parts are now worked, each table captioned, and part (c) shows why the
answer lands exactly on a class boundary (the cumulative frequency reaches $n/2$
precisely at the end of that class) and why the boundaries are $0.5, 5.5, 10.5$
when the classes read $1-5, 6-10$.

Also fixed the interpolation diagram, which labelled $B$ as $(1.3,29)$ where the
table says $13.95$, and $E$ as $(m,205)$ for $(m,25)$. The similar-triangles step
asserted $m=13.06$ with no working; it now derives it, and the point is made that
this *is* the grouped-median formula read off a picture.

**Two more boundary errors from the environment conversion**, both found by
searching for a `\textbf{...}` pseudo-heading trapped inside a worked block:

> the median solution had swallowed "median from a frequency table for discrete
> data" and "Median of a Continuous Data"; the LSD solution had swallowed
> "Design of Experiments" and its table.

That check — *a heading inside a solution means the solution ran too far* — is a
better detector than block length, because these blocks were not unusually long.
Worth running after any change that infers where a block ends.

### 2026-08-01 (later still) — Both courses now use the same environments

User asked why examples were not uniform: `\begin{example} … \end{example}` and
`\begin{solution} … \end{solution}`, the way the probability notes already did
it. Correct, and my earlier reasoning against it was wrong.

**Statistics was genuinely mixed** — 20 `example_` environments *and* 25 bare
`\textbf{Example}`; 35 `solution` and 22 bare. So the same page could show a
numbered, ruled example next to an unnumbered bold word.

**All 63 bare markers converted.** Also renamed `example_`, `definition_`,
`remark_`, `note_` to the unadorned names probability uses, with the same
`thm`-based counter structure. Probability's 6 `\begin{proof}[\textbf{Solution}]`
became `\begin{solution}`, and its 2 inline `\textbf{Note:}` became `note`.
**Both courses are now at zero bare markers**, same environment names, same
counters.

`tag_bold_markers()` and the `.mk` CSS are deleted. What remains is the check,
which now warns about *any* bold marker word that is not an environment.

**One structural fix this required**: the grouped-data mode list opened a
`\begin{enumerate}` that was closed only 42 lines later, after the worked example
*and* its solution — so both sat inside a bullet list. This is the "unclosed list"
I cited in a previous commit as the reason conversion was unsafe. It was one list,
and closing it where it actually ends took two lines.

**The boundary rule took two goes, and the first was quietly wrong.**

> My first algorithm took the *largest* balanced end before the next heading.
> Where a solution is followed by figures with no heading between, that swallows
> them: one solution ran to **306 lines** and absorbed an entire subsection of
> continuous-data figures, and **four `example` blocks swallowed their own
> `solution`**, which should be siblings. The build did not care — the LaTeX was
> still balanced, so it compiled and rendered without complaint.
>
> Caught by listing every block over 25 lines with its first and last substantive
> line and reading the tails. A solution ending in "The mode is the most
> frequently occurring value" is not a solution ending.
>
> Correct rule: end at the *first* point where the block balances **and** the
> author left a topic break (three or more blank lines). Largest block is now 89
> lines, no example contains a solution.

> **Balanced is not the same as correct.** A structural check that passes tells
> you the file compiles, not that the boundaries are where they belong. For
> anything that infers extent from layout, list the results by size and read the
> edges of the biggest ones.

### 2026-08-01 (later) — A marker after `\\` is silently not a marker

User spotted an `Example` on the Moments page that had no label and no number,
while every other example on the page had both. The maths was fine and the
solution was there; the *heading* had come loose.

**Cause.** `tag_bold_markers()` in `site/build.py` matches
`<p class='noindent'><span class='cmbx…'>Example</span>`. A marker only becomes
its own paragraph if a **blank line** precedes it in the `.tex`. After `\\` it
stays inside the running paragraph, tex4ht emits it as an inline `<span>`, and
the regex never sees it — no label, no rule, no number, and the example is
skipped by the counter so every later example on that page is misnumbered too.

Nine markers in the statistics source were affected. **One of them I introduced
myself** in the previous commit, adding a `Solution` label directly under a line
of given data with no blank line. So this is not a legacy-notes problem — it is
a trap for anyone editing these files, including me.

**The build now reports it.** `report_stray_markers()` warns with the page name
and the fix. Verified both directions: silent on correct source, and it names
`intro_statssu15.html` when the bug is deliberately reintroduced.

Getting the check right took three attempts, which is the part worth remembering:

1. First version flagged **43** in the probability course. All false — that course
   uses real `\begin{solution}` environments, which render inside
   `<span class='head'>` and are already styled by `tag_theorems()`.
2. Excluding `class='head'` within 80 characters left **7** still false. tex4ht
   pads output with runs of whitespace hundreds of characters long, so a fixed
   lookback window misses the very thing it is looking for.
3. Anchoring to the enclosing `<p` instead of a character count gives **0** false
   positives on both courses. Also skips `(Exercise)`-style inline parentheticals.

> **A checker that reports clean proves nothing until it has been shown to fail
> on a known-bad input.** Same lesson as the overflow checker in `.viewport/`.

### 2026-08-01 — Captions settled; every unsolved example resolved

**Caption policy is written down** in `.viewport/CAPTIONS.md`. Every figure gets one;
tables only when the table is a *thing* rather than the *working*. The test: if removing
the surrounding text leaves the table meaningless, caption it. Statistics went from 0/42
figures captioned to 42/42; probability was already 31/38.

**All 12 unsolved examples resolved.** Nine were false alarms — worked but never labelled
`Solution`, or not examples at all (a list of continuous variables, two illustrations of
how to write H0/H1). Two were genuinely unfinished and are now worked in full.

**A second recurring pattern, alongside the "loose statement first" one below.**

> **Orphan data.** A dataset is presented under `\textbf{Example}` and then never used.
> Found three times now: the bar-chart 18 values, the ANOVA `F1/F2/F3` table, and the
> sit-ups data. Each time the surrounding prose reads fine, so it survives proofreading.
> **When auditing a course, list every table and check something downstream consumes it.**

> **Answers computed from numbers that are not the ones printed.** The Type II error
> example printed z = −1.26 but its answer 0.8925 is the area for −1.24. The printed
> answer was right and the printed working was wrong, which is the hardest kind to catch
> by reading. **Recompute every stated numerical answer, don't check the algebra only.**

**My own error worth recording**: I captioned 42 figures by matching position in the file
to a list I had built from node labels, without opening each drawing. Eleven were wrong —
a box plot captioned as a stem-and-leaf plot, and six correlation diagrams labelled
strong/weak where the pictures say perfect/fair. **A caption asserts something about the
picture; it has to be read off the picture.** Corrected the same day, but it was live for
one commit.

Also fixed: deciles labelled `D_25, D_50, D_75` (deciles divide into ten parts, so those do
not exist), the ANOVA sum-of-squares proof abandoning its cross-product term rather than
showing it is zero, and LSD using 1.96 one line below quoting t = 1.943.


### 2026-07-31 (latest) — Tutorial sheets found and added; Chapter 1 problems complete

**Repository is now on GitHub**: `github.com/nephatmwanza/maths-notes`, **private**, branch
`main`. Name is deliberately provisional — nothing depends on it, rename freely. (The user
is considering `wj-…`; undecided.) A `git bundle` snapshot also sits in
`~/Backups/` for Google Drive; verified restorable, all 106 tracked files byte-identical.

**The tutorial sheets are the better source, and they were being missed.**
`~/LaTeX_Projects/Introduction to Probability 2026/` holds `Tutorial_Sheet_1..4.pdf`
(Feb–March 2026, last semester) — **49 questions**, already grouped one sheet per block of
the syllabus, and the thing students actually work through. Prefer these over the exam
papers. Extracted to `courses/introduction-to-probability/problems/tutorial_sheet_*.txt`.

| Sheet | Qs | Topic | Maps to |
|---|---|---|---|
| 1 | 12 | sample spaces, axioms, counting | §1.2–1.3, §1.5 |
| 2 | 14 | conditional probability, Bayes; then discrete/continuous r.v.s, c.d.f. | §1.4; ch.2 |
| 3 | 11 | m.g.f.s, named discrete distributions | §2.4, §2.5 |
| 4 | 12 | named continuous, joint distributions, covariance | §2.6, ch.3 |

**Two source-editing traps, both hit while doing this — read before bulk-editing the .tex:**

1. **`...` inside `samples at={0,1,...,15}` is pgfplots range syntax, not maths.** Converting
   it to `\ldots` as a typography fix breaks the build with a confusing
   `Missing \endcsname` error pointing at an unrelated `hypergeom(...)` line. Only convert
   `...` to `\ldots` in prose and maths, never inside a tikz/pgfplots option.
2. **Never use `\s*` in a regex over the `.tex`** — it matches newlines and will silently
   join two lines. Anchor patterns within a single line.

`site/make-course.sh` catches both by failing loudly and refusing to leave a stale
`build/`. Trust it rather than eyeballing the output.

**`pdftotext` silently drops set symbols — always render the page.** Sheet 2 Q5 extracts as
`P(A  B) = 1/3`, which is unsolvable as printed: with `P(A|B)=5/14` it forces
`P(A∪B) > 1`. The PDF actually shows `P(A ∩ B′)`, and it then works out cleanly.

    pdftoppm -png -r 130 -f 1 -l 1 Tutorial_Sheet_2.pdf out

**Assignment 1 duplicates Tutorial Sheet 1** — 7 of its 15 questions are the same
questions. Transcribe once, cite the sheet. Check `problems/README.md` before adding.

**Done — 56 problems. Chapter 1 complete; all four Tutorial Sheets complete.**

| Section | Problems |
|---|---|
| §1.3 Definitions and Axioms | 7 |
| §1.4 Conditional probability & Bayes | 13 |
| §1.5 Counting Techniques | 9 |
| §2.2 Discrete Random Variables | 1 |
| §2.3 Continuous Random Variables | 2 |
| §2.4 Expectations and generating functions | 5 |
| §2.5 Named discrete distributions | 7 |
| §2.6 Named continuous distributions | 6 |
| §2.7 Cumulative Distribution Function | 1 |
| §3.2 Joint Distributions | 4 |
| §3.3 Conditional functions and independence | 1 |

**Remaining:**

1. **Assignments 2–4 (12)** → chapters 2–3. **Dedupe against Sheets 3 and 4 first** —
   Assignment 1 turned out to be 7/15 duplicates of Sheet 1, so expect overlap here too.
2. **Exam papers** — the user has said *ignore for now*. They are also not separable at
   question level (see the earlier entry).

**A second false statement found in the source material.** Sheet 4 Q11(c) asks for a proof
that $\rho(aX+b, cY+d) = \rho(X,Y)$. That holds only when $ac>0$: in general
$\rho = \operatorname{sign}(ac)\,\rho(X,Y)$, since $\operatorname{sd}(aX+b)=|a|\operatorname{sd}(X)$.
Verified numerically — with $a=-2$, $c=5$ the correlation flips sign. The solution proves
the correct statement and flags the exception rather than "proving" something false. This
is the second such case after the Vandermonde identity; **do not assume a printed identity
is true — check it.**

**Verification is not optional.** Every answer written so far was checked computationally
before being written down — exhaustive enumeration where the space allows (all 15 gender
arrangements, all 210 committees, all 24 die-and-coin outcomes, every ordered triple from
the ball box, all 30240 arrangements of EXCELLENT), exact rational arithmetic otherwise.
This is what has been turning up the errors in the notes; keep doing it.

**Style note for solutions.** Where the arithmetic is the easy part, say the thing students
actually miss. Two examples now in §1.4: why drawing without replacement leaves
`P(second is white)` equal to `P(first is white)`, and why a 98%-sensitive test still
returns almost nothing but false alarms for a disease affecting one person in ten thousand.


### 2026-07-31 (latest) — Past-paper practice problems; corrections found by verifying the maths

**The new direction (user's idea, 2026-07-31):** turn the tutorial/past-paper problems
into *the* solved problems on the site, **grouped by topic**, because —

> "one of the issues learners have is identifying on which topic is the question coming from"

That is the product insight. The solutions are the draw; the topic labelling is the thing
nobody else provides.

**Source material.** `/home/corban/LaTeX_Projects/Introduction To Probability Exam
Questions/` — 11 papers (4 assignments, a quiz, 3 tests, 3 exams), **57 top-level
questions, 469 items including parts. Questions only, no solutions.**

**Critical scoping finding — tag at sub-part level, not question level.** The assignments
and quiz contain clean single-topic questions. The *exam* papers do not: a single
"question" is typically "(a) define … (b) prove … (c) compute …" and spans four or five
topics. A keyword classifier put 39 of 57 questions in multiple topics and 9 in none —
which is itself evidence for the user's point: if a matcher cannot place these, students
certainly cannot. **The unit of work is the sub-part.** Rough topic spread across the 57
questions (a question can touch several): expectation 33, continuous r.v. 26, conditional
25, joint 17, named continuous 13, counting 12, c.d.f. 11, axioms 10, named discrete 10,
inequalities 4, discrete r.v. 4.

**Mechanism, built and working.** In the LaTeX preamble:

```latex
\begin{problem}{Examination}  ... \end{problem}
\begin{solution}              ... \end{solution}
```

`problem` records provenance (shown as a `[Examination]` tag). `build.py` collapses each
solution that follows a problem into a `<details>` — no JavaScript, works without it,
keyboard- and screen-reader-accessible. Worked examples in the body of the notes are
exposition and stay open; only problem solutions collapse.

**Done so far:** section 1.5 (Counting Techniques) has five past-paper problems with full
solutions. **Remaining: the other ten topics.** Suggested order — counting (done),
conditional probability/Bayes, expectation, named discrete, named continuous, joint.

**Verification is now part of the job.** Every answer written was checked by *exhaustive
enumeration*, not by re-deriving it — all 9! arrangements of FACETIOUS, all 30240 of
EXCELLENT, all 2520 of BIOLOGY, counted directly and compared against the closed form.
Do this for every solution added; it is cheap and it is the only thing that makes the
site trustworthy.

**Errors found in the existing notes by doing this** (all fixed):

| Where | Error |
|---|---|
| Remark 1.5.8 (4) | Vandermonde stated as $\binom{m+n}{n}$; it is $\binom{m+n}{k}$. The stated form fails in 222 of 510 cases for $m,n\le 6$. |
| Example 1.5.9 | "at most 2 defectives" read $\binom50+\binom51+\binom42$; last term is $\binom52$ (gave 12, not 16). |
| Remark 2.4.19 | `d^^2` is a LaTeX escape, not $d^2$ — printed raw source. Same line differentiated w.r.t. $X$ instead of $t$. |
| Total probability example | intermediate line `0.0125+0.140+0.080` sums to 0.2325, not the 0.0345 concluded. Products are 0.014 and 0.008. |
| Exponential warranty (ii) | dropped the minus sign from the antiderivative (part (i) had it right). |
| Multinomial example | missing `!` on $k_3$; $P^7$ subscripted `{1,2}` instead of the group sizes `{3,2,2}`. |

Checked and **correct**: all other Remark 1.5.8 identities, the two hypergeometric
identities, every numeric answer in the document (Bayes 0.0345/0.246, binomial 0.26272,
Poisson 0.1563/0.9084/0.3134, normal 0.1357/0.0228/0.8211/0.8164, hypergeometric
0.07022/0.584/0.9934/0.0769, licence plates 1 757 600), and all four probability tables
(each sums to 1 with correct marginals). The 24 listed permutations of $\{p,q,r,s\}$ taken
3 at a time are the complete distinct set.

**Blank figures were not empty.** Figures 2.27–2.29 shaded regions under the normal curve
with TikZ `pattern=north east lines`, which tex4ht cannot convert — the same defect class
as the `pattern=dots` fixed earlier. Solid translucent fills in the house palette; 36 → 41
SVGs. These are the diagrams that teach z-table reading, so they were worth repairing
rather than deleting. Every figure and table in the document now has a real caption.

**Also:** tables and the arrangements list are centred (they always carried `\centering`;
the CSS that made them scrollable also made them fill the line). Several `tikzpicture`
environments set `[->]` as the default for *every* path, which put an arrowhead on the peak
of the bell curve.

**Open question for the user:** these are past papers. Fine to publish with solutions, but
worth a sanity check that none are *current* assessed coursework before going live.


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
