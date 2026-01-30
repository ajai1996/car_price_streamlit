import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load model and scaler
# -----------------------------
model = pickle.load(open('best_rf_model.pkl', 'rb'))
scaler = pickle.load(open('ss.pkl', 'rb'))

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# -----------------------------
# App Title
# -----------------------------
st.markdown(
    "<h1 style='text-align: center;'>🚗 Car Price Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Predict the selling price of a car using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Input fields
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    year = st.number_input(
        "Manufacturing Year",
        min_value=1990,
        max_value=2035,
        value=2015,
        step=1
    )

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=50000,
        step=1000
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        options=["Petrol", "Diesel", "CNG"]
    )

with col2:
    present_price = st.number_input(
        "Present Price (₹ Lakhs)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    owner = st.selectbox(
        "Number of Previous Owners",
        options=[0, 1, 2, 3]
    )

    transmission = st.selectbox(
        "Transmission",
        options=["Manual", "Automatic"]
    )

seller_type = st.selectbox(
    "Seller Type",
    options=["Dealer", "Individual"]
)

# -----------------------------
# Encoding (same as training)
# -----------------------------
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}

fuel_encoded = fuel_map[fuel_type]
seller_encoded = seller_map[seller_type]
transmission_encoded = transmission_map[transmission]

# -----------------------------
# Prediction
# -----------------------------
st.divider()

if st.button("🔍 Predict Price", use_container_width=True):
    input_data = np.array([[year,
                            present_price,
                            kms_driven,
                            fuel_encoded,
                            seller_encoded,
                            transmission_encoded,
                            owner]])

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]

    prediction = round(prediction, 2)

    st.success(f"💰 Estimated Selling Price: ₹ {prediction} Lakhs")

# -----------------------------
# Footer
# -----------------------------

