# 🌾 Kisan Mitra (AgroHelper)

> **Smart Mandi Discovery for Indian Farmers**
> *Real-time Data Analysis using e-NAM & Open Govt Data*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![API](https://img.shields.io/badge/API-eNAM%20Govt%20Data-green)

---

## 📖 About the Project
**Kisan Mitra** is a B.Tech CSE project I built to bridge the information gap between farmers and markets. The main issue it solves is that farmers often don't know which Mandi is offering the best price for their crops on any given day.

Instead of relying on manual checks or guesswork, this tool connects directly to the **e-NAM (Electronic National Agriculture Market)** API. It grabs live data from mandis across India and runs a comparison algorithm to recommend the **"Best Market to Sell"**, helping farmers identify where they can get the highest profit margin.

## 🚀 What It Does
* **Tracks Live Prices:** It fetches daily prices for over 130 crops from 20+ states.
* **Smart Suggestions:** The code compares prices across different mandis in a selected state and highlights the one with the highest "Modal Price."
* **Visuals:** I used **Plotly** to render zoomable, interactive charts so users can compare market trends visually rather than looking at raw tables.
* **Auto-Cleaning:** The backend script handles data issues like duplicate market entries and normalizes inconsistent column names coming from the API.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (I added custom CSS to make the dashboard look professional).
* **Backend:** Python 3.10+
* **Data Handling:** Pandas
* **Charts:** Plotly Express
* **Connectivity:** `requests` library (to fetch JSON data from data.gov.in).

## 📂 Project Structure
```text
AgroHelper/
├── .streamlit/
│   └── config.toml       # UI Theme Configuration
├── src/
│   ├── __init__.py
│   ├── api_engine.py     # Core logic: API Fetching 
│   └── styles.py         # Styling
├── app.py                # Main Application 
├── requirements.txt      # Project Dependencies
├── .gitignore            # Git exclusions
└── README.md             # Documentation

⚙️ How to Install & Run
If you want to run this on your local machine, just follow these steps:

1.Clone the repo Get the files onto your machine by typing: 
  git clone https://github.com/nikhil123421/
  cd AgroHelper

2. Set up the environment It's best to use a virtual environment so you don't mess up your global Python install:
   python -m venv venv
   For Windows:
   venv\Scripts\activate
   For macOS/Linux:
   source venv/bin/activate

3. Install the required packages listed in the text file:
   pip install -r requirements.txt

4. Launch the app Fire up the streamlit server:
   streamlit run app.py

🧪 Testing the Project
Since this app relies on a live external API, here is how you can manually test if it's working correctly:

1. Check Connection: Open the app in your browser (usually http://localhost:8501). Look at the sidebar—it should say "Connection Status: Connected". If it says "Error," check your internet or the API limits.

2. Run a Functional Test:
   Select a State (e.g., "Maharashtra") from the dropdown.
   Then Select a Commodity (e.g., "Onion" or "Wheat").
   Then Click the "Analyze Markets" button.

3. Verify Results:
   Wait a few seconds for the data to process.

   Success: A bar chart should appear showing different prices, and the "Recommendation Card" at the top should display a Mandi name with a price higher than 0.

   Note: If the graph is empty, the API might not have data for that specific crop today. Try changing the crop to verify the system is working.
