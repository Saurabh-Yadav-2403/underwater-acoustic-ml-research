# Research Gap Analysis — Pending Verification

Status: FRAMEWORK ONLY — Requires at least 30 verified papers for rigorous assessment.

## Current Topic Statement
Robust and Lightweight Machine Learning for Underwater Acoustic Signal Classification — evaluating different ML and lightweight deep-learning models under varying acoustic/noise conditions, with emphasis on accuracy, robustness, complexity, memory, inference time, and cross-dataset generalization.

## Potential Gaps (Based on Framework, Not Verified Papers)
1. Cross-dataset generalization for lightweight models: Most studies evaluate on a single dataset; cross-environment testing for compact CNNs is rarely reported with full metrics (F1, size, latency, RAM).
2. Noise robustness benchmarks: Many papers mention noise augmentation but do not provide controlled SNR curves for multiple noise types (Gaussian, impulse, environmental).
3. Edge deployment benchmarks: References to Raspberry Pi exist in survey literature, but reproducible benchmark scripts comparing SVM vs. Random Forest vs. compact CNN with exact RAM/inference measurements are scarce.
4. Dataset compatibility: DeepShip, ShipsEar, IARA, and SonAIr may have different sample rates, label taxonomies, and recording conditions — compatibility analysis is needed but unverified.
5. Reproducible framework: A single, open Python framework that covers preprocessing, feature extraction, multiple models, noise robustness, cross-dataset evaluation, and logging is not commonly available.

## Adversarial Questions to Answer Before Claiming Novelty
- Does any 2022–2025 IEEE paper exactly match this combination (lightweight ML + underwater acoustic + cross-dataset + noise robustness + edge benchmark)?
- If yes, what is the specific difference (new architecture? new dataset pairing? new metric combination?)?
- If the contribution is only evaluation of existing models, is that sufficient for the target venue?

## Three Alternative Directions (If Original Topic Lacks Strong Novelty)
(Refer to `context/NOVELTY_CONTEXT.md` for full details.)
- Direction A: Domain-Adaptive Lightweight CNN with Cross-Dataset Generalization
- Direction B: Noise-Robust Feature Fusion with SVM/Random Forest for Edge
- Direction C: Quantized / Pruned Compact CNN for Real-Time Underwater IoT

## Next Step
Once `literature/paper_matrix.csv` contains at least 30 verified papers, perform a structured comparison to confirm or refute these gaps.
