import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import json

DASHBOARD_DIR = "data/derived-data"

HEALTH_FILE = {f"{DASHBOARD_DIR}/outcomes.csv"}
AQI_FILE = {f"{DASHBOARD_DIR}/aqi.csv"}

outcomes = pd.read_csv("outcomes.csv")

color_palette = [
    "#cf1020", # 
    "#A4343A", # 
    "#800000", # 
    "#550000", # 
    "#2c1608"  # 
]

health_long = outcomes.melt(
    id_vars="County",
    value_vars=[
        "Asthma Incidence",
        "COPD Deaths",
        "COVID Deaths",
        "Heart Failures",
        "Stroke Deaths",
    ],
    var_name="Health Outcome",
    value_name="Rate"
)

health_long

st.set_page_config(page_title="")

st.title("# Defining Parameters of Carbon Emissions and their Effects on Community Health in Illinois by County")
st.write("How do varying carbon emissions affect the AQI of Illinois and what effects do they have on health? We generated graphs tracking various factors, measured by county.")

##Load Data



##User Inputs

param = st.selectbox("Select Health Outcome", ["Asthma Incidence", "COPD Deaths", "COVID Deaths", "Heart Failures", "Stroke Deaths"])
st.subheader(f"Selected View: {param}")

carb_chart = alt.Chart(health_long).mark_line(point=True).encode(
    x=alt.X("County:N", title="Counties", sort=None),
    y=alt.Y("Rate:Q", title="Death/Incidence Rates"),
    color=alt.Color("Health Outcome:N",
                    scale=alt.Scale(range=color_palette),
                    title="Health Outcome"),
    tooltip=["County", "Rate", "Health Outcome"]
).properties(
    width=600,
    height=400,
    title="Health Outcomes Rates by County from Most to Least (Top 20 Carbon Emitting in Illinois)"
)

st.altair_chart(carb_chart, use_container_width=True)
