import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

st.set_page_config(page_title="Contacts Dashboard", page_icon="🇺🇸", layout="wide")

st.title("Magenta Network Strength")

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
    data = pd.read_csv('./data/WMCA.csv')
    data = data.iloc[:, [3, 5, 6, 7, 36, 47, 58]] ## integer location based indexing
    # City, Zip, lat, long, Avg Ookla Download Mbps, Avg Ookla Download Mbps - VZ, Avg Ookla Download Mbps - AT&T, 
    data = data.dropna()
    data["radius"] = data["Avg Ookla Download Mbps"] * 40
    numeric_data = data.iloc[:, [4,5,6]].to_numpy()
    max_index = np.argmax(numeric_data, axis=1)
    data["r"] = reds[max_index]
    data["g"] = greens[max_index]
    data["b"] = blues[max_index]
    return data

data = load_data()

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=38.0,
            longitude=-107.0,
            zoom=3,
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position=["longitude", "latitude"],
                get_line_color=[255, 255, 255],
                get_fill_color=["r", "g", "b"],
                get_radius="radius",
            )
        ],
    #    tooltip={"text": "{object.Zip_agg}"}
    )
)