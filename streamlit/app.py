import streamlit as st
import requests


# ============================================================
# API configuration
# ============================================================

API_URL = "https://immo-eliza-deployment-jr60.onrender.com/predict"


# ============================================================
# Streamlit interface
# ============================================================

st.title("🏠 Immo Eliza - House Price Prediction")

st.write(
    "Enter property information to estimate its price."
)


# ============================================================
# User inputs
# ============================================================

livable_surface = st.number_input(
    "Living surface (m²)",
    min_value=10,
    value=120
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=0,
    value=1
)

latitude = st.number_input(
    "Latitude",
    value=50.83
)

longitude = st.number_input(
    "Longitude",
    value=4.35
)

state_of_property = st.selectbox(
    "State of property",
    [
        "good",
        "to be renovated",
        "to restore"
    ]
)

epc_score = st.selectbox(
    "EPC score",
    [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
    ]
)

province = st.text_input(
    "Province",
    value="brussels"
)


# ============================================================
# Prediction
# ============================================================

if st.button("Predict price"):

    data = {
        "livable_surface": livable_surface,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "latitude": latitude,
        "longitude": longitude,
        "state_of_property": state_of_property,
        "epc_score": epc_score,
        "province": province
    }


    response = requests.post(
        API_URL,
        json=data
    )


    if response.status_code == 200:

        prediction = response.json()["prediction"]

        st.success(
            f"Estimated price: {prediction:,.0f} €"
        )

    else:

        st.error(
            "Prediction failed"
        )