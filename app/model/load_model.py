import joblib
import os

model_path = os.path.join("models", "best_xgb_model.pkl")

def load_model():
    return joblib.load(model_path)
