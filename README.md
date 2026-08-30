# CarPrice AI 🚗

**Date of Completion:** August 31, 2026

**Languages used:**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)  [![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

**Applications used:**

[![VS Code](https://img.shields.io/badge/VS_Code-Editor-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/) [![Anaconda](https://img.shields.io/badge/Anaconda-Environment-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)

**Author:** Animesh Sanghi | Google Certified Data Analyst  
**Contact:** [animeshsanghi.da@gmail.com](mailto:animeshsanghi.da@gmail.com) | 9406570600  
**LinkedIn:** [animeshsanghi-da](https://www.linkedin.com/in/animeshsanghi-da/) | **GitHub:** [animeshsanghi-da](https://github.com/animeshsanghi-da)

---

CarPrice AI is an end-to-end machine learning web application built using **Python**, **VSCode**, **Anaconda**, **Scikit-Learn**, and **Streamlit**. The app enables users to input car specifications (brand, year, KM driven, fuel type, transmission, previous owners, engine capacity, mileage, max power, and number of seats) and get smooth, real-time market price estimations.

---

## 📌 Features

- **Large-Scale Dataset**: Includes a 120,000-row dataset (`data/cars.csv`) pre-loaded with real-world automotive specifications and pricing attributes.
- **Continuous Sensitivity & Smooth Scaling**: Built using **Ridge Regression on Log-Transformed Prices** ($\log(1+y)$) to guarantee that every single UI adjustment (e.g., adding 1 seat or altering mileage) immediately updates the predicted price without staircasing artifacts.
- **Interactive UI**: Clean, custom-styled interface built using Streamlit and custom CSS (`style.py`).
- **Data & Model Metrics**: Displays real-time dataset rows and column shapes along with an expandable dataset viewer.

---

## 📁 Directory Structure

```
car_price_predictor/
│
├── data/
│   └── cars.csv              # Car dataset (1.2 Lakh rows)
├── app.py                    # Streamlit web application interface
├── predict.py                # ML pipeline & Ridge Regression model trainer
├── style.py                  # Custom CSS styling module for Streamlit UI
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Technology Stack & Libraries

- **Environment**: Anaconda (Python 3.10)
- **IDE**: Visual Studio Code
- **Frontend / UI**: Streamlit, Custom CSS
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn (`ColumnTransformer`, `OneHotEncoder`, `StandardScaler`, `Ridge`)
- **Model Serialization**: Joblib

---

## ⚙️ Installation & Setup

### 1. Create and Activate Conda Environment

Open Anaconda Prompt or VSCode Terminal and run:

```bash
# Create a new isolated environment
conda create -n carprice_ai python=3.10 -y

# Activate the environment
conda activate carprice_ai
```

### 2. Set Up Project Directory & Dependencies

Navigate into your project folder and install the required packages:

```bash
cd car_price_predictor
pip install -r requirements.txt
```

---

## 🚀 Execution Workflow

### Step 1: Train the Machine Learning Model
Ensure `data/cars.csv` is present in the `data/` directory, then train the model pipeline using log-scale target encoding and Ridge regression:

```bash
python predict.py
```

This will generate `model.joblib` in the root folder.

### Step 2: Run the Streamlit Application
Launch the interactive dashboard:

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Architecture

### 1. Target Log-Transformation
The target `selling_price` is transformed using $y_{\text{log}} = \log(1 + y)$ (`np.log1p`). This converts multiplicative percentage effects (e.g., brand premiums, annual depreciation, extra owners penalty) into an additive linear space. Predictions are transformed back using $y = \exp(y_{\text{log}}) - 1$ (`np.expm1`).

### 2. Preprocessing (`ColumnTransformer`)
- **Categorical Columns** (`brand`, `fuel`, `transmission`): Encoded using `OneHotEncoder(drop="first", handle_unknown="ignore")` to prevent multicollinearity (dummy variable trap).
- **Numerical Columns** (`year`, `km_driven`, `owner`, `engine`, `mileage`, `max_power`, `seats`): Standardized using `StandardScaler()` so feature scale disparities (e.g., KM vs Seats) do not skew optimization weights.

### 3. Ridge Regression Model
Unlike tree-based models (`RandomForest` or `GradientBoosting`) that group numbers into discrete leaf bins/staircases, **Ridge Regression** fits a continuous mathematical hyperplane, ensuring every UI slider tick smoothly impacts the predicted price.

### 4. Model Training: What, Why & How
- **What:** We trained a **Ridge Regression** model on log-transformed car prices (`np.log1p`). 
- **Why:** Decision trees group numbers into discrete "bins," which causes price updates to freeze when you make minor UI changes (like adding 1 seat or 1,000 km). Ridge Regression fits a smooth, continuous mathematical surface, ensuring every single slider adjustment instantly reflects a realistic price shift while avoiding model overfitting.
- **How:** A 120,000-row dataset is passed through a Scikit-Learn `Pipeline`. Categorical features (brand, fuel, transmission) are converted into binary columns via `OneHotEncoder`, numeric inputs (mileage, engine, seats) are standardized using `StandardScaler`, and the Ridge model learns the underlying log-scale price weights. At prediction time, outputs are converted back to standard rupee values using `np.expm1`.

---

## 📝 License

This project is licensed under the MIT License.