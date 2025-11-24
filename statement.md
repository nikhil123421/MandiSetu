# Project Statement: Kisan Mitra (AgroHelper)

## 1. Problem Statement
The biggest issue Indian farmers face right now isn't growing the crops—it's selling them. 

Currently, there is a massive information gap. A farmer in a village might sell his produce at the local Mandi for a low price, simply because he doesn't know that a market 20km away is offering double the rate. Middlemen often take advantage of this lack of data, and farmers end up losing a huge chunk of their hard-earned profit. 

They need a way to see prices across different markets instantly, without relying on word-of-mouth or agents.

## 2. Scope of the Project
The goal of **Kisan Mitra** is to build a "decision support system." 

**What it does:**
* It acts as a search engine for agricultural prices.
* It focuses specifically on the Indian market using the government's e-NAM (National Agriculture Market) network.
* It covers major commodities (Cereals, Pulses, Vegetables, Fruits).

**What it does NOT do (Boundaries):**
* It is **not** an e-commerce site; farmers cannot sell crops directly through the app.
* It does not handle logistics or transport booking.
* It is purely an analytics tool to help them decide *where* to go.

## 3. Target Users
* **Farmers:** The primary users who need to check daily rates before loading their trucks.
* **Farming Cooperatives (FPOs):** Groups that sell in bulk and need to identify the most profitable state or district to target.
* **Educated Rural Youth:** Often, the younger generation in farming families uses smartphones to help their parents make better financial decisions.

## 4. High-Level Features
* **Live Mandi Search:** Users can select their State and Crop to see a list of active markets and their current prices.
* **"Best Price" Algorithm:** The system automatically highlights the Mandi offering the highest modal price, so the user doesn't have to calculate manually.
* **Data Visualization:** Instead of boring text lists, I used bar charts to visually compare prices. This makes it easier to spot price differences at a glance.
* **Spam/Duplicate Removal:** The backend cleans up the raw government data, removing repeated entries so the user gets a clean list.
