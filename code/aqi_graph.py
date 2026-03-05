import pandas as pd
import altair as alt
import streamlit as st

aqi = pd.read_csv("daily_aqi_by_county_2025.csv")

color_palette = [
    "#041556", # 
    "#748dc6", # 
    "#c3e8ff", # 
    "#601414", # 
    "#c48f8f"  # 
]

#Data Cleaning

aqi = aqi[["State Name", "county Name", "AQI", "Defining Parameter"]]
aqi.rename(columns={"State Name": "State", "county Name": "County"}, inplace=True)

aqi = aqi[aqi["State"] == "Illinois"]

aqi = aqi.groupby(["County", "Defining Parameter"], as_index=False).agg({"AQI": "mean"})

#Data Graphing

aqi_chart = alt.Chart(aqi).mark_bar().encode(
    x=alt.X("County:N", title="Counties in Illinois"),
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
).interactive()

aqi_chart
