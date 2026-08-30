import numpy as np
import datetime
import os
import joblib
import pandas as pd
import streamlit as st
from style import apply_custom_styles

st.set_page_config(
    page_title="CarPrice AI", 
    page_icon="🚗", 
    layout="wide"
)

# Apply custom CSS styling
apply_custom_styles()

st.title("🚗 CarPrice AI")
st.write("Enter car specifications to estimate market price.")

# Dataset Loading
dataset_path = os.path.join("data", "cars.csv")
try:
    df = pd.read_csv(dataset_path)

    st.subheader("📊 Dataset Information")
    col_row, col_col = st.columns(2)
    with col_row:
        st.metric("Total Rows", df.shape[0])
    with col_col:
        st.metric("Total Columns", df.shape[1])

    with st.expander("Preview Dataset"):
        st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Error loading dataset from {dataset_path}: {e}")
    st.stop()

# Model Loading
model_path = "model.joblib"
try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(
        f"Failed to load trained model ('{model_path}'). "
        "Please run 'python predict.py' first to generate the model file."
    )
    st.stop()

st.divider()
st.subheader("🔧 Input Specifications")

# Extract unique dropdown values from CSV
brand_options = sorted(df["brand"].dropna().unique().tolist())
fuel_options = sorted(df["fuel"].dropna().unique().tolist())
transmission_options = sorted(df["transmission"].dropna().unique().tolist())

current_year = datetime.datetime.now().year

# Form Input Section
with st.form(key="car_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        brand = st.selectbox("Car Brand", options=brand_options)
        year = st.number_input(
            "Manufacturing Year",
            min_value=1990,
            max_value=current_year,
            step=1,
            value=2020,
        )
        km_driven = st.number_input(
            "KM Driven", 
            min_value=0, 
            max_value=1000000, 
            step=10000, 
            value=50000
        )
        fuel = st.selectbox(
            "Fuel Type", 
            options=fuel_options
        )
        transmission = st.selectbox("Transmission", options=transmission_options)

    with col2:
        owner = st.number_input(
            "Number of Previous Owners", min_value=0, max_value=10, step=1, value=1
        )
        engine = st.number_input(
            "Engine Capacity (cc)",
            min_value=0.0,
            max_value=10000.0,
            step=100.0,
            value=1200.0,
        )
        mileage = st.number_input(
            "Mileage (kmpl)",
            min_value=0.0,
            max_value=100.0,
            step=0.5,
            value=18.0,
        )
        max_power = st.number_input(
            "Maximum Power (BHP)",
            min_value=0.0,
            max_value=1000.0,
            step=1.0,
            value=80.0,
        )
        seats = st.number_input(
            "Number of Seats", 
            min_value=2, 
            max_value=12, 
            step=1, 
            value=5
        )

    submit_btn = st.form_submit_button(label="Predict Price")

# Prediction handling
if submit_btn:
    try:
        input_data = pd.DataFrame(
            [
                {
                    "brand": brand,
                    "year": year,
                    "km_driven": km_driven,
                    "fuel": fuel,
                    "transmission": transmission,
                    "owner": owner,
                    "engine": engine,
                    "mileage": mileage,
                    "max_power": max_power,
                    "seats": seats,
                }
            ]
        )

        # Predict log price and convert back using expm1
        predicted_log_price = model.predict(input_data)[0]
        predicted_price = np.expm1(predicted_log_price)
        final_price = max(0, predicted_price)

        st.success(f"💰 Estimated Car Price: ₹{final_price:,.2f}")
    except Exception as e:
        st.error(f"An error occurred during price prediction: {e}")

# =====================================================================
# 👨‍💻 Author: Animesh Sanghi
# =====================================================================
# Title:    Google Certified Data Analyst | MBA '28 MUJ
# Phone:    9406570600
# Email:    animeshsanghi.da@gmail.com
# LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
# GitHub:   https://github.com/animeshsanghi-da
# =====================================================================