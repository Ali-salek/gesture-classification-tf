import os
import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def test_modules_installed():
    try:
        import pandas
        import sklearn
    except ImportError as e:
        pytest.fail(f"Required module not installed: {e}")

def test_data_exists():
    dataset_path = 'data/cleaned_dataset.csv'
    assert os.path.exists(dataset_path), f"Dataset file not found at {dataset_path}"

def test_data_loading():
    dataset_path = 'data/cleaned_dataset.csv'
    try:
        df = pd.read_csv(dataset_path)
        assert not df.empty, "Dataset is empty"
    except Exception as e:
        pytest.fail(f"Failed to load dataset: {e}")