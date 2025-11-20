import streamlit as st

def apply_custom_css(page_name='landing'):
    # 1. DEFINE COLORS
    bg_color = "#D1E7DD"  
    card_color = "#FFFFFF"  

    # 2. DETERMINE CSS BASED ON PAGE
    if page_name == 'landing':
        page_bg = f"""
            /* BACKGROUND: Solid Green Top Half, White Bottom Half */
            background: linear-gradient(180deg, {bg_color} 680px, {card_color} 680px);
            background-repeat: no-repeat;
            background-attachment: scroll;  
        """
        container_style = f"""
            /* Center the main Streamlit content area (The Block-Container) */
            .main .block-container {{
                max-width: 1000px; /* Wider for the landing page hero section */
                margin: 0vh auto; /* Remove top/bottom margin */
            }}
            /* Header Title for Landing Page */
            .header-title {{
                font-size: 3.8rem !important; /* Slightly larger heading */
                font-weight: 900;
                line-height: 1;
                color: #1A202C; /* Darker text for contrast on light green */
                text-align: left; /* Left align for hero section */
            }}
            /* Subtitle on Landing Page */
            .main h3 {{
                font-size: 1.8rem;
                font-weight: 500;
                color: #4A5568;
                margin-top: 0.5rem;
            }}
            /* Caption/Description Text on Landing Page */
            .main div[style*='font-size: 1.2rem'] {{
                margin-top: 1.5rem;
                margin-bottom: 30px !important;
            }}
            /* Centered Feature Blocks (h4) */
            .main .stColumn h4 {{
                text-align: center;
                color: #198754;
            }}
        """
    
    elif page_name == 'selection':
        # Solid Green Background
        bg_color = "#D1E7DD"
        card_color = "#FFFFFF"
        page_bg = f"background-color: {bg_color};"
        
        container_style = f"""
            /* 1. Center the main Streamlit content area (The Block-Container) */
            .main .block-container {{
                /* OPTIMIZED Max Width to 700px for a more focused form */
                max-width: 700px;  
                /* Center Horizontally and provide top/bottom margin */
                margin: 8vh auto;  
            }}
            
            /* 2. Center the custom header title */
            .header-title {{
                /* INCREASED font size from 3rem to 3.5rem */
                font-size: 3.5rem !important;
                font-weight: 800;
                line-height: 0.8;
                color: #198754;
                text-align: center;  
            }}
            
            /* 3. Center the button group (Apply Form container) */
            div[data-testid="stForm"] {{
                display: flex;
                flex-direction: column;
                align-items: center;  
            }}

            /* 4. CHUNKY BUTTONS (Bigger) - Specific to Selection Page Button */
            /* This overrides the global button style for the main CTA */
            div[data-testid="stForm"] div.stButton > button {{
                padding: 1rem 1.8rem !important;  
                font-size: 1.15rem !important;  
                border-radius: 50px;
                border-width: 10px;
                box-shadow: 0 5px 10px rgba(0,0,0,0.05);
            }}

            /* 5. INPUT LABELS (Bigger) */
            .stSelectbox label p {{
                font-size: 1.4rem !important;  
                font-weight: 600;
                color: #4A5568;
            }}
            
            /* 6. INPUT BOX HEIGHT (Optional - makes dropdowns feel chunkier) */
            .stSelectbox div[data-baseweb="select"] > div {{
                min-height: 55px;  
                top: auto !important;
            }}
            
            /* 7. TEXT INSIDE DROPDOWN (Current Value/Placeholder) */
            .stSelectbox div[data-baseweb="select"] > div div:first-child span,
            .stSelectbox div[data-baseweb="select"] > div div:first-child {{
                font-size: 1.25rem !important;  
                font-weight: 500;
                color: #1A202C;
            }}
            /* Remove margins from images added for context, as they were removed from app.py */
            .main .stImage {{
                margin-top: 2rem;
            }}
        """
    
    # ------------------------------------------------------------------
    # Using the non-card style for the 'else' (e.g., 'results') page
    # ------------------------------------------------------------------
    else:
        page_bg = f"background-color: {bg_color};"
        container_style = f"""
            /* Center the Streamlit Content Block (Using original 'else' settings) */
            .main .block-container {{
                max-width: 1000px;
                margin: 5vh auto;  
            }}
            
            /* TITLE STYLING */
            .header-title {{
                font-size: 3rem !important;
                font-weight: 800;
                line-height: 0.8;
                color: #198754;  
                text-align: center;
            }}
            
            /* Center button for results page as well */
            div[data-testid="stForm"] {{
                display: flex;
                flex-direction: column;
                align-items: center;  
            }}
            
            /* Remaining styles from your original 'else' block */
            .stSelectbox label p {{
                font-size: 1.15rem !important;
                font-weight: 600;
                color: #4A5568;
            }}
            .stSelectbox div[data-baseweb="select"] > div {{
                min-height: 45px;
                top: auto !important;
            }}
            /* Ensure the progress bar max value does not overflow the chart */
            div[data-testid="stProgressbar"] > div > div {{
                height: 100% !important;
            }}
        """

    # 3. INJECT CSS
    st.markdown(f"""
        <style>
            /* GLOBAL FONTS */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
            html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; color: #1A202C; }}
            
            /* DYNAMIC BACKGROUND */
            .stApp {{
                {page_bg}
            }}
            
            /* DYNAMIC CONTAINER (Card Style) */
            {container_style}

            /* --- FIX FOR TOP GAP (CRITICAL) --- */
            
            /* 1. Remove the invisible Streamlit Header */
            header[data-testid="stHeader"] {{
                display: none !important;
            }}
            
            /* 2. Force content to start near the top */
            .block-container {{
                padding-top: 1rem !important;  
                padding-bottom: 3rem;
            }}
            
            /* 3. Remove extra margin from the first element */
            .main .block-container div[data-testid="stMarkdownContainer"] > *:first-child {{
                margin-top: 0 !important;
            }}

            /* HIDE DEFAULT FOOTER */
            footer {{visibility: hidden;}}
            
            /* FIX DROPDOWN DIRECTION - Force dropdowns to open downward */
            div[data-baseweb="select"] div[data-baseweb="popover"] {{
                transform: translate3d(0px, 40px, 0px) !important;
                top: auto !important;
                bottom: auto !important;
            }}
            
            /* Ensure dropdown menu has proper z-index and positioning */
            div[data-baseweb="popover"] {{
                z-index: 9999 !important;
                position: absolute !important;
            }}
            
            /* GLOBAL BUTTON STYLING (Override for Selection Page CTA is done above) */
            div.stButton > button {{
                border-radius: 50px;
                background-color: {card_color};
                color: #198754; /* Matching Darker Green */
                border: 2px solid #198754;
                font-weight: 600;
                padding: 0.5rem 1.2rem; /* Standard Padding */
                transition: all 0.3s ease;
            }}
            div.stButton > button:hover {{
                background-color: #198754;
                color: {card_color};
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(25, 135, 84, 0.2);
            }}

            /* CUSTOM HEADER TITLE CLASS (Global) */
            .header-title {{
                text-align: center;
                color: #198754;
                margin-bottom: 0;
                font-weight: 1000;
            }}

            /* INPUT FORM STYLING */
            .stSelectbox > div > div {{  
                border-radius: 10px;  
                border-color: #CED4DA;  
                background-color: #F8F9FA;
            }}
            
            /* METRICS & TABLES */
            div[data-testid="stMetric"] {{
                background-color: #F1F8F5;
                border: 1px solid #D1E7DD;
                border-radius: 12px;
                padding: 15px;
                text-align: center;
            }}


            /* ANIMATION */
            .element-container {{ animation: fadeIn 0.5s ease-out; }}
            @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        </style>
    """, unsafe_allow_html=True)
