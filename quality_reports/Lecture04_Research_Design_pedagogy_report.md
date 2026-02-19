# Pedagogical Review: Lecture04_Research_Design.tex
**Date:** 2026-02-18
**Reviewer:** pedagogy-reviewer agent
**File:** `/Users/andrew/Workspace/econ692/Slides/Lecture04_Research_Design.tex`
**Slide count:** 21 content frames + 5 auto-generated section title frames + 1 title page = 27 rendered pages

---

## Summary

- **Patterns followed:** 7/13
- **Patterns violated:** 3/13
- **Patterns partially applied:** 3/13
- **Estimated quality score:** 78/100 as-is; 90+ after implementing recommendations 1–3

A lean, well-paced deck with an excellent running example and strong visual-first discipline. The core PO → DAG → identification narrative is coherent and the PFL thread holds throughout. Main weaknesses: zero Socratic questions in 11 theory slides, the Selection Bias slide attempts too much in one pass, no explicit learning objectives, and the Empirical Strategy Drafting section lacks a model paragraph. The deck is classroom-ready but would benefit from targeted additions.

---

## Overall Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Narrative arc | Strong | PO → DAG → software → workshop → drafting is a clean logical progression |
| Learning objectives | Absent | No explicit "by the end of today you will..." slide |
| Prior knowledge assumption | Appropriate | PO notation re-introduced without re-deriving from scratch; DAG basics explained |
| Concept scaffolding | Strong | Fork → Chain → Collider → PFL DAG → Backdoor Criterion builds well |
| PFL running example | Excellent | Used on 11 of 21 content slides, grounding every abstraction |
| Active learning structure | Good | Workshop prompt clear; drafting sprint well-specified |
| Notation consistency | Strong | D_i, Y_i, Y_i(1), Y_i(0), τ_i used consistently throughout |
| Cognitive load | Mixed | Most slides fine; Selection Bias slide is the main overload point |
| Transitions | Good | Auto-frames provide visual breaks; "Where Does Bias Come From?" is excellent bridge |
| Key takeaways | Partial | No deck-level takeaway slide; individual sections have summary lines |
| Timing alignment | Good | 21 content slides for ~195 min instructional time is well-proportioned |
| Assessment alignment | Good | Drafting sprint maps directly onto Empirical Strategy Draft rubric |
| Feedback loops | Weak | Only 3 questions (all on Check-in); zero embedded thought questions in theory slides |

---

## Pattern-by-Pattern Assessment

### Pattern 1: Motivation Before Formalism — FOLLOWED
Deck opens with the PFL research question before any notation. Every DAG structure is shown as TikZ before the application or formal-criterion slides. "Where Does Bias Come From?" motivates DAGs before the DAG section begins. Well-executed throughout.

### Pattern 2: Incremental Notation — FOLLOWED
"The Setup" introduces D_i, Y_i, Y_i(1), Y_i(0) before the switching equation. The next slide adds only τ_i, ATE, ATT. No single slide introduces more than 4–5 new symbols. **Minor gap:** A parenthetical "-- this is just the compact way to write: you observe whichever potential outcome matches your treatment status" would help slower readers on the switching equation slide.

### Pattern 3: Worked Example After Every Definition — PARTIALLY APPLIED
PFL applications follow most definitions quickly. Fork → Fork PFL, Chain → Chain PFL, Collider → Collider PFL, all within one slide. Backdoor Criterion stated and immediately applied to PFL on the same slide. **Minor gap:** "Three Fundamental Structures" uses abstract X/Y/Z nodes — the PFL example arrives two slides later. Consider adding one-line PFL hooks under each panel (e.g., "e.g., political environment → PFL and employment").

### Pattern 4: Progressive Complexity — FOLLOWED
Ordering: individual PO → averages (ATE/ATT) → selection bias → DAG structures (simple → applied) → backdoor criterion → parallel trends. Mediator and collider come after fork, which is correct (confounding is the most intuitive entry point). Clean.

### Pattern 5: Fragment Reveals — VIOLATED (no-pause adaptation needed)
Project rules prohibit `\pause`. The spirit of the pattern — problem before solution — is not addressed in the Selection Bias slide, which reveals algebra and interpretation simultaneously. **Fix (no overlay):** Split into two slides: (A) naive comparison + "what's wrong with this?", (B) underbrace decomposition + PFL interpretation. Apply similarly to 2–3 other dense slides.

### Pattern 6: Standout Slides — FOLLOWED
`\AtBeginSection` auto-generates full-screen section frames at all five major pivots. "Where Does Bias Come From?" functions as an organic bridge. **Minor gap:** ggdag slide ends with a package install command; next content slide immediately starts the workshop. A one-sentence bridge ("Now you'll apply these tools to your own DAG") would smooth this transition.

### Pattern 7: Two-Slide Strategy for Dense Theorems — PARTIALLY APPLIED
Backdoor Criterion states the formal block + applies to PFL on the same slide. The two conditions use blended formal/informal language. **Fix:** Add a follow-up slide with mini-TikZ diagrams illustrating a descendant violation and a path-blocking success. Alternatively, add plain-English glosses for each condition on the current slide.

### Pattern 8: Semantic Color — PARTIALLY APPLIED
Green (usfgreen) = treatment effect, target, "block it" — semantically coherent throughout. Gray = confounders/unobserved. **Problems:** (1) Red used identically for Mediator "Caution" (a design choice) and Collider "Danger" (an error) — two different risk levels. Consider orange/usfgold for mediator caution. (2) Fork panel has green X→Y edge; Chain panel has no colored edges — inconsistent within the three-panel comparison slide.

### Pattern 9: Box Hierarchy — FOLLOWED
`\begin{block}` appears 3 times: "Reminder" (check-in), "Key insight" (DAG building blocks), "Backdoor Criterion" (formal theorem). One per frame, appropriate usage each time. No stacking.

### Pattern 10: Box Fatigue — FOLLOWED
Maximum one colored box per frame. Three frames total. Well within limits.

### Pattern 11: Socratic Embedding — VIOLATED
**Zero embedded thought questions in 11 theory slides.** All 3 questions are on the Check-in slide (logistical). The workshop and drafting sections have activity prompts, but no embedded pedagogical questions during exposition. Target: 2–3 embedded questions.

**Suggested placements:**
- Bottom of "The Fundamental Problem": "For your project: which estimand do you actually want — ATE or ATT?"
- Bottom of "Three Fundamental Structures": "Look at your planned controls. For each one: fork, chain node, or collider?"
- Bottom of "DAGs and Parallel Trends": "Name the single biggest time-varying confounder threatening parallel trends in your setting."

### Pattern 12: Visual-First — FOLLOWED
Every DAG structure shown as TikZ before any formal criterion. Full PFL DAG appears before the Backdoor Criterion is stated. The three-panel "Three Fundamental Structures" layout is particularly effective.

### Pattern 13: Two-Column Comparisons — FOLLOWED
"Where Does Bias Come From?" presents PO vs. DAGs side-by-side with a unifying takeaway. ATE vs. ATT as a two-row inline table. Three-panel three-column layout for the structure comparison. All correctly applied.

---

## Deck-Level Analysis

### Narrative Arc

Three intellectual phases:

**Phase 1 (PO, slides 4–7):** What is the causal quantity we want? Why can't we compute it directly? What goes wrong with naive comparisons? Names the target (ATT) and the enemy (selection bias).

**Phase 2 (DAGs, slides 8–15):** Where does the bias come from structurally? How do we find the right adjustment set? The PFL DAG slide synthesizes all three structures into a single applied diagram.

**Phase 3 (Tools + Practice, slides 16–21):** How do you actually build and analyze a DAG? Now do it for your own project.

**Gap:** The deck opens with "Does access to paid family leave increase female employment?" and never explicitly returns to answer this question in terms of what the DAG implies for estimation. A one-slide capstone ("What the PFL DAG tells us: control for political environment, do not control for childbearing timing, look for DiD variation in adoption timing") would close the loop.

### Pacing

Theory section (PO slides + DAG slides): 10 content slides across 60 allocated minutes ≈ 6 min/slide. Appropriate for graduate seminar with discussion. DAG section has 8 content slides between section breaks (upper limit; a Socratic question at "Three Fundamental Structures" would create a natural checkpoint). Text/visual balance is good: six TikZ diagrams interrupt the theory run.

### Student Concerns

- **SUTVA:** The switching equation embeds SUTVA (no interference between units) without naming it. For PFL, cross-state spillovers are a substantive concern. One sentence: "(We assume no spillovers between states — SUTVA.)"
- **Conditional ignorability:** The backdoor criterion is the graphical equivalent of the unconfoundedness assumption $\{Y_i(0),Y_i(1)\} \indep D_i \mid \mathbf{Z}$. Students from a regression background won't know this. One bridge sentence on the Backdoor Criterion slide.
- **Collider example:** "Family-friendly ranking" is abstract for students who haven't conditioned on rankings. A more immediate example: "selecting only high-employment states because that's where you found data" resonates with their current data struggles.
- **ggdag output:** Slide shows code but no expected output. Students during the workshop won't know if their code is working. Add: "Produces: a DAG plot and a printed adjustment set in the console."
- **Drafting sprint register:** Students writing their first empirical strategy draft often struggle with academic register. A two-sentence model opening would help without doing their work.

---

## Critical Recommendations

**1. Add 2–3 Socratic questions to theory slides (High Priority)**
Zero embedded questions across 11 theory slides is the single highest-severity gap. Use italic one-liners at the bottom of "The Fundamental Problem," "Three Fundamental Structures," and "DAGs and Parallel Trends."

**2. Add explicit learning objectives after the Agenda slide (High Priority)**
4-bullet "By the end of today you will be able to..." slide. Suggested: (1) Define ATE and ATT and explain why they differ. (2) Draw a DAG with forks, chains, and colliders for a real research setting. (3) Apply the backdoor criterion to find a minimum adjustment set. (4) Draft an identification strategy paragraph.

**3. Split "Selection Bias" into two slides (Medium Priority)**
(A) Show naive comparison + "What's wrong with this?"; (B) show decomposition + PFL interpretation. No `\pause` needed — two slides.

**4. Add a model paragraph to the Drafting Sprint slide (Medium Priority)**
Two-sentence model identification opening in italic. Prevents register problems without doing students' work for them.

**5. Add a capstone slide before Wrap-Up (Low-Medium Priority)**
Close the PFL narrative loop: what does the DAG imply for the estimation strategy? This models the reasoning students must apply to their own projects.

---

## Minor Issues Log

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| m1 | Line 144 | Contraction "don't tell us" | "do not tell us" |
| m2 | Line 401 | $\mathbf{Z}$ bold notation used without defining bold = set | Add "(a set of variables)" on first use |
| m3 | Line 399 | "Pearl, 2009" inline citation without `\cite{}` | Add `\cite{pearl2009causality}` |
| m4 | Lines 108, 131 | `\small`…`\normalsize` toggle mid-slide | Apply `\small` to entire frame or use `\footnotesize` only on equations |
| m5 | Line 319 | "Family-friendly ranking" collider is abstract | Replace/supplement with "selecting only high-employment states in your sample" |
| m6 | Lines 191–232 | Chain panel has no colored edges; Fork panel has green X→Y edge | Color Chain path consistently with Fork panel |
| m7 | Line 498 | ggdag slide shows no expected output | Add one-line: "Produces: a DAG plot and adjustment set in the console" |
| m8 | Global | No SUTVA acknowledgment | Add one sentence to The Setup: "(We assume no spillovers between states — SUTVA.)" |
| m9 | Global | No connection between backdoor criterion and conditional ignorability | One-line bridge on Backdoor Criterion slide |
