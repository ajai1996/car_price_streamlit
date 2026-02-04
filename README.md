# 🚗 Car Price Prediction Web App

A Machine Learning–based web application that predicts the **selling price of a used car** based on key features such as year, present price, kilometers driven, fuel type, seller type, transmission, and number of previous owners.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and provides an easy-to-use, interactive interface for real-time predictions.

---
## 🎬 Application Demo

![Car Price Prediction App Demo](https://raw.githubusercontent.com/ajai1996/github_practi/refs/heads/main/Recording%202026-02-04%20100249.gif)



## 🔍 Problem Statement

Estimating the resale price of a used car is challenging due to multiple influencing factors.  
This project uses **Supervised Machine Learning (Linear Regression)** to predict car prices accurately based on historical data.

---

## 🧠 Machine Learning Approach

- **Model Used:** Linear Regression  
- **Feature Scaling:** MinMaxScaler  
- **Target Variable:** Selling Price (in Lakhs)  
- **Dropped Feature:** Car_Name (not relevant for prediction)

### Input Features:
- Manufacturing Year  
- Present Price (in Lakhs)  
- Kilometers Driven  
- Fuel Type (Petrol / Diesel / CNG)  
- Seller Type (Dealer / Individual)  
- Transmission (Manual / Automatic)  
- Number of Previous Owners  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Pickle**

----

## ▶️ How to Run the Application Locally

Follow the steps below to run the **Car Price Prediction Streamlit App** on your local machine.

---
1️⃣ Clone the Repository
```bash
git clone https://github.com/ajai1996/car_price_streamlit.git
cd car_price_streamlit
```
2️⃣ Create a Virtual Environment
```bash
   python -m venv venv

    venv\Scripts\activate
```
3️⃣ Install Required Dependencies
```bash
    pip install -r requirements.txt
```
4️⃣ Ensure Required Files Are Present

Make sure the following files exist in the project directory:

app.py

lin_model.pkl

ss.pkl

5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```





