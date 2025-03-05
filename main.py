import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

st.set_page_config(page_title="Map Example", page_icon="📍", layout="wide")

st.title("Employees / Locations Map")

st.logo(image="images/t-mobile-logo.png", 
        icon_image="images/t-logo.png")

# Magenta: 226, 0, 116
# Red: 207, 0 , 0
# Blue: 0, 168, 224
reds = np.array([226, 244, 0])
greens = np.array([0, 164, 168])
blues = np.array([116, 96, 224])
@st.cache_data
def load_data():
    data = pd.read_csv('./data/locations.csv')
    # City, State, lat, long, SPEED
    # data = data.dropna()
    data["radius"] = data["EMPLOYEES_HERE"] * 400
    
    data["r"] = reds[0]
    data["g"] = greens[0]
    data["b"] = blues[0]
    return data

data = load_data()

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=38.0,
            longitude=-100.0,
            zoom=3.5,
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position=["LONGITUDE", "LATITUDE"],
                get_line_color=[255, 255, 255],
                get_fill_color=["r", "g", "b"],
                get_radius="radius",
            )
        ],
       tooltip={"text": "{EMPLOYEES_HERE}"}
    )
)