import streamlit as st
import pandas as pd
import altair as alt

DASHBOARD_DIR = "data/derived-data"

HEALTH_FILE = {f"{DASHBOARD_DIR}/outcomes.csv"}
AQI_FILE = {f"{DASHBOARD_DIR}/aqi.csv"}

outcomes = pd.read_csv("data/derived-data/outcomes.csv")
aqi = pd.read_csv("daily_aqi_by_county_2025.csv")

st.set_page_config(page_title="Illinois Emissions and Health Dashboard", layout="wide")

st.title("Impact of Carbon Emissions on Community Health in Illinois by County")
st.caption("Exploring the relationship between air quality and carbon emissions on pertinent health outcomes in Illinois, with the goal to determine whether high emissions correlates with higher health outcomes")

color_palette = [
    "#041556", # 
    "#748dc6", # 
    "#c3e8ff", # 
    "#601414", # 
    "#c48f8f"  # 
]

st.sidebar.title("Dashboard Navigation")
section = st.sidebar.radio(
    "Select Visualization",
    ["Health Outcomes", "Air Quality Index (AQI)"]
)
st.sidebar.caption("Data Analytics and Visualization for Public Policy")
"""Sidebar"""

if section == "Health Outcomes":

    st.header("Health Outcomes in Top 20 Carbon-Emitting Counties")
    st.write("This visualization compares the most common health outcomes associated with carbon emissions across Illinois counties, organized from highest emitting counties to least.")

st.set_page_config(page_title="")

st.title("Defining Parameters of Carbon Emissions and their Effects on Community Health in Illinois by County")
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

        st.altair_chart(carb_chart, use_container_width=True)

##User Inputs
color_palette = [
    "#cf1020",  
    "#A4343A",  
    "#800000",  
    "#550000",  
    "#2c1608"    
]

param = st.sidebar.multiselect(
    "Select Health Outcome:", 
    options=sorted(health_long["Health Outcome"].unique()),
    default=sorted(health_long["Health Outcome"].unique())
)

st.subheader(f"Selected View: {param}")

filtered_health = health_long[health_long["Health Outcome"].isin(param)]

if len(param) == 0:
    st.warning("Please select at least one health outcome.")
else:
    carb_chart = alt.Chart(filtered_health).mark_line(point=True).encode(
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
