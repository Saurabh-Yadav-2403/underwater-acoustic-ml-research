# CODE CONTEXT — Python Implementation Framework

Status: PARTIALLY TESTED — BASELINE CLASSIFIERS RUN ON DEEPSHIP FEATURES. NO FABRICATED RESULTS.

## Implemented and Tested Components
- `preprocess_audio.py` — Tested and used to create DeepShip train/val/test splits and feature matrices
- `run_preprocessing.py` — Executed successfully to generate experiment manifests and features
- Baseline classifiers (SVM, Random Forest) — Implemented in `run_baseline_experiments.py` and tested on DeepShip features

## Project Structure Under `code/` (Updated)
```
code/
├── preprocessing/
│   ├── __init__.py
│   ├── preprocess_audio.py (TESTED — used for DeepShip experiments)
│   └── feature_extraction.py (framework — untested)
├── models/
│   ├── __init__.py
│   ├── baseline_models.py (SVM, Random Forest — TESTED via run_baseline_experiments.py)
│   ├── compact_cnn.py (framework — untested)
│   └── domain_adaptive.py (framework — untested)
├── experiments/
│   ├── run_baseline_experiments.py (TESTED — real results generated)
│   └── experiment_logger.py (framework — untested)
├── utils/
│   ├── __init__.py
│   ├── download_verify.py (unimplemented — needs real URLs)
│   └── cross_dataset.py (framework — untested)
└── rpi_deploy_notes.md (optional deployment notes — unimplemented)
```

## Key Functions (Status Update)
- `extract_mfcc(path, sr=22050, n_mfcc=13)` — TESTED — used in preprocessing pipeline
- `extract_mel_spectrogram(path, sr=22050, n_mels=128)` — TESTED — used in preprocessing pipeline
- `compute_feature_vector(features, method="mean_std")` — TESTED — converts variable-length features to fixed vectors
- `build_feature_matrix(samples, feature_type="combined")` — TESTED — creates X, y matrices for ML
- `evaluate_model(model, X_test, y_test)` — TESTED — computes accuracy, macro-F1, latency
- `load_split(manifest_json)` — TESTED — used in preprocessing pipeline
- `train_svm(X_train, y_train)` — TESTED — via scikit-learn SVC
- `train_random_forest(X_train, y_train)` — TESTED — via scikit-learn RandomForestClassifier

## Reproducibility Requirements (Followed)
- [x] Save exact `requirements.txt` and Python version (inherited from environment)
- [x] Save random seed (`np.random.seed(42)` used in all experiments)
- [x] Save preprocessing parameters (sample rate=22050, duration=5.0, n_mfcc=13, n_mels=128, n_fft=2048, hop_length=512)
- [x] Save model architecture as code (SVM and Random Forest configurations saved)
- [x] Log all hyperparameters in JSON per experiment (see experiments/results/baseline_results.json)
- [x] Only include results from actual runs (baseline results are REAL — no fabrication)

## Important Constraints (Followed)
- [x] NO fabricated experimental results written to `experiments/`
- [x] Any result table comes from an actual run of the code above
- [ ] If an experiment fails, document the failure rather than inventing success numbers (N/A — baseline succeeded)

## Experimental Results (REAL)
- **Experiments completed**: Baseline classification (SVM, Random Forest) on DeepShip dataset
- **Results location**: `experiments/results/baseline_results.json`
- **Key findings**: 
  - Random Forest outperforms SVM (66.67% vs 41.67% accuracy)
  - Both baselines show room for improvement versus deep learning approaches (~90% in literature)
  - Feature dimensionality: 334 dimensions (MFCC + delta/delta + mel-spectrogram)
  - Dataset split: 43 train, 8 validation, 12 test samples across 4 classes (Cargo, Passengership, Tanker, Tug)

## Next Development Steps
1. Implement and test `compact_cnn.py` with basic architecture
2. Implement domain adaptation components for Direction A
3. Run cross-dataset experiments (DeepShip → ShipsEar) once datasets verified
4. Implement noise robustness experiments with controlled SNR levels
5. Compare against literature results from verified papers in paper_matrix.csv