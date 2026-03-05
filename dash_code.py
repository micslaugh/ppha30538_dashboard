import streamlit as st
import pandas as pd
import altair as alt

DASHBOARD_DIR = "data/derived-data"

HEALTH_FILE = {f"{DASHBOARD_DIR}/outcomes.csv"}
AQI_FILE = {f"{DASHBOARD_DIR}/aqi.csv"}

outcomes = pd.read_csv("data/derived-data/outcomes.csv")
aqi = pd.read_csv("data/derived-data/aqi.csv")


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
#"""Sidebar"""

if section == "Health Outcomes":

    st.header("Health Outcomes in Top 20 Carbon-Emitting Counties")
    st.write("This visualization compares the most common health outcomes associated with carbon emissions across Illinois counties, organized from highest emitting counties to least.")

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

    outcome_select = st.sidebar.multiselect(
        "Selected Health Outcomes:",
        options=sorted(health_long["Health Outcome"].unique()),
        default=sorted(health_long["Health Outcome"].unique())
    )

    if len(outcome_select) > 0:
        select = ", ".join(outcome_select)
        st.markdown(f"Showing: {select}")
    else:
        st.warning("Please select at least one health outcome.")

    health_select = health_long[health_long["Health Outcome"].isin(outcome_select)]

    if len(outcome_select) > 0:
        carb_chart = alt.Chart(health_select).mark_rect().encode(
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


elif section == "Air Quality Index (AQI)":

    st.header("Air Quality Index (AQI) by Defining Parameter")
    st.write("This chart displays AQI levels across Illinois counties, organized from most emitting counties to least, separated by deifning pollutants." \
    "" \
    "By separating by pollutant, we can identify which contaminants are driving poor air quality in specific counties.")

    aqi_chart = alt.Chart(aqi).mark_bar().encode(
        x=alt.X("County:N", title="Counties in Illinois", sort=None),
        y=alt.Y("AQI:Q", title="Air Quality Index (AQI)"),
        color=alt.Color("Defining Parameter:N",
                    scale=alt.Scale(range=color_palette),
                    legend=alt.Legend(title="Defining Parameters")),
    tooltip=[
        alt.Tooltip("County:N"),
        alt.Tooltip("AQI:Q"),
        alt.Tooltip("Defining Parameter:N")
    ]
    ).properties(
        width=600,
        height=400,
        title="AQI of Illinois Counties by Defining Parameters"
    )

    st.altair_chart(aqi_chart, use_container_width=True)

st.markdown("---")

with st.expander("Methodology & Notes"):
    st.markdown("""
    **Data Sources**
    - Environmental Protection Agency (EPA)
    - Centers for Disease Control and Prevention (CDC)
    - Illinois General Assembly (ILGA)
    
    **Data Processing**
    - Counties were standardized by direct carbon emissions for merging.
    - Health outcomes were filtered to top 20 carbon-emitting counties.
    - Incidence and death rates were calculated to allow cross-county comparison.
    - Datasets were reshaped into long format for visualization aid using Altair.
    
    **Policy Implications**
    - Identifies counties with overlapping environmental and health burdens.
    - Facilitates targeted pollutant regulation intervention.
    - Establishes standards for emissions typing and tracking
    """)

st.caption("University of Chicago, Harris School of Public Policy")
