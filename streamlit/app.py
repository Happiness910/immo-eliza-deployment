import streamlit as st
import requests


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="Immo Eliza",
    page_icon="🏠",
    layout="centered"
)


# ============================================================
# Custom style
# ============================================================

st.markdown("""
<style>

.stApp {

    background: linear-gradient(
        135deg,
        #ffe5ec,
        #ffb3c6,
        #ff8fa3
    );

}


h1 {

    text-align: center;
    color: #5c1020;

}


h2, h3 {

    color: #7a1f3d;

}


/* Input boxes */

div[data-baseweb="input"] {

    background-color: rgba(255,255,255,0.8);

}


/* Prediction card */

div[data-testid="stMetric"] {

    background: linear-gradient(
        135deg,
        #ff758f,
        #ffb199
    );

    padding: 25px;

    border-radius: 20px;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.2);

}


div[data-testid="stMetricLabel"] {

    color: #5c1020;

}


div[data-testid="stMetricValue"] {

    color: white;

    font-size: 40px;

}


/* Buttons */

.stButton button {

    background-color: #c9184a;

    color: white;

    border-radius: 20px;

    height: 3em;

    width: 100%;

}


.stButton button:hover {

    background-color: #ff4d6d;

}


</style>
""", unsafe_allow_html=True)

# ============================================================
# API configuration
# ============================================================

API_URL = "https://immo-eliza-deployment-jr60.onrender.com/predict"


# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("🏠 Immo Eliza")

st.sidebar.success("Machine Learning Demo")

st.sidebar.write("""
Estimate the selling price of a property in Belgium using a trained XGBoost regression model.

### Technologies
- FastAPI
- Streamlit
- Docker
- Render
- XGBoost
""")


# ============================================================
# Main title
# ============================================================

st.title("🏠 Immo Eliza")

st.write(
    "Estimate the selling price of your Belgian property in just a few seconds."
)

st.divider()


# ============================================================
# Property information
# ============================================================

st.subheader("🏡 Property Information")

col1, col2 = st.columns(2)

with col1:

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

with col2:

    province = st.selectbox(
        "Province",
        ['brussels','vlaams_brabant','antwerp','east_flanders','west_flanders','brabant_wallon','limburg','hainaut','namur','liege','luxembourg']
    )

    latitude = st.number_input(
        "Latitude",
        value=50.83
    )

    longitude = st.number_input(
        "Longitude",
        value=4.35
    )


# ============================================================
# Energy information
# ============================================================

st.subheader("⚡ Property Condition")

state_of_property = st.selectbox(
    "State of property",
    ['to_be_renovated','excellent','normal','fully_renovated','to_renovate','not_specified','new','to_demolish','to_restore','under_construction']
)

epc_score = st.selectbox(
    "EPC score",
    [
        "A",
        "A+",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "not_specified"
    ]
)

# ============================================================
# Energy efficiency gauge
# ============================================================

energy_position = {
    "A+": 100,
    "A": 90,
    "B": 75,
    "C": 60,
    "D": 45,
    "E": 30,
    "F": 15,
    "G": 5,
    "not_specified": 0
}


position = energy_position.get(epc_score, 0)


st.write("⚡ Energy efficiency")


gauge = f"""
<div style='
    width:100%;
    height:25px;
    background:linear-gradient(to right, red, orange, green);
    border-radius:12px;
    position:relative;
'>

<div style='
    position:absolute;
    left:{position}%;
    transform:translateX(-50%);
    width:18px;
    height:18px;
    background:white;
    border:3px solid black;
    border-radius:50%;
    top:3px;
'>
</div>

</div>
"""


st.markdown(
    gauge,
    unsafe_allow_html=True
)


st.caption(
    f"EPC rating: {epc_score}"
)

# ============================================================
# Prediction button
# ============================================================

if st.button("💰 Predict Price", use_container_width=True):

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

    with st.spinner("Predicting property price..."):

        response = requests.post(
            API_URL,
            json=data
        )

    if response.status_code == 200:

        prediction = response.json()["prediction"]

        st.balloons()

        st.metric(
            label="🏠 Estimated Property Price",
            value=f"€ {prediction:,.0f}"
        )

        st.caption(
            f"EPC rating: {epc_score}"
        )

        # ============================================================
        # Price category indicator
        # ============================================================

        if prediction < 250000:

            st.info("💡 **Affordable property**")

        elif prediction < 500000:

            st.success("🏡 **Mid-range property**")

        elif prediction < 1000000:

            st.warning("✨ **Premium property**")

        else:

            st.error("👑 **Luxury property**")


        st.success(
            "Prediction successfully generated!"
        )

    else:

        st.error(
            "Prediction failed. Please try again."
        )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "❤️ Built with Streamlit, FastAPI, Docker and XGBoost."
)