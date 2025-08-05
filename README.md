# EpiAccess: Epidemic Forecasting & Healthcare Analysis Dashboard

A comprehensive web application for analyzing infectious disease trends, generating forecasts, and visualizing epidemic patterns across countries and regions. Features advanced healthcare access clustering to understand global health infrastructure patterns.

## 🎯 What This Project Does

This dashboard helps users understand and predict epidemic patterns by:

• **Analyzing real outbreak data** from COVID-19, SARS, and Monkeypox epidemics
• **Generating 6-month forecasts** of disease progression with confidence intervals
• **Creating "what-if" scenarios** showing how past outbreaks would look if they happened in 2025
• **Mapping disease distribution** worldwide with interactive visualizations
• **Clustering countries by healthcare access** using machine learning to identify access patterns
• **Providing AI-generated insights** in plain English about epidemic trends and healthcare capacity

## 📊 Real Data Sources

We use authentic epidemic and health expenditure datasets, not simulated data:

### Epidemic Data
• **COVID-19 Data**: 44,785 records from 2020-2022 covering 212 countries
  - Source: [COVID-19 Dataset on Kaggle](https://www.kaggle.com/datasets/bolkonsky/covid19)

• **SARS Data**: 2,538 records from March-July 2003 covering 37 countries
  - Source: [SARS Outbreak 2003 Complete Dataset](https://www.kaggle.com/datasets/imdevskp/sars-outbreak-2003-complete-dataset?select=sars_2003_complete_dataset_clean.csv)

• **Monkeypox Data**: 15,792 records from 2022 covering 109 countries
  - Source: [Monkeypox Dataset Daily Updated](https://www.kaggle.com/datasets/deepcontractor/monkeypox-dataset-daily-updated?select=Daily_Country_Wise_Confirmed_Cases.csv)

• **Total Epidemic Dataset**: 63,115 records across 222 unique countries

### Healthcare Access Data
• **Health Expenditure Data**: World Bank health spending indicators (2015-2022) covering 175 countries
  - Health expenditure per capita (USD)
  - Health expenditure as percentage of GDP
  - GDP data for economic context
  - Source: World Bank Open Data Platform

All data has been cleaned, standardized, and unified into a consistent format for analysis.

### Data Attribution
All datasets are publicly available and used under their respective licenses:
• COVID-19 data compiled by Bolkonsky
• SARS data maintained by imdevskp  
• Monkeypox data curated by deepcontractor
• Health expenditure data from World Bank Open Data

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
• **Reliability**: Best for trend analysis and resource planning (not precise predictions)

### 3. Healthcare Access Clustering Analysis
• **Machine Learning Clustering**: K-means algorithm identifies 4 distinct healthcare access patterns
• **Multi-Dimensional Analysis**: Uses health spending per capita, GDP percentage, and economic capacity
• **Real-World Categories**: 
  - High Access - Advanced Economy (countries like USA, Germany)
  - Medium-High Access - Developing (countries like Brazil, Thailand)
  - High Priority - Limited Resources (countries with high health priority but resource constraints)
  - Low Access - Resource Constrained (countries needing healthcare investment)
• **Interactive Visualizations**: Enhanced scatter plots with adjustable point sizes and jitter options
• **Economic Pattern Analysis**: GDP vs health spending relationships with trend lines
• **Statistical Insights**: Correlation analysis and efficiency metrics for each cluster

### 4. Enhanced Access Clustering Visualizations
• **Health Spending Tab**: Bar charts comparing per capita spending and GDP percentage by cluster
• **Global Distribution Tab**: 
  - Interactive scatter plots with point sizes based on GDP
  - Adjustable display options (point size, jitter, log scale)
  - Cluster center visualization
  - Comprehensive hover tooltips
• **Economic Patterns Tab**:
  - Enhanced scatter plot showing GDP vs health spending relationships
  - Optional trend lines for each cluster
  - Correlation analysis and efficiency ratios
  - Top performers identification
• **Smart Color Coding**: Consistent colors across all visualizations for easy pattern recognition

### 5. AI-Powered Insights
• **Plain English Summaries**: "Brazil: 15% increase trend observed over recent weeks (medium confidence)"
• **Trend Analysis**: Identifies increasing, decreasing, or stable patterns
• **Confidence Scoring**: High/Medium/Low reliability ratings based on data quality
• **Visual Indicators**: Color-coded confidence levels with trend arrows (📈📉➡️)
• **Healthcare Access Insights**: Automatic cluster characterization and country comparisons
• **Educational Focus**: Designed for learning and analysis, not clinical decisions

### 6. "Project to 2025" Scenarios
• **What-If Analysis**: Shows how historical outbreaks would unfold if they started in 2025
• **Timeline Shifting**: Maintains original outbreak patterns but with current dates
• **Emergency Planning**: Useful for preparedness exercises and resource planning
• **Clear Warnings**: Multiple reliability indicators (5-6/10) and appropriate use guidelines

### 7. Interactive Disease Mapping
• **World Visualization**: Choropleth maps showing case distribution by country
• **Bubble Maps**: Alternative view with geographic coordinates
• **Regional Statistics**: Breakdown of cases by continent
• **Top Affected Lists**: Sortable tables of most impacted countries

### 8. Navigation System
• **Seamless Switching**: Move between epidemic trends, disease map, and healthcare access clustering
• **Consistent Design**: Uniform interface across all components
• **Easy Access**: One-click navigation between different analysis modes

### 9. Interactive Exploration
Users can adjust clustering parameters, forecasting options, and visualization settings to explore the data from different angles.

### 10. Dual Forecasting Approaches
The dashboard now offers two complementary forecasting methods:
• **Exponential Smoothing**: Traditional statistical approach with high transparency
• **PyTorch Neural Network**: Machine learning approach for complex pattern recognition
• **Educational Comparison**: Users can compare both methods to understand their strengths and limitations

### 11. Marcos Research Integration
The dashboard incorporates research from Marcos et al. on epidemic forecasting and healthcare utilization:
• **Pattern Recognition**: Advanced algorithms for identifying epidemic curve patterns
• **Healthcare Utilization Analysis**: Methods for understanding healthcare system responses
• **Visualization Techniques**: Research-backed approaches to data visualization
• **Educational Framework**: Structured learning about epidemic forecasting principles

## 🔧 Technical Implementation

### **🔮 Forecasting Methodology Explained**

#### **What is Time Series Forecasting?**
Time series forecasting is like predicting the weather - we look at patterns from the past to estimate what will happen in the future. In our case, instead of temperature and rainfall, we're looking at disease case numbers over time.

**Simple Example:**
• If COVID-19 cases were 100 today, 120 tomorrow, and 150 the next day
• We can see an upward trend and predict it might reach 180 cases the following day
• Our system does this mathematically across months of data

#### **Why We Use Exponential Smoothing**
Think of exponential smoothing like a "weighted memory" system:

**How It Works:**
• **Recent data matters more** - Yesterday's case count is more important than last month's
• **Older data still helps** - But historical patterns provide context
• **Smooths out noise** - Ignores random daily fluctuations to see the real trend

**Real-World Analogy:**
Imagine you're trying to predict how busy a coffee shop will be tomorrow:
• Today's customer count (most important)
• This week's pattern (very important) 
• Last month's data (somewhat important)
• Last year's data (background context)

This is exactly how exponential smoothing weighs epidemic data!

#### **Why This Method Works for Epidemics**
Epidemics follow predictable patterns called "epidemic curves":

**Typical Epidemic Phases:**
1. **Slow Start** - Few cases, gradual increase
2. **Exponential Growth** - Cases double rapidly (most dangerous phase)
3. **Peak** - Maximum daily cases reached
4. **Decline** - Cases start falling as population builds immunity/intervention works
5. **Tail** - Low-level cases continue for extended period

**Our Smart Adjustments:**
• **Epidemic Dampening** - Prevents unrealistic endless growth predictions
• **Trend Detection** - Automatically identifies which phase an outbreak is in
• **Context Awareness** - Understands that epidemics eventually decline

#### **What Are Confidence Intervals?**
Confidence intervals are like "error bars" that show uncertainty:

**95% Confidence Interval Means:**
• We're 95% confident the real number will fall within this range
• **Upper bound** - Worst-case scenario (higher than predicted)
• **Lower bound** - Best-case scenario (lower than predicted)
• **Center line** - Most likely outcome

**Visual Example:**
```
Predicted cases: 1,000
Confidence interval: 800 - 1,200
Meaning: We're 95% sure actual cases will be between 800-1,200
```

#### **How Our 6-Month Forecasting Works**

**Step-by-Step Process:**
1. **Data Preparation**
   • Clean historical case numbers
   • Identify trend patterns
   • Remove data outliers

2. **Pattern Recognition**
   • Calculate recent trend (growing/declining/stable)
   • Measure volatility (how much numbers jump around)
   • Assess data quality (more data = more confidence)

3. **Future Projection**
   • Apply exponential smoothing to recent trends
   • Add epidemic-specific dampening to prevent unrealistic growth
   • Generate 180 daily predictions (6 months)

4. **Uncertainty Calculation**
   • Measure how much past predictions varied from reality
   • Apply this uncertainty to future predictions
   • Create upper/lower confidence bounds

**Why 6 Months?**
• **Short enough** - Patterns don't change dramatically over this timeframe
• **Long enough** - Useful for planning and resource allocation
• **Evidence-based** - Research shows forecasting accuracy diminishes significantly beyond 6 months
• **Practical balance** - Provides actionable insights without overconfident long-term predictions

#### **Model Reliability by Use Case**

**Higher Reliability (7-8/10):**
• **Trend Direction** - Is the epidemic growing, declining, or staying stable?
• **Pattern Recognition** - How similar is this outbreak to historical ones?
• **Relative Comparison** - Which countries/regions are most affected?
• **Resource Planning** - Approximate healthcare capacity needs

**Medium Reliability (5-6/10):**
• **Approximate Numbers** - General magnitude of case counts (within broad ranges)
• **Timeline Estimates** - Rough timing of peaks or declines
• **2025 Projections** - "What-if" scenario planning only

**Lower Reliability (3-4/10):**
• **Exact Case Counts** - Precise daily numbers
• **External Factor Prediction** - Policy changes, new variants, behavioral shifts
• **Long-term Predictions** - Anything beyond 6 months
• **Individual Decision Making** - Personal health or medical decisions

#### **Why Not Use More Complex Models?**

**We Could Use Machine Learning, But:**
• **Data Requirements** - Need massive datasets with consistent quality
• **Overfitting Risk** - Complex models can memorize noise instead of real patterns
• **Interpretability** - Harder to explain and understand how predictions are made
• **Epidemic Context** - General AI models don't understand epidemic-specific patterns
• **Educational Value** - Simpler models are better for learning and transparency

**Exponential Smoothing Advantages:**
• **Proven Track Record** - Used successfully in epidemiology for decades
• **Transparent** - Easy to understand how predictions are made
• **Robust** - Works well with limited or imperfect data
• **Fast** - Generates predictions quickly for multiple countries
• **Educational** - Great for understanding forecasting principles

### 🏥 Healthcare Access Clustering Methodology

#### **What is Healthcare Access Clustering?**
Healthcare access clustering groups countries based on similar patterns of healthcare spending and economic capacity. Think of it like organizing countries into "healthcare neighborhoods" - countries with similar healthcare resources and priorities end up in the same group.

#### **Why Use Machine Learning for Healthcare Analysis?**
Instead of making subjective judgments about which countries have "good" or "poor" healthcare access, we let the data speak for itself. The clustering algorithm finds natural patterns in the data that might not be obvious at first glance.

**Real-World Example:**
• You might think all wealthy countries have great healthcare access
• But some wealthy countries spend relatively little on healthcare (low priority)
• While some developing countries spend a high percentage of their GDP on health (high priority)
• Clustering reveals these nuanced patterns automatically

#### **Our Three-Dimensional Approach**
We analyze countries using three key healthcare indicators:

**1. Health Expenditure per Capita (USD)**
• **What it shows**: How much each person's healthcare costs on average
• **Why it matters**: Higher spending often means better access to care
• **Examples**: USA ~$12,000/person, India ~$75/person

**2. Health Expenditure as % of GDP**
• **What it shows**: How much of a country's economy goes to healthcare
• **Why it matters**: Shows national healthcare priority level
• **Examples**: USA ~18% of GDP, Bangladesh ~2.5% of GDP

**3. Economic Capacity (Total GDP)**
• **What it shows**: Size of the country's overall economy
• **Why it matters**: Larger economies can afford more healthcare infrastructure
• **Examples**: USA ~$25 trillion, Luxembourg ~$85 billion

#### **How K-Means Clustering Works**
K-means is like organizing a scattered group of people into 4 distinct circles:

**Step-by-Step Process:**
1. **Start with Raw Data** - Plot all 175 countries in 3D space (spending, priority, capacity)
2. **Standardize Measurements** - Make sure no single metric dominates (like converting feet and meters to same scale)
3. **Find Natural Groups** - Algorithm finds 4 cluster centers that minimize within-group differences
4. **Assign Countries** - Each country goes to its nearest cluster center
5. **Label Clusters** - We interpret what each cluster represents in real-world terms

**Why 4 Clusters?**
• **Simple enough** - Easy to understand and interpret
• **Detailed enough** - Captures major healthcare access patterns
• **Research-backed** - Studies show 4-5 clusters work well for country-level health analysis

#### **Our Four Healthcare Access Clusters**

**🟢 High Access - Advanced Economy**
• **Profile**: Wealthy countries with high absolute spending
• **Characteristics**: >$1,500 per capita AND >$100B GDP
• **Examples**: USA, Germany, Japan, France
• **Healthcare Reality**: Advanced facilities, latest technology, comprehensive coverage

**🟡 Medium-High Access - Developing**
• **Profile**: Growing economies with good healthcare priority
• **Characteristics**: >$300 per capita AND >6% of GDP
• **Examples**: Brazil, Thailand, South Africa, Malaysia
• **Healthcare Reality**: Expanding systems, improving access, mixed public-private

**🔵 High Priority - Limited Resources**
• **Profile**: Countries prioritizing health despite economic constraints
• **Characteristics**: >6.5% of GDP AND <$400 per capita
• **Examples**: Sierra Leone, Malawi, Nepal, Cambodia
• **Healthcare Reality**: Strong political commitment, efficient use of limited resources

**🔴 Low Access - Resource Constrained**
• **Profile**: Countries with limited healthcare spending and capacity
• **Characteristics**: Lower across all metrics
• **Examples**: Afghanistan, Chad, Central African Republic
• **Healthcare Reality**: Basic care only, significant infrastructure needs

#### **Why These Categories Matter**
Different clusters need different types of international health support:

• **High Access**: Technology sharing, research collaboration
• **Medium-High**: Infrastructure investment, specialist training
• **High Priority**: Financial support, capacity building
• **Low Access**: Basic infrastructure, emergency health systems

#### **Technical Implementation Details**

**Data Preprocessing:**
• **Missing Data Handling**: Use 2020-2022 averages for stability
• **Outlier Management**: Cap extreme values to prevent distortion
• **Feature Scaling**: Standardize all metrics to 0-1 range

**Clustering Algorithm:**
• **Method**: K-means with k=4 clusters
• **Initialization**: K-means++ for better starting points
• **Iterations**: Up to 300 iterations with early stopping
• **Random State**: Fixed seed (42) for reproducible results

**Validation Methods:**
• **Silhouette Analysis**: Measures how well-separated clusters are
• **Elbow Method**: Confirms 4 clusters is optimal number
• **Domain Expert Review**: Healthcare professionals validate cluster interpretations

### Data Processing Pipeline (`utils/data_processor.py`)
• **Unified Schema**: Converts different dataset formats into consistent structure
• **Country Standardization**: Maps various country names to standard format
• **Date Normalization**: Handles different date formats across datasets
• **Missing Data Handling**: Fills gaps and handles inconsistencies
• **Performance Optimization**: Processes 63k+ records efficiently

### Forecasting Engine (`utils/forecast_engine.py`)
• **EpidemicForecaster Class**: Main forecasting logic with epidemic-specific adjustments
• **Exponential Smoothing**: Proven time series method adapted for epidemic curves
• **EpidemicTimeSeriesModel**: PyTorch-based neural network for complex pattern recognition
• **Trend Detection**: Automatically identifies growth/decline patterns
• **Batch Processing**: Handles multiple countries simultaneously
• **Error Handling**: Graceful fallbacks for insufficient data
• **Model Selection**: User choice between traditional and machine learning approaches

### Healthcare Access Clustering (`pages/Healthcare Access.py`)
• **K-means Implementation**: Scikit-learn clustering with 4 optimized clusters
• **Data Preprocessing**: 3-year averaging (2020-2022) for pandemic stability
• **Interactive Visualizations**: Enhanced scatter plots with GDP-based point sizing
• **Statistical Analysis**: Correlation analysis and efficiency ratio calculations
• **Multi-Tab Interface**: Health spending, global distribution, and economic patterns

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
• **Insights Panel**: Real-time generated summaries and trend analysis
• **Comparison Charts**: Bar charts for country-to-country analysis

### Access Clustering Interface
• **Three-Tab Design**: Health spending, global distribution, and economic patterns
• **Interactive Controls**: Point size adjustment, jitter options, log scaling, trend lines
• **Smart Color Coding**: Consistent four-cluster color scheme across all visualizations
• **Comprehensive Statistics**: Summary tables, correlation analysis, and efficiency metrics
• **Country Listings**: Organized by cluster with spending averages and key metrics

### Reliability Features
When using "Project to 2025" mode, users see:
• **Prominent warnings** about scenario planning nature
• **Reliability scores** (5-6/10) throughout the interface
• **Clear guidance** on appropriate vs inappropriate uses
• **Educational tooltips** explaining assumptions and limitations

## 📊 What Makes This Project Unique

### 1. **Real Data, Real Insights**
Unlike many educational projects that use simulated data, EpiAccess analyzes authentic epidemic records from three major global outbreaks. This provides genuine insights into how diseases spread and how healthcare systems respond.

### 2. **Practical Healthcare Analysis**
The healthcare access clustering isn't just academic - it identifies real patterns that could inform international health policy and resource allocation decisions.

### 3. **Scientific Rigor with Accessibility**
We use proven epidemiological methods (exponential smoothing) but present results in plain English that non-experts can understand and act upon.

### 4. **Transparency About Limitations**
Rather than overselling capabilities, we're explicit about reliability levels, appropriate use cases, and methodology limitations.

### 5. **Interactive Exploration**
Users can adjust clustering parameters, forecasting options, and visualization settings to explore the data from different angles.

### 6. **Dual Forecasting Approaches**
The dashboard now offers two complementary forecasting methods:
• **Exponential Smoothing**: Traditional statistical approach with high transparency
• **PyTorch Neural Network**: Machine learning approach for complex pattern recognition
• **Educational Comparison**: Users can compare both methods to understand their strengths and limitations

### 7. **Marcos Research Integration**
The dashboard incorporates research from Marcos et al. on epidemic forecasting and healthcare utilization:
• **Pattern Recognition**: Advanced algorithms for identifying epidemic curve patterns
• **Healthcare Utilization Analysis**: Methods for understanding healthcare system responses
• **Visualization Techniques**: Research-backed approaches to data visualization
• **Educational Framework**: Structured learning about epidemic forecasting principles

## ⚠️ Important Disclaimers

### Educational Purpose
• **Primary Use**: Educational analysis and learning about epidemic patterns
• **NOT for**: Real-time health decisions, clinical guidance, or policy making
• **Data Limitations**: Historical data may not reflect current healthcare improvements or changes

### Forecasting Reliability
• **6-Month Forecasts**: Medium reliability (6-7/10) for trend analysis and educational purposes
• **Best for**: Understanding epidemic patterns, comparative analysis, learning forecasting concepts
• **Limitations**: Cannot predict policy changes, new variants, external shocks, or healthcare improvements
• **Educational Value**: Excellent for learning about epidemic curves and forecasting principles

### 2025 Projections Reliability
• **Scenario Planning Only**: Medium-low reliability (4-5/10) for educational "what-if" exercises
• **Good for**: Understanding outbreak patterns, emergency planning concepts, comparative analysis
• **NOT for**: Actual predictions, policy decisions, economic planning, or real emergency planning
• **Major assumptions**: 2025 conditions identical to historical conditions (highly unrealistic)
• **Educational Purpose**: Demonstrates forecasting concepts and pattern recognition

### Healthcare Access Clustering Reliability
• **Pattern Recognition**: High reliability (8-9/10) for identifying general access categories
• **Good for**: Understanding global health patterns, educational analysis, research concepts
• **Limitations**: Based on spending data only; doesn't capture healthcare quality, outcomes, or accessibility
• **NOT for**: Individual country detailed assessments, policy recommendations, or funding decisions
• **Educational Focus**: Great for learning about health economics and clustering analysis

## 🛠️ Installation & Setup

### Prerequisites
• **Python 3.8+** (Python 3.9+ recommended)
• **Package Manager**: pip or conda
• **Memory**: 4GB+ RAM recommended for clustering analysis
• **Storage**: 100MB+ for data files

### Quick Start
```bash
# Clone the repository
git clone [repository-url]
cd EpiAccess

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Home.py
```

### Detailed Installation
```bash
# Create virtual environment (recommended)
python -m venv epiaccess_env
source epiaccess_env/bin/activate  # On Windows: epiaccess_env\Scripts\activate

# Install specific packages if not using requirements.txt
pip install streamlit>=1.40.0 pandas>=2.2.0 numpy>=1.26.4
pip install plotly>=5.22.0 scikit-learn>=1.4.0 openpyxl>=3.1.0
pip install matplotlib>=3.8.4 seaborn>=0.13.2

# Verify installation
python -c "import streamlit, pandas, sklearn, plotly; print('All dependencies installed successfully!')"
```

### Data Requirements
The app expects these files in the `data/` directory:

**Epidemic Data:**
• `cleaned_covid_data.csv` - COVID-19 time series data
• `sars_2003_complete_dataset_clean.csv` - SARS outbreak data  
• `Daily_Country_Monkeypox_Confirmed_Cases.csv` - Monkeypox case data

**Healthcare Access Data:**
• `cleaned_health_expenditure.xlsx` - World Bank health spending data (2015-2022)

### First Run Setup
1. **Download Data**: Ensure all required data files are in the `data/` directory
2. **Test Access**: Visit `http://localhost:8501` after running the app
3. **Performance Check**: Allow 10-15 seconds for initial clustering calculations
4. **Browser Compatibility**: Works best with Chrome, Firefox, or Safari

## 📁 Project Structure

```
├── Home.py                      # Main landing page with navigation
├── pages/
│   ├── Disease Trends.py        # Main forecasting dashboard
│   ├── Disease Map.py           # Interactive disease mapping
│   └── Healthcare Access.py     # Healthcare access clustering analysis
├── utils/
│   ├── data_processor.py        # Data cleaning and unification
│   └── forecast_engine.py       # Forecasting and insights engine
├── data/
│   ├── cleaned_covid_data.csv             # COVID-19 epidemic data
│   ├── sars_2003_complete_dataset_clean.csv # SARS outbreak data
│   ├── Daily_Country_Monkeypox_Confirmed_Cases.csv # Monkeypox data
│   └── cleaned_health_expenditure.xlsx    # World Bank health spending data
├── requirements.txt             # Python package dependencies
└── README.md                   # This comprehensive documentation
```

## 🔮 Future Development Plans

### Recently Completed ✅
• **Healthcare Access Clustering**: Advanced K-means analysis with interactive visualizations

• **Enhanced Data Processing**: World Bank health expenditure integration

• **Interactive Controls**: Point size adjustment, jitter options, log scaling

• **Statistical Analysis**: Correlation analysis and efficiency metrics

• **Multi-Tab Visualizations**: Health spending, global distribution, and economic patterns

• **Streamlined Navigation**: Clean, three-page application structure

• **PyTorch Integration**: Added neural network forecasting as an alternative to exponential smoothing

• **Marcos Research Implementation**: Incorporated research-backed visualization and analysis techniques

### Planned Features
• **Predictive Access Models**: Forecasting healthcare access trends over time

• **Enhanced Forecasting**: Additional statistical models and ensemble methods

• **Real-time Data**: Integration with live epidemic monitoring systems

• **Mobile Optimization**: Responsive design for mobile devices

• **Cluster Validation**: Advanced statistical validation of healthcare access clusters

### Ongoing Improvements
• **Performance Optimization**: Faster clustering calculations and data loading

• **Additional Diseases**: Expand to include more epidemic datasets (influenza, dengue, etc.)

• **Advanced Analytics**: Deep learning models for complex pattern recognition

• **Export Capabilities**: PDF reports, Excel exports, and data download options

• **User Experience**: Enhanced tooltips, better error handling, and guided tours
