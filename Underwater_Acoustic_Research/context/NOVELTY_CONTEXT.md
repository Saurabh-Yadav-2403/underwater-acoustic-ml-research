# NOVELTY CONTEXT — Novelty Assessment

Status: PENDING adversarial verification with 30+ real papers. Not claimed as verified.

## Topic Statement
"Robust and Lightweight Machine Learning for Underwater Acoustic Signal Classification" — investigating robust and lightweight ML techniques for underwater acoustic classification using public datasets, emphasizing accuracy, robustness, computational complexity, memory, inference time, and cross-dataset generalization.

## Preliminary Novelty Assessment (Based on Training Knowledge — Needs Verification)
- High-level concept: Combining underwater acoustic classification WITH lightweight ML + cross-dataset evaluation IS a recognized research direction.
- Potential weakness: If the contribution is only "evaluate SVM, Random Forest, and compact CNN on DeepShip/IARA," this may be considered an application study rather than a novel contribution, since many papers since 2021 have performed similar evaluations.
- Potential strength: If the contribution includes a NEW method (e.g., a specific noise-robust feature extraction pipeline, a domain-adaptive lightweight architecture with measurable cross-dataset gains, and explicit Raspberry Pi deployment benchmarks), this could be defensible.

## Counterexamples / Similar Work (Need Live Verification)
The following categories exist in literature and must be checked against real papers:
1. DeepShip dataset evaluations with CNN/LSTM (2021+ papers).
2. Noise-robust underwater classification with augmentation / adversarial training.
3. Cross-dataset studies across ShipsEar and DeepShip.
4. Edge/embedded deployment studies for underwater IoT (Raspberry Pi references exist in surveys but full benchmark studies are rarer).

## Three Alternative Directions (Defensible Gaps) — If Original Topic Is Weak

### Direction A: Domain-Adaptive Lightweight CNN with Cross-Dataset Generalization
- Gap: Most lightweight CNNs are trained and tested on a single dataset; domain adaptation between DeepShip and ShipsEar is rarely evaluated for compact models.
- RQ: Can a sub-1MB CNN with domain-adversarial training maintain >85% macro-F1 when trained on DeepShip and tested on ShipsEar?
- Contribution: A reproducible benchmark + domain adaptation layer for underwater acoustic transfer.

### Direction B: Noise-Robust Feature Fusion (MFCC + Mel-Spectrogram + Statistical) with SVM Baseline for Edge
- Gap: High-performing deep models dominate literature, but lightweight statistical + spectral fusion for noisy underwater recordings with explicit memory/inference benchmarks on Raspberry Pi is underreported.
- RQ: Does a fused feature + Random Forest / linear SVM achieve competitive macro-F1 under added Gaussian/impulse noise with <50MB RAM?
- Contribution: A reproducible, low-resource baseline framework + noise robustness curves.

### Direction C: Quantized / Pruned Compact CNN for Real-Time Underwater IoT Classification
- Gap: Model compression (quantization, pruning, knowledge distillation) is well-studied for image/audio on edge, but rarely applied specifically to underwater acoustic signals with cross-environment validation.
- RQ: Can a quantized MobileNet-style architecture (<500KB, <100ms inference on Raspberry Pi 4) maintain within 3% accuracy drop vs. full model across DeepShip and IARA?
- Contribution: A compressed model + deployment script + cross-dataset performance report.

## Verification Requirements Before Claiming Novelty
- [ ] Confirm at least 30 real papers exist with verifiable DOIs.
- [ ] Confirm no recent (2024–2025) IEEE paper exactly matches the proposal's combination.
- [ ] Confirm dataset download pages exist and licenses allow academic use.
- [ ] Confirm no fabricated citations exist in paper matrix.
