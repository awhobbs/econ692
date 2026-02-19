# Substance Review: Lecture04_Research_Design.tex
**Date:** 2026-02-18
**Reviewer:** domain-reviewer agent
**File:** `/Users/andrew/Workspace/econ692/Slides/Lecture04_Research_Design.tex`
**Course:** ECON 692 Applied Economics Seminar — Week 4 (Feb 19, 2026)
**Topic:** Potential Outcomes Framework and DAGs

---

## Summary

- **Overall assessment:** SOUND with MINOR ISSUES
- **Total issues:** 9
- **Blocking issues (prevent teaching):** 0
- **Non-blocking issues (should fix when possible):** 9

The lecture is substantively correct. Every derivation step is valid, the backdoor criterion is stated accurately, the DAG taxonomy is correct, and the R code is functionally sound. All nine issues are minor: small imprecisions, omitted assumptions appropriate for a formal treatment, a missing bibliography entry, and one layout option worth verifying. None prevent the lecture from being taught as-is.

---

## Issue Table

| # | Claim / Code | Correctness | Fix |
|---|-------------|-------------|-----|
| 1.1 | Consistency equation Y_i = D_i·Y_i(1) + (1-D_i)·Y_i(0) stated without naming the embedded assumption | CORRECT math; SUTVA/consistency unnamed | Note SUTVA or label the equation as requiring no interference |
| 1.2 | "For policy evaluation, we usually want the ATT" | Defensible but overstated | Hedge: "for retrospective policy evaluation, we want the ATT" |
| 1.3 | Mediator slide: conditioning on CHILD "underestimates" total effect | Direction correct only if mediated path is positive; generalization imprecise | Replace with "recovers the direct effect rather than the total effect" |
| 2.1 | Selection bias decomposition: all algebra steps | CORRECT | No fix needed |
| 2.2 | ATE = E[Y_i(1)-Y_i(0)], ATT = E[Y_i(1)-Y_i(0)|D_i=1] | CORRECT | No fix needed |
| 3.1 | Pearl (2009) cited for backdoor criterion — no `\cite{}` command; Pearl absent from .bib | Citation accurate; no formal `\cite{}` | Add Pearl 2009 to Bibliography_base.bib and use `\cite{}` |
| 4.1 | dagify() specification matches stated DAG | CORRECT | No fix needed |
| 4.2 | ggdag_adjustment_set(pfl_dag) with no explicit exposure/outcome args | CORRECT (inherited from dagify()) | No fix needed |
| 4.3 | layout = "sugiyama" in ggdag() | Valid igraph layout; version-dependent | Add comment noting this requires ggraph >= 2.1.0 |
| 5.1 | Backdoor criterion check: {POL} satisfies both conditions given the PFL DAG | CORRECT | No fix needed |
| 5.2 | Parallel trends / DAG connection | CORRECT | No fix needed |

---

## Lens 1: Assumption Stress Test

### Issue 1.1: Consistency / SUTVA Assumed but Not Named
- **Slide:** "The Setup: Paid Family Leave" (line 77)
- **Severity:** MINOR
- **Claim:** `$Y_i = D_i \cdot Y_i(1) + (1-D_i) \cdot Y_i(0)$` with note "only one potential outcome per unit."
- **Problem:** This is the consistency / switching equation. It embeds: (a) consistency — observed outcome under treatment D_i equals Y_i(D_i); (b) SUTVA — no interference between units. For a PFL example, SUTVA is substantively non-trivial: cross-state spillovers would break the equation. Neither assumption is named. Graduate students who read Angrist & Pischke or Imbens & Rubin will encounter these terms and won't know where the equation came from.
- **Fix:** Add one sentence below the equation: *"This requires consistency ($Y_i = Y_i(D_i)$) and no interference between units (SUTVA). For state-level policies, SUTVA rules out cross-state spillovers."*

### Issue 1.2: ATT Preference Overstated
- **Slide:** "The Fundamental Problem" (lines 100-104)
- **Severity:** MINOR
- **Claim:** "For policy evaluation, we usually want the ATT."
- **Problem:** ATE is the right target when the policy is not yet implemented and planners want the average effect if universally applied, or when external validity is the goal. ATT is right for retrospective evaluation of adopters. The conclusion is correct for PFL, but "usually" overgeneralizes.
- **Fix:** "For retrospective policy evaluation — did this policy work for the places that adopted it? — we want the ATT."

### Issue 1.3: "Underestimates" Is Direction-Dependent
- **Slide:** "The Chain: Mediators" (lines 297-299)
- **Severity:** MINOR
- **Claim:** "controlling for childbearing blocks one and **underestimates** the total effect."
- **Problem:** "Underestimates" is correct only if the mediated path operates in the same direction as the direct path. If PFL increases childbearing and childbearing decreases near-term employment (plausible), conditioning on CHILD could overestimate the direct effect. The slide assumes a specific sign on the mechanism.
- **Fix:** Replace "underestimates the total effect" with "recovers the direct effect rather than the total effect." If directional claim is wanted, add: *"In this case, where PFL enables continued employment through childbearing timing, the direct effect is likely smaller than the total effect."*

---

## Lens 2: Derivation Verification

### All Correct

**Selection bias decomposition verification:**

Step 1 — Substituting the observation equation:
- `E[Y_i | D_i=1]` = `E[Y_i(1) | D_i=1]` (since D_i=1 implies 1-D_i=0) ✓
- `E[Y_i | D_i=0]` = `E[Y_i(0) | D_i=0]` (since D_i=0 implies D_i=0) ✓

Step 2 — Add and subtract `E[Y_i(0)|D_i=1]`:
- `E[Y_i(1)|D_i=1] - E[Y_i(0)|D_i=0]`
- `= E[Y_i(1)-Y_i(0)|D_i=1] + [E[Y_i(0)|D_i=1] - E[Y_i(0)|D_i=0]]`
- `= ATT + Selection bias` ✓

Both terms are labeled correctly. CORRECT.

**ATE = E[Y_i(1) - Y_i(0)]** — unconditional expectation over all units. CORRECT.
**ATT = E[Y_i(1) - Y_i(0) | D_i=1]** — conditional on treated. CORRECT.

---

## Lens 3: Citation Fidelity

### Issue 3.1: Pearl (2009) Correctly Attributed but Not Formally Cited
- **Slide:** "The Backdoor Criterion" (line 399)
- **Current:** `\begin{block}{Backdoor Criterion (Pearl, 2009)}`
- **Assessment:** Attribution is accurate. The backdoor criterion was introduced in Pearl (1993, 1995) and consolidated in Pearl (2000/2009) *Causality: Models, Reasoning, and Inference*. Citing Pearl (2009) is the dominant practice in applied econometrics. NOT incorrect.
- **Problem:** No `\cite{}` command; Pearl (2009) absent from `Bibliography_base.bib`. Students cannot look up the reference.
- **Fix:** Add to `Bibliography_base.bib`:
  ```bibtex
  @book{Pearl2009_causality,
    author    = {Pearl, Judea},
    title     = {Causality: Models, Reasoning, and Inference},
    edition   = {2nd},
    publisher = {Cambridge University Press},
    year      = {2009},
    address   = {Cambridge, UK}
  }
  ```
  Then add `\cite{Pearl2009_causality}` as footnote or parenthetical on that slide.

---

## Lens 4: Code–Theory Alignment

### Issue 4.1: dagify() Specification — CORRECT
- **Code:** `dagify(EMP ~ PFL + POL + CHILD, PFL ~ POL, CHILD ~ PFL, exposure = "PFL", outcome = "EMP")`
- **Assessment:** Encodes exactly the edges in the PFL DAG TikZ diagram:
  - EMP ← PFL, EMP ← POL, EMP ← CHILD, PFL ← POL, CHILD ← PFL
  No extraneous edges; no missing edges. CORRECT.

### Issue 4.2: ggdag_adjustment_set() — CORRECT
- `exposure` and `outcome` inherited from `dagify()`. Function returns {POL} — matches what the slide claims. CORRECT.

### Issue 4.3: layout = "sugiyama" — Advisory
- **Severity:** MINOR
- `"sugiyama"` is a valid igraph hierarchical layout accessible via ggraph. It became reliably available in ggraph >= 2.1.0 (2022). Students on older installations may get an error.
- **Fix:** Add comment `# requires ggraph >= 2.1.0` or substitute `layout = "nicely"` as universal default and demonstrate "sugiyama" live.

---

## Lens 5: Backward Logic Check

### All Correct — Clean Scaffold

Complete backward trace from wrap-up to setup:
- "Refine your DAG" ← DAG Workshop ← DAG Software demo ← Backdoor Criterion ← Fork/Chain/Collider slides ← DAG Building Blocks ← "Where Does Bias Come From?" ← Selection Bias decomposition ← Potential Outcomes setup. Every step is supported by a prior slide. No circular arguments. No prerequisite assumed before introduction.

The "DAGs and Parallel Trends" slide connects DAG confounders to DiD from Lecture 03. Clean and well-motivated; self-contained enough for a student who missed Lecture 03.

---

## Cross-Lecture Consistency Check

| Item | Lecture 03 | Lecture 04 | Status |
|------|-----------|-----------|--------|
| Y_i(0), Y_i(1) notation | Used without defining (flagged in L03 review) | Formally defined with PFL example | CONSISTENT — L04 plugs the L03 gap |
| ATE | Mentioned | Formally defined | CONSISTENT |
| ATT | Not defined | Formally defined | NO CONFLICT |
| D_i | Binary treatment | Binary PFL indicator | CONSISTENT |
| Selection bias | Named as concept | Formally decomposed | CONSISTENT |
| Parallel trends | Core DiD assumption | Connected to DAG confounders | CONSISTENT |
| \E macro | Defined in header.tex | Used throughout | CONSISTENT |

No notation conflicts. L04 intentionally re-introduces the PO framework that L03 assumed — good design.

---

## Priority Fixes

1. **[MINOR]** Add SUTVA/consistency sentence to "The Setup" slide (Issue 1.1) — one sentence, high precision payoff
2. **[MINOR]** Change "underestimates" to "recovers the direct effect" on mediator slide (Issue 1.3) — prevents sign confusion
3. **[MINOR]** Add Pearl (2009) to `Bibliography_base.bib` (Issue 3.1) — housekeeping
4. **[MINOR]** Add ggraph version comment to ggdag code snippet (Issue 4.3) — prevents student frustration
5. **[MINOR]** Hedge ATT preference claim (Issue 1.2) — accuracy

---

## Positive Findings

- **Selection bias decomposition is executed flawlessly.** The add-and-subtract step, linearity of expectation, and ATT/selection bias labels are all correct. Exactly the right way to introduce this to applied students.
- **Collider treatment is precise.** "Collider paths are closed by default — no bias" is exactly correct in d-separation terms. Many introductory treatments get this wrong by being vague about what "closed" means.
- **dagify() code matches the theoretical DAG exactly.** Every edge in the TikZ diagram appears exactly once in the code. Students who copy this will get a correct computational answer.
