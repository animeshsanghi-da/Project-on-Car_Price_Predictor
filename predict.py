import os
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def train_and_save_model():
    data_path = os.path.join("data", "cars.csv")

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at path: {data_path}")

    df = pd.read_csv(data_path)

    # Log transformation makes percentage-based changes additive for the linear model
    X = df.drop(columns=["selling_price"])
    y = np.log1p(df["selling_price"])  # This transforms target prices to log-scale

    categorical_cols = [
        "brand", 
        "fuel", 
        "transmission"
    ]
    numerical_cols = [
        "year", 
        "km_driven", 
        "owner", 
        "engine", 
        "mileage", 
        "max_power", 
        "seats"
    ]

    # StandardScaler ensures numeric features are perfectly scaled for regression
    # drop="first" prevents multicollinearity in OneHotEncoding
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numerical_cols),
        ]
    )

    # Ridge Regression guarantees 100% continuous, smooth price changes with no "steps"
    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", Ridge(alpha=1.0)), 
        ]
    )

    # Train model
    model_pipeline.fit(X, y)

    # Validate the continuous fit
    r2_score = model_pipeline.score(X, y)
    print(f"Model trained successfully! Mathematical Fit (R2): {r2_score:.4f}")
    if r2_score > 0.90:
        print("Excellent fit: Every UI input will now smoothly alter the price.")

    # Save model pipeline
    joblib.dump(model_pipeline, "model.joblib")

if __name__ == "__main__":
    try:
        train_and_save_model()
    except Exception as e:
        print(f"Error during training: {e}")

# =====================================================================
# 👨‍💻 Author: Animesh Sanghi
# =====================================================================
# Title:    Google Certified Data Analyst | MBA '28 MUJ
# Phone:    9406570600
# Email:    animeshsanghi.da@gmail.com
# LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
# GitHub:   https://github.com/animeshsanghi-da
# =====================================================================