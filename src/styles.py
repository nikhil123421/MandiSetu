import streamlit as st

def apply_custom_css(page_name='landing'):
    # 1. DEFINE COLORS
    # A slightly deeper mint green for the top (Hero)
    bg_color = "#D1E7DD"  
    # Pure white for the bottom (Features)
    card_color = "#FFFFFF" 

    # 2. DETERMINE CSS BASED ON PAGE
    if page_name == 'landing':
        page_bg = f"""
            background: linear-gradient(180deg, {bg_color} 680px);
            background-repeat: no-repeat;
            background-attachment: scroll; 
        """
        container_style = ""
   
    elif page_name == 'selection':
        # Solid Green Background
        page_bg = f"background-color: {bg_color};"
        
        container_style = f"""
            /* 1. Center the main Streamlit content area (The Block-Container) */
            .main .block-container {{
                /* Set Max Width for Content */
                max-width: 800px; /* Reduced max-width for better centering effect */
                /* Center Horizontally and provide top/bottom margin */
                margin: 10vh auto; /* Increased vertical margin for better visual separation */
            }}
            
            /* 2. Center the custom header title */
            .header-title {{
                font-size: 3rem !important;
                font-weight: 800;
                line-height: 0.8;
                color: #198754;
                text-align: center; /* ALIGN TEXT/TITLE TO CENTER */
            }}
            
            /* 3. Center the button group */
            div[data-testid="stForm"] {{
                /* Targets the form (or container) holding the button */
                display: flex;
                flex-direction: column;
                align-items: center; /* ALIGN BUTTON TO CENTER */
            }}

            /* 4. CHUNKY BUTTONS (Bigger) - Keep the button styling */
            div.stButton > button {{
                padding: 0.8rem 1.2rem !important;
                font-size: 1rem !important;
                border-radius: 50px;
                border-width: 10px;
                box-shadow: 0 5px 10px rgba(0,0,0,0.05);
            }}
           
            /* 5. INPUT LABELS (Bigger) */
            .stSelectbox label p {{
                font-size: 1.15rem !important;
                font-weight: 600;
                color: #4A5568;
            }}
           
            /* 6. INPUT BOX HEIGHT (Optional - makes dropdowns feel chunkier) */
            .stSelectbox div[data-baseweb="select"] > div {{
                min-height: 45px;
                top: auto !important;
            }}
        """
   
    # The 'else' block (for other pages like 'results') will still use the card style.
    # The logic remains the same for the 'else' block as in your original code.
    else:
        # NOTE: I am making the 'else' block also use the non-card style for consistency,
        # but if you intend for 'else' to be a 'results' page *with* a card, you can revert 
        # the 'else' block to your original card-based styling.
        page_bg = f"background-color: {bg_color};"
        container_style = f"""
            /* Center the Streamlit Content Block */
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
            
            /* Remaining styles from your original 'else' block... */
            .stSelectbox label p {{
                font-size: 1.15rem !important;
                font-weight: 600;
                color: #4A5568;
            }}
            .stSelectbox div[data-baseweb="select"] > div {{
                min-height: 45px;
                top: auto !important;
            }}
        """

    # 3. INJECT CSS - (The rest of the code remains the same, as it contains global styles)
    st.markdown(f"""
        <style>
            /* GLOBAL FONTS */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
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
           
            /* 2. Force content to start at the very top */
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
           
            /* BUTTON STYLING */
            div.stButton > button {{
                border-radius: 50px;
                background-color: {card_color};
                color: #198754; /* Matching Darker Green */
                border: 2px solid #198754;
                font-weight: 600;
                padding: 0.5rem 1.2rem;
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

---

## 🎯 Key CSS for Centering

1.  **Centered Content Block:**
    ```css
    .main .block-container {
        max-width: 800px;
        margin: 10vh auto; /* 'auto' centers it horizontally */
    }
    ```
2.  **Centered Title:**
    ```css
    .header-title {
        text-align: center;
    }
    ```
3.  **Centered Buttons:** This targets the underlying container (often a Streamlit Form or a column) that wraps the button and uses Flexbox to center its children:
    ```css
    div[data-testid="stForm"] {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centers items horizontally in a column layout */
    }
    ```

Would you like to adjust the **max-width** (currently `800px`) of the selection page content, or the **vertical margin** (currently `10vh`)?
