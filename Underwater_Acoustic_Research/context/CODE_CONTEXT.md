# CODE CONTEXT — Python Implementation Framework

Status: FRAMEWORK ONLY — NO CODE TESTED. NO DATASET DOWNLOADED. NO RESULTS FABRICATED.

## Recommended Environment Setup (Untested)
```bash
conda create -n underwater_acoustic python=3.11 -y
conda activate underwater_acoustic
pip install numpy pandas scikit-learn librosa tensorflow torch matplotlib seaborn
```
Note: This is an untested installation sequence. Verify package compatibility before use.

## Project Structure Under `code/`
```
code/
├── setup_env.sh / setup_env.bat
├── download_verify.py (unimplemented — needs real URLs)
├── preprocess_audio.py (framework — untested)
├── feature_extraction.py (MFCC / mel-spectrogram — untested)
├── baseline_models.py (SVM, Random Forest, compact CNN — untested)
├── train_evaluate.py (training loop, metrics — untested)
├── noise_robustness.py (noise injection framework — untested)
├── cross_dataset.py (cross-dataset evaluation framework — untested)
├── experiment_logger.py (logs, graphs, ablation — untested)
└── rpi_deploy_notes.md (optional deployment notes — unimplemented)
```

## Key Functions (Unimplemented / Untested — Framework Only)
- `extract_mfcc(path, sr=22050, n_mfcc=13)` — returns feature array.
- `extract_mel_spectrogram(path, sr=22050, n_mels=128)` — returns mel spec.
- `load_split(manifest_json)` — loads train/test indices from saved manifest.
- `evaluate_model(model, X_test, y_test, metrics=['accuracy','macro_f1','inference_time_ms','ram_mb'])`

## Reproducibility Requirements (Verified Protocol)
- Save exact `requirements.txt` and Python version.
- Save random seed (`np.random.seed(42)` or equivalent) for every experiment.
- Save preprocessing parameters (sample rate, window size, hop length, normalization method).
- Save model architecture as code (not binary weights unless saved with version).
- Log all hyperparameters in a JSON file per experiment.

## Important Constraints
- NO fabricated experimental results will be written to `experiments/`.
- Any result table must come from an actual run of the code above.
- If an experiment fails, document the failure (error message, stack trace summary) rather than inventing success numbers.

## Next Development Steps
1. Once dataset URLs are verified, implement `download_verify.py`.
2. Once a small sample of audio is available, test `preprocess_audio.py` and `feature_extraction.py`.
3. Only after feature extraction works, implement `baseline_models.py`.
4. Run first experiment; log results honestly (even if poor).
