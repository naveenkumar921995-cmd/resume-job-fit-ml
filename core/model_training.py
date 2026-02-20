import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_model():
    df = pd.read_csv("data/training_data.csv")

    X = df[["skill_match", "semantic_similarity", 
            "keyword_density", "experience_years"]]
    y = df["fit_score"]

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)

    joblib.dump(model, "models/regression_model.pkl")

    return mse, r2
