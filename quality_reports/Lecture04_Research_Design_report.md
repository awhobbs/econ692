# Quality Report: Lecture04_Research_Design.tex
**Course:** ECON 692 Applied Economics Seminar, University of San Francisco
**Instructor:** Andrew Hobbs
**Review Date:** 2026-02-18
**Reviewer:** Proofreading Agent (claude-sonnet-4-6)

---

## Executive Summary

The file is well-structured, mathematically sound, and pedagogically clear. The DAG exposition is strong, the running PFL example is consistent throughout, and the notation is internally coherent. Nine issues were identified: one critical (missing bibliography infrastructure for the only citation in the file), three medium (pronoun inconsistency, contractions, a sentence fragment), and five low-severity items (punctuation/style choices and minor phrasing issues). No overflow or mathematical notation inconsistencies were found.

**Overall Quality Score: 84 / 100** (above the 80-point commit gate; does not reach the 90-point PR/deployment gate until the citation issue is resolved)

---

## Issue Summary Table

| # | Line | Issue | Severity | Category |
|---|------|-------|----------|----------|
| 1 | 399 | "Pearl, 2009" cited in prose only — no `\cite{}`, no bib entry, no bibliography infrastructure | Critical | Academic Quality / Consistency |
| 2 | 42 | Pronoun mismatch: "Has anyone started sketching **your** causal story?" | Medium | Grammar |
| 3 | 144, 379, 528, 555 | Informal contractions: don't, shouldn't, I'll | Medium | Academic Quality |
| 4 | 481 | Dangling modifier / sentence fragment on "ggdag in R" slide | Medium | Grammar |
| 5 | 132 | Run-on sentence in "Selection Bias" slide | Low | Grammar |
| 6 | 423 | Awkward colon construction: "Parallel trends requires:" | Low | Grammar |
| 7 | 436 | Tense shift: "drove...will diverge" | Low | Grammar |
| 8 | 46 | "11:59pm" — inconsistent with professional typographic convention | Low | Consistency / Typo |
| 9 | 555 | First-person "I'll be circulating" on a projected slide | Low | Academic Quality |

---

## Critical Issues

### Issue 1: Pearl (2009) cited in prose only — no LaTeX citation, no bib entry, no bibliography
- **Location:** Line 399 — frame "The Backdoor Criterion"
- **Current:** `\begin{block}{Backdoor Criterion (Pearl, 2009)}`
- **Proposed:** Add a `@book{Pearl2009_causality, ...}` entry to `Bibliography_base.bib`, add `\usepackage{natbib}` (or biblatex) to `header.tex`, add `\bibliography{../Bibliography_base}` before `\end{document}`, and replace the prose citation with `\begin{block}{Backdoor Criterion \citep{Pearl2009_causality}}`.
- **Category:** Academic Quality / Consistency
- **Severity:** Critical

  The string `(Pearl, 2009)` is hardcoded prose inside a `\block` title. The file contains no `\bibliographystyle`, `\bibliography`, or `\usepackage{natbib}`/`biblatex` command, and `Bibliography_base.bib` has no Pearl entry. As written, this is an unverifiable claim with no citation infrastructure. In a graduate seminar on causal inference, the backdoor criterion is a foundational result attributed to Pearl — it must be formally cited.

  Suggested bib entry to add to `Bibliography_base.bib`:
  ```bibtex
  @book{Pearl2009_causality,
    author    = {Pearl, Judea},
    title     = {Causality: Models, Reasoning, and Inference},
    edition   = {2},
    publisher = {Cambridge University Press},
    address   = {Cambridge, UK},
    year      = {2009}
  }
  ```

---

## Medium Issues

### Issue 2: Pronoun mismatch — "anyone … your"
- **Location:** Line 42 — frame "Check-in"
- **Current:** `\item Has anyone started sketching your causal story?`
- **Proposed:** `\item Has anyone started sketching \textbf{their} causal story?`
- **Category:** Grammar
- **Severity:** Medium

  "Has anyone" establishes a third-person subject; "your" is second person. Compare with line 41, which correctly uses "their data source" after "Has anyone."

---

### Issue 3: Informal contractions in academic lecture slides
- **Location:** Lines 144, 379, 528, 555
- **Category:** Academic Quality
- **Severity:** Medium

  | Line | Current | Proposed |
  |------|---------|----------|
  | 144 | `they don't tell us` | `they do not tell us` |
  | 379 | `\textbf{Mediator (don't control):}` | `\textbf{Mediator (do not control):}` |
  | 528 | `that shouldn't be` | `that should not be` |
  | 555 | `I'll be circulating.` | `I will be circulating.` (see also Issue 9) |

  Contractions are informal register and inconsistent with the professional presentation quality expected in a graduate seminar. The rest of the file correctly avoids contractions.

---

### Issue 4: Sentence fragment on "ggdag in R" slide
- **Location:** Line 481 — frame "ggdag in R"
- **Current:** `For publication-quality figures in your paper or final presentation.`
- **Proposed:** `Use \texttt{ggdag} for publication-quality figures in your paper or final presentation.`
- **Category:** Grammar
- **Severity:** Medium

  The line is a prepositional phrase with no main clause. Adding a subject and verb resolves this and makes the purpose of the slide immediately explicit.

---

## Low Issues

### Issue 5: Run-on sentence in "Selection Bias" slide
- **Location:** Line 132
- **Current:** `\textbf{Selection bias for PFL:} states that adopt PFL may have had higher female employment \textit{even without} the policy -- liberal, urban states pass PFL \textit{and} have stronger female labor markets.`
- **Proposed:** Split: `\textbf{Selection bias for PFL:} states that adopt PFL may have had higher female employment \textit{even without} the policy. Liberal, urban states pass PFL \textit{and} tend to have stronger female labor markets.`
- **Category:** Grammar / Severity:** Low

---

### Issue 6: Awkward colon construction — "Parallel trends requires:"
- **Location:** Line 423
- **Current:** `\textbf{Parallel trends requires:} absent PFL...`
- **Proposed:** `\textbf{Parallel trends assumption:} absent PFL...`
- **Category:** Grammar / **Severity:** Low

  "Requires" is a transitive verb expecting an object, not a colon. Replacing with a noun label matches heading style used elsewhere.

---

### Issue 7: Tense shift — "drove … will diverge"
- **Location:** Line 436
- **Current:** `political environment drove both adoption timing and employment growth -- early adopters will diverge from controls before the policy, which a pre-trends test detects.`
- **Proposed:** `political environment drives both adoption timing and employment growth -- early adopters diverge from controls before the policy, which a pre-trends test can detect.`
- **Category:** Grammar / **Severity:** Low

---

### Issue 8: Inconsistent time formatting — "11:59pm"
- **Location:** Line 46
- **Current:** `at 11:59pm.`
- **Proposed:** `at 11:59 PM.` (also add comma: "Friday, February 20")
- **Category:** Consistency / **Severity:** Low

---

### Issue 9: First-person "I'll be circulating" on a projected slide
- **Location:** Line 555
- **Current:** `\textit{Goal: a rough draft to build on over the next two weeks. I'll be circulating.}`
- **Proposed:** Remove "I'll be circulating." — say it verbally instead.
- **Category:** Academic Quality / **Severity:** Low

---

## No Issues Found In

- Mathematical notation: `\E`, `\Var`, `\indep` macros used correctly; display-math equations properly delimited; conditioning notation consistent
- DAG TikZ code: node/edge definitions consistent across all five diagrams; color convention (green = treatment path, red = warning) applied uniformly
- Capitalization of slide titles: title case used consistently throughout
- Bullet parallelism: enumerated and itemized lists are parallel in structure
- Em-dash style: `--` with surrounding spaces applied uniformly (intentional typographic choice)
- Terminology: "potential outcomes," "DAG," "confounder," "mediator," "collider," "backdoor criterion," "adjustment set," "parallel trends," "event study" all used consistently
- Overflow risk: no slides appear at overflow risk; `\small` used appropriately on math-heavy slides
- Section structure: five sections map cleanly to the agenda table
