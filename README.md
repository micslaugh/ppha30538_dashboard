# Analysis of Carbon Emissions and Public Health Outcomes

This project processes and visualizes carbon emissions by county in Illinois and tracks their relationship to public health outcomes across the state, including cancer, COPD, asthma, and worsening complications for Covid-19, stroke, and heart failure.

## Setup

```bash
conda env create -f environment.yml
```

## Project Structure

```
data/
  raw-data/           # Raw data files
    ghgp_data_2021.xlsx    # Carbon emissions data
    bladder_cancer.csv		# Bladder cancer data
    heart_stroke_mortality.csv  # Heart failure and stroke mortality data
    breast_cancer.csv		# Breast cancer data
    Illinois_Counties.geojson # Illinois county geo data
    colorectal_cancer.csv		# Colorectal cancer data
    kidney_cancer.csv # Kidney cancer data
    crude_asthma.csv	#	Asthma data
    lung-bronch_cancer.csv  # Lung and bronchus cancer data
    crude_COPD.csv			# COPD data
    population_illinois.xlsx  # Illinois population data
    daily_aqi_by_county_2025.csv	# US AQI data
    us-counties.csv #
  derived-data/       # Filtered data and output plots
    fire_filtered.gpkg  # Fire data filtered to post-2015
    cpi_filtered.csv    # CPI data filtered to 2020 onwards
code/                 # Data processing and plot creation 
  preprocessing.qmd   # Organizes health data and cleans emissions and AQI data
  cancer_graph.py			# Plots cancer incidence bar graph
  county_map.py			  # Maps cancer incidence and emissions maps
  emissions-cancer_scatter.py   # Plots cancer incidence and emissions scatter plot
environment.yml	      # Defines required packages
README.md             # Explains project structure
```


## Usage

1. Run preprocessing to filter data:
   ```bash
   python code/preprocessing.py
   ```

2. Generate the fire perimeter plot:
   ```bash
   python code/plot_fires.py
   ```
