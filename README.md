# EpiAccess: Epidemic Forecasting & Healthcare Analysis Dashboard

A comprehensive web application for analyzing infectious disease trends, generating forecasts, and visualizing epidemic patterns across countries and regions.

## 🎯 What This Project Does

This dashboard helps users understand and predict epidemic patterns by:

• **Analyzing real outbreak data** from COVID-19, SARS, and Monkeypox epidemics
• **Generating 6-month forecasts** of disease progression with confidence intervals
• **Creating "what-if" scenarios** showing how past outbreaks would look if they happened in 2025
• **Mapping disease distribution** worldwide with interactive visualizations
• **Providing AI-generated insights** in plain English about epidemic trends

## 📊 Real Data Sources

We use authentic epidemic datasets, not simulated data:

• **COVID-19 Data**: 44,785 records from 2019-2020 covering 212 countries
  - Source: [COVID-19 Dataset on Kaggle](https://www.kaggle.com/datasets/bolkonsky/covid19)
• **SARS Data**: 2,538 records from March-July 2003 covering 37 countries
  - Source: [SARS Outbreak 2003 Complete Dataset](https://www.kaggle.com/datasets/imdevskp/sars-outbreak-2003-complete-dataset?select=sars_2003_complete_dataset_clean.csv)
• **Monkeypox Data**: 15,792 records from 2022 covering 109 countries
  - Source: [Monkeypox Dataset Daily Updated](https://www.kaggle.com/datasets/deepcontractor/monkeypox-dataset-daily-updated?select=Daily_Country_Wise_Confirmed_Cases.csv)
• **Total Dataset**: 63,115 records across 222 unique countries

All data has been cleaned, standardized, and unified into a consistent format for analysis.

### Data Attribution
All datasets are publicly available on Kaggle and used under their respective licenses:
• COVID-19 data compiled by Bolkonsky
• SARS data maintained by imdevskp  
• Monkeypox data curated by deepcontractor

We acknowledge the original data collectors and maintainers who made this analysis possible.

## 🚀 Key Features

### 1. Interactive Epidemic Dashboard
• **Disease Selection**: Choose between COVID-19, SARS, or Monkeypox
• **Country Filtering**: Select specific countries or view top affected regions
• **Metric Options**: Track total cases, daily new cases, deaths, or death rates
• **Date Range Filtering**: Focus on specific time periods
• **Real-time Charts**: Interactive time series and comparison visualizations

### 2. 6-Month Forecasting Engine
• **Scientific Method**: Uses exponential smoothing with epidemic curve modeling
• **Confidence Intervals**: Shows uncertainty ranges (95% confidence bands)
• **Smart Dampening**: Prevents unrealistic exponential growth projections
• **Multiple Countries**: Compare forecasts across different regions
• **Performance Optimized**: Handles up to 5 countries simultaneously for responsive analysis

### 3. AI-Powered Insights
• **Plain English Summaries**: "Brazil: 15% increase in COVID-19 cases forecast for next month (high confidence)"
• **Trend Analysis**: Identifies increasing, decreasing, or stable patterns
• **Confidence Scoring**: High/Medium/Low reliability ratings based on data quality
• **Visual Indicators**: Color-coded confidence levels with trend arrows (📈📉➡️)

### 4. "Project to 2025" Scenarios
• **What-If Analysis**: Shows how historical outbreaks would unfold if they started in 2025
• **Timeline Shifting**: Maintains original outbreak patterns but with current dates
• **Emergency Planning**: Useful for preparedness exercises and resource planning
• **Clear Warnings**: Multiple reliability indicators (5-6/10) and appropriate use guidelines

### 5. Interactive Disease Mapping
• **World Visualization**: Choropleth maps showing case distribution by country
• **Bubble Maps**: Alternative view with geographic coordinates
• **Regional Statistics**: Breakdown of cases by continent
• **Top Affected Lists**: Sortable tables of most impacted countries

### 6. Navigation System
• **Seamless Switching**: Move between dashboard, map, and other analysis pages
• **Consistent Design**: Uniform interface across all components
• **Easy Access**: One-click navigation to different analysis modes

## 🔧 Technical Implementation

### Data Processing Pipeline (`utils/data_processor.py`)
• **Unified Schema**: Converts different dataset formats into consistent structure
• **Country Standardization**: Maps various country names to standard format
• **Date Normalization**: Handles different date formats across datasets
• **Missing Data Handling**: Fills gaps and handles inconsistencies
• **Performance Optimization**: Processes 63k+ records efficiently

### Forecasting Engine (`utils/forecast_engine.py`)
• **EpidemicForecaster Class**: Main forecasting logic with epidemic-specific adjustments
• **Exponential Smoothing**: Proven time series method adapted for epidemic curves
• **Trend Detection**: Automatically identifies growth/decline patterns
• **Batch Processing**: Handles multiple countries simultaneously
• **Error Handling**: Graceful fallbacks for insufficient data

### Insights Generation (`utils/forecast_engine.py`)
• **InsightGenerator Class**: Converts numerical forecasts to human-readable text
• **Trend Metrics**: Calculates 1-month, 3-month, and 6-month percentage changes
• **Confidence Assessment**: Evaluates reliability based on historical data quality
• **Natural Language**: Generates insights in conversational English

## 📱 User Interface

### Dashboard Layout
• **Header Section**: Title, navigation, and key metrics cards
• **Filter Panel**: Disease, country, date, and metric selection
• **Main Chart Area**: Interactive time series with forecasting
• **Insights Panel**: AI-generated summaries and trend analysis
• **Comparison Charts**: Bar charts for country-to-country analysis

### Reliability Features
When using "Project to 2025" mode, users see:
• **Prominent warnings** about scenario planning nature
• **Reliability scores** (5-6/10) throughout the interface
• **Clear guidance** on appropriate vs inappropriate uses
• **Educational tooltips** explaining assumptions and limitations

## ⚠️ Important Disclaimers

### Forecasting Reliability
• **6-Month Forecasts**: Medium-high reliability (7-8/10) for pattern analysis
• **Best for**: Trend identification, comparative analysis, resource planning
• **Limitations**: Cannot predict policy changes, new variants, or external shocks

### 2025 Projections Reliability
• **Scenario Planning**: Medium reliability (5-6/10) for emergency planning
• **Good for**: Pattern comparison, preparedness exercises, relative impact assessment
• **NOT for**: Precise predictions, policy decisions, economic planning
• **Major assumptions**: 2025 conditions = historical conditions (unrealistic)

## 🛠️ Installation & Setup

### Prerequisites
• Python 3.8+
• Streamlit
• Pandas, NumPy
• Plotly for visualizations

### Quick Start
```bash
# Clone the repository
git clone [repository-url]

# Install dependencies
pip install streamlit pandas plotly numpy

# Run the application
python -m streamlit run epiaccess_app.py --server.port 8503
```

### Data Requirements
The app expects these files in the `data/` directory:
• `cleaned_covid_data.csv` - COVID-19 time series data
• `sars_2003_complete_dataset_clean.csv` - SARS outbreak data
• `Daily_Country_Monkeypox_Confirmed_Cases.csv` - Monkeypox case data

## 📁 Project Structure

```
├── epiaccess_app.py              # Main landing page
├── pages/
│   ├── epidemic_dashboard.py     # Main forecasting dashboard
│   ├── disease_map.py           # Interactive mapping page
│   ├── healthcare_facilities.py # Healthcare analysis (placeholder)
│   └── access_clustering.py     # Access analysis (placeholder)
├── utils/
│   ├── data_processor.py        # Data cleaning and unification
│   └── forecast_engine.py       # Forecasting and insights engine
├── data/
│   ├── [raw data files]         # Original epidemic datasets
│   └── processed/               # Cleaned and unified data
└── README.md                    # This documentation
```

## 🔮 Future Development Plans

### Planned Features
• **Healthcare Facilities Mapping**: Integration with hospital capacity data
• **Access Clustering Analysis**: Healthcare accessibility by region
• **Enhanced Forecasting**: Additional statistical models and ensemble methods
• **Real-time Data**: Integration with live epidemic monitoring systems
• **Mobile Optimization**: Responsive design for mobile devices

### Ongoing Improvements
• **Performance Optimization**: Faster loading and processing
• **Additional Diseases**: Expand to include more epidemic datasets
• **Advanced Analytics**: Machine learning models for pattern recognition
• **Export Capabilities**: PDF reports and data download options
