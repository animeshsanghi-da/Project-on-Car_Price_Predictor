import streamlit as st


def apply_custom_styles():
    custom_css = """
    <style>
        /* Main Layout Styles */
        .main {
            padding: 1.5rem;
        }
        
        /* Heading Styles */
        h1 {
            color: #1E3A8A;
            font-weight: 800;
        }
        
        /* Custom Button Styles */
        div.stButton > button {
            width: 100%;
            background-color: #2563EB;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            border: none;
            transition: background-color 0.3s ease;
        }
        
        div.stButton > button:hover {
            background-color: #1D4ED8;
            color: white;
        }
        
        /* Metric Box Styling */
        div[data-testid="stMetricValue"] {
            font-size: 30px;
            font-weight: bold;
            color: #0D9488;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# =====================================================================
# 👨‍💻 Author: Animesh Sanghi
# =====================================================================
# Title:    Google Certified Data Analyst | MBA '28 MUJ
# Phone:    9406570600
# Email:    animeshsanghi.da@gmail.com
# LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
# GitHub:   https://github.com/animeshsanghi-da
# =====================================================================