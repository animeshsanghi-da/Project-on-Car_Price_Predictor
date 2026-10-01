# CarPrice AI

CarPrice AI is a **Python-based end-to-end machine learning web application** that provides real-time market price valuations for used cars based on user-input vehicle specifications.

The project utilizes Scikit-Learn to train a continuous Ridge Regression pipeline on log-transformed car prices ( $\log(1+y)$ ), delivering continuous sensitivity and smooth price scaling without staircasing artifacts through an interactive Streamlit interface.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)  [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)  [![Joblib](https://img.shields.io/badge/Joblib-4BA2C5?style=for-the-badge&logo=python&logoColor=white)](https://joblib.readthedocs.io/)  [![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)  [![Visual Studio Code](https://img.shields.io/badge/VS_Code-0078D4?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

## Project Features

- Integration of a 120,000-row automotive dataset (`data/cars.csv`) pre-loaded with real-world pricing attributes
- Continuous sensitivity & smooth scaling via Ridge Regression to eliminate discrete binning freeze
- Log-scale target transformation using $y_{\text{log}} = \log(1+y)$ (`np.log1p`) for additive percentage modeling
- Automated feature preprocessing pipeline using `ColumnTransformer`, `OneHotEncoder`, and `StandardScaler`
- Custom interactive UI built with Streamlit and styled via dedicated CSS (`style.py`)
- Real-time prediction engine converting log outputs back to standard currency values via `np.expm1`
- Live dataset metrics display showcasing row/column shapes and an expandable viewer
- Model serialization using Joblib for quick deployment and execution

## Automotive & Model Features

The machine learning pipeline processes the following vehicle specifications:

1. **Categorical Attributes:** Brand (Manufacturer), Fuel Type (Petrol, Diesel, CNG, LPG, Electric), and Transmission (Manual, Automatic)
2. **Numerical Attributes:** Manufacturing Year, Kilometers Driven, Previous Owners, Engine Capacity (CC), Mileage (kmpl), Max Power (bhp), and Number of Seats

## Technologies Used

- Python
- Scikit-Learn
- Streamlit
- Pandas
- NumPy
- Joblib
- Anaconda
- Visual Studio Code

## Project Structure

```text
car_price_predictor/
├── data/
│   └── cars.csv
├── app.py
├── predict.py
├── style.py
├── requirements.txt
└── README.md
```

## File Information

| File / Folder | Purpose |
| --- | --- |
| `app.py` | Streamlit web application interface for real-time car price estimation |
| `predict.py` | Machine learning pipeline builder and Ridge Regression model trainer |
| `style.py` | Custom CSS styling module for enhancing the Streamlit UI layout |
| `requirements.txt` | Defines necessary Python library dependencies for the environment |
| `data/cars.csv` | Automotive dataset containing 120,000 rows of vehicle specs and market prices |
| `README.md` | Comprehensive project documentation and usage guide |

## Installation

### 1. Open the Project Folder

```text
cd car_price_predictor
```

### 2. Create a Virtual Environment

```text
conda create -n carprice_ai python=3.10 -y
```

### 3. Activate the Virtual Environment

```text
conda activate carprice_ai
```

### 4. Install the Required Libraries

```text
pip install -r requirements.txt
```

## How to Run

### 1. Train the Machine Learning Model

Ensure `data/cars.csv` is located in the `data/` directory, then run the model training pipeline:

```text
python predict.py
```

This command creates:

```text
model.joblib
```

### 2. Launch the Web Application

Execute the Streamlit application to start the interactive dashboard:

```text
streamlit run app.py
```

## System Workflow

```text
Raw Car Dataset (1.2 Lakh Rows)
           ↓
Target Log Transformation (np.log1p)
           ↓
ColumnTransformer Preprocessing
(OneHotEncoder & StandardScaler)
           ↓
Ridge Regression Model Training
           ↓
Model Serialization (model.joblib)
           ↓
Streamlit Web UI Input Capture
           ↓
Inverse Transformation (np.expm1)
           ↓
Real-Time Market Price Output
```

## Machine Learning Architecture

The application uses a continuous mathematical modeling pipeline tailored for smooth valuation updates:

| Architecture Component | Implementation Scope |
| --- | --- |
| **Target Log-Transformation** | Converts multiplicative price factors into additive linear space ($y_{\text{log}} = \log(1+y)$) |
| **Categorical Preprocessing** | `OneHotEncoder(drop="first", handle_unknown="ignore")` for brand, fuel, and transmission |
| **Numerical Standardization** | `StandardScaler()` normalizes features with diverse scales (e.g., KM vs Seats) |
| **Ridge Regression Model** | Fits a continuous mathematical hyperplane to prevent discrete leaf binning/staircasing artifacts |
| **Inverse Output Mapping** | Reverts log-scale predictions back to standard rupee values using $y = \exp(y_{\text{log}}) - 1$ |

## Important Note

The continuous responsiveness of the UI rely on Ridge Regression. Tree-based algorithms (like Random Forest or Gradient Boosting) group continuous numbers into discrete leaf bins, which can cause price predictions to freeze during subtle slider adjustments (such as changing seats or adding 1,000 km).

This project is created for machine learning deployment and educational purposes.

## Useful Links

- [Python](https://www.python.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

## Created By

**Name:** Animesh Sanghi  
**Profession:** Google Certified Data Analyst  
**LinkedIn:** [linkedin.com/animeshsanghi-da](https://www.linkedin.com/in/animeshsanghi-da/)
**GitHub:** [github.com/animeshsanghi-da](https://github.com/animeshsanghi-da)  
**Email:** animeshsanghi.da@gmail.com

## Project Status

```text
Machine Learning & Web Analytics Project
```

## License

This project is licensed under the MIT License.
