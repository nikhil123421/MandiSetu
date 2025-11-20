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
    initial_sidebar_state="collapsed" # Hidden on landing page
)

# Initialize Session State for "Page Navigation"
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def start_app():
    st.session_state.page = 'dashboard'

# 2. APPLY STYLING
apply_custom_css()

# ---------------------------------------------------------
# PAGE 1: LANDING PAGE
# ---------------------------------------------------------
if st.session_state.page == 'landing':
    
    # Centered Layout
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacing
    st.title("🌾 Mandi Setu")
    st.markdown("### Intelligent Market Discovery for Indian Farmers")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Why use Mandi Setu?**
        * 📊 **Real-Time Prices:** Live data from e-NAM & Agmarknet.
        * 🚀 **Smart Intelligence:** Instantly find the highest paying mandi.
        * 📱 **Easy to Use:** Designed for mobile and desktop.
        """)
    
    with col2:
        st.info("💡 **Status:** Online | Data updated daily.")
        # The "Call to Action" Button
        st.button("🚀 Check Best Prices Now", on_click=start_app, use_container_width=True)


# ---------------------------------------------------------
# PAGE 2: MAIN DASHBOARD
# ---------------------------------------------------------
elif st.session_state.page == 'dashboard':
    
    # Show Sidebar only on Dashboard
    with st.sidebar:
        st.title("🌾 Mandi Setu ")
        st.caption("Real-time Mandi Intelligence")
        st.markdown("---")
        
        # DATA LISTS
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

        def_state = state_list.index("Maharashtra") if "Maharashtra" in state_list else 0
        def_crop = crop_list.index("Wheat") if "Wheat" in crop_list else 0

        selected_state = st.selectbox("📍 Select State", state_list, index=def_state)
        selected_crop = st.selectbox("🥬 Select Crop", crop_list, index=def_crop)
        
        st.markdown("---")
        search_btn = st.button("🔍 Find Best Prices")
        st.markdown("---")
        st.button("🔙 Back to Home", on_click=lambda: st.session_state.update(page='landing'))

    # DASHBOARD LOGIC
    st.title(f"📊 Analysis: {selected_crop} in {selected_state}")
    
    # Trigger search automatically on page load OR button click
    # Since user is already on dashboard, we can show data immediately or wait for button.
    # Let's wait for button to save API calls.
    if search_btn:
        with st.spinner(f"📡 Fetching data..."):
            time.sleep(1.0)
            try:
                raw_df = fetch_mandi_data(selected_state, selected_crop)
                if not raw_df.empty:
                    df = raw_df.sort_values(by="Modal Price", ascending=False).drop_duplicates(subset=["Market", "District"])
                else:
                    df = raw_df
            except ValueError:
                st.warning(f"⚠️ No active markets found.")
                st.stop()
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()

        best_price = df["Modal Price"].max()
        avg_price = round(df["Modal Price"].mean())
        best_market_row = df.loc[df["Modal Price"].idxmax()]
        cheapest_mandi = best_market_row["Market"]
        
        c1, c2, c3 = st.columns(3)
        c1.metric("💰 Max Price", f"₹{best_price}")
        c2.metric("📉 Avg Price", f"₹{avg_price}")
        c3.metric("📍 Best Market", cheapest_mandi)

        st.markdown("---")

        # Charts
        fig = px.bar(
            df, x="Market", y="Modal Price", color="Modal Price",
            color_continuous_scale=px.colors.sequential.Greens,
            template="plotly_white", hover_data=["District", "Date"], 
            height=500
        )
        fig.update_layout(xaxis_title=None, plot_bgcolor="rgba(0,0,0,0)", yaxis_title="Price (₹/Q)", font_family="Roboto", showlegend=False)
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---") 

        # Table
        st.subheader("📋 Live Price Board")
        st.dataframe(
            df.sort_values(by="Modal Price", ascending=False),
            use_container_width=True, hide_index=True,
            column_config={
                "District": st.column_config.TextColumn("District"),
                "Market": st.column_config.TextColumn("Market", width="medium"), 
                "Modal Price": st.column_config.ProgressColumn("Price", format="₹%d", max_value=int(best_price * 1.2)),
                "Date": st.column_config.DateColumn("Date", format="DD MMM")
            }
        )
        st.success(f"✅ **Recommendation:** Sell at **{cheapest_mandi}** for max profit.")
    else:
        st.info("👈 Select your State and Crop from the Sidebar to begin.")
