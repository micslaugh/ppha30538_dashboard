import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import json

DASHBOARD_DIR = "data/derived-data"

HEALTH_FILE = {f"{DASHBOARD_DIR}/outcomes.csv"}
AQI_FILE = {f"{DASHBOARD_DIR}/aqi.csv"}

st.set_page_config(page_title="")

st.title("# Defining Parameters of Carbon Emissions and their Effects on Community Health in Illinois by County")
st.write("How do varying carbon emissions affect the AQI of Illinois and what effects do they have on health? We generated graphs tracking various factors, measured by county.")

##Load Data

@st.cache_data
def load_outcomes():
    outcomes = pd.read_csv("data/derived-data/outcomes.csv")
    return outcomes

@st.cache_data
def load_aqi():
    aqi = pd.read_csv("data/derived-data/aqi.csv")
    return aqi

outcomes_df = load_outcomes()
aqi_df = load_aqi()

health_outcomes = [col for col in outcomes_df.columns if col not in ["County", "Total Direct Emissions", "Population"]]


##User Inputs

param = st.selectbox("Health Outcome", ["", "", "", "", ""])

if "" not in st.session_state:
    st.session_state

st.altair_chart()