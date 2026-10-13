import sys
sys.path.insert(0, 'code')
from preprocess_audio import discover_dataset, load_audio_fixed, extract_mfcc, extract_mel_spectrogram
import librosa
import numpy as np
from pathlib import Path

# Test on a sample file
dataset_root = r'Underwater_Acoustic_Research/datasets/DeepShip/DeepShip-main'

# Discover dataset
classes = sorted([d.name for d in Path(dataset_root).iterdir() if d.is_dir()])
print(f'Classes: {classes}')

# Count files
for c in classes:
    files = list(Path(dataset_root, c).glob('*.wav'))
    print(f'  {c}: {len(files)} files')

# Load one sample
sample_path = list(Path(dataset_root, 'Cargo').glob('*.wav'))[0]
y, sr = librosa.load(str(sample_path), sr=None)
print(f'\nSample: {sample_path.name}')
print(f'Original: sr={sr} Hz, duration={len(y)/sr:.2f}s')

# Test fixed duration load
y_fixed = load_audio_fixed(str(sample_path))
print(f'Fixed: sr={22050} Hz, shape={y_fixed.shape}')

# Test feature extraction
mfcc = extract_mfcc(y_fixed)
print(f'MFCC shape: {mfcc.shape}')

mel = extract_mel_spectrogram(y_fixed)
print(f'Mel-spectrogram shape: {mel.shape}')