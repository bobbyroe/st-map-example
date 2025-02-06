import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contacts Dashboard", page_icon="🇺🇸", layout="wide")

st.title("Magenta Network Strength")

st.logo(image="images/t-mobile-logo.png", 
        icon_image="images/t-logo.png")
@st.cache_data
def load_data():
    data = pd.read_csv('./data/20250114 - Waste Management Customer Analysis (ATT-VZ).csv')
    data = data.iloc[:, [6, 7, 30, 36, 47, 58]] # integer location based indexing
    data = data.dropna()
    return data

data = load_data()
# st.write(data)
st.map(data, size="DirectionDegrees", use_container_width=True)


