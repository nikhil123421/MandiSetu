import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        /* 1. GOOGLE FONT */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        /* 2. MAIN BACKGROUND */
        .stApp {
            background-color: #ffffff;
        }

        /* 3. SIDEBAR STYLE */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa;
            border-right: 1px solid #e0e0e0;
        }

        /* 4. METRIC CARDS */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 5px solid #2E8B57;
        }

        /* 5. CUSTOM BUTTONS */
        div.stButton > button {
            background-color: #2E8B57;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px 24px;
            font-weight: 500;
        }
        div.stButton > button:hover {
            background-color: #256f46;
        }

        /* 6. CLEAN UP UI */
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;}    

        /* Enforce minimum width (User can drag larger, but not smaller than 300px) */
        section[data-testid="stSidebar"] {
            min-width: 300px !important;
        }
        
    </style>
    """, unsafe_allow_html=True)