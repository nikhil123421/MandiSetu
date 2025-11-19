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

        /* 5. BUTTONS */
        div.stButton > button {
            background-color: #2E8B57;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px 24px;
            font-weight: 500;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #256f46;
        }

        /* 6. CLEAN UI */
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;}    
        [data-testid="stToolbar"] {visibility: hidden; display: none;}

        /* --------------------------------------------------
           7. THE UNIVERSAL FIX (SMART PADDING)
           -------------------------------------------------- */
        
        /* For Phones (Screens smaller than 768px) */
        @media (max-width: 768px) {
            /* REMOVE the huge white margins Streamlit adds by default */
            .block-container {
                padding-top: 3rem !important;
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
            }
            
            /* Make fonts slightly smaller so they don't wrap */
            h1, h2, h3 {
                font-size: 1.5rem !important;
            }
            
            /* Force Plotly charts to fit within the screen */
            .js-plotly-plot {
                width: 100% !important;
            }
        }

        /* For Desktops (Screens wider than 768px) */
        @media (min-width: 768px) {
            .block-container {
                padding-top: 5rem !important; /* Standard comfortable spacing */
                max-width: 1200px; /* Prevents it from getting too wide on ultra-wide monitors */
            }
        }
        
    </style>
    """, unsafe_allow_html=True)
