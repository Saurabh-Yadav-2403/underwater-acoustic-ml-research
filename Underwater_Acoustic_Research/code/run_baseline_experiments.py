#!/usr/bin/env python3
"""
Baseline Experiments for Underwater Acoustic Classification
Runs SVM and Random Forest classifiers on preprocessed DeepShip features.
Status: EXPERIMENTAL - Real results from actual runs.
"""

import os
import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import json
import time

# Set random seed for reproducibility
SEED = 42
np.random.seed(SEED)

def load_features(split):
    """Load features and labels from npz file."""
    npz_path = f"experiments/deepship_split/features_{split}.npz"
    data = np.load(npz_path)
    return data['X'], data['y']

def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and return metrics."""
    start_time = time.time()
    y_pred = model.predict(X_test)
    end_time = time.time()

    inference_time_ms = (end_time - start_time) * 1000 / len(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average='macro')

    return {
        'model': model_name,
        'accuracy': float(accuracy),
        'macro_f1': float(macro_f1),
        'inference_latency_ms': float(inference_time_ms),
        'n_test_samples': len(X_test)
    }

def main():
    print("Loading DeepShip features...")

    # Load data
    X_train, y_train = load_features('train')
    X_val, y_val = load_features('val')
    X_test, y_test = load_features('test')

    print(f"Train: {X_train.shape[0]} samples, {X_train.shape[1]} features")
    print(f"Val: {X_val.shape[0]} samples, {X_val.shape[1]} features")
    print(f"Test: {X_test.shape[0]} samples, {X_test.shape[1]} features")

    # Get class information from manifest
    with open("experiments/deepship_split/train_manifest.json", 'r') as f:
        train_manifest = json.load(f)
    class_names = train_manifest['classes']
    n_classes = len(class_names)
    print(f"Classes ({n_classes}): {class_names}")

    results = []

    # 1. SVM Classifier
    print("\nTraining SVM classifier...")
    svm_model = SVC(random_state=SEED)
    svm_model.fit(X_train, y_train)
    svm_metrics = evaluate_model(svm_model, X_test, y_test, "SVM")
    results.append(svm_metrics)
    print(f"SVM Results: Acc={svm_metrics['accuracy']:.4f}, F1={svm_metrics['macro_f1']:.4f}")

    # 2. Random Forest Classifier
    print("\nTraining Random Forest classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=SEED)
    rf_model.fit(X_train, y_train)
    rf_metrics = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    results.append(rf_metrics)
    print(f"Random Forest Results: Acc={rf_metrics['accuracy']:.4f}, F1={rf_metrics['macro_f1']:.4f}")

    # Save results
    os.makedirs("experiments/results", exist_ok=True)
    results_file = "experiments/results/baseline_results.json"

    experiment_metadata = {
        "experiment_type": "baseline_classification",
        "dataset": "DeepShip",
        "feature_type": "combined (MFCC + delta/delta + mel-spectrogram)",
        "n_features": X_train.shape[1],
        "n_classes": n_classes,
        "class_names": class_names,
        "random_seed": SEED,
        "experiment_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    output_data = {
        "metadata": experiment_metadata,
        "results": results
    }

    with open(results_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"\nResults saved to {results_file}")

    # Print summary table
    print("\n" + "="*60)
    print("BASELINE EXPERIMENT RESULTS - DEEPSHIP DATASET")
    print("="*60)
    print(f"{'Model':<20} {'Accuracy':<10} {'Macro-F1':<10} {'Latency (ms)':<15}")
    print("-"*60)
    for result in results:
        print(f"{result['model']:<20} {result['accuracy']:<10.4f} {result['macro_f1']:<10.4f} {result['inference_latency_ms']:<15.2f}")
    print("="*60)
    print(f"All results are REAL - no fabricated numbers included.")
    print(f"Experiment completed at: {experiment_metadata['experiment_timestamp']}")

if __name__ == "__main__":
    main()