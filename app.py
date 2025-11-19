import streamlit as st
import time
import pandas as pd
import plotly.express as px  
from src.api_engine import fetch_mandi_data
from src.styles import apply_custom_css

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Mandi Setu", 
    page_icon="🌾", 
    layout="wide",
    )

# 2. APPLY CUSTOM STYLING
apply_custom_css()

# 3. SIDEBAR UI
with st.sidebar:
    st.title("🌾 Mandi Setu ")
    st.caption("Real-time Mandi Intelligence System")
    st.markdown("---")
    
    # --- FULLY COMPREHENSIVE STATE LIST (Verified from Data) ---
    state_list = sorted([
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", 
        "Chattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", 
        "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
        "Maharashtra", "Manipur", "Meghalaya", "Nagaland", "Odisha", "Pondicherry", 
        "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
        "Uttar Pradesh", "Uttrakhand", "West Bengal"
    ])
    
    # --- FULLY COMPREHENSIVE CROP LIST (All 130+ Items from API) ---
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

    # Defaults: State = Maharashtra (check index exists), Crop = Wheat
    default_state_index = state_list.index("Maharashtra") if "Maharashtra" in state_list else 0
    default_crop_index = crop_list.index("Wheat") if "Wheat" in crop_list else 0

    selected_state = st.selectbox("📍 Select State", state_list, index=default_state_index)
    selected_crop = st.selectbox("🥬 Select Crop", crop_list, index=default_crop_index)
    
    st.markdown("---")
    
    # Search Button
    search_btn = st.button("🔍 Find Best Prices")
    
    st.markdown("---")
    st.info("💡 **System Status:**\nConnected to e-NAM Govt API.")

# 4. MAIN DASHBOARD LOGIC
if search_btn:
    # Loading Animation
    with st.spinner(f"📡 Analyzing market data for {selected_crop} in {selected_state}..."):
        time.sleep(1.0) # UI Experience delay
        try:
            raw_df = fetch_mandi_data(selected_state, selected_crop)
            if not raw_df.empty:
                df = raw_df.sort_values(by="Modal Price", ascending=False).drop_duplicates(subset=["Market", "District"])
            else:
                df = raw_df

        except ValueError:
            st.warning(f"⚠️ No active markets found for **{selected_crop}** in **{selected_state}** today.\n\nThis is common for seasonal crops. Try selecting a different crop or state.")
            st.stop()
        except Exception as e:
            st.error(f"Could not fetch data. Server Error: {e}")
            st.stop()

    # --- TOP KPI SECTION ---
    st.markdown(f"## 📊 Market Analysis: **{selected_crop}**")
    st.markdown(f"Region: **{selected_state}** | Currency: **INR (₹/Quintal)**")
    
    # Calculate Logic
    best_price = df["Modal Price"].max()
    avg_price = round(df["Modal Price"].mean())
    
    # Get the row with the max price safely
    best_market_row = df.loc[df["Modal Price"].idxmax()]
    cheapest_mandi = best_market_row["Market"]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Highest Market Price", f"₹{best_price}", "High Demand")
    col2.metric("📉 Average State Price", f"₹{avg_price}", "Market Rate")
    col3.metric("📍 Recommended Market", cheapest_mandi, "Sell Here")

    st.markdown("---")

    # --- MAIN VISUALIZATION SECTION (Vertical Layout) ---
    
    # 1. THE BIG CHART (Full Width)
    st.subheader("📈 Price Trends by Market")
    
    fig = px.bar(
        df, 
        x="Market", 
        y="Modal Price",
        color="Modal Price",
        color_continuous_scale=px.colors.sequential.Greens,
        template="plotly_white",
        hover_data=["District", "Date"], 
        height=600
    )

    fig.update_layout(
        xaxis_title="Mandi Location",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Price (₹/Quintal)",
        font_family="Roboto",
        showlegend=False,
        margin=dict(l=0, r=0, t=30, b=0) 
    )
    fig.update_coloraxes(showscale=False)
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---") 

    # 2. THE TABLE (Full Width below chart)
    st.subheader("📋 Live Price Board")
    
    st.dataframe(
        df.sort_values(by="Modal Price", ascending=False),
        use_container_width=True,
        hide_index=True,
        column_config={
            "District": st.column_config.TextColumn("District"),
            "Market": st.column_config.TextColumn("Market Name", width="large"), 
            "Modal Price": st.column_config.ProgressColumn( 
                "Price Strength",
                format="₹%d",
                min_value=0,
                max_value=int(best_price * 1.2),
            ),
            "Date": st.column_config.DateColumn("Arrival Date", format="DD MMM YYYY")
        }
    )

    # 7. FINAL ACTIONABLE INSIGHT
    st.success(f"✅ **Recommendation:** Transport your {selected_crop} stock to **{cheapest_mandi}** ({best_market_row['District']}) to gain **₹{best_price - avg_price}** more per quintal than the average.")

else:
    # LANDING PAGE (Initial State)
    st.title("👋 Welcome to Mandi Setu")
    
    # Professional Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Intelligent Mandi Discovery System
        
        **Mandi Setu** uses real-time government data to help farmers find the highest paying markets (Mandis) for their produce.
        
        **How it works:**
        1. **Select Region:** Choose your current State.
        2. **Select Commodity:** Choose from major crops (Wheat, Rice, etc.).
        3. **Analyze:** Our algorithm compares prices across active Mandis.
        
        """)
    
    with col2:
        st.info("🚀 **Version 1.0**\n\nStatus: **Online**\nData Source: **e-NAM / data.gov.in**")