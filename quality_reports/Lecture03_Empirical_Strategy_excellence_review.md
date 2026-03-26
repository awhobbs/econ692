# Slide Excellence Review: Lecture03_Empirical_Strategy.tex

**Date:** 2026-02-11
**File:** `Slides/Lecture03_Empirical_Strategy.tex`
**Slide count:** 34 (30 content + 4 section dividers)
**Agents completed:** Visual Audit, Pedagogy Review, Proofreading, TikZ Review
**Agents partial:** Substance Review (rate-limited before completing)

---

## Overall Quality Score: GOOD

| Dimension | Critical | Medium | Low |
|-----------|----------|--------|-----|
| Visual/Layout | 2 | 13 | 14 |
| Pedagogical | 1 | 5 | 3 |
| Proofreading | 0 | 4 | 6 |
| TikZ | 1 | 3 | 2 |
| **Totals** | **4** | **25** | **25** |

---

## Critical Issues (Immediate Action Required)

### C1. No Worked Examples for Any Method (Pedagogy)
The entire Methods Overview (slides 5-14, ~10 content slides) contains zero worked examples. Not one concrete numerical calculation. DiD is defined, its assumption stated, and usage criteria listed across three consecutive definitional slides with no example. SC and SDID follow the same pattern.

**Fix:** Add at minimum a 2x2 DiD calculation: "Treatment group: wages $8 pre, $10 post. Control group: wages $7 pre, $8 post. DiD = (10-8) - (8-7) = 1." This takes one slide. For SC, a toy example showing weights would be ideal.

### C2. DiD TikZ Arrow Misplaced (TikZ)
The treatment effect arrow in the DiD diagram goes from (4.2, 3.0) to (4.2, 4.35), but the counterfactual line at x=4.2 is at y=2.85 (computed: 2 + 0.5*(4.2-2.5) = 2.85). The arrow bottom is 0.15 units too high. This makes the displayed treatment effect 1.35 instead of the correct 1.5. The arrow should start at (4.2, 2.85).

**Fix:** Change `\draw[red, thick, <->] (4.2,3) -- (4.2,4.35)` to `\draw[red, thick, <->] (4.2,2.85) -- (4.2,4.35)`.

### C3. DiD Setup Equation May Overflow Column (Visual)
The displayed equation `(\bar{Y}_{T,\text{post}} - \bar{Y}_{T,\text{pre}}) - (\bar{Y}_{C,\text{post}} - \bar{Y}_{C,\text{pre}})` is ~20em wide inside a 0.55-width column (~8.7cm), risking overfull hbox.

**Fix:** Move equation below the columns environment to span full `\textwidth`, or use `\small` on the equation.

### C4. Continuous Treatments Slide 13 Overloaded (Visual)
Slide 13 has intro text, 2-item bullet list, displayed equation, problem statement, 3-item list with nested 2-item sub-list, and a final bullet -- approximately 15+ lines of content.

**Fix:** Split into two slides: (A) "The Standard Approach" -- intro, examples, TWFE equation; (B) "The Problem with TWFE" -- Callaway citation, negative weights, level vs. causal responses.

---

## High-Priority Issues (Should Fix)

### H1. No Socratic Questions in Technical Content (Pedagogy)
The Methods Overview section (10 slides) contains zero embedded thought-provoking questions. All questions are either discussion check-ins (slide 3) or activity prompts (slide 17).

**Fix:** Add 2-3 questions: After parallel trends: "For your project, what would violate parallel trends?" After the Comparison table: "Which method fits your data structure?"

### H2. Visual-First Violated: Diagrams on Right, Text on Left (Pedagogy)
On both DiD and SC Setup slides, the TikZ diagram is in the RIGHT column while definitions/formula are in the LEFT column. Students read left-to-right, encountering notation before the visual.

**Fix:** Swap column order (diagram left, definitions right), or present diagram on standalone slide first.

### H3. No Visual Support for SDID (Pedagogy)
SDID is the most complex method presented and has zero visual support -- no diagram, no figure, entirely text.

**Fix:** Add a simple schematic showing unit weights + time weights (e.g., a grid with highlighted rows/columns).

### H4. "Treated" Label Overlaps Vertical Dashed Line in SC Diagram (TikZ)
In the SC diagram, `\node[usfgreen, above] at (2.5,2.6)` places "Treated" centered on x=2.5, but the vertical dashed treatment-time line also passes through x=2.5. The dashed line cuts through the middle of the label text.

**Fix:** Move label to `\node[usfgreen, above left] at (2.3,2.6)` or use a white background fill: `\node[usfgreen, above, fill=white, inner sep=1pt]`.

### H5. Missing Counterfactual Label in DiD Diagram (TikZ)
The dashed green counterfactual line has no label. Students won't understand what it represents.

**Fix:** Add `\node[usfgreen, right, font=\footnotesize] at (4.5,3) {Counterfactual};`

---

## Medium-Priority Issues (Next Revision)

### Visual/Layout

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| M1 | No transition slides within Methods Overview | Slides 5-14 | Add standout slide before Continuous Treatments |
| M2 | DiD Key Assumption slide too dense | Slide 7 | Split: assumption + testability on one slide, staggered treatment warning on another |
| M3 | Choosing Packages: 7 stacked items | Slide 18 | Use two-column layout (R left, Python right) |
| M4 | Seven consecutive "Step N" Git slides | Slides 23-29 | Add progress indicator or checkpoint slide between Steps 3-4 |
| M5 | Zero `\includegraphics` in entire deck | Global | Add at least a GitHub UI screenshot for Git section |
| M6 | Inconsistent `\vspace` usage | Global | Standardize: 8pt for section breaks, 4pt for tight breaks |
| M7 | Font size inconsistency across tables | Slides 2,12,14,30 | Use `\small` for all tables consistently |
| M8 | No semantic color in Git comparison | Slide 21 | Red for "Without" column, green for "With Git" column |
| M9 | Wrap-Up slide dense with three separate lists | Slide 34 | Reduce `\vspace{12pt}` to `\vspace{6pt}`, merge "Due" and "Before next class" |
| M10 | `\small` + `\footnotesize` double reduction | Slide 14 | Keep table at `\small`, widen columns slightly |
| M11 | Missing bridge slide before Workshop | Between slides 14-15 | Add "Now let's apply this to YOUR project" transition |
| M12 | No deck takeaway slide | End | Add "Today you learned..." before logistical wrap-up |

### Pedagogy

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| M13 | TWFE equation introduces 7 symbols at once | Slide 13 | Build up with underbrace decomposition or define terms beforehand |
| M14 | No progressive builds (split-slide) anywhere | Global | Use 3-4 problem-then-solution slide pairs |
| M15 | No sub-method transitions | Within Section 1 | Brief cues when shifting DiD -> SC -> SDID |
| M16 | Narrative doesn't tie back to opening | Slide 34 | Revisit "How do you identify a causal effect?" |

### Proofreading

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| M17 | `fixest (Sun & Abraham)` misleading | Line 140 | Change to `fixest::sunab()` or just `fixest` |
| M18 | Contractions in academic slides | Lines 276, 324, 485, 633 | `aren't` -> `are not`, `Don't` -> `Do not`, etc. |
| M19 | No `\cite{}` commands; all inline text refs | Global | Replace with proper `\cite{}` or `\textcite{}` |
| M20 | Inconsistent "pre-treatment" vs "pre-period" | Throughout | Standardize on one term |

### TikZ

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| M21 | SC pre-treatment lines overlap identically | Diagram 2 | Draw solid green on top of dashed gray, or slightly offset |
| M22 | `red` arrow not in defined color palette | Both diagrams | Define `\definecolor{effectred}` in preamble |
| M23 | No dots at data points | Both diagrams | Add `\fill` circles at key coordinates |

---

## Low-Priority Issues

| # | Issue | Severity |
|---|-------|----------|
| L1 | `na\"ive` could use Unicode `naïve` with XeLaTeX | Low |
| L2 | "Weaker than both" in comparison table is imprecise for SDID | Low |
| L3 | "Convex hull" used without brief definition | Low |
| L4 | Section title capitalization inconsistent (agenda vs section headers) | Low |
| L5 | `\vspace{12pt}` on Lightning Presentations slide could be 6pt | Low |
| L6 | de Chaisemartin et al. slide doesn't name their specific package | Low |
| L7 | Missing notation refresher for $Y_i(0)$, ATE from Week 2 | Low |
| L8 | $D_i$ used for continuous dose but typically denotes binary treatment | Low |
| L9 | Colon after full author list (line 230) implies direct quotation | Low |
| L10 | Data Sprint slide merges two closing paragraphs | Low |
| L11 | Git install slide URL may be tight in texttt | Low |
| L12 | No `\bibliography` or `\printbibliography` despite project having .bib | Low |
| L13 | SC diagram "Synthetic" label at (4.5,3.4) close to axis edge | Low |

---

## Recommended Next Steps

### Before Teaching (Priority 1 -- Critical Fixes)
1. Fix DiD arrow coordinates (C2) -- 1-minute edit
2. Split Continuous Treatments slide 13 (C4) -- 10-minute restructure
3. Add 1-2 worked examples (C1) -- 15-20 minutes for a DiD numerical example

### Before Next Revision (Priority 2 -- High Fixes)
4. Add counterfactual label to DiD diagram (H5)
5. Fix "Treated" label overlap in SC diagram (H4)
6. Add Socratic questions in methods section (H1)
7. Swap column order on DiD/SC slides (H2)

### Polish Pass (Priority 3 -- Medium Fixes)
8. Standardize contractions, vspace, and terminology
9. Add bridge/transition slides
10. Consider two-column layout for Choosing Packages
11. Add semantic color to Git comparison slide
