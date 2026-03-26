# Plan: Lecture 06 — EDA & Early Figures

**Status:** DRAFT
**File:** `Slides/Lecture06_EDA_Figures.tex`
**Session:** Thursday March 5, 10:00am–12:00pm, LM 244B (2-hour replacement)

---

## Context

Week 6 topic is "Exploratory data analysis; early figures." Empirical Strategy Draft is due the next day (Friday March 6). This is a shorter 2-hour morning session replacing the usual 4-hour evening class. Students have built cleaning pipelines (Week 5) and need to transition to looking at their data and polishing their drafts.

---

## Slide Plan (~21 content frames + title + 3 auto-section slides)

### Opening (10:00–10:10)
| # | Title | Notes |
|---|-------|-------|
| 1 | Title page `[plain]` | Date: March 5, 2026 |
| 2 | Today's Agenda | Times start 10:00 (not 4:35) |
| 3 | Check-in | 3 project questions + block reminder: draft due tomorrow |

### Section 1: EDA for Causal Inference (10:10–10:40, 30 min)
| # | Title | Notes |
|---|-------|-------|
| 4 | Learning Objectives | 3 objectives linking cleaning → EDA → identification |
| 5 | EDA Is Not Just Description | Two-col: descriptive vs. causal EDA |
| 6 | The Pre-Trends Plot | **TikZ diagram**: treated (green) vs. control (gray) lines, dashed treatment line, τ̂ arrow |
| 7 | Four Key EDA Checks | Table: pre-trends, balance, panel structure, outliers |
| 8 | Summary Statistics: What to Report | Two-col + R code snippet `[fragile]` |
| 9 | The Event Study Plot | Two-col: description + **TikZ schematic** (dots + CI bars) |
| 10 | EDA Checklist | 5-item checklist before running models |

### Section 2: Early Figures Workshop (10:40–11:00, 20 min)
| # | Title | Notes |
|---|-------|-------|
| 11 | Workshop: Your First EDA Figure | Green timer "20 minutes." Task A: pre-trends plot, Task B: summary stats |
| 12 | Starter Code: Pre-Trends Plot | `[fragile]` ggplot2 template (~15 lines) |
| 13 | Figure Quality Standards | Two-col: common problems vs. fixes |
| 14 | Saving Figures Reproducibly | `[fragile]` ggsave() pattern |
| 15 | Workshop Share-out | 2 volunteers show plots, group feedback |

### Section 3: Work Sprint (11:00–11:50, 50 min)
| # | Title | Notes |
|---|-------|-------|
| 16 | Sprint Goals | Green timer "50 minutes." Track A (EDA) / Track B (draft polish) |
| 17 | Using Claude Code for EDA | Prompt patterns table |
| 18 | Empirical Strategy Draft: What It Should Contain | 5-component checklist |

### Wrap-up (11:50–12:00)
| # | Title | Notes |
|---|-------|-------|
| 19 | Sprint Checkpoint | 5 self-check questions |
| 20 | Key Takeaways | 4 numbered items |
| 21 | Wrap-Up & Next Week | Draft due tomorrow; Week 7 = methods workshop |

---

## TikZ Diagrams (2)

1. **Pre-trends chart** (Frame 6): Two lines over ~6 time periods, vertical dashed treatment divider, τ̂ arrow. Reuse L03 DiD idiom.
2. **Event study schematic** (Frame 9): Dots + CI bars at integer relative-time positions, dashed vertical at t=0. Pre-period near zero, post-period positive.

## Code Frames (3, all `[fragile]`)
- Frame 8: R summary stats by group (6 lines)
- Frame 12: ggplot2 pre-trends template (~15 lines)
- Frame 14: ggsave() pattern (4 lines)

---

## Verification

1. Compile with 3-pass XeLaTeX (no bibtex needed unless we add citations)
2. Check PDF renders ~25 pages (21 content + title + 3 section slides)
3. Verify no overfull hbox warnings on content slides
4. Run proofread agent for typos/overflow
5. Visual audit for layout consistency

---

## Files to Create/Modify

- **Create:** `Slides/Lecture06_EDA_Figures.tex`
- **No bib changes needed** (no citations planned)
