"""
Preprocessing & Feature Extraction for Underwater Acoustic Classification
Tested on DeepShip dataset structure (class subdirectories with .wav files).
"""

import os
import json
import librosa
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings("ignore")

# ----------------------------------------------------------------------
# Configuration (adjust as needed)
# ----------------------------------------------------------------------
SAMPLE_RATE = 22050           # Target sample rate for all audio
N_MFCC = 13                   # Number of MFCC coefficients
N_MELS = 128                  # Mel bands for spectrogram
N_FFT = 2048                  # FFT window size
HOP_LENGTH = 512              # Hop length for STFT
DURATION = 5.0                # Fixed duration (seconds) — pad/truncate
SEED = 42

np.random.seed(SEED)

# ----------------------------------------------------------------------
# Core Feature Extraction
# ----------------------------------------------------------------------
def load_audio_fixed(path: str, sr: int = SAMPLE_RATE, duration: float = DURATION) -> np.ndarray:
    """Load audio, resample, and pad/truncate to fixed duration."""
    y, _ = librosa.load(path, sr=sr, duration=duration)
    target_len = int(sr * duration)
    if len(y) < target_len:
        y = np.pad(y, (0, target_len - len(y)), mode='constant')
    else:
        y = y[:target_len]
    return y


def extract_mfcc(y: np.ndarray, sr: int = SAMPLE_RATE,
                 n_mfcc: int = N_MFCC, n_fft: int = N_FFT,
                 hop_length: int = HOP_LENGTH) -> np.ndarray:
    """Extract MFCC features: shape (n_mfcc, time_frames)."""
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc,
                                n_fft=n_fft, hop_length=hop_length)
    # Delta and delta-delta for temporal dynamics
    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
    # Stack: (3 * n_mfcc, time_frames)
    return np.vstack([mfcc, mfcc_delta, mfcc_delta2])


def extract_mel_spectrogram(y: np.ndarray, sr: int = SAMPLE_RATE,
                            n_mels: int = N_MELS, n_fft: int = N_FFT,
                            hop_length: int = HOP_LENGTH) -> np.ndarray:
    """Extract log-mel spectrogram: shape (n_mels, time_frames)."""
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                         n_fft=n_fft, hop_length=hop_length)
    log_mel = librosa.power_to_db(mel, ref=np.max)
    return log_mel


def extract_combined_features(y: np.ndarray, sr: int = SAMPLE_RATE) -> Dict[str, np.ndarray]:
    """Extract both MFCC and mel-spectrogram features."""
    return {
        "mfcc": extract_mfcc(y, sr),
        "mel_spectrogram": extract_mel_spectrogram(y, sr)
    }


# ----------------------------------------------------------------------
# Noise Augmentation (for robustness testing)
# ----------------------------------------------------------------------
def add_gaussian_noise(y: np.ndarray, snr_db: float = 10.0) -> np.ndarray:
    """Add Gaussian white noise at specified SNR (dB)."""
    signal_power = np.mean(y ** 2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(noise_power), y.shape)
    return y + noise


def add_impulse_noise(y: np.ndarray, density: float = 0.01,
                      amplitude_range: Tuple[float, float] = (-1.0, 1.0)) -> np.ndarray:
    """Add random impulse (salt-and-pepper) noise."""
    mask = np.random.random(y.shape) < density
    impulses = np.random.uniform(amplitude_range[0], amplitude_range[1], y.shape)
    y_noisy = y.copy()
    y_noisy[mask] = impulses[mask]
    return y_noisy


def augment_with_noise(y: np.ndarray, snr_db: float = 10.0,
                       noise_type: str = "gaussian") -> np.ndarray:
    """Apply noise augmentation."""
    if noise_type == "gaussian":
        return add_gaussian_noise(y, snr_db)
    elif noise_type == "impulse":
        return add_impulse_noise(y)
    else:
        raise ValueError(f"Unknown noise type: {noise_type}")


# ----------------------------------------------------------------------
# Dataset Loading & Splitting
# ----------------------------------------------------------------------
def discover_dataset(root_dir: str) -> List[Dict]:
    """
    Discover all .wav files under class subdirectories.
    Returns list of dicts: {'path': ..., 'class': ..., 'class_idx': ...}
    """
    root = Path(root_dir)
    class_dirs = sorted([d for d in root.iterdir() if d.is_dir()])
    class_to_idx = {d.name: i for i, d in enumerate(class_dirs)}

    samples = []
    for class_dir in class_dirs:
        for wav_file in class_dir.glob("*.wav"):
            samples.append({
                "path": str(wav_file),
                "class": class_dir.name,
                "class_idx": class_to_idx[class_dir.name]
            })
    return samples


def create_stratified_split(samples: List[Dict],
                            train_ratio: float = 0.7,
                            val_ratio: float = 0.15,
                            test_ratio: float = 0.15,
                            seed: int = SEED) -> Tuple[List, List, List]:
    """Create stratified train/val/test split preserving class ratios."""
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6

    np.random.seed(seed)
    by_class = {}
    for s in samples:
        by_class.setdefault(s["class_idx"], []).append(s)

    train, val, test = [], [], []
    for class_idx, class_samples in by_class.items():
        np.random.shuffle(class_samples)
        n = len(class_samples)
        n_train = int(n * train_ratio)
        n_val = int(n * val_ratio)

        train.extend(class_samples[:n_train])
        val.extend(class_samples[n_train:n_train + n_val])
        test.extend(class_samples[n_train + n_val:])

    np.random.shuffle(train)
    np.random.shuffle(val)
    np.random.shuffle(test)
    return train, val, test


def save_manifest(split_name: str, samples: List[Dict], out_dir: str,
                  feature_params: Dict = None):
    """Save split manifest with metadata for reproducibility."""
    os.makedirs(out_dir, exist_ok=True)
    manifest = {
        "split": split_name,
        "n_samples": len(samples),
        "classes": sorted(set(s["class"] for s in samples)),
        "feature_params": feature_params or {
            "sample_rate": SAMPLE_RATE,
            "duration": DURATION,
            "n_mfcc": N_MFCC,
            "n_mels": N_MELS,
            "n_fft": N_FFT,
            "hop_length": HOP_LENGTH
        },
        "samples": samples
    }
    out_path = os.path.join(out_dir, f"{split_name}_manifest.json")
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Saved {split_name} manifest: {out_path} ({len(samples)} samples)")


def load_manifest(manifest_path: str) -> List[Dict]:
    """Load samples from manifest."""
    with open(manifest_path, "r") as f:
        data = json.load(f)
    return data["samples"]


# ----------------------------------------------------------------------
# Feature Matrix Construction (for traditional ML)
# ----------------------------------------------------------------------
def compute_feature_vector(features: Dict[str, np.ndarray],
                           method: str = "mean_std") -> np.ndarray:
    """
    Convert variable-length feature matrices to fixed-size vectors.
    method: 'mean_std' -> concatenate mean and std across time axis for each feature type
    """
    vectors = []
    for feat_name, feat_matrix in features.items():
        # feat_matrix shape: (feature_dim, time_frames)
        mean_feat = np.mean(feat_matrix, axis=1)
        std_feat = np.std(feat_matrix, axis=1)
        vectors.append(mean_feat)
        vectors.append(std_feat)
    return np.concatenate(vectors)


def build_feature_matrix(samples: List[Dict],
                         feature_type: str = "mfcc",
                         augment: bool = False,
                         snr_db: float = 10.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Build feature matrix X and label vector y from samples.
    feature_type: 'mfcc', 'mel', or 'combined'
    Returns: X (n_samples, n_features), y (n_samples,)
    """
    X_list, y_list = [], []

    for s in samples:
        y_audio = load_audio_fixed(s["path"])
        if augment:
            y_audio = augment_with_noise(y_audio, snr_db, "gaussian")

        feats = extract_combined_features(y_audio)

        if feature_type == "mfcc":
            feat_vec = compute_feature_vector({"mfcc": feats["mfcc"]})
        elif feature_type == "mel":
            feat_vec = compute_feature_vector({"mel_spectrogram": feats["mel_spectrogram"]})
        elif feature_type == "combined":
            feat_vec = compute_feature_vector(feats)
        else:
            raise ValueError(f"Unknown feature_type: {feature_type}")

        X_list.append(feat_vec)
        y_list.append(s["class_idx"])

    return np.array(X_list), np.array(y_list)


# ----------------------------------------------------------------------
# Main Pipeline Function
# ----------------------------------------------------------------------
def run_preprocessing_pipeline(dataset_root: str,
                               output_dir: str,
                               feature_type: str = "combined") -> Dict:
    """
    Full preprocessing pipeline: discover -> split -> extract features -> save.
    Returns dict with paths to saved artifacts.
    """
    print(f"Discovering dataset at: {dataset_root}")
    samples = discover_dataset(dataset_root)
    print(f"Found {len(samples)} samples across {len(set(s['class'] for s in samples))} classes")

    train, val, test = create_stratified_split(samples)
    print(f"Split: train={len(train)}, val={len(val)}, test={len(test)}")

    feature_params = {
        "sample_rate": SAMPLE_RATE,
        "duration": DURATION,
        "n_mfcc": N_MFCC,
        "n_mels": N_MELS,
        "n_fft": N_FFT,
        "hop_length": HOP_LENGTH,
        "feature_type": feature_type
    }

    # Save manifests
    save_manifest("train", train, output_dir, feature_params)
    save_manifest("val", val, output_dir, feature_params)
    save_manifest("test", test, output_dir, feature_params)

    # Build feature matrices for traditional ML
    X_train, y_train = build_feature_matrix(train, feature_type)
    X_val, y_val = build_feature_matrix(val, feature_type)
    X_test, y_test = build_feature_matrix(test, feature_type)

    print(f"Feature shapes: train={X_train.shape}, val={X_val.shape}, test={X_test.shape}")

    # Save feature matrices
    np.savez(os.path.join(output_dir, "features_train.npz"), X=X_train, y=y_train)
    np.savez(os.path.join(output_dir, "features_val.npz"), X=X_val, y=y_val)
    np.savez(os.path.join(output_dir, "features_test.npz"), X=X_test, y=y_test)

    return {
        "manifest_dir": output_dir,
        "feature_params": feature_params,
        "n_classes": len(set(s["class"] for s in samples)),
        "class_names": sorted(set(s["class"] for s in samples))
    }


if __name__ == "__main__":
    # Quick test: discover dataset and show stats
    dataset_root = r"C:\Users\SYTEC\OneDrive\Desktop\Research\Underwater_Acoustic_Research\datasets\DeepShip\DeepShip-main"
    samples = discover_dataset(dataset_root)
    print(f"Total samples: {len(samples)}")
    for s in samples[:3]:
        print(f"  {s['class']}: {s['path']}")