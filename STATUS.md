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

**SCOPING / PRE-BUILD.** Audience, interactivity, and the free/paid phasing are now
decided (see Decisions below). Not yet decided: which course to build first, the exact
quiz interaction model, and the technical stack. No code, no content conversion, no build
has started.

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

## Content reconciliation process — the Dr Nawa problem

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

## Open questions

4. **Which course to build first?** Two candidates, both live — the user is tutoring both
   this semester:
   - **Introduction to Statistics** — user's own notes AND exam questions both exist as
     `.tex` (2020, dated but complete as a pair). Best candidate to prove the *whole*
     pattern (notes + quiz engine) end to end, since both halves already exist in some form.
   - **Mat1110** — recent (Jan 2026) authored notes exist, but no exam-question companion
     has been located under an obviously matching name yet. Possibly the same course as the
     folder "Analytic Geometry and Calculus Exam Questions" under UNZA's course-code
     naming — **needs the user to confirm this mapping**, not assumed.
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
