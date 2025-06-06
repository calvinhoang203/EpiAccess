# COVID-19 Dashboard

A comprehensive dashboard for visualizing and analyzing COVID-19 data, built with Streamlit.

## Features

- **Disease Map**: Geographic visualization of COVID-19 cases and incidence rates
- **Epidemics**: Forecast and trend analysis of COVID-19 cases
- **Facilities**: Analysis of healthcare facility distribution and capacity
- **Health Access**: Clustering analysis of healthcare access patterns

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/covid-dashboard.git
   cd covid-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Make sure you have the COVID-19 data file in the `data` directory:
   - The app expects a file named `cleaned_covid_data.csv` in the `data` directory
   - The data should be in CSV format with columns for date, location, cases, deaths, etc.

## Running the App

To run the Streamlit app, use the following command:

```
streamlit run streamlit_covid_dashboard.py
```

This will start the Streamlit server and open the dashboard in your default web browser.

## Data Structure

The app expects the COVID-19 data to be in a CSV file with the following columns:

- `date`: The date of the data point (in YYYY-MM-DD format)
- `location`: The country or region name
- `continent`: The continent of the location
- `total_cases`: Total number of COVID-19 cases
- `total_deaths`: Total number of COVID-19 deaths
- `new_cases`: Number of new cases
- `new_deaths`: Number of new deaths
- `total_cases_per_million`: Total cases per million population
- `total_deaths_per_million`: Total deaths per million population
- `new_cases_per_million`: New cases per million population
- `new_deaths_per_million`: New deaths per million population
- `hospital_beds_per_thousand`: Number of hospital beds per thousand population
- `life_expectancy`: Life expectancy in years
- `human_development_index`: Human Development Index (0-1)
- `gdp_per_capita`: GDP per capita
- `population_density`: Population density

## Customization

You can customize the dashboard by modifying the `streamlit_covid_dashboard.py` file:

- Add new tabs or visualizations
- Change the color scheme
- Add new data sources
- Modify the clustering parameters

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data source: Our World in Data (https://ourworldindata.org/covid-cases)
- Built with Streamlit (https://streamlit.io/)
- Visualization libraries: Plotly, Matplotlib, Seaborn