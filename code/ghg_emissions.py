import pandas as pd
import altair as alt
import streamlit as st

ghgp = pd.read_excel("ghgp_data_2021_0.xlsx")
outcomes = pd.read_csv("outcomes.csv")

color_palette = [
    "#041556", # 
    "#748dc6", # 
    "#c3e8ff", # 
    "#601414", # 
    "#c48f8f"  # 
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

#Data Cleaning

ghgp = ghgp.iloc[3:].reset_index(drop=True)

ghgp = ghgp[["Unnamed: 4", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 13"]]
ghgp.rename(columns={"Unnamed: 4": "State", "Unnamed: 7": "County", "Unnamed: 8": "Latitude", "Unnamed: 9": "Longitude", "Unnamed: 13": "Total Direct Emissions"}, inplace=True)

ghgp = ghgp[ghgp["State"] == "IL"]
ghgp = ghgp.dropna()

ghgp["County"] = (ghgp["County"]
                  .astype(str)
                  .str.strip()
                  .str.lower()
                  .str.replace(r"county.*$", "", regex=True)
                  .str.replace(r"\s+", " ", regex=True)
                  .str.strip()
                  .str.title()
)

ghgp = ghgp.groupby("County", as_index=False).agg({
    "Total Direct Emissions": "sum",
    "Latitude": "mean",
    "Longitude": "mean"
})

ghgp = ghgp[ghgp["County"] != "Lasalle"]

#Data Graphing

heat_chart = alt.Chart(health_long).mark_rect().encode(
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

heat_chart