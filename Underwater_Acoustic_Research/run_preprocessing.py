import sys
sys.path.insert(0, 'code')
from preprocess_audio import run_preprocessing_pipeline

result = run_preprocessing_pipeline(
    dataset_root=r'datasets/DeepShip/DeepShip-main',
    output_dir=r'experiments/deepship_split',
    feature_type='combined'
)
print(f'\nResult: {result}')