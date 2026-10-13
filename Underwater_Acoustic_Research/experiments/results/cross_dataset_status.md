# Cross-Dataset Evaluation — Verified Status

Status: NOT PERFORMED — DATASET ACCESS UNVERIFIED. NO FABRICATED RESULTS.

## Verified Dataset Access Status
- DeepShip (`datasets/DeepShip/DeepShip-main/`): VERIFIED — 68 .wav files inspected (Cargo, Passengership, Tanker, Tug). Preprocessing executed (manifests + feature matrices saved).
- ShipsEar (`https://data.mendeley.com/datasets/4tgpdyrp2d/1`): Mendeley domain verified; download/access requires authentication (page shows "Dataset Not Found" / auth barrier). No files downloaded. No audio inspected.
- IARA (institutional repository reference): URL unverified by live fetch. No download confirmed. No audio inspected.
- SonAIr (search reference): URL unverified. No download confirmed.

## Cross-Dataset Protocol (Not Executed)
The cross-dataset evaluation protocol (`load_cross_dataset_pair` in `reproducible_framework.py`) requires:
1. Verified dataset paths for both train and test datasets.
2. Aligned label taxonomy (e.g., DeepShip's 4 classes vs ShipsEar's 5 classes — taxonomy differences unverified).
3. Actual feature extraction and model training/evaluation across paired datasets.

None of these requirements are met with verified data. Therefore:
- NO cross-dataset accuracy metrics exist.
- NO cross-dataset macro-F1 metrics exist.
- NO cross-dataset inference latency measurements exist.
- NO fabricated cross-dataset claims are included in any paper section.

## What Would Be Required (Verified Framework — Not Executed)
To complete cross-dataset evaluation with verified results:
1. Confirm ShipsEar download/access (resolve Mendeley auth barrier or find alternative source).
2. Confirm IARA download/access (verify institutional repository URL).
3. Resolve label taxonomy alignment (compare DeepShip 4-class vs ShipsEar 5-class vs IARA taxonomy — requires inspection of actual dataset metadata).
4. Execute `load_cross_dataset_pair` with verified manifest paths.
5. Train baseline models (SVM, Random Forest, or CNN if implemented) on DeepShip train set.
6. Evaluate on ShipsEar/IARA test sets using `track_direction_a_metrics`.
7. Log all results with reproducible parameters (seed=42, feature_type="combined", etc.).
8. Save verified metrics to `experiments/` (no fabricated numbers).

## Verified Note for Paper
The paper (`paper/draft_sections_1_4.md` Section 5) clearly states cross-dataset evaluation is NOT PERFORMED. Section 6 clearly labels cross-dataset metrics as NOT AVAILABLE. Section 7 includes this as a verified limitation. No cross-dataset results are fabricated.
