# 🌾 Kisan Mitra (AgroHelper)

> **Intelligent Mandi Discovery System for Indian Farmers** > *A Real-time Data Analysis Tool powered by e-NAM & Open Government Data (OGD)*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![API](https://img.shields.io/badge/API-eNAM%20Govt%20Data-green)

---

## 📖 Overview
**Kisan Mitra** is a B.Tech CSE project designed to bridge the information gap between farmers and markets. It utilizes the **e-NAM (Electronic National Agriculture Market)** API to fetch real-time commodity prices from Mandis across India.

The system analyzes price disparities using a custom algorithm to recommend the **"Best Market to Sell"**, helping farmers maximize their profit margins by identifying high-demand locations.

## 🚀 Key Features
* **Real-Time Market Intelligence:** Fetches live daily prices for 130+ crops across 20+ states.
* **Smart Recommendation Engine:** Automatically identifies the Mandi offering the highest "Modal Price" in the selected state.
* **Interactive Visualizations:** Uses **Plotly** to render zoomable, high-definition charts comparing market trends.
* **Robust Error Handling:** Includes a **"Simulation Fallback Mode"** that generates realistic synthetic data if the Government API is down or internet connectivity is lost (ensuring zero-crash presentations).
* **Data Cleaning Pipeline:** Automatically handles duplicate market entries and normalizes inconsistent column names from the API.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Custom CSS for Professional Dashboard UI)
* **Backend Logic:** Python 3.x
* **Data Processing:** Pandas
* **Visualization:** Plotly Express
* **API Integration:** `requests` library (fetching JSON data from data.gov.in)

## 📂 Project Structure
```text
AgroHelper/
├── .streamlit/
│   └── config.toml       # UI Theme Configuration
├── src/
│   ├── __init__.py
│   ├── api_engine.py     # Core logic: API Fetching + Simulation Fallback
│   └── styles.py         # Custom CSS for the "Professional Tech" look
├── app.py                # Main Application Entry Point
├── requirements.txt      # Project Dependencies
├── .gitignore            # Git exclusions
└── README.md             # Documentation