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

        /* 3. HIDE MENUS */
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;}    
        [data-testid="stToolbar"] {visibility: hidden; display: none;}

        /* 4. METRIC CARDS */
        div[data-testid="stMetric"] {
            background-color: #f8f9fa;
            border: 1px solid #e0e0e0;
            padding: 10px;
            border-radius: 8px;
            border-left: 4px solid #2E8B57;
        }

        /* 5. BUTTONS */
        div.stButton > button {
            background-color: #2E8B57;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 1.1rem;
            width: 100%;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #256f46;
            transform: scale(1.02);
        }

        /* 6. MOBILE OPTIMIZATION */
        @media (max-width: 768px) {
            .block-container {
                padding-top: 2rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            h1 { font-size: 2rem !important; }
            
            /* Hide sidebar arrow on mobile to prevent cutting */
            [data-testid="stSidebarCollapsedControl"] {
                display: none;
            }
        }
    </style>
    """, unsafe_allow_html=True)
