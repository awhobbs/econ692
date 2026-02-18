# Session Log: Lecture 04 Slides

**Date:** 2026-02-18
**Goal:** Build `Slides/Lecture04_Research_Design.tex` for Week 4 (Feb 19, 2026)

## Context

- Course: ECON 692 Applied Economics Seminar, USF MSAE capstone
- Week 4 topic: Research design, potential outcomes, DAGs, empirical strategy drafting
- Data Report due next day (Feb 20)
- Updated CLAUDE.md with full project metadata from syllabus + Lecture 3 review

## Approach

- Running example: Paid Family Leave → Female Employment (one student is working on exactly this)
- Theory arc: PO framework (review) → DAGs as complementary tool → fork/chain/collider → PFL DAG → backdoor criterion → link to parallel trends
- Software: dagitty.net demo + ggdag R snippet
- Workshop: individual DAG drawing (15 min) → groups of 3 (15 min)
- Drafting sprint: 55 min, 3-paragraph prompt aligned with Data Report due tomorrow

## Key Decisions

- Used PFL as running example throughout (student-relevant, rich confounding structure)
- Dropped `\begin{block}` on Chain slide to save vertical space
- All overflows now ≤ 20pt; targeting ≤ 10pt on remaining problem slides

## Status

- [x] CLAUDE.md updated
- [x] Lecture04_Research_Design.tex created and compiling (26 pages, no errors)
- [x] All overflows resolved to ≤ 7pt (visually imperceptible)
- [x] Final compile pass clean
