import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from datetime import datetime
import numpy as np

# Set page config
st.set_page_config(
    page_title="Disease Map - EpiAccess",
    page_icon="🗺️",
    layout="wide"
)

@st.cache_data
def load_epidemic_data():
    """Load processed epidemic data"""
    try:
        data = pd.read_csv("data/processed/unified_epidemic_data.csv")
        data['date'] = pd.to_datetime(data['date'])
        
        with open("data/processed/disease_metadata.json", "r") as f:
            metadata = json.load(f)
            
        return data, metadata
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

def get_country_totals(data, disease, metric='total_cases'):
    """Get latest totals by country for mapping"""
    disease_data = data[data['disease'] == disease]
    
    # Get the latest data for each country
    latest_data = disease_data.groupby('country').agg({
        'date': 'max',
        metric: 'max',
        'region': 'last'
    }).reset_index()
    
    # Filter out countries with zero cases
    latest_data = latest_data[latest_data[metric] > 0]
    
    return latest_data

def create_choropleth_map(country_data, disease, metric, title):
    """Create interactive choropleth map"""
    
    # Country code mapping for better map visualization
    country_code_mapping = {
        'United States': 'USA',
        'United Kingdom': 'GBR',
        'Russia': 'RUS',
        'China': 'CHN',
        'South Korea': 'KOR',
        'Iran': 'IRN',
        'Bolivia': 'BOL',
        'Venezuela': 'VEN',
        'Syria': 'SYR',
        'Vietnam': 'VNM',
        'Laos': 'LAO',
        'Moldova': 'MDA',
        'North Macedonia': 'MKD',
        'Tanzania': 'TZA',
        'Democratic Republic of Congo': 'COD',
        'Republic of Congo': 'COG',
        'Ivory Coast': 'CIV',
        'Brunei': 'BRN',
        'East Timor': 'TLS',
        'Palestine': 'PSE'
    }
    
    # Add ISO codes for better map matching
    country_data['iso_alpha'] = country_data['country'].map(country_code_mapping)
    
    # Create the choropleth map
    fig = px.choropleth(
        country_data,
        locations='iso_alpha',
        color=metric,
        hover_name='country',
        hover_data={metric: ':,.0f', 'region': True},
        color_continuous_scale='Reds',
        title=title,
        labels={metric: metric.replace('_', ' ').title()}
    )
    
    # Update layout
    fig.update_layout(
        title=dict(text=title, font_size=20, x=0.5),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            showland=True,
            landcolor='rgb(217, 217, 217)',
            showocean=True,
            oceancolor='rgb(230, 245, 255)',
            projection_type='equirectangular'
        ),
        height=600,
        coloraxis_colorbar=dict(
            title=metric.replace('_', ' ').title(),
            thicknessmode="pixels",
            thickness=15,
            lenmode="pixels",
            len=300
        )
    )
    
    return fig

def create_bubble_map(country_data, disease, metric, title):
    """Create bubble map as alternative visualization"""
    
    # Approximate coordinates for major countries (simplified)
    country_coords = {
        'United States': [39.8283, -98.5795],
        'Brazil': [-14.2350, -51.9253],
        'India': [20.5937, 78.9629],
        'China': [35.8617, 104.1954],
        'Russia': [61.5240, 105.3188],
        'United Kingdom': [55.3781, -3.4360],
        'Germany': [51.1657, 10.4515],
        'France': [46.6034, 1.8883],
        'Italy': [41.8719, 12.5674],
        'Spain': [40.4637, -3.7492],
        'Canada': [56.1304, -106.3468],
        'Nigeria': [9.0820, 8.6753],
        'South Africa': [-30.5595, 22.9375]
    }
    
    # Add coordinates to data
    coords_data = []
    for _, row in country_data.iterrows():
        country = row['country']
        if country in country_coords:
            coords_data.append({
                'country': country,
                'lat': country_coords[country][0],
                'lon': country_coords[country][1],
                metric: row[metric],
                'region': row['region']
            })
    
    if not coords_data:
        # Return empty figure if no coordinate data
        return go.Figure().add_annotation(
            text="Geographic coordinates not available",
            xref="paper", yref="paper", x=0.5, y=0.5,
            showarrow=False, font_size=16
        )
    
    coords_df = pd.DataFrame(coords_data)
    
    # Create bubble map
    fig = px.scatter_geo(
        coords_df,
        lat='lat',
        lon='lon',
        size=metric,
        color=metric,
        hover_name='country',
        hover_data={metric: ':,.0f', 'region': True},
        color_continuous_scale='Reds',
        title=title,
        size_max=50
    )
    
    fig.update_layout(
        title=dict(text=title, font_size=20, x=0.5),
        geo=dict(
            projection_type='natural earth',
            showland=True,
            landcolor='rgb(217, 217, 217)',
            showocean=True,
            oceancolor='rgb(230, 245, 255)'
        ),
        height=600
    )
    
    return fig

def display_regional_statistics(country_data, disease, metric):
    """Display statistics by region"""
    if country_data.empty:
        return
    
    regional_stats = country_data.groupby('region').agg({
        metric: ['sum', 'count', 'mean']
    }).round(0)
    
    regional_stats.columns = ['Total Cases', 'Countries Affected', 'Average per Country']
    regional_stats = regional_stats.sort_values('Total Cases', ascending=False)
    
    st.subheader(f"📊 Regional Statistics - {disease}")
    
    # Display as columns for better layout
    regions = regional_stats.index.tolist()
    if len(regions) >= 3:
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        
        for i, region in enumerate(regions[:6]):  # Show top 6 regions
            with cols[i % 3]:
                total = int(regional_stats.loc[region, 'Total Cases'])
                countries = int(regional_stats.loc[region, 'Countries Affected'])
                st.metric(
                    f"{region}",
                    f"{total:,}",
                    delta=f"{countries} countries"
                )

def main():
    # Header with navigation
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("🗺️ Disease Distribution Map")
        st.markdown("**Visualize current epidemic case distribution worldwide**")
    
    with col2:
        if st.button("📊 Back to Dashboard", use_container_width=True):
            st.switch_page("pages/epidemic_dashboard.py")
    
    # Load data
    data, metadata = load_epidemic_data()
    
    if data is None:
        st.error("Failed to load epidemic data.")
        return
    
    # Sidebar filters
    st.sidebar.header("🎛️ Map Controls")
    
    # Disease selection
    diseases = sorted(data['disease'].unique())
    selected_disease = st.sidebar.selectbox(
        "Select Disease",
        diseases,
        help="Choose which disease to map"
    )
    
    # Metric selection
    metric_options = {
        'total_cases': 'Total Cases',
        'total_deaths': 'Total Deaths',
        'new_cases': 'Peak Daily Cases',
        'new_deaths': 'Peak Daily Deaths'
    }
    
    selected_metric = st.sidebar.selectbox(
        "Select Metric",
        list(metric_options.keys()),
        format_func=lambda x: metric_options[x],
        help="Choose what to visualize on the map"
    )
    
    # Map type selection
    map_type = st.sidebar.radio(
        "Map Type",
        ["Choropleth", "Bubble Map"],
        help="Choose visualization style"
    )
    
    # Get country data for selected disease and metric
    country_data = get_country_totals(data, selected_disease, selected_metric)
    
    if country_data.empty:
        st.warning(f"No data available for {selected_disease} - {metric_options[selected_metric]}")
        return
    
    # Display map
    st.subheader(f"🌍 {selected_disease} - {metric_options[selected_metric]} Distribution")
    
    title = f"{selected_disease}: {metric_options[selected_metric]} by Country"
    
    if map_type == "Choropleth":
        fig = create_choropleth_map(country_data, selected_disease, selected_metric, title)
    else:
        fig = create_bubble_map(country_data, selected_disease, selected_metric, title)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display regional statistics
    display_regional_statistics(country_data, selected_disease, selected_metric)
    
    # Top affected countries table
    st.subheader(f"📈 Top Affected Countries - {selected_disease}")
    
    top_countries = country_data.nlargest(10, selected_metric)[
        ['country', selected_metric, 'region']
    ].copy()
    
    top_countries.columns = ['Country', metric_options[selected_metric], 'Region']
    top_countries[metric_options[selected_metric]] = top_countries[metric_options[selected_metric]].apply(
        lambda x: f"{x:,.0f}"
    )
    
    st.dataframe(
        top_countries,
        use_container_width=True,
        hide_index=True
    )
    
    # Additional navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏥 Healthcare Facilities", use_container_width=True):
            st.switch_page("pages/healthcare_facilities.py")
    
    with col2:
        if st.button("🔬 Access Clustering", use_container_width=True):
            st.switch_page("pages/access_clustering.py")
    
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("epiaccess_app.py")

if __name__ == "__main__":
    main() 