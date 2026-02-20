import joblib
import numpy as np
import os

def load_model():
    model_path = "models/regression_model.pkl"
    
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found. Train the model first.")

    return joblib.load(model_path)


def predict_fit(skill_match, semantic_similarity,
                keyword_density, experience_years):

    model = load_model()

    features = np.array([[skill_match,
                          semantic_similarity,
                          keyword_density,
                          experience_years]])

    prediction = model.predict(features)[0]
    return round(prediction, 2)
