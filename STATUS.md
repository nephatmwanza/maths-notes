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

## Open questions

4. **Which course to build first? — Narrowing.** Mat1110 and Introduction to Statistics
   remain the semester's real teaching priority but are both blocked on the user supplying
   current material ("I will get everything this week or as days proceed"). **Introduction
   to Probability has no such blocker and could be started immediately** — proposed in
   this conversation turn, not yet confirmed by the user, as the first real build target:
   it needs conversion but not reconciliation, making it the simplest possible first pass
   at the notes+quiz pattern. Probability Theory (MAT 3902) would be a good *second*
   example specifically because it exercises the reconciliation process, once the simple
   case is proven.
5. **Exact quiz interaction model.** User said: "solve the questions and put them in the
   engine where learners have to search for themselves" — read as: worked solutions exist
   in the system, but the interaction requires the learner to search/attempt rather than
   being handed the answer passively. Needs confirming whether that means (a) an
   attempt-first-then-reveal quiz flow, (b) a searchable bank of solved problems the
   learner browses/searches directly, or (c) both.
6. **Technical approach for the free phase.** Not yet decided. Leaning towards reusing the
   pattern already proven on the climate portfolio site — a static site (the climate site
   uses Hugo + PaperMod, which already has client-side search via Fuse.js) for the notes
   side, plus a lightweight client-side quiz component (question/answer data in JSON, no
   backend) for the engine side. This would let phase 1 be free to host (e.g. GitHub
   Pages) with no accounts or payment infrastructure, deferring that harder problem to the
   paid phase as the user already intends. Not committed — worth confirming before
   building anything.

## How to resume this project cold

1. Read this file top to bottom.
2. Check the Status Log below — the most recent entry is where things actually left off.
3. Once there is code: check `git log` in this directory for the detailed history.
4. Do not assume anything happened that isn't recorded here or in git — if it's not
   written down, treat it as not done yet.

---

## Status Log

*(most recent first — append new entries, never rewrite old ones)*

### 2026-07-30 (latest) — Power cut mid-session; resumed cleanly from this file
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
