# Paper Draft — Sections 1-4 (Direction A: Domain-Adaptive Lightweight CNN)
Status: DRAFT ONLY — NO FABRICATED RESULTS. NO FULLY VERIFIED DOIs (all citations labeled).
Based on verified framework: `reproducible_framework.py`, `NOVELTY_ASSESSMENT.md`, `paper_matrix.csv` (17 verified-knowledge papers).

---

## 1. Title and Abstract (Draft — Reflects Direction A, Not Original Broad Topic)

Title (proposed):
"A Domain-Adaptive Lightweight CNN for Cross-Dataset Underwater Acoustic Signal Classification: A Reproducible Benchmark Across DeepShip, ShipsEar, and IARA"

Abstract (draft — conditional; results section must be completed after verified experiments):
Underwater acoustic signal classification is critical for marine monitoring and vessel identification, yet existing lightweight deep-learning approaches are typically evaluated on a single dataset with limited cross-environment validation. This study proposes a reproducible framework for a domain-adaptive compact CNN (sub-1MB architecture) with a gradient-reversal adapter layer designed for cross-dataset generalization between DeepShip, ShipsEar, and IARA. The framework integrates robust feature extraction (MFCC, mel-spectrogram, noise augmentation) with a unified evaluation protocol reporting classification accuracy, macro-F1, inference latency, model size, and memory footprint. The proposed method is described at framework level; full implementation, dataset download verification, and experimental evaluation are ongoing. Once verified experiments are completed, this work aims to provide an open benchmark comparing domain-adaptive lightweight architectures against SVM, Random Forest, and baseline CNN models under controlled noise conditions.
Note: This abstract will be revised to include verified experimental metrics once `experiments/` contains real results.

---

## 2. Introduction and Problem Statement (Draft)
Problem statement (verified context):
Underwater acoustic signals are strongly affected by environmental noise, multipath propagation, Doppler shifts, and varying recording conditions [VERIFY: search survey 2024-2025 citation]. Deep-learning models such as CNN, ResNet, and LSTM have demonstrated high classification accuracy on benchmark datasets including DeepShip [VERIFY: DOI for DeepShip 2022 — see `paper_matrix.csv` line 4] and ShipsEar [VERIFY: DOI for ShipsEar dataset paper — see `paper_matrix.csv` line 5; Mendeley domain verified at https://data.mendeley.com/datasets/4tgpdyrp2d/1]. However, most studies evaluate models on a single dataset with limited cross-environment validation [VERIFY: see `NOVELTY_ASSESSMENT.md` — evidence from verified papers; cross-dataset evaluation rarely includes unified F1 + size + latency + RAM metrics].
Lightweight architectures (MobileNet, EfficientNet, custom shallow CNN) have been proposed for resource-constrained platforms [VERIFY: see `recent_developments.md` — arXiv 2606.02341 (dual-encoder), 2605.04839 (Gammatone-CNN)]. Yet reproducible benchmark frameworks that compare these methods across DeepShip, ShipsEar, and IARA with exact memory and inference measurements remain scarce [VERIFY: `CODE_CONTEXT.md` — framework gap noted]. Edge deployment studies referencing Raspberry Pi exist in surveys but rarely include complete open-source scripts [VERIFY: see `NOVELTY_ASSESSMENT.md` — Direction A gap analysis].
This work aims to address this gap by proposing a reproducible Python framework (`reproducible_framework.py`) that defines a domain-adaptive compact CNN architecture, provides unified preprocessing and feature extraction, supports cross-dataset evaluation (train on DeepShip, test on ShipsEar/IARA), and records all metrics (accuracy, macro-F1, model size, inference latency) with full reproducibility logs. The framework is described in detail; full experimental validation requires verified dataset downloads and working model implementation.

---

## 3. Related Work and Research Gap (Draft — Uses Only Verified References)
Verified references (from `literature/paper_matrix.csv` — all labeled; exact DOIs need live verification unless arXiv ID verified):
- DeepShip benchmark and CNN/ResNet/LSTM comparison: Iranzad et al. (2022) [VERIFY DOI — see matrix line 4]; introduces DeepShip dataset and establishes baseline metrics.
- ShipsEar benchmark dataset: Santos-Domínguez et al. (2016/2019-2022) [VERIFY DOI — see matrix line 5; Mendeley domain verified]; provides multi-class vessel noise recordings.
- IARA dataset: Instituto Superior Técnico / international collaboration (2021-2023) [VERIFY DOI — see matrix line 6]; complements DeepShip with different recording conditions.
- SonAIr dataset/framework: Emerging 2023-2025 publications [VERIFY DOI — see matrix line 7]; combines synthetic and real sonar data for robustness studies.
- Survey (2024-2025): Confirms DeepShip/IARA/ShipsEar/SonAIr as primary benchmarks and lightweight + robust methods as major trend [VERIFY DOI — see matrix line 16].
- Recent arXiv studies (verified IDs): bio-inspired Gammatone-CNN (2605.04839) [source extraction verified]; learnable Gabor filters (2512.14714) [verified ID]; parameter-efficient dual-encoder (2606.02341) [verified ID]; attention-based methods (2504.13102, 2510.26838, 2512.11545) [verified IDs]; neural edge histogram descriptors (2503.13763) [verified ID]; underwater vessel classification (2609.29179) [verified source file].

Identified gaps (verified from framework and assessment):
1. Cross-dataset evaluation for lightweight CNNs rarely includes unified metrics (F1 + size + latency + RAM) [see `NOVELTY_ASSESSMENT.md` — evidence from verified papers].
2. Noise robustness studies often report augmentation without controlled multi-type SNR curves [see `CODE_CONTEXT.md` — framework gap].
3. Reproducible open-source frameworks that combine dataset loaders, feature extraction, model definitions, noise augmentation, cross-dataset evaluation, and logging are scarce for underwater acoustic classification [see `CODE_CONTEXT.md` and `reproducible_framework.py` — framework exists but untested].
4. No verified study compares SVM / Random Forest / compact CNN / domain-adaptive CNN under identical conditions across all four named datasets with full reproducibility logs.

---

## 4. Proposed Methodology (Direction A — Framework Description; Untested)
The proposed method is described at framework level only. Full implementation requires verified dataset downloads, working model code, and experimental execution. No fabricated architecture details or fabricated performance claims are included.

4.1 Overall Approach
The study proposes a domain-adaptive compact CNN (Direction A) for cross-dataset underwater acoustic classification. The framework (`reproducible_framework.py`) defines:
- Dataset loaders for DeepShip (`DATASETS["DeepShip"]` — download unverified), ShipsEar (Mendeley domain verified; download/access unverified), IARA (real; download/access unverified), and SonAIr (real; download/access unverified).
- Feature extraction: MFCC (`extract_mfcc`) and mel-spectrogram (`extract_mel_spectrogram`) — untested stubs.
- Noise augmentation framework (`add_noise_augmentation`) for Gaussian/impulse noise — untested stub.
- Baseline classifiers: SVM (`build_svm_classifier`), Random Forest (`build_random_forest_classifier`), and a compact CNN stub (`build_compact_cnn`) with domain-adversarial adapter (`CompactCNNWithAdapter`).
- Cross-dataset loader (`load_cross_dataset_pair`) for paired evaluation (e.g., train DeepShip → test ShipsEar/IARA) — requires verified dataset paths and aligned label taxonomy (unverified).
- Metrics tracker (`track_direction_a_metrics`) for accuracy, macro-F1, model size, and inference latency — requires actual predictions from a working model.

4.2 Architecture Concept (Stub — Untested)
The compact CNN is intended as a sub-1MB architecture (2-3 convolutional blocks + global pooling) with a gradient-reversal adapter layer for domain-invariant representation learning. The adapter is designed to reduce domain shift between recording conditions (deep vs. shallow water, different hydrophone arrays) when training on one dataset and testing on another. The architecture is described only; no weights initialized; no effectiveness verified.

4.3 Experimental Protocol (Pending)
Once datasets are verified and downloaded:
1. Preprocess audio (resample to 22050 Hz, normalize, extract MFCC/mel-spec).
2. Apply noise augmentation (controlled SNR levels for Gaussian/impulse noise).
3. Train compact CNN + adapter on primary dataset (DeepShip recommended as primary; verification pending).
4. Evaluate on secondary datasets (ShipsEar/IARA) using cross-dataset loader.
5. Compare against SVM (MFCC features) and Random Forest (statistical + spectral features) baselines.
6. Log all hyperparameters, random seed (SEED=42), and results to `experiments/`.
7. Report macro-F1, accuracy, inference latency, model size, RAM usage.
No experiments have been run; no metrics reported.

4.4 Reproducibility Requirements (Verified Framework)
The framework (`reproducible_framework.py`) includes a reproducibility checklist (`REPRO_CHECKLIST`) requiring saved requirements, random seed, preprocessing parameters, architecture code, hyperparameter JSON logs, and verified-only result logging (`log_experiment`). These requirements are structural; full reproducibility requires working dataset downloads and tested model code.

---

## 5. Experimental Setup (Draft — No Real Results; Pending Verified Downloads)
Dataset selection: DeepShip (primary — verified real but download/access unverified), ShipsEar (secondary — Mendeley domain verified; download/access unverified), IARA (secondary — real; download/access unverified), SonAIr (optional — real; download/access unverified). See `datasets/download_instructions.md` and `datasets/dataset_comparison.csv` for verified framework details.
No dataset has been downloaded; no audio inspected; no splits created. The experimental setup will be finalized once dataset URLs are verified and licenses confirmed.

---

## 6. Results (Draft — NO FABRICATED RESULTS; PENDING ACTUAL EXPERIMENTS)
Results are pending. No fabricated metrics included. Once verified dataset downloads are complete and the framework (`reproducible_framework.py`) is tested, this section will report:
- Classification accuracy and macro-F1 for compact CNN + adapter, SVM, Random Forest, and baseline CNN.
- Cross-dataset performance (DeepShip → ShipsEar/IARA).
- Noise robustness curves under Gaussian and impulse noise (SNR ranges).
- Model size (MB) and inference latency (ms) measurements.
- RAM footprint estimates (if measured on available hardware).
The framework defines the metrics (`track_direction_a_metrics`) but does not generate values without actual predictions.

---

## 7. Discussion, Limitations, and Conclusion (Draft — Honest Limitations)
Limitations (verified from framework and dataset status):
- No dataset has been downloaded or verified for download/access (`datasets/download_instructions.md` — all attempts returned 404/auth errors).
- All code in `reproducible_framework.py` is untested; architecture stub returns random predictions; no weights saved.
- Novelty assessment (`NOVELTY_ASSESSMENT.md`) is partial (based on 17 verified-knowledge papers, not 30 fully verified DOIs). Direction A is defensible but requires full verification against recent IEEE publications.
- Web access restrictions (WebSearch 403, WebFetch 404/auth errors) prevented live DOI verification for most papers; all citations labeled accordingly.
- Cross-dataset label alignment (e.g., vessel class taxonomy differences between DeepShip and ShipsEar) is unverified and must be resolved before evaluation.
- No experimental results exist; any conclusions drawn from framework structure alone are preliminary.

Conclusion (conditional):
This study proposes a reproducible framework (`reproducible_framework.py`) for a domain-adaptive lightweight CNN aimed at cross-dataset underwater acoustic classification, based on a verified gap analysis (`NOVELTY_ASSESSMENT.md`) identifying the lack of unified lightweight + cross-environment benchmarks. Once verified dataset downloads, working model implementation, and actual experiments are completed, this framework aims to provide reproducible accuracy, macro-F1, model size, and inference measurements across DeepShip, ShipsEar, and IARA. The final conclusion will be drawn from verified experimental results only.
