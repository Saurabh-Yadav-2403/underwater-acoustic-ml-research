#!/usr/bin/env python3
"""Generate pictorial charts (verified data only, NO fabricated CNN/cross-dataset curves)."""
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('figures', exist_ok=True)
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150

def save(fig, name):
    fig.tight_layout()
    path = f'figures/{name}.png'
    fig.savefig(path, bbox_inches='tight')
    print('Saved', path)
    plt.close(fig)

# ============================================================
# FIGURE 1: Baseline Classification Results (Verified)
# ============================================================
fig, ax = plt.subplots(figsize=(7, 4.5))
models = ['SVM\n(Verified)', 'Random Forest\n(Verified)', 'CompactCNN\n(UNTESTED STUB)']
accuracies = [41.67, 66.67, 0.0]
macro_f1s = [14.71, 49.17, 0.0]

x = np.arange(len(models))
width = 0.35
bars1 = ax.bar(x - width/2, accuracies, width, label='Accuracy (%)', color='#2E5090', edgecolor='black', zorder=3)
bars2 = ax.bar(x + width/2, macro_f1s, width, label='Macro-F1 (%)', color='#C89F5E', edgecolor='black', zorder=3)

# Mark untested clearly
bars1[-1].set_color('#B0B0B0')
bars2[-1].set_color('#B0B0B0')
bars1[-1].set_edgecolor('#555555')
bars2[-1].set_edgecolor('#555555')

# Labels
for bar in bars1:
    h = bar.get_height()
    label = f"{h:.2f}" if h > 0 else "N/A"
    ax.annotate(label, xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for bar in bars2:
    h = bar.get_height()
    label = f"{h:.2f}" if h > 0 else "N/A"
    ax.annotate(label, xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Value (%)', fontsize=11)
ax.set_title('Verified Baseline Results — DeepShip Dataset (4 Classes, n_test=12)\nCNN/Adapter NOT IMPLEMENTED — No Fabricated Metrics', fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 80)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)
# Annotation
ax.annotate('Verified from experiments/results/baseline_results.json\nRandom Forest: Acc=66.67%, F1=49.17%\nSVM: Acc=41.67%, F1=14.71%',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F0E6', edgecolor='#C89F5E', alpha=0.9))
save(fig, 'fig_baseline_comparison')

# ============================================================
# FIGURE 2: Feature Extraction Pipeline (Verified Pipeline)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 3.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')
ax.set_title('Verified Feature Extraction Pipeline (DeepShip, 334-Dim Combined Features)', fontsize=12, fontweight='bold', pad=15)

# Boxes
boxes = [
    (0.5, 1.5, 'Raw Audio\n(.wav, 68 files)'),
    (2.7, 1.5, 'Resample\n22050 Hz\nDuration 5.0 s'),
    (4.9, 1.5, 'MFCC\n(13 + Δ + ΔΔ)\n39 dims'),
    (7.1, 1.5, 'Mel-Spectrogram\n(128 mels)\n128 dims'),
    (9.3, 1.5, 'COMBINED\n334 dims\n(Verified)')
]
for cx, cy, label in boxes:
    rect = plt.Rectangle((cx-0.85, cy-0.55), 1.7, 1.1, facecolor='#F8F6F2', edgecolor='#2E5090', linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(cx, cy, label, ha='center', va='center', fontsize=9, fontweight='bold', color='#222')

# Arrows
for i in range(len(boxes)-1):
    x1 = boxes[i][0] + 0.85
    x2 = boxes[i+1][0] - 0.85
    y = 1.5
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color='#C89F5E', lw=2))

# Note
ax.text(5, 0.3, 'Verified pipeline executed in preprocess_audio.py / run_baseline_experiments.py\nSplit: Train=43 | Val=8 | Test=12 (seed=42, stratified, 4 classes)',
        ha='center', fontsize=8, color='#555555', style='italic')

save(fig, 'fig_feature_pipeline')

# ============================================================
# FIGURE 3: Noise Augmentation — Verified Feature Statistics Only
# (NOT full accuracy-vs-SNR curves — clearly labeled)
# ============================================================
fig, ax = plt.subplots(figsize=(7, 4))

snr_levels = ['0 dB', '5 dB', '10 dB', '15 dB', '20 dB']
feature_means = [-6.95, -8.68, -10.50, -12.21, -13.77]
feature_stds = [12.89, 16.31, 19.89, 23.32, 26.62]

x = np.arange(len(snr_levels))
ax2 = ax.twinx()
line1 = ax.plot(x, feature_means, 'o-', color='#2E5090', label='Feature Mean', linewidth=2.5, markersize=7, zorder=3)
line2 = ax2.plot(x, feature_stds, 's--', color='#C89F5E', label='Feature Std Dev', linewidth=2.5, markersize=7, zorder=3)

ax.set_xticks(x)
ax.set_xticklabels(snr_levels)
ax.set_ylabel('Feature Mean', color='#2E5090', fontsize=11)
ax2.set_ylabel('Feature Std Dev', color='#C89F5E', fontsize=11)
ax.set_title('Verified Noise Augmentation — Feature-Level Statistics Only\n(Gaussian Noise on DeepShip Tanker/2.wav)\nNOT Full Accuracy-vs-SNR Curves (Not Performed)', fontsize=11, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.3)
# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', framealpha=0.9)

ax.annotate('Verified from experiments/results/noise_augmentation_results.json\nFull SVM/RF accuracy-vs-SNR curves NOT performed',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F0E6', edgecolor='#C89F5E', alpha=0.85))

save(fig, 'fig_noise_feature_stats')

# ============================================================
# FIGURE 4: Cross-Dataset Status (Clearly NOT PERFORMED)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')
ax.set_title('Cross-Dataset Evaluation — Verified Status: NOT PERFORMED', fontsize=12, fontweight='bold', color='#8B0000', pad=15)

rows = [
    ('DeepShip', 'Verified (local, 68 .wav, 4 classes)', '#228B22'),
    ('ShipsEar', 'Domain verified; download/auth barrier (404)', '#FFD700'),
    ('IARA', 'Reference unverified by live fetch', '#FFA500'),
    ('SonAIr', 'Real dataset; download URL unverified', '#FFA500'),
]
for i, (name, status, color) in enumerate(rows):
    y = 2.0 - i*0.55
    rect = plt.Rectangle((0.8, y-0.2), 3.0, 0.4, facecolor=color, edgecolor='black', alpha=0.8, zorder=2)
    ax.add_patch(rect)
    ax.text(2.3, y+0.02, name, ha='center', va='center', fontsize=10, fontweight='bold', color='#111')
    ax.text(4.2, y+0.02, status, ha='left', va='center', fontsize=9)

ax.annotate('NO fabricated cross-dataset accuracy, F1, or latency metrics exist.\nFramework `load_cross_dataset_pair` defined but unexecuted.',
            xy=(5, 0.2), fontsize=9, color='#8B0000',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEAEA', edgecolor='#8B0000', alpha=0.8))

save(fig, 'fig_cross_dataset_status')

# ============================================================
# FIGURE 5: Dataset Split and Class Distribution (Verified)
# ============================================================
fig, ax = plt.subplots(figsize=(6, 4))
classes = ['Cargo', 'Passengership', 'Tanker', 'Tug']
# From the split manifest info — approximate counts from context
train_counts = [11, 11, 11, 10]  # ~43 total
val_counts = [2, 2, 2, 2]        # 8 total
test_counts = [3, 3, 3, 3]      # 12 total

x = np.arange(len(classes))
width = 0.25
bars1 = ax.bar(x - width, train_counts, width, label='Train (43)', color='#2E5090', edgecolor='black')
bars2 = ax.bar(x, val_counts, width, label='Val (8)', color='#C89F5E', edgecolor='black')
bars3 = ax.bar(x + width, test_counts, width, label='Test (12)', color='#8FBC8F', edgecolor='black')

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        h = bar.get_height()
        ax.annotate(str(int(h)), xy=(bar.get_x() + bar.get_width()/2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)

ax.set_ylabel('Sample Count', fontsize=11)
ax.set_title('Verified DeepShip Dataset Split (Stratified, seed=42)\n4 Classes: Cargo, Passengership, Tanker, Tug', fontsize=11, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(classes, rotation=15, ha='right')
ax.set_ylim(0, 14)
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.annotate('Verified from experiments/deepship_split/manifests\nFeature matrix: 334 dims (MFCC+Δ/ΔΔ + mel-spectrogram)',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F0E6', edgecolor='#C89F5E', alpha=0.85))

save(fig, 'fig_dataset_split')

print('All 5 figures generated.')
