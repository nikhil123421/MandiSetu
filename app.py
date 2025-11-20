import streamlit as st
import time
import pandas as pd
import plotly.express as px  
from src.api_engine import fetch_mandi_data
from src.styles import apply_custom_css

# 1. CONFIGURATION
st.set_page_config(
    page_title="Mandi Setu", 
    page_icon="🌾", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. SESSION STATE (Initialize this FIRST)
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'data' not in st.session_state:
    st.session_state.data = None
if 'selected_state' not in st.session_state:
    st.session_state.selected_state = "Maharashtra"
if 'selected_crop' not in st.session_state:
    st.session_state.selected_crop = "Wheat"

# 3. APPLY STYLING (Now we know which page is active)
apply_custom_css(st.session_state.page)

# NAVIGATION
def go_to_selection():
    st.session_state.page = 'selection'

def go_to_results():
    st.session_state.page = 'results'
    st.session_state.data = None 

def go_home():
    st.session_state.page = 'landing'
    st.session_state.data = None

# =========================================================
# PAGE 1: LANDING PAGE
# =========================================================
if st.session_state.page == 'landing':
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # HERO SECTION
    col1, col2 = st.columns([1.4, 1], gap="large")
    
    with col1:
        st.markdown("# 🌱 Empowering Indian Farmers")
        st.markdown("### Find the Best Price for Your Hard Work.")
        st.markdown("""
        <div style='font-size: 1.2rem; color: #444; margin-bottom: 20px;'>
        Don't sell blindly. <b>Mandi Setu</b> connects you to real-time government data from e-NAM to help you find the highest paying markets in your state.
        </div>
        """, unsafe_allow_html=True)
        st.button("🚀 Start Your Search", on_click=go_to_selection, use_container_width=True)

    with col2:
        st.image("https://images.unsplash.com/photo-1625246333195-78d9c38ad449?q=80&w=1000&auto=format&fit=crop", use_container_width=True,)

    st.write("---")

    # FEATURES (White Background)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 📡 Real-Time Data")
        st.caption("Verified auction prices directly from Agmarknet.")
    with c2:
        st.markdown("#### 📊 Smart Analytics")
        st.caption("Our algorithm finds the top paying Mandi instantly.")
    with c3:
        st.markdown("#### 📱 Mobile First")
        st.caption("Works perfectly on your phone, even with 4G.")
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **System Status:** Online | Data Source: **Ministry of Agriculture (OGD)**")


# =========================================================
# PAGE 2: SELECTION PAGE
# =========================================================
elif st.session_state.page == 'selection':
    
    # --- MODIFIED LAYOUT: HEADER ---
    # Using columns here to make the 'Home' button and Title align horizontally
    h_col1, h_col2, h_col3 = st.columns([1, 4, 1])
    with h_col1:
        st.button("← Home", on_click=go_home)
    with h_col2:
        st.markdown("<h2 class='header-title'>📍 Select Your Region & Crop</h2>", unsafe_allow_html=True)
    # -------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    state_list = sorted([
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", 
        "Chattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", 
        "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
        "Maharashtra", "Manipur", "Meghalaya", "Nagaland", "Odisha", "Pondicherry", 
        "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
        "Uttar Pradesh", "Uttrakhand", "West Bengal"
    ])
    
    crop_list = sorted([
        "Amaranthus", "Amla(Nelli Kai)", "Amphophalus", "Amranthas Red", "Apple", 
        "Arecanut(Betelnut/Supari)", "Arhar (Tur/Red Gram)(Whole)", "Arhar Dal(Tur Dal)", 
        "Ashgourd", "Bajra(Pearl Millet/Cumbu)", "Banana", "Banana - Green", "Beans", 
        "Beetroot", "Bengal Gram(Gram)(Whole)", "Betal Leaves", "Bhindi(Ladies Finger)", 
        "Bitter gourd", "Black Gram (Urd Beans)(Whole)", "Black pepper", "Bottle gourd", 
        "Brinjal", "Cabbage", "Capsicum", "Carrot", "Cashewnuts", "Castor Seed", 
        "Cauliflower", "Chikoos(Sapota)", "Chili Red", "Chilly Capsicum", "Chow Chow", 
        "Cluster beans", "Coconut", "Coconut Oil", "Coconut Seed", "Coffee", "Colacasia", 
        "Copra", "Coriander(Leaves)", "Cotton", "Cowpea(Veg)", "Cucumbar(Kheera)", 
        "Custard Apple (Sharifa)", "Dhaincha", "Drumstick", "Dry Chillies", "Duster Beans", 
        "Elephant Yam (Suran)", "Field Pea", "Fig(Anjura/Anjeer)", "Firewood", "Fish", 
        "French Beans (Frasbean)", "Garlic", "Ginger(Dry)", "Ginger(Green)", "Gram Raw(Chholia)", 
        "Grapes", "Green Avare (W)", "Green Chilli", "Green Gram (Moong)(Whole)", 
        "Green Gram Dal (Moong Dal)", "Green Peas", "Ground Nut Seed", "Groundnut", 
        "Groundnut pods (raw)", "Guar", "Guava", "Gur(Jaggery)", "Indian Beans (Seam)", 
        "Jasmine", "Jowar(Sorghum)", "Jute", "Kabuli Chana(Chickpeas-White)", "Kakada", 
        "Karbuja(Musk Melon)", "Kinnow", "Knool Khol", "Kodo Millet(Varagu)", "Kulthi(Horse Gram)", 
        "Leafy Vegetable", "Lemon", "Lime", "Little gourd (Kundru)", "Long Melon(Kakri)", 
        "Mahua", "Maize", "Mango", "Mango (Raw-Ripe)", "Marigold(Calcutta)", "Mashrooms", 
        "Masur Dal", "Methi(Leaves)", "Mint(Pudina)", "Moath Dal", "Mousambi(Sweet Lime)", 
        "Mustard", "Mustard Oil", "Onion", "Onion Green", "Orange", "Paddy(Dhan)(Basmati)", 
        "Paddy(Dhan)(Common)", "Papaya", "Papaya (Raw)", "Pear(Marasebu)", "Peas Wet", 
        "Peas cod", "Peas(Dry)", "Pegeon Pea (Arhar Fali)", "Pepper garbled", "Pepper ungarbled", 
        "Persimon(Japani Fal)", "Pineapple", "Pointed gourd (Parval)", "Pomegranate", "Potato", 
        "Pumpkin", "Raddish", "Rat Tail Radish (Mogari)", "Rice", "Ridgeguard(Tori)", 
        "Rose(Local)", "Round gourd", "Rubber", "Seemebadnekai", "Seetapal", 
        "Sesamum(Sesame,Gingelly,Til)", "Snakeguard", "Soyabean", "Spinach", "Sponge gourd", 
        "Squash(Chappal Kadoo)", "Surat Beans (Papadi)", "Sweet Potato", "Sweet Pumpkin", 
        "Tamarind Fruit", "Tapioca", "Tender Coconut", "Thogrikai", "Thondekai", "Tinda", 
        "Tomato", "Tube Flower", "Tube Rose(Loose)", "Turmeric", "Turmeric (raw)", "Turnip", 
        "Water Melon", "Wheat", "Wood", "Yam (Ratalu)"
    ])

    try:
        idx_state = state_list.index(st.session_state.selected_state)
        idx_crop = crop_list.index(st.session_state.selected_crop)
    except:
        idx_state, idx_crop = 0, 0

    c1, c2 = st.columns(2)
    with c1:
        sel_state = st.selectbox("📍 Select State", state_list, index=idx_state)
    with c2:
        sel_crop = st.selectbox("🥬 Select Commodity", crop_list, index=idx_crop)

    st.session_state.selected_state = sel_state
    st.session_state.selected_crop = sel_crop

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔍 Analyze Market Trends", on_click=go_to_results, use_container_width=True)

    # -------------------------------------------------------------------
    ## 🏞️ Visual Context for Farmers
    # -------------------------------------------------------------------
    # Add vertical spacing
    
    # Use columns to place the two images side-by-side (in a row) and centered.
    # We use empty columns on the sides ([1, 4, 4, 1]) to push the image columns (4, 4) to the center.
    img_col1, img_col2 = st.columns(2)
    
    # The image URLs are placeholders for appropriate Indian farmer imagery
    image_url_1 = "https://cdn.pixabay.com/photo/2023/03/31/14/52/rice-field-7890204_1280.jpg" # Farmer working in a green field
    image_url_2 = "https://cdn.pixabay.com/photo/2020/06/29/11/58/sheep-5352474_1280.jpg" # Farmer with a bullock or in a village setting

    with img_col1:
        st.image(image_url_1, use_container_width=True)
        # Triggering an image for context: 

    with img_col2:
        st.image(image_url_2, use_container_width=True)
        # Triggering another image for context:

# =========================================================
# PAGE 3: RESULTS DASHBOARD
# =========================================================
elif st.session_state.page == 'results':
    
    # --- MODIFIED LAYOUT: HEADER ---
    h_col1, h_col2, h_col3 = st.columns([1, 4, 1])
    with h_col1:
        st.button("← Back to Search", on_click=go_to_selection)
    # -------------------------------
    
    if st.session_state.data is None:
        with st.spinner(f"📡 Connecting to e-NAM servers..."):
            time.sleep(1.5)
            try:
                raw_df = fetch_mandi_data(st.session_state.selected_state, st.session_state.selected_crop)
                if not raw_df.empty:
                    clean_df = raw_df.sort_values(by="Modal Price", ascending=False).drop_duplicates(subset=["Market", "District"])
                    st.session_state.data = clean_df
                else:
                    st.warning("API returned success but data was empty.")
                    st.stop()
            except ValueError:
                st.warning(f"⚠️ **No active markets found.**\n\nIt seems **{st.session_state.selected_crop}** isn't being traded in **{st.session_state.selected_state}** today.")
                st.stop()
            except Exception as e:
                st.error(f"Server Error: {e}")
                st.stop()
    
    df = st.session_state.data
    
    st.markdown(f"## 📊 Analysis: **{st.session_state.selected_crop}**")
    st.caption(f"Region: {st.session_state.selected_state} | Currency: INR (₹/Quintal)")
    
    best_price = df["Modal Price"].max()
    avg_price = round(df["Modal Price"].mean())
    best_market_row = df.loc[df["Modal Price"].idxmax()]
    # FIX: Renamed 'cheapest_mandi' to 'best_mandi' for accuracy
    best_mandi = best_market_row["Market"]
    
    c1, c2, c3 = st.columns(3)
    c1.metric("💰 Max Price", f"₹{best_price}")
    c2.metric("📉 Avg Price", f"₹{avg_price}")
    # FIX: Used the correctly named variable 'best_mandi'
    c3.metric("📍 Best Market", best_mandi)

    st.write("---")

    fig = px.bar(
        df, x="Market", y="Modal Price", color="Modal Price",
        color_continuous_scale=px.colors.sequential.Greens,
        template="plotly_white", hover_data=["District", "Date"], 
        height=500
    )
    fig.update_layout(xaxis_title=None, plot_bgcolor="rgba(0,0,0,0)", yaxis_title="Price (₹/Q)", font_family="Inter", showlegend=False)
    fig.update_coloraxes(showscale=False)
    st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.subheader("📋 Live Price Board")
    st.dataframe(
        df.sort_values(by="Modal Price", ascending=False),
        use_container_width=True, hide_index=True,
        column_config={
            "District": st.column_config.TextColumn("District"),
            "Market": st.column_config.TextColumn("Market", width="medium"), 
            "Modal Price": st.column_config.ProgressColumn("Price", format="₹%d", max_value=int(best_price * 1.2)),
            "Date": st.column_config.DateColumn("Date", format="MM/DD/YYYY")
        }
    )
    
    # FIX: Used the correctly named variable 'best_mandi'
    st.success(f"✅ **Recommendation:** Sell at **{best_mandi}** ({best_market_row['District']}) for maximum profit.")
