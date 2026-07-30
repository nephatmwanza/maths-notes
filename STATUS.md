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

## Scope rule — settled, do not revisit without the user raising it

**Only the 61 authored `.tex` files are in scope for the web app.** The reference PDFs
sitting alongside them are other people's copyrighted material and must not be republished,
converted, or otherwise built into any public-facing product. This was flagged and agreed
on 2026-07-30, before any brainstorming started.

## Current phase

**BRAINSTORMING.** No decisions have been made yet on audience, format, or technology. No
code, no build, no content has been touched. The three open questions below are what the
brainstorm needs to resolve before any building starts.

## Open questions

1. **Audience** — the user's own students (a companion to lectures), the general public
   (a portfolio/reputation piece, parallel to the climate site), or a paid/gated product?
   This last option connects to an earlier side conversation about serving *local* Zambian
   MSc/BSc students directly.
2. **What "interactive" means** — a clean searchable/browsable notes site (documentation
   style), a quiz/practice engine built from the exam-question banks with revealable
   solutions, or something more ambitious?
3. **Free and open, or gated/paid?** Affects hosting, whether accounts/payments are needed,
   and how much of the 61 documents ship at launch versus later.

## How to resume this project cold

1. Read this file top to bottom.
2. Check the Status Log below — the most recent entry is where things actually left off.
3. Once there is code: check `git log` in this directory for the detailed history.
4. Do not assume anything happened that isn't recorded here or in git — if it's not
   written down, treat it as not done yet.

---

## Status Log

*(most recent first — append new entries, never rewrite old ones)*

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
