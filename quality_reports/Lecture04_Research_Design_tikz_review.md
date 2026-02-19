# TikZ Visual Quality Review: Lecture04_Research_Design.tex

**Date:** 2026-02-18
**File:** `Slides/Lecture04_Research_Design.tex`
**Lines reviewed:** 195–368
**Diagrams reviewed:** 5
**Reviewer:** TikZ Visual Critic (harsh devil's advocate)

---

## Issue Summary

| Diagram | CRITICAL | MAJOR | MINOR |
|---------|----------|-------|-------|
| 1: Three Fundamental Structures (lines 195–231) | 2 | 3 | 2 |
| 2: The Fork: Confounders (lines 240–251) | 0 | 1 | 1 |
| 3: The Chain: Mediators (lines 279–292) | 2 | 2 | 2 |
| 4: The Collider: A Subtle Danger (lines 314–325) | 0 | 2 | 1 |
| 5: The PFL DAG (lines 350–368) | 0 | 3 | 2 |
| Cross-diagram consistency | 1 | 2 | 0 |
| **TOTALS** | **5** | **13** | **8** |

**Verdict: NEEDS REVISION** before the deck is used for publication or video recording. Classroom-ready as-is, but several issues will be visually apparent on projection.

---

## Diagram 1: Three Fundamental Structures (lines 195–231)

### CRITICAL: Chain Diagram Width Causes Severe Visual Imbalance
- **Location:** Lines 209–215, Chain nodes at x=0, 1.6, 3.2
- **Problem:** All three subdiagrams sit in equal 0.32\textwidth columns, but horizontal extents differ radically. At scale=0.75: Fork spans 2.0 units (x: −1 to +1), Collider spans 2.0 units, Chain spans 3.2 units (x: 0 to 3.2) — 60% wider. The Chain overflows its visual column and the three "equivalent" canonical structures look structurally unequal — violating the pedagogical intent.
- **Fix:** Move Chain nodes to X at (−1, 0), M at (0, 0), Y at (1, 0). Gives 2-unit span matching Fork and Collider. Arrow segments remain readable (visible length ≈ 0.97cm per segment at this scale).

### CRITICAL: Vertical Misalignment Across Three Subdiagrams
- **Location:** All three columns — Fork height 1.4 units, Collider height 1.1 units, Chain height 0 units
- **Problem:** `\centering` with no `\vspace` equalization. Bounding box heights differ: Fork (1.05cm), Collider (0.825cm), Chain (0cm — purely horizontal). The three diagrams will not align horizontally despite representing parallel concepts.
- **Fix:** Add `yshift` to Chain to center it at y=0.7 (Fork's midpoint): move all Chain nodes up by +0.7 units after the width fix. OR add explicit `\vspace` before each tikzpicture to equalize top whitespace.

### MAJOR: Fork Treatment Arrow Uses `thick` Instead of `line width=1.5pt`
- **Location:** Line 201 — `\draw[->, usfgreen, thick] (X) -- (Y)`
- **Problem:** Every other treatment arrow uses `line width=1.5pt`. `thick` is 0.8pt by default — the Fork's X→Y is nearly half the visual weight of all other green treatment arrows. Students comparing Diagram 1 to Diagram 2 see the weight change with no semantic reason.
- **Fix:** `\draw[->, usfgreen, line width=1.5pt] (X) -- (Y);`

### MAJOR: Chain and Collider Subdiagrams Have No Color on Any Arrow
- **Location:** Lines 213–214, 226–227
- **Problem:** Fork colors X→Y green to signal "treatment path." Chain and Collider arrows are all plain black. No visual cue identifies which arrow corresponds to the relationship of interest in each structure. In a lecture hall, students cannot parse which arrow matters.
- **Fix:** Color the Chain path green (X→M→Y in usfgreen). For Collider, color X→C and Y→C, or add a "$\tau$?" edge label.

### MAJOR: Collider Vertical Proportion Feels Compressed
- **Location:** Lines 222–225 — C at (0, −0.3) with X/Y at y=0.8
- **Problem:** Vertical span 1.1 units at scale=0.75 gives 0.825cm. The V-shape looks more like a shallow U than a clear V at this scale.
- **Fix:** Move C to (0, −0.6) to increase span to 1.4 units, matching Fork's height.

### MINOR: No Explicit `\usetikzlibrary` Declaration
- **Location:** `Preambles/header.tex`
- **Problem:** `>=stealth` works via TikZ defaults but has no explicit `\usetikzlibrary{arrows.meta}` load.
- **Fix:** Add `\usetikzlibrary{arrows.meta, positioning}` to header; change `>=stealth` to `>=Stealth`.

### MINOR: Rectangular vs. Circular Node Shapes Not Annotated
- **Problem:** Abstract diagrams use circles; applied diagrams use rounded rectangles. Reasonable distinction but never explained. Circle nodes use `font=\small`; rounded-rectangle nodes use `font=\footnotesize` — backwards (applied nodes have more text).
- **Fix:** Add brief note below Diagram 1 OR standardize to `font=\footnotesize` for all nodes.

---

## Diagram 2: The Fork: Confounders (lines 240–251)

### MAJOR: τ=? Label Sits on Arrow Shaft with No Clearance
- **Location:** Line 250 — `node[midway, below, font=\footnotesize, usfgreen] {$\tau = ?$}`
- **Problem:** `node[midway, below]` places the label TOP at the arrow midpoint. At `line width=1.5pt`, the τ ascender visually merges with the arrow shaft. On a projector, this is invisible noise.
- **Fix:** Add `yshift=-4pt`: `node[midway, below, yshift=-4pt, font=\footnotesize, usfgreen] {$\tau = ?$}`

### MINOR: POL→PFL and POL→EMP Visually Asymmetric
- **Assessment:** Geometric distances are equal (both ≈ 3.11 units). POL is centered over the PFL–EMP midpoint (x=2.2). No action needed — diagram is correctly balanced.

---

## Diagram 3: The Chain: Mediators (lines 279–292)

### CRITICAL: `bend right=55` on Downward Arc Bows LEFT — "direct" Label Collides with CHILD Node
- **Location:** Lines 290–292 — `(PFL) to[bend right=55] node[right, ...] {direct} (EMP)`
- **Problem:** Arc travels from PFL(0,3) to EMP(0,0) — straight south. In TikZ, "right" facing south is west (negative x). The arc bows LEFT with apex at approximately (x≈−1.3, y=1.5). The `node[right]` label at that point extends from x≈−1.3 to x≈−0.5. The CHILD node at (0, 1.5) has its left border at approximately x≈−1.0. The "direct" label and CHILD node border directly overlap at x=−0.7 to −0.5, y=1.4–1.6. The arc itself may graze CHILD's left border.
- **Fix:** Change `bend right=55` to `bend left=55` (arc bows RIGHT into open space). Change `node[right]` to `node[right, xshift=2pt]`. The label will appear clearly at approximately (x=1.3, y=1.5).

### CRITICAL: `dashed` Used for "Direct Path" Conflicts with `dashed` for "Collider Node" in Diagram 4
- **Location:** Line 290 (dashed edge = direct path) vs. line 319 (dashed node border = collider danger)
- **Problem:** `dashed` carries two contradictory semantic meanings across slides. A student will encounter `dashed` meaning: (1) direct causal path (Diagram 3) and (2) dangerous collider variable (Diagram 4). Additionally, the project's standard definition of `dashed` = counterfactual is violated by both. This destroys visual vocabulary consistency.
- **Fix Option A (recommended):** Change Diagram 3's direct arc to solid gray: `\draw[->, gray, thick] (PFL) to[bend left=55] node[right] {direct} (EMP);`
- **Fix Option B:** Change Diagram 4's RANK node border from `dashed` to `draw=red!60`. Remove `dashed` from the node.

### MAJOR: Chain Arrows PFL→CHILD and CHILD→EMP Have No `line width` Specified
- **Location:** Lines 287–288 — `\draw[->, usfgreen] (PFL) -- (CHILD)` and `\draw[->, usfgreen] (CHILD) -- (EMP)`
- **Problem:** Default TikZ line width ≈ 0.4pt — approximately 1/4 the visual weight of `line width=1.5pt` treatment arrows in Diagrams 2, 4, 5. The chain path is the primary pedagogical feature of this slide yet is drawn nearly invisibly thin by comparison.
- **Fix:** `\draw[->, usfgreen, line width=1.5pt] (PFL) -- (CHILD)` and same for CHILD→EMP. The direct arc can use `line width=0.8pt` to visually subordinate it.

### MAJOR: "direct" Label Uses `\scriptsize` — Below Readability Floor
- **Location:** Line 292 — `node[right, font=\scriptsize, usfgreen] {direct}`
- **Problem:** `\scriptsize` at 12pt base ≈ 8pt — two steps below `\footnotesize` (10pt). Will be nearly illegible when projected.
- **Fix:** Change to `font=\footnotesize`.

### MINOR: Chain Arrows Same Visual Weight as Direct Arc
- **Problem:** All three arrows (PFL→CHILD, CHILD→EMP, dashed arc) are the same ultra-thin default weight. No visual hierarchy distinguishes the "main" chain path from the "direct" path.
- **Fix:** After setting chain arrows to `line width=1.5pt`, set direct arc to `line width=0.8pt` to subordinate it.

### MINOR: All Three Arrows in Diagram 3 Are usfgreen — Direct Path Indistinguishable from Chain Path
- **Problem:** Direct path (should be distinct) and chain path (PFL→EMP mechanism) are the same color. After fixing the arc direction, use a different color (e.g., gray) for the direct path to semantically distinguish it.

---

## Diagram 4: The Collider: A Subtle Danger (lines 314–325)

### MAJOR: RANK Node Uses `fill=codebg` Instead of `fill=lightgray`
- **Location:** Line 319 — `fill=codebg` on RANK node
- **Problem:** All other "control variable / do-not-condition-on" nodes use `fill=lightgray`: POL in Diagram 2, POL and CHILD in Diagram 5. `codebg` is semantically defined as a code-listing background color. The visual difference (#F0F0F0 vs. #F5F5F5) is invisible at projection but represents a maintenance hazard and semantic mismatch.
- **Fix:** Change to `fill=lightgray`.

### MAJOR: τ Label and Converging Collider Arrows Create Visually Crowded Center Zone
- **Location:** Line 324 — τ label at (2.2, ~1.5); PFL→RANK and EMP→RANK converge to RANK at (2.2, 0)
- **Problem:** The two collider arrows converging to RANK pass through the x=1.5–3 region at y≈0.7–1.0, directly below the τ label. The visual center is congested.
- **Fix:** Move RANK to (2.2, −0.3) to increase vertical breathing room between the τ arrow and the convergence zone.

### MINOR: RANK Node Label Uses Typographic Quotes Inside `\shortstack`
- **Location:** Line 320 — `\shortstack{``Family-friendly''\\ranking}`
- **Problem:** Typographic quotes add visual weight inside a small rounded-corner node. Minor robustness issue.
- **Fix:** `\shortstack{``Family-friendly''\\ ranking}` (add space before "ranking" for optical balance) or `\enquote{Family-friendly}` with csquotes.

---

## Diagram 5: The PFL DAG (lines 350–368)

### MAJOR: τ Label Uses `font=\small` — Larger Than All Other τ Labels
- **Location:** Line 361 — `node[midway, above, font=\small, usfgreen] {$\tau$}`
- **Problem:** Diagrams 2 and 4 use `font=\footnotesize` for τ labels. `\small` = 10.95pt; `\footnotesize` = 9pt — a 22% size difference. The summary DAG has a larger τ than the detail diagrams — backwards from expected visual hierarchy.
- **Fix:** Change to `font=\footnotesize`.

### MAJOR: CHILD Node Fill Inconsistent with Diagram 3
- **Location:** Line 357–358 — `fill=lightgray` on CHILD in Diagram 5 vs. no fill in Diagram 3
- **Problem:** Same real-world variable, different visual treatment. Worse: in Diagram 5, CHILD uses `fill=lightgray` — the same fill as POL (the confounder). This visually conflates the mediator with the confounder, directly contradicting the lecture's core message: "do NOT control for CHILD."
- **Fix:** Give CHILD a distinctive fill in BOTH diagrams: `fill=usfgold!20` (gold = warning / "be careful") clearly distinguishes it from POL's `fill=lightgray`. Update Diagram 3 consistently.

### MAJOR: POL→EMP and CHILD→EMP Arrows Crowd Around EMP Node Boundary
- **Location:** Lines 363–365 — Both arrows arrive near EMP(5, 1.2) from different angles
- **Problem:** POL→EMP descends from upper-left, CHILD→EMP rises from lower-left. Near the EMP node boundary (x≈4.5), both arrowheads arrive within 0.3 units vertically of each other. Visually congested near EMP.
- **Fix:** Add `shorten >=2pt` to all arrows in this diagram: add `[shorten >=2pt, shorten <=2pt]` to each `\draw` call, or set `every path/.append style={shorten >=2pt}` at the tikzpicture level.

### MINOR: PFL DAG Collapses Direct vs. Mediated Path Without Annotation
- **Location:** Line 360 — single thick green PFL→EMP arrow labeled τ
- **Problem:** Diagram 3 distinguished "direct" from "mediated" paths. Diagram 5 collapses both into τ without signaling this. Pedagogically consistent but loses information from the prior slide.
- **Fix (optional):** Add `node[midway, below, font=\scriptsize, darkgray] {(total effect)}` to clarify τ includes both channels.

### MINOR: No `shorten` on Any Arrow Across All Five Diagrams
- **Problem:** TikZ arrows stop exactly at node borders. For rounded-corner nodes, arrowheads can appear to clip into corners rather than land cleanly at edge midpoints.
- **Fix:** Add `shorten >=1pt, shorten <=1pt` globally to each tikzpicture or as a `tikzset`.

---

## Cross-Diagram Consistency Issues

### CRITICAL: `dashed` Carries Three Conflicting Meanings
- **Location:** Line 290 (direct path edge), line 319 (collider node border), project standard (counterfactual)
- **See Issue above (Diagram 3 CRITICAL #2).** Must resolve before teaching. Recommended: establish `dashed` = counterfactual only; use solid gray for direct path; use `draw=red!60` for collider danger.

### MAJOR: No `inner sep` Specification — Nodes Feel Tight
- **Location:** All rounded-corner nodes
- **Problem:** Default TikZ `inner sep` ≈ 3pt at \footnotesize. Text nearly touches node borders. Professional DAG visualizations (e.g., ggdag defaults) use ≈6pt padding.
- **Fix:** Add `inner sep=4pt` to each tikzpicture style: `[>=stealth, scale=0.88, every node/.style={inner sep=4pt}]`

### MAJOR: Circle Node Font (`\small`) vs. Rectangle Node Font (`\footnotesize`) Inconsistency
- **Location:** Diagram 1 circles use `font=\small`; all applied diagrams use `font=\footnotesize`
- **Problem:** Abstract nodes render 22% larger than applied nodes. No semantic motivation for this size difference.
- **Fix:** Standardize all node label fonts to `font=\footnotesize`.

---

## Must-Fix Before Approval (CRITICAL — 5 issues)

1. **Diagram 3, lines 290–292:** Change `bend right=55` → `bend left=55` and `node[right]` → `node[right, xshift=2pt]` to fix the arc direction and label-CHILD collision.
2. **Cross-diagram:** Eliminate conflicting `dashed` semantics. Change Diagram 3's direct arc to `gray, thick` (solid). Change Diagram 4's RANK node from `dashed` to `draw=red!60`.
3. **Diagram 1, lines 209–215:** Reduce Chain subdiagram width to match Fork and Collider (move nodes to x=−1, 0, +1).
4. **Diagram 5, line 357:** Change CHILD fill from `fill=lightgray` to `fill=usfgold!20` in Diagram 5 AND add same fill to CHILD in Diagram 3 — distinguishes mediator from confounder visually.
5. **Diagram 1, vertical alignment:** Add `yshift=+0.7` to Chain nodes so diagram centers align horizontally.

## Should-Fix Before Deployment (MAJOR — 13 issues)

6. Issue (D1): Change Fork treatment arrow to `line width=1.5pt`
7. Issue (D1): Add color to Chain and Collider subdiagram arrows
8. Issue (D1): Move Collider C node to (0, −0.6) for clearer V-shape
9. Issue (D2): Add `yshift=-4pt` to τ=? label
10. Issue (D3): Specify `line width=1.5pt` on PFL→CHILD and CHILD→EMP
11. Issue (D3): Change "direct" label to `font=\footnotesize`
12. Issue (D4): Change RANK fill from `codebg` to `lightgray`
13. Issue (D4): Move RANK to (2.2, −0.3) for vertical breathing room
14. Issue (D5): Change τ label to `font=\footnotesize`
15. Issue (D5): Add `shorten >=2pt` to Diagram 5 arrows
16. Issue (cross): Add `inner sep=4pt` to all node styles
17. Issue (cross): Standardize circle node fonts to `\footnotesize`
18. Issue (cross): Address RANK fill inconsistency (already covered in D4 fix)

## Nice-to-Fix (MINOR — 8 issues)

Explicit `\usetikzlibrary` load, RANK label quotes, Chain visual hierarchy (direct vs. chain weights), τ "total effect" annotation, global shorten across all diagrams, visual vocabulary footnote on Diagram 1.
