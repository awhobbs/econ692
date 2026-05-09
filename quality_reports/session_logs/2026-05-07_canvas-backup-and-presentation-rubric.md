# Session Log — 2026-05-07: Canvas backup + presentation rubric draft

## Goal

Defensive snapshot of Canvas state after the platform was hacked + down earlier in the day. Plus draft a final-presentation grading rubric and prep questions for tonight's two presenters (Tuan, Evan).

## Work Done

### 1. Final presentation rubric (drafted, no Canvas equivalent)

Confirmed via Canvas API that the **Final Presentation assignment (ID 7641205) has no rubric attached**. Drafted a 15-pt rubric (5 criteria: research question, identification, results, slides/figures, delivery) calibrated to the Preliminary Results rubric Andrew was already using.

Built a Google Doc with three identical rubric tables for tonight's grading: <https://docs.google.com/document/d/1EkVFu0VNWpgAtmv8UV-x2gjI4bKnpWpRNim68KVcZ40/edit>.

### 2. Q&A questions for Tuan and Evan

Three substantive questions each based on the full-draft grade files. For Tuan: WAS-vs-TWFE reconciliation (the WAS estimates are all null and not engaged with in the discussion); income as a bad control; where displaced demand goes. For Evan: are deltas additive in the LP; substitution heterogeneity; spec for the proposed A/B experiment.

### 3. Canvas backup (`canvas_backup/2026-05-07/`)

Pulled all 36 assignments — descriptions, rubrics, criterion IDs — plus all submissions and current grades. Saved as markdown:

- 8 milestone files (one per major assignment) with rubrics
- 1 WPR template (4-pt rubric, applies to all 13 WPRs)
- 1 participation template (1 pt each, no rubric)
- 3 grade tables (milestones, WPRs, participation)
- Student roster + index + README

**Headline finding:** Final Presentation and Reproducibility Materials both have no rubric on Canvas. Local rubric in use for Final Presentation; Reproducibility still needs one before 5/15.

### 4. Backup is gitignored (FERPA)

Repo is public. Backup contains student names + grades. Added `canvas_backup/` to `.gitignore` to keep it local-only. Repo's `assignments/` directory was already ignored for the same reason.

## Open Items / Next Actions

- **Tonight (5/7):** Run final presentations round 1 with the locally drafted rubric. Use the Google Doc for grading.
- **Before 5/14:** Catch up grading on 4/29 + 5/6 WPRs and 4/30 participation (currently all ungraded).
- **Before 5/15:** Decide whether to add a rubric to the Reproducibility Materials assignment on Canvas.
- **Cecilia Vigil:** Late-policy decision pending — Empirical Strategy + Data Report show 0 from very late submissions; multiple missing WPRs.
- **Chris Tsang:** Empirical Strategy + Preliminary Results = 0 (not submitted); 4/8 WPR + 5/6 WPR not submitted.
- **Gaziz Makhanov:** Lowest milestone scores; 4/29 WPR submitted late (5/3) still ungraded.
