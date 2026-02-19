# Visual Layout Audit: Lecture04_Research_Design.tex

**File:** `/Users/andrew/Workspace/econ692/Slides/Lecture04_Research_Design.tex`
**Header:** `/Users/andrew/Workspace/econ692/Preambles/header.tex`
**Format:** Beamer, 16:9, 12pt base, XeLaTeX
**Slides audited:** 22 content frames + 5 auto-generated section dividers = 27 total pages
**Audit date:** 2026-02-18
**Auditor:** Visual Audit Agent

**Summary:** The deck is structurally clean and compiles without reported errors. Overflow risk is low overall. Main actionable issues: (1) font-size inconsistency — Collider right column drops to `\footnotesize` while peers use `\small`; (2) Chain TikZ "direct" label uses `\scriptsize` below readability floor; (3) bare `\textcolor{red}` used for warnings instead of defined palette; (4) "Draw Your DAG" workshop slide is dense and warrants splitting; (5) no deck-closing takeaway slide. No overlay commands present (policy-compliant). No box fatigue (never more than one `\begin{block}` per frame).

---

## Issue Table

| Issue | Severity | Slide | Fix |
|-------|----------|-------|-----|
| Chain TikZ "direct" label uses `\scriptsize` (below 0.85em floor) | Medium | "The Chain: Mediators" (slide 11, line 292) | Change `font=\scriptsize` to `font=\footnotesize` |
| Collider right column drops to `\footnotesize`; frame already opens with `\small` | Medium | "The Collider: A Subtle Danger" (slide 13, line 328) | Remove redundant `\footnotesize` declaration |
| Collider TikZ quoted `\shortstack` node may overfull hbox in narrow column | Medium | "The Collider: A Subtle Danger" (slide 13, line 319) | Remove outer typographic quotes from node label; add `minimum width=2.2cm` |
| "Draw Your DAG" frame is dense (two workshop phases, two itemize blocks) | Medium | "Draw Your DAG" (slide 17) | Split into two slides: one per step |
| `\textcolor{red}` not in defined palette | Low | Slides 9, 13 (lines 217, 230, 340) | Define `\definecolor{warnred}{HTML}{C0392B}` in header; replace all `\textcolor{red}` |
| Contraction "don't control" in label | Low | "The PFL DAG" (slide 14, line 379) | Change to "do not control" |
| Mid-arrow τ label: `\footnotesize` on Fork slide, `\small` on PFL DAG slide | Low | Slides 10, 14 (lines 250, 361) | Standardize to `font=\footnotesize` on PFL DAG slide |
| `\vspace{12pt}` oversized on sparse "Share-outs" slide | Low | "Share-outs" (slide 20, lines 561, 570) | Reduce to `\vspace{8pt}` |
| Agenda table col 3 has no explicit width | Low | "Today's Agenda" (slide 2, line 20) | Change to `p{5.5cm}` |
| No deck-closing takeaway slide | Low | End of deck | Add "Today's Key Ideas" before "Wrap-Up" |
| `\vspace` values not standardized (2–12pt range, no system) | Low | Global | Standardize: 4pt tight, 8pt paragraph, 12pt only for frame-level section breaks |

---

## Critical Issues

None. No slide exceeds the declared 7pt overflow tolerance. No overlay commands (`\pause`, `\onslide`, `\only`, `\uncover`) present. No broken image references. No box fatigue.

---

## Medium Issues

### M1. Chain TikZ "direct" label uses `\scriptsize` (line 292)

**Slide:** "The Chain: Mediators" (slide 11)

The dashed "direct" label on the bent arrow from PFL to EMP uses `font=\scriptsize`. At 12pt base, `\scriptsize` ≈ 8pt — below the 0.85em readability floor. This label is pedagogically important (it explains why the direct path exists). All other TikZ edge labels use `\footnotesize`.

**Fix:**
```latex
% Current (line 292):
  node[right, font=\scriptsize, usfgreen] {direct} (EMP);
% Fixed:
  node[right, font=\footnotesize, usfgreen] {direct} (EMP);
```

---

### M2. Collider right column drops to `\footnotesize` (line 328)

**Slide:** "The Collider: A Subtle Danger" (slide 13)

Frame opens with `\small` at line 309, then right column drops another level to `\footnotesize` at line 328. At 12pt base: `\small` ≈ 10.95pt, `\footnotesize` ≈ 10pt. Right column body text is noticeably smaller than peer frames. All other two-column DAG frames use only frame-level `\small`.

**Fix:** Remove the `\footnotesize` declaration at line 328.

---

### M3. Collider TikZ node with quoted `\shortstack` (lines 319-320)

**Slide:** "The Collider: A Subtle Danger" (slide 13)

```latex
\node[draw, rounded corners, dashed, font=\footnotesize, fill=codebg]
  (RANK) at (2.2, 0) {\shortstack{``Family-friendly''\\ranking}};
```

The typographic quotes add ~2em width. No `minimum width` is set; TikZ auto-sizes the node. With `scale=0.88` in a 0.48\textwidth column, this is borderline.

**Fix:**
```latex
\node[draw, rounded corners, dashed, font=\footnotesize, fill=codebg, minimum width=2.2cm]
  (RANK) at (2.2, 0) {\shortstack{Family-friendly\\ranking}};
```

---

### M4. "Draw Your DAG" frame is content-dense (lines 507-530)

**Slide:** "Draw Your DAG" (slide 17)

Contains: bold heading (Step 1), intro sentence, 4-item itemize, tool note, bold heading (Step 2), intro sentence, 3-item itemize — approximately 14 distinct lines before spacing. Densest non-math slide in the deck. Also gives instructor a natural mid-workshop pause point.

**Fix:** Split into two slides: "Draw Your DAG — Individual" (Step 1) and "Draw Your DAG — Groups" (Step 2).

---

## Low / Cosmetic Issues

### L1. `\textcolor{red}` not in defined palette

**Slides:** "Three Fundamental Structures" (lines 217, 230), "The Collider" (line 340)

Pure `#FF0000` red is not in the theme palette. Inconsistent with USF branding.

**Fix:** Add `\definecolor{warnred}{HTML}{C0392B}` to `header.tex`; replace all `\textcolor{red}` with `\textcolor{warnred}`.

---

### L2. τ label font inconsistent across DAG slides

**Slides:** "The Fork: Confounders" (line 250, `font=\footnotesize`) vs. "The PFL DAG" (line 361, `font=\small`)

**Fix:** Standardize to `font=\footnotesize` on line 361.

---

### L3. `\vspace{12pt}` on sparse "Share-outs" slide (lines 561, 570)

Slide has minimal content; two 12pt spacers leave excessive white space at bottom.

**Fix:** Reduce both to `\vspace{8pt}`. Consider adding "What we are listening for:" framing sentence.

---

### L4. Agenda table col 3 has no explicit width (line 20)

Current spec: `{@{}r@{\hspace{8pt}}l@{\hspace{16pt}}l@{}}`. Longest entry "Empirical strategy drafting" fits now, but any extension risks overflow.

**Fix:** Change to `{@{}r@{\hspace{8pt}}l@{\hspace{16pt}}p{5.5cm}@{}}`.

---

### L5. No deck-closing takeaway slide

Deck ends with logistics. No slide consolidates the conceptual arc: PO → DAGs → backdoor criterion → empirical strategy.

**Recommended addition** (before "Wrap-Up & Next Week"):
```latex
\begin{frame}{Today's Key Ideas}
  \begin{itemize}
    \item \textbf{Potential outcomes} define your estimand and name the problem (selection bias).
    \item \textbf{DAGs} reveal where bias enters and what to condition on to remove it.
    \item \textbf{The backdoor criterion} gives a formal rule: block all non-causal paths without conditioning on descendants of treatment.
  \end{itemize}
  \vspace{8pt}
  \textit{Your empirical strategy is a written argument for why your adjustment set satisfies this criterion.}
\end{frame}
```

---

### L6. `\vspace` values not standardized (range 2–12pt)

No consistent system. Recommend: 4pt for tight breaks within a thought; 8pt for paragraph-level separation; 12pt only before a new section heading within a frame.

---

## Checks Passed

- **Overlay commands:** None present. Policy-compliant per `.claude/rules/no-pause-beamer.md`.
- **Image paths:** No `\includegraphics` — all diagrams are pure TikZ. No broken references.
- **Box/block fatigue:** `\begin{block}` appears on 3 frames only (lines 45, 183, 399), one per frame. No stacking.
- **Section structure:** Five sections map cleanly to the agenda table.
- **Color convention:** green = treatment path, red = warnings — applied uniformly across all DAGs.

---

*Report generated by Visual Audit Agent. Do NOT edit source file based on this report without reviewing the compiled PDF.*
