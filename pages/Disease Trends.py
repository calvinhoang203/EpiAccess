import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime, timedelta
import numpy as np
import sys
import os

# Add utils to path for forecasting modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.forecast_engine import EpidemicForecaster, InsightGenerator

# Page config
st.set_page_config(
    page_title="📊 Epidemic Trends",
    page_icon="📊",
    layout="wide"
)

# Load data and metadata with caching
@st.cache_data
def load_epidemic_data():
    """Load processed epidemic data and metadata"""
    try:
        # Load unified dataset
        data = pd.read_csv("data/processed/unified_epidemic_data.csv")
        data['date'] = pd.to_datetime(data['date'])
        
        # Load metadata
        with open("data/processed/disease_metadata.json", "r") as f:
            metadata = json.load(f)
        
        # Load summary stats
        with open("data/processed/data_summary.json", "r") as f:
            summary = json.load(f)
        
        return data, metadata, summary
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

@st.cache_data
def filter_data(data, disease, countries, date_range):
    """Filter data based on user selections"""
    filtered = data[data['disease'] == disease].copy()
    
    if countries:
        filtered = filtered[filtered['country'].isin(countries)]
    
    if date_range:
        start_date, end_date = date_range
        filtered = filtered[
            (filtered['date'] >= pd.to_datetime(start_date)) & 
            (filtered['date'] <= pd.to_datetime(end_date))
        ]
    
    return filtered

def create_forecast_chart(data, metric, countries, disease, show_forecast=True, show_confidence=True, project_to_2025=False, use_pytorch=False):
    """Create time series chart with optional forecasting and 2025 projection"""
    if data.empty:
        return go.Figure().add_annotation(
            text="No data available for selected filters",
            xref="paper", yref="paper", x=0.5, y=0.5,
            showarrow=False, font_size=16
        )
    
    # Create color palette for countries
    colors = px.colors.qualitative.Set3
    fig = go.Figure()
    
    # Initialize forecaster if needed
    forecaster = EpidemicForecaster() if (show_forecast or project_to_2025) else None
    
    selected_countries = countries if countries else data['country'].unique()[:5]  # Limit to 5 for performance
    
    for i, country in enumerate(selected_countries):
        country_data = data[data['country'] == country].sort_values('date')
        if not country_data.empty:
            
            if project_to_2025 and forecaster:
                # Use 2025 projection mode
                try:
                    projection_result = forecaster.project_to_current_year(data, disease, country, metric, 2025, use_pytorch)
                    
                    if projection_result['success']:
                        projected_dates = projection_result['projected_dates']
                        projected_values = projection_result['projected_values']
                        
                        # Projected historical data (what it would look like in 2025)
                        fig.add_trace(go.Scatter(
                            x=projected_dates,
                            y=projected_values,
                            mode='lines+markers',
                            name=f"{country} (If in 2025)",
                            line=dict(color=colors[i % len(colors)], width=2),
                            marker=dict(size=4),
                            hovertemplate=f'<b>{country} (Projected to 2025)</b><br>' +
                                        'Date: %{x}<br>' +
                                        f'{metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                                        f'<i>Based on {projection_result["original_period"]} pattern</i><br>' +
                                        f'<i>Forecast method: {projection_result["forecast_method"]}</i><br>' +
                                        '<b>⚠️ Scenario planning only - Reliability: 5-6/10</b><br>' +
                                        '<extra></extra>'
                        ))
                        
                        # Add forecast if enabled
                        if show_forecast:
                            forecast_dates = projection_result['forecast_dates']
                            forecast_values = projection_result['forecast_values']
                            lower_bound = projection_result['lower_bound']
                            upper_bound = projection_result['upper_bound']
                            
                            # Forecast line
                            fig.add_trace(go.Scatter(
                                x=forecast_dates,
                                y=forecast_values,
                                mode='lines',
                                name=f"{country} (2025 Forecast)",
                                line=dict(color=colors[i % len(colors)], width=2, dash='dash'),
                                hovertemplate=f'<b>{country} 2025 Forecast</b><br>' +
                                            'Date: %{x}<br>' +
                                            f'Predicted {metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                                            f'<i>Forecast method: {projection_result["forecast_method"]}</i><br>' +
                                            '<b>⚠️ Scenario planning only - Reliability: 5-6/10</b><br>' +
                                            '<extra></extra>'
                            ))
                            
                            # Confidence intervals
                            if show_confidence:
                                # Use a simple semi-transparent color based on the country index
                                alpha = 0.2
                                confidence_colors = [
                                    f'rgba(255, 0, 0, {alpha})',     # Red
                                    f'rgba(0, 0, 255, {alpha})',     # Blue  
                                    f'rgba(0, 128, 0, {alpha})',     # Green
                                    f'rgba(255, 165, 0, {alpha})',   # Orange
                                    f'rgba(128, 0, 128, {alpha})',   # Purple
                                    f'rgba(255, 192, 203, {alpha})', # Pink
                                    f'rgba(0, 255, 255, {alpha})',   # Cyan
                                    f'rgba(255, 255, 0, {alpha})',   # Yellow
                                ]
                                
                                fig.add_trace(go.Scatter(
                                    x=forecast_dates + forecast_dates[::-1],
                                    y=upper_bound + lower_bound[::-1],
                                    fill='toself',
                                    fillcolor=confidence_colors[i % len(confidence_colors)],
                                    line=dict(color='rgba(255,255,255,0)'),
                                    name=f"{country} (95% CI)",
                                    showlegend=False,
                                    hoverinfo='skip'
                                ))
                    else:
                        st.warning(f"Could not project {country} to 2025: {projection_result['message']}")
                        
                except Exception as e:
                    st.warning(f"Could not project {country} to 2025: {str(e)}")
            
            else:
                # Regular mode: show historical data
                fig.add_trace(go.Scatter(
                    x=country_data['date'],
                    y=country_data[metric],
                    mode='lines+markers',
                    name=f"{country} (Historical)",
                    line=dict(color=colors[i % len(colors)], width=2),
                    marker=dict(size=4),
                    hovertemplate=f'<b>{country}</b><br>' +
                                'Date: %{x}<br>' +
                                f'{metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                                '<extra></extra>'
                ))
                
                # Add forecast if enabled
                if show_forecast and forecaster:
                    try:
                        forecast_result = forecaster.generate_forecast(data, disease, country, metric, use_pytorch)
                        
                        if forecast_result['success'] and forecast_result['forecast_values']:
                            forecast_dates = forecast_result['forecast_dates']
                            forecast_values = forecast_result['forecast_values']
                            lower_bound = forecast_result['lower_bound']
                            upper_bound = forecast_result['upper_bound']
                            
                            # Forecast line
                            fig.add_trace(go.Scatter(
                                x=forecast_dates,
                                y=forecast_values,
                                mode='lines',
                                name=f"{country} (Forecast)",
                                line=dict(color=colors[i % len(colors)], width=2, dash='dash'),
                                hovertemplate=f'<b>{country} Forecast</b><br>' +
                                            'Date: %{x}<br>' +
                                            f'Predicted {metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                                            f'<i>Forecast method: {forecast_result["forecast_method"]}</i><br>' +
                                            '<extra></extra>'
                            ))
                            
                            # Confidence intervals
                            if show_confidence:
                                # Use a simple semi-transparent color based on the country index
                                alpha = 0.2
                                confidence_colors = [
                                    f'rgba(255, 0, 0, {alpha})',     # Red
                                    f'rgba(0, 0, 255, {alpha})',     # Blue  
                                    f'rgba(0, 128, 0, {alpha})',     # Green
                                    f'rgba(255, 165, 0, {alpha})',   # Orange
                                    f'rgba(128, 0, 128, {alpha})',   # Purple
                                    f'rgba(255, 192, 203, {alpha})', # Pink
                                    f'rgba(0, 255, 255, {alpha})',   # Cyan
                                    f'rgba(255, 255, 0, {alpha})',   # Yellow
                                ]
                                
                                fig.add_trace(go.Scatter(
                                    x=forecast_dates + forecast_dates[::-1],
                                    y=upper_bound + lower_bound[::-1],
                                    fill='toself',
                                    fillcolor=confidence_colors[i % len(confidence_colors)],
                                    line=dict(color='rgba(255,255,255,0)'),
                                    name=f"{country} (95% CI)",
                                    showlegend=False,
                                    hoverinfo='skip'
                                ))
                    
                    except Exception as e:
                        st.warning(f"Could not generate forecast for {country}: {str(e)}")
    
    # Update layout
    if project_to_2025:
        title = f'{disease} - {metric.replace("_", " ").title()} Projected to 2025 [⚠️ SCENARIO PLANNING - Reliability: 5-6/10]'
        if show_forecast:
            title += " with Forecast"
    else:
        title = f'{disease} - {metric.replace("_", " ").title()} {"with 6-Month Forecast" if show_forecast else "Over Time"}'
    
    fig.update_layout(
        title=dict(
            text=title, 
            font_size=20, 
            x=0.50,  # Move slightly more to the left from 0.5 for better centering
            y=0.99,  # Move upward from default position
            xanchor='center',  # Ensure center anchoring
            yanchor='top'  # Anchor from top
        ),
        xaxis_title="Date",
        yaxis_title=metric.replace("_", " ").title(),
        hovermode='x unified',
        height=600,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_time_series_chart(data, metric, countries, disease):
    """Create interactive time series chart"""
    return create_forecast_chart(data, metric, countries, disease, show_forecast=False)

def create_comparison_chart(data, metric, countries, disease):
    """Create comparison bar chart for selected countries"""
    if data.empty:
        return go.Figure()
    
    # Get latest values for each country
    latest_data = data.groupby('country')[metric].max().reset_index()
    latest_data = latest_data.sort_values(metric, ascending=False)
    
    if countries:
        latest_data = latest_data[latest_data['country'].isin(countries)]
    else:
        latest_data = latest_data.head(10)  # Top 10 countries
    
    fig = px.bar(
        latest_data,
        x='country',
        y=metric,
        color=metric,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        title=dict(
            text=f'{disease} - Peak {metric.replace("_", " ").title()} by Country',
            font_size=18,
            x=0.47,  # Match the main chart's centering
            y=0.92,  # Move upward for consistency
            xanchor='center',
            yanchor='top'
        ),
        xaxis_title="Country",
        yaxis_title=metric.replace("_", " ").title(),
        height=400,
        xaxis_tickangle=-45
    )
    
    return fig

def display_key_metrics(data, disease, summary):
    """Display key metrics cards"""
    if disease in summary:
        stats = summary[disease]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Countries Affected",
                f"{stats['total_countries']:,}",
                help="Total number of countries with reported cases"
            )
        
        with col2:
            st.metric(
                "Peak Total Cases",
                f"{stats['peak_cases']['total_cases']:,}",
                help="Highest cumulative case count across all countries"
            )
        
        with col3:
            st.metric(
                "Peak Daily Cases",
                f"{stats['peak_cases']['daily_cases']:,}",
                help="Highest single-day case count"
            )
        
        with col4:
            if stats['total_deaths'] > 0:
                st.metric(
                    "Total Deaths",
                    f"{stats['total_deaths']:,}",
                    help="Total death count across all countries"
                )
            else:
                st.metric(
                    "Data Period",
                    f"{stats['date_range']['start'][:7]} to {stats['date_range']['end'][:7]}",
                    help="Available data timeframe"
                )

def display_insights_panel(data, disease, countries, metric, project_to_2025=False, use_pytorch=False):
    """Display insights panel with forecasting information"""
    if not data.empty and countries:
        # Initialize forecaster and insight generator
        forecaster = EpidemicForecaster()
        insight_generator = InsightGenerator()
        
        # Get forecasts for selected countries
        forecast_results = forecaster.batch_forecast(data, disease, countries, metric, use_pytorch)
        
        # Generate insights
        insights = insight_generator.generate_batch_insights(forecast_results, disease, metric.replace('_', ' '))
        
        # Display insights
        st.subheader("📊 Forecasting Insights")
        
        # Add forecast method information
        forecast_method = "PyTorch Neural Network" if use_pytorch else "Exponential Smoothing"
        st.info(f"**Forecast Method:** {forecast_method}")
        
        if use_pytorch:
            st.markdown("""
            **About PyTorch Forecasting:**
            - Uses a simple neural network to learn patterns in the time series data
            - Can capture complex non-linear relationships in the data
            - May perform better for datasets with irregular patterns
            - Training time is longer than traditional methods
            """)
        else:
            st.markdown("""
            **About Exponential Smoothing:**
            - Traditional statistical method for time series forecasting
            - Works well for data with clear trends and seasonal patterns
            - Faster computation than neural network approaches
            - May struggle with highly irregular data
            """)
        
        # Display insights for each country
        for insight in insights:
            with st.expander(f"**{insight['country']}** - {insight['summary']}"):
                st.markdown(insight['details'])

def main():
    # Add sidebar styling for consistency
    st.markdown("""
    <style>
    /* Sidebar Navigation Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    .css-1aumxhk {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Sidebar links styling */
    [data-testid="stSidebar"] a {
        color: white !important;
        text-decoration: none !important;
        padding: 0.75rem 1rem !important;
        border-radius: 8px !important;
        margin: 0.25rem 0 !important;
        transition: all 0.3s ease !important;
        font-weight: 500 !important;
        text-transform: capitalize !important;
    }
    
    [data-testid="stSidebar"] a:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        transform: translateX(5px) !important;
    }
    
    [data-testid="stSidebar"] .element-container {
        margin: 0.25rem 0 !important;
    }
    
    /* Current page indicator */
    [data-testid="stSidebar"] a[aria-current="page"] {
        background: rgba(255, 255, 255, 0.3) !important;
        border-left: 4px solid white !important;
        font-weight: 600 !important;
    }
    
    /* Sidebar header */
    [data-testid="stSidebar"] .css-1lcbmhc {
        padding-top: 2rem !important;
    }
    
    /* Make sidebar text white */
    [data-testid="stSidebar"] .css-1lcbmhc h1, 
    [data-testid="stSidebar"] .css-1lcbmhc h2,
    [data-testid="stSidebar"] .css-1lcbmhc h3,
    [data-testid="stSidebar"] .css-1lcbmhc p,
    [data-testid="stSidebar"] .css-1lcbmhc span {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with navigation
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("🦠 Epidemic Forecast Dashboard")
        st.markdown("**Get 6-month forecasts of disease cases by region**")
    
    with col2:
        if st.button("🗺️ View on Map", use_container_width=True):
            st.switch_page("pages/Disease Map.py")
    
    # Load data
    data, metadata, summary = load_epidemic_data()
    
    if data is None:
        st.error("Failed to load epidemic data. Please check data files.")
        return
    
    # Sidebar filters
    st.sidebar.header("🔍 Filter Options")
    
    # Disease selection
    diseases = sorted(data['disease'].unique())
    selected_disease = st.sidebar.selectbox(
        "Select Disease Type",
        diseases,
        help="Choose which disease to analyze"
    )
    
    # Get disease-specific data for further filtering
    disease_data = data[data['disease'] == selected_disease]
    available_countries = sorted(disease_data['country'].unique())
    
    # Country selection
    selected_countries = st.sidebar.multiselect(
        "Select Countries/Regions",
        available_countries,
        default=[],
        help="Leave empty to show top affected countries. Select specific countries for forecasting."
    )
    
    # Date range selection
    min_date = disease_data['date'].min().date()
    max_date = disease_data['date'].max().date()
    
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        help=f"Data available from {min_date} to {max_date}"
    )
    
    # Metric selection
    metric_options = {
        'total_cases': 'Total Cases',
        'new_cases': 'Daily New Cases',
        'total_deaths': 'Total Deaths',
        'new_deaths': 'Daily New Deaths'
    }
    
    selected_metric = st.sidebar.selectbox(
        "Select Metric",
        list(metric_options.keys()),
        format_func=lambda x: metric_options[x],
        help="Choose which metric to display and forecast"
    )
    
    # Forecast options
    st.sidebar.markdown("---")
    st.sidebar.header("🔮 Forecast Options")
    
    show_forecast = st.sidebar.checkbox(
        "Enable 6-Month Forecasting",
        value=True,
        help="Show predicted values with confidence intervals"
    )
    
    show_confidence = st.sidebar.checkbox(
        "Show Confidence Intervals",
        value=True,
        disabled=not show_forecast,
        help="Display uncertainty bands around forecasts"
    )
    
    # 2025 Projection option
    project_to_2025 = st.sidebar.checkbox(
        "🕐 Project to 2025",
        value=False,
        help="Show what the epidemic would look like if it happened in 2025"
    )
    
    # Add PyTorch forecasting option
    use_pytorch = st.sidebar.checkbox("Use PyTorch Neural Network (Experimental)", value=False)
    if use_pytorch:
        st.sidebar.info("PyTorch forecasting may take longer to compute but can capture more complex patterns.")
    
    if project_to_2025:
        st.sidebar.warning("⚠️ **Scenario Planning Tool Only**")
        st.sidebar.markdown("""
        **Reliability Level: Medium (5-6/10)**
        
        ✅ **Good for:**
        - Pattern comparison
        - Emergency planning
        - Resource estimation
        
        ❌ **NOT for:**
        - Precise predictions
        - Policy decisions
        - Economic planning
        """)
        
        with st.sidebar.expander("📖 How to Interpret 2025 Projections"):
            st.markdown("""
            **What this shows:**
            - Historical outbreak patterns shifted to 2025 timeline
            - Same progression shapes, different dates
            
            **Major assumptions:**
            - 2025 conditions = historical conditions
            - No healthcare improvements
            - No population immunity changes
            - No pathogen evolution
            
            **Use as:** Emergency drill scenarios, not predictions
            """)
    
    # Filter data
    filtered_data = filter_data(data, selected_disease, selected_countries, date_range)
    
    # Display key metrics
    display_key_metrics(filtered_data, selected_disease, summary)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Time series chart with forecasting
        st.subheader(f"📈 {metric_options[selected_metric]} Trends")
        
        # Add warning banner for 2025 projections
        if project_to_2025:
            st.error("""
            🚨 **SCENARIO PLANNING MODE ACTIVE** 🚨
            
            You are viewing **historical patterns projected to 2025** - this is NOT a prediction!
            
            **Reliability: Medium (5-6/10)** | **Best for: Emergency planning scenarios**
            """)
            
            col_warn1, col_warn2 = st.columns(2)
            with col_warn1:
                st.info("""
                ✅ **Reliable for:**
                - Pattern shape analysis
                - Relative outbreak comparisons  
                - Resource planning estimates
                - Emergency response training
                """)
            with col_warn2:
                st.warning("""
                ❌ **NOT reliable for:**
                - Precise case predictions
                - Exact timeline forecasts
                - Policy recommendations
                - Economic impact planning
                """)
            
            st.markdown("---")
        
        if project_to_2025:
            # 2025 projection mode
            forecast_chart = create_forecast_chart(
                filtered_data, selected_metric, selected_countries, 
                selected_disease, show_forecast, show_confidence, project_to_2025, use_pytorch
            )
        elif show_forecast:
            forecast_chart = create_forecast_chart(
                filtered_data, selected_metric, selected_countries, 
                selected_disease, show_forecast, show_confidence, project_to_2025, use_pytorch
            )
        else:
            forecast_chart = create_time_series_chart(
                filtered_data, selected_metric, selected_countries, selected_disease
            )
        
        st.plotly_chart(forecast_chart, use_container_width=True)
        
        # Add explanation below chart for 2025 mode
        if project_to_2025:
            st.info("""
            💡 **Understanding This Chart:**
            
            The solid lines show how historical epidemic patterns would unfold if they started in January 2025. 
            The dashed lines (if enabled) show 6-month forecasts from the end of those projected patterns.
            
            **Remember:** This assumes 2025 conditions are identical to historical conditions - which is unrealistic!
            Real 2025 outcomes would likely be very different due to improved healthcare, vaccines, and lessons learned.
            """)
        
        # Comparison chart
        st.subheader(f"🏆 Country Comparison")
        comparison_chart = create_comparison_chart(
            filtered_data, selected_metric, selected_countries, selected_disease
        )
        st.plotly_chart(comparison_chart, use_container_width=True)
    
    with col2:
        # Insights panel
        display_insights_panel(filtered_data, selected_disease, selected_countries, selected_metric, project_to_2025, use_pytorch)
        
        # Additional controls and info
        st.markdown("---")
        st.subheader("ℹ️ Data Info")
        
        if selected_disease in metadata:
            disease_info = metadata[selected_disease]
            st.markdown(f"**Countries:** {disease_info['total_records']:,} records")
            st.markdown(f"**Period:** {disease_info['start_date']} to {disease_info['end_date']}")
        
        # Data export
        if st.button("📊 Export Data", use_container_width=True):
            csv = filtered_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{selected_disease}_{selected_metric}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎯 Access Clustering", key="clustering_nav"):
            st.switch_page("pages/Healthcare Access.py")
    
    with col2:
        if st.button("🗺️ Disease Map", key="disease_map_nav"):
            st.switch_page("pages/Disease Map.py")
    
    with col3:
        if st.button("🏠 Home", key="home_nav"):
            st.switch_page("Home.py")

if __name__ == "__main__":
    main() 