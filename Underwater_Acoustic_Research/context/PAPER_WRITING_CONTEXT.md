# PAPER WRITING CONTEXT — Section Guide (Results Only From Actual Experiments)

Status: GUIDE ONLY — NO SECTIONS WRITTEN WITH FABRICATED RESULTS.

## Section Structure (As Requested)
1. Title and Abstract
2. Introduction and Problem Statement
3. Related Work and Research Gap
4. Proposed Methodology
5. Experimental Setup and Results
6. Discussion, Limitations and Conclusion
7. References and Citation Verification

## Rules Per Section (Verified Constraints)
- Title / Abstract: Can be drafted from the user's abstract; must reflect the ACTUAL contribution once determined (not the generic abstract alone).
- Introduction: Cite real papers with verified DOIs. If a paper is not yet verified, use a placeholder like `[CITE: verify DOI]` and never invent a citation.
- Related Work: Must include at least references from the verified paper matrix (`literature/paper_matrix.csv`). If the matrix is empty, state: "This section will be completed once the verified paper matrix reaches at least 30 entries."
- Methodology: Describe the exact code framework (`code/` files). If the method is not yet implemented, say so explicitly: "The proposed method is described at framework level; full implementation and testing are ongoing."
- Experimental Setup: Describe dataset selection (from `datasets/download_instructions.md` and `dataset_comparison.csv`). If no dataset is downloaded, say: "Dataset selection is pending verified download links; the primary dataset under consideration is DeepShip (verification pending)."
- Results: ONLY from actual experiment runs (`experiments/` logs). If no experiments exist, this section must say: "Results are pending. No fabricated metrics will be included. Once experiments are run, this section will report accuracy, macro-F1, noise robustness curves, model size, inference latency, and RAM usage."
- Discussion / Limitations: Must honestly discuss limitations (e.g., unverified datasets, web access restrictions during research, untested code). Do not omit limitations.
- Conclusion: Must align with actual results. If no results exist, the conclusion must be conditional: "This study aims to... The final conclusion will be drawn after verified experiments."
- References: Every citation must have a verified source. Use `[VERIFY]` tags for any unverified entry.

## Citation Verification Protocol
- Before adding any citation, confirm DOI or URL resolves.
- Record citation verification status in `literature/annotated_bibliography.md`.
- If a citation cannot be verified, it must NOT appear in the paper's reference list.

## Publication Venue Strategy (No Acceptance Guarantee)
- Investigate IEEE venues: IEEE Access, IEEE Journal of Oceanic Engineering, IEEE Signal Processing Letters, IEEE Transactions on Neural Networks and Learning Systems.
- Investigate conferences: ICASSP, OCEANS, IEEE ISSPIT.
- For each venue, check recent scope and submission deadlines (requires live access or verified venue pages).
- Record venue recommendations in `paper/publication_venues.md` without guaranteeing acceptance.

## Unresolved Paper Tasks
- Complete verified bibliography (30+ papers).
- Confirm dataset download and compatibility.
- Implement and test code framework.
- Run experiments and log real results.
- Draft each section with real citations and real results only.
