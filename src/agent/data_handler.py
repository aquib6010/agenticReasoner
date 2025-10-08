import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def load_train_data():
    """Load training data"""
    train_path = DATA_DIR / "ethosTrain.csv"
    return pd.read_csv(train_path)

def load_test_data():
    """Load test data"""
    test_path = DATA_DIR / "ethosTest.csv"
    return pd.read_csv(test_path)

def prepare_output_template():
    """Prepare output dataframe in required format"""
    out_path = DATA_DIR / "ethosOut.csv"
    return pd.read_csv(out_path)

def save_predictions(df, filename="ethosOut.csv"):
    """Save model predictions in ethosOut.csv format"""
    save_path = DATA_DIR / filename
    df.to_csv(save_path, index=False)
    print(f"✅ Saved predictions to {save_path}")
    