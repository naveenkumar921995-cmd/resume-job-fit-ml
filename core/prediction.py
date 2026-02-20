import joblib
import numpy as np

model = joblib.load("models/regression_model.pkl")

def predict_fit(skill_match, semantic_similarity, 
                keyword_density, experience_years):

    features = np.array([[skill_match, semantic_similarity,
                          keyword_density, experience_years]])

    prediction = model.predict(features)[0]
    return round(prediction, 2)
