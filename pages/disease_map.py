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
    """Create interactive choropleth map with enhanced styling"""
    
    # Enhanced country code mapping for better map visualization
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
        'Palestine': 'PSE',
        'Taiwan': 'TWN',
        'Hong Kong': 'HKG',
        'Singapore': 'SGP'
    }
    
    # Add ISO codes for better map matching
    country_data['iso_alpha'] = country_data['country'].map(country_code_mapping)
    
    # Choose color scale based on disease type
    disease_colors = {
        'COVID-19': 'OrRd',  # Orange-Red for COVID
        'SARS': 'YlOrRd',    # Yellow-Orange-Red for SARS
        'Monkeypox': 'Purples'  # Purple scale for Monkeypox
    }
    color_scale = disease_colors.get(disease, 'Reds')
    
    # Create the enhanced choropleth map
    fig = px.choropleth(
        country_data,
        locations='iso_alpha',
        color=metric,
        hover_name='country',
        hover_data={
            metric: ':,.0f', 
            'region': True,
            'iso_alpha': False  # Hide ISO code from hover
        },
        color_continuous_scale=color_scale,
        title=title,
        labels={metric: metric.replace('_', ' ').title()}
    )
    
    # Enhanced layout with better styling
    fig.update_layout(
        title=dict(
            text=title, 
            font=dict(size=24, color='#2c3e50', family="Arial Black"),
            x=0.47,  # Center horizontally
            xanchor='center',  # Ensure center anchoring
            y=0.92,  # Adjust vertical position to be more centered over map
            yanchor='top'  # Anchor from top
        ),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="rgb(50, 50, 50)",
            coastlinewidth=0.5,
            showland=True,
            landcolor='rgb(245, 245, 245)',
            showocean=True,
            oceancolor='rgb(240, 248, 255)',
            showlakes=True,
            lakecolor='rgb(240, 248, 255)',
            showcountries=True,
            countrycolor="rgb(200, 200, 200)",
            countrywidth=0.3,
            projection_type='natural earth',  # Better projection
            bgcolor='rgba(0,0,0,0)'  # Transparent background
        ),
        height=650,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
        plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot background
        coloraxis_colorbar=dict(
            title=dict(
                text=metric.replace('_', ' ').title(),
                font=dict(size=14, color='#2c3e50')
            ),
            thicknessmode="pixels",
            thickness=20,
            lenmode="pixels",
            len=400,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgb(200, 200, 200)',
            borderwidth=1,
            tickfont=dict(color='#2c3e50'),
            x=1.02
        ),
        margin=dict(l=0, r=100, t=100, b=20)  # Adjust margins for better title spacing
    )
    
    # Enhanced hover template
    fig.update_traces(
        hovertemplate='<b>%{hovertext}</b><br>' +
                     f'{metric.replace("_", " ").title()}: %{{z:,.0f}}<br>' +
                     'Region: %{customdata[1]}<br>' +
                     '<extra></extra>'
    )
    
    return fig

def create_bubble_map(country_data, disease, metric, title):
    """Create enhanced bubble map as alternative visualization"""
    
    # Expanded coordinates for better coverage
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
        'South Africa': [-30.5595, 22.9375],
        'Australia': [-25.2744, 133.7751],
        'Japan': [36.2048, 138.2529],
        'Argentina': [-38.4161, -63.6167],
        'Mexico': [23.6345, -102.5528],
        'Turkey': [38.9637, 35.2433],
        'Iran': [32.4279, 53.6880],
        'Indonesia': [-0.7893, 113.9213]
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
        # Return styled empty figure
        return go.Figure().add_annotation(
            text="Geographic coordinates not available for selected countries",
            xref="paper", yref="paper", x=0.5, y=0.5,
            showarrow=False, 
            font=dict(size=18, color='#7f8c8d'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgb(200, 200, 200)',
            borderwidth=1
        )
    
    coords_df = pd.DataFrame(coords_data)
    
    # Choose color scale based on disease
    disease_colors = {
        'COVID-19': 'OrRd',
        'SARS': 'YlOrRd',
        'Monkeypox': 'Purples'
    }
    color_scale = disease_colors.get(disease, 'Reds')
    
    # Create enhanced bubble map
    fig = px.scatter_geo(
        coords_df,
        lat='lat',
        lon='lon',
        size=metric,
        color=metric,
        hover_name='country',
        hover_data={
            metric: ':,.0f', 
            'region': True,
            'lat': False,
            'lon': False
        },
        color_continuous_scale=color_scale,
        title=title,
        size_max=60,
        opacity=0.7
    )
    
    # Enhanced bubble map layout
    fig.update_layout(
        title=dict(
            text=title, 
            font=dict(size=24, color='#2c3e50', family="Arial Black"),
            x=0.47,  # Center horizontally
            xanchor='center',  # Ensure center anchoring
            y=0.92,  # Adjust vertical position to be more centered over map
            yanchor='top'  # Anchor from top
        ),
        geo=dict(
            projection_type='natural earth',
            showland=True,
            landcolor='rgb(245, 245, 245)',
            showocean=True,
            oceancolor='rgb(240, 248, 255)',
            showlakes=True,
            lakecolor='rgb(240, 248, 255)',
            showcountries=True,
            countrycolor="rgb(200, 200, 200)",
            countrywidth=0.3,
            showcoastlines=True,
            coastlinecolor="rgb(50, 50, 50)",
            coastlinewidth=0.5,
            bgcolor='rgba(0,0,0,0)'
        ),
        height=650,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        coloraxis_colorbar=dict(
            title=dict(
                text=metric.replace('_', ' ').title(),
                font=dict(size=14, color='#2c3e50')
            ),
            thicknessmode="pixels",
            thickness=20,
            lenmode="pixels",
            len=400,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgb(200, 200, 200)',
            borderwidth=1,
            tickfont=dict(color='#2c3e50'),
            x=1.02
        ),
        margin=dict(l=0, r=100, t=100, b=20)  # Adjust margins for better title spacing
    )
    
    return fig

def display_regional_statistics(country_data, disease, metric):
    """Display enhanced regional statistics with better styling"""
    if country_data.empty:
        return
    
    regional_stats = country_data.groupby('region').agg({
        metric: ['sum', 'count', 'mean']
    }).round(0)
    
    regional_stats.columns = ['Total Cases', 'Countries Affected', 'Average per Country']
    regional_stats = regional_stats.sort_values('Total Cases', ascending=False)
    
    # Enhanced styling with custom CSS
    st.markdown("""
    <style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.subheader(f"📊 Regional Statistics - {disease}")
    st.markdown("---")
    
    # Display as enhanced columns
    regions = regional_stats.index.tolist()
    if len(regions) >= 3:
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        
        for i, region in enumerate(regions[:6]):  # Show top 6 regions
            with cols[i % 3]:
                total = int(regional_stats.loc[region, 'Total Cases'])
                countries = int(regional_stats.loc[region, 'Countries Affected'])
                avg = int(regional_stats.loc[region, 'Average per Country'])
                
                # Enhanced metric display
                st.metric(
                    label=f"🌍 {region}",
                    value=f"{total:,}",
                    delta=f"{countries} countries affected",
                    help=f"Average per country: {avg:,}"
                )

def main():
    # Enhanced header with better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(90deg, #3498db, #2980b9);
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
    }
    .subtitle {
        color: #7f8c8d;
        font-size: 18px;
        text-align: center;
        margin-bottom: 30px;
    }
    .callout-box {
        background-color: #f8f9fa;
        border-left: 4px solid #e74c3c;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }
    .insight-box {
        background-color: #e8f4fd;
        border-left: 4px solid #3498db;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with navigation
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("🗺️ Disease Incidence Map")
        st.markdown('<p class="subtitle">Explore how different regions are affected by disease outbreaks</p>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
        if st.button("📊 Back to Dashboard", use_container_width=True, type="primary"):
            st.switch_page("pages/epidemic_dashboard.py")
    
    # Add user guidance warnings
    st.markdown("""
    <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; padding: 15px; margin: 20px 0;">
    <h4 style="color: #856404; margin-top: 0;">ℹ️ How to Use This Map</h4>
    <ul style="color: #856404; margin-bottom: 0;">
    <li><strong>Start by selecting a disease</strong> from the sidebar to see available data</li>
    <li><strong>Filter by regions/continents</strong> to focus on specific geographic areas</li>
    <li><strong>Choose specific countries</strong> for detailed analysis (optional)</li>
    <li><strong>Select different metrics</strong> to compare cases, deaths, or daily peaks</li>
    <li><strong>Hover over countries</strong> on the map for detailed information</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    data, metadata = load_epidemic_data()
    
    if data is None:
        st.error("Failed to load epidemic data.")
        return
    
    # Enhanced sidebar with better styling
    st.sidebar.markdown("""
    <style>
    .sidebar-header {
        background-color: #34495e;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown('<div class="sidebar-header">🎛️ Map Controls</div>', unsafe_allow_html=True)
    
    # Add sidebar guidance
    st.sidebar.markdown("""
    <div style="background-color: #e1f5fe; border-left: 3px solid #0288d1; padding: 10px; margin: 10px 0; font-size: 0.9em;">
    <strong>💡 Quick Start:</strong><br>
    1. Select a disease<br>
    2. Choose continents/regions (optional)<br>
    3. Pick specific countries (optional)<br>
    4. Select metric to visualize<br>
    <em>Tip: Select 2-3 continents for best comparisons!</em>
    </div>
    """, unsafe_allow_html=True)
    
    # Disease selection
    diseases = sorted(data['disease'].unique())
    selected_disease = st.sidebar.selectbox(
        "Select Disease",
        diseases,
        help="Choose which disease to analyze"
    )
    
    # Get disease-specific data for filtering
    disease_data = data[data['disease'] == selected_disease]
    
    # Show data availability info
    total_countries_for_disease = disease_data['country'].nunique()
    total_regions_for_disease = disease_data['region'].nunique()
    
    st.sidebar.markdown(f"""
    <div style="background-color: #f0f9ff; border: 1px solid #bae6fd; border-radius: 4px; padding: 8px; margin: 5px 0; font-size: 0.85em;">
    📊 <strong>{selected_disease} Data:</strong><br>
    • {total_countries_for_disease} countries<br>
    • {total_regions_for_disease} regions
    </div>
    """, unsafe_allow_html=True)
    
    # Region/Continent filtering (NEW FEATURE)
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🌍 Continental & Regional Filtering**")
    
    available_regions = sorted(disease_data['region'].dropna().unique())
    selected_regions = st.sidebar.multiselect(
        "Select Continents/Regions",
        available_regions,
        default=[],
        help="Filter by specific continents or regions. Leave empty to show all regions. Select 2-3 for best comparative analysis."
    )
    
    # Show region filtering warning with continental context
    if len(available_regions) > 0 and not selected_regions:
        continent_examples = available_regions[:3] if len(available_regions) >= 3 else available_regions
        examples_str = ", ".join(continent_examples)
        st.sidebar.markdown(f"""
        <div style="background-color: #fff7ed; border-left: 3px solid #f97316; padding: 8px; margin: 5px 0; font-size: 0.8em;">
        ℹ️ All continents/regions selected by default<br>
        <em>Try: {examples_str}</em>
        </div>
        """, unsafe_allow_html=True)
    
    # Country filtering (enhanced)
    available_countries = sorted(disease_data['country'].unique())
    if selected_regions:
        # Filter countries by selected regions
        region_filtered_data = disease_data[disease_data['region'].isin(selected_regions)]
        available_countries = sorted(region_filtered_data['country'].unique())
        
        regions_str = " + ".join(selected_regions)
        st.sidebar.markdown(f"""
        <div style="background-color: #f0fdf4; border-left: 3px solid #22c55e; padding: 8px; margin: 5px 0; font-size: 0.8em;">
        ✅ {len(available_countries)} countries available<br>
        <strong>From:</strong> {regions_str}
        </div>
        """, unsafe_allow_html=True)
    
    selected_countries = st.sidebar.multiselect(
        "Select Specific Countries",
        available_countries,
        default=[],
        help="Filter by specific countries within selected regions"
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
    
    # Apply filters
    filtered_data = disease_data.copy()
    if selected_regions:
        filtered_data = filtered_data[filtered_data['region'].isin(selected_regions)]
    if selected_countries:
        filtered_data = filtered_data[filtered_data['country'].isin(selected_countries)]
    
    # Add dynamic warnings based on user selections
    warning_messages = []
    
    if not selected_regions and not selected_countries:
        st.info("💡 **Tip**: Select specific regions or countries from the sidebar to focus your analysis!")
    
    if selected_regions and not selected_countries:
        regions_str = ", ".join(selected_regions)
        st.success(f"🌍 **Filtering by regions**: {regions_str}. Optionally select specific countries for more focused analysis.")
    
    if selected_countries:
        countries_str = ", ".join(selected_countries[:3])
        if len(selected_countries) > 3:
            countries_str += f" and {len(selected_countries) - 3} more"
        st.success(f"🎯 **Focusing on**: {countries_str}")
    
    # Get country data for selected disease and metric
    country_data = get_country_totals(filtered_data, selected_disease, selected_metric)
    
    if country_data.empty:
        st.error("❌ **No Data Available**")
        st.markdown("""
        <div style="background-color: #f8d7da; border: 1px solid #f5c6cb; border-radius: 5px; padding: 15px; margin: 20px 0;">
        <h4 style="color: #721c24; margin-top: 0;">🚨 No Data Found</h4>
        <p style="color: #721c24; margin-bottom: 0;">
        No data available for <strong>{disease}</strong> - <strong>{metric}</strong> with your current filter selections.<br>
        <strong>Try:</strong>
        </p>
        <ul style="color: #721c24; margin-bottom: 0;">
        <li>Selecting different regions or clearing region filters</li>
        <li>Choosing a different disease from the sidebar</li>
        <li>Selecting a different metric (total cases, deaths, etc.)</li>
        <li>Clearing country filters to see all available data</li>
        </ul>
        </div>
        """.format(disease=selected_disease, metric=metric_options[selected_metric]), unsafe_allow_html=True)
        return
    
    # Warning about data limitations
    total_filtered_countries = len(country_data)
    if total_filtered_countries < 5:
        st.warning(f"⚠️ **Limited Data**: Only {total_filtered_countries} countries have data for your current selection. Consider broadening your filters for more comprehensive analysis.")
    
    # Enhanced callout section with insights (NEW FEATURE)
    st.markdown("---")
    
    # Color coding explanation
    max_cases = country_data[selected_metric].max()
    median_cases = country_data[selected_metric].median()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="callout-box">
        <h4>🎨 Color Legend</h4>
        <p><strong>Darkest Red:</strong> Highest case counts ({max_cases:,.0f})</p>
        <p><strong>Medium Red:</strong> Above median ({median_cases:,.0f}+)</p>
        <p><strong>Light Colors:</strong> Below median cases</p>
        <p><strong>Gray:</strong> No reported cases or insufficient data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Basic insight summary
        top_country = country_data.loc[country_data[selected_metric].idxmax(), 'country']
        top_cases = country_data[selected_metric].max()
        total_countries = len(country_data)
        total_cases = country_data[selected_metric].sum()
        
        st.markdown(f"""
        <div class="insight-box">
        <h4>📊 Key Insights</h4>
        <p><strong>Most Affected:</strong> {top_country} ({top_cases:,.0f} cases)</p>
        <p><strong>Countries with Data:</strong> {total_countries}</p>
        <p><strong>Total Across Region:</strong> {total_cases:,.0f}</p>
        <p><strong>Average per Country:</strong> {total_cases/total_countries:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display map
    st.subheader(f"🌍 {selected_disease} - {metric_options[selected_metric]} Distribution")
    
    title = f"{selected_disease}: {metric_options[selected_metric]} by Country"
    
    if map_type == "Choropleth":
        fig = create_choropleth_map(country_data, selected_disease, selected_metric, title)
    else:
        fig = create_bubble_map(country_data, selected_disease, selected_metric, title)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced interpretation guide (NEW FEATURE)
    st.markdown(f"""
    <div class="insight-box">
    <h4>📖 How to Interpret This Map</h4>
    <ul>
    <li><strong>Hover over countries</strong> to see exact case numbers and regional classification</li>
    <li><strong>Darker colors</strong> indicate higher case counts relative to other countries</li>
    <li><strong>Geographic clustering</strong> may indicate transmission patterns or reporting similarities</li>
    <li><strong>Missing data</strong> appears as gray - this could mean no cases or insufficient reporting</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Display regional statistics
    display_regional_statistics(country_data, selected_disease, selected_metric)
    
    # Add warning about regional statistics requirements
    total_countries = len(country_data)
    unique_regions = country_data['region'].nunique()
    region_list = sorted(country_data['region'].unique())
    
    if total_countries < 3:
        st.markdown("""
        <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; padding: 15px; margin: 15px 0;">
        <h4 style="color: #856404; margin-top: 0;">ℹ️ Regional Statistics Notice</h4>
        <p style="color: #856404; margin-bottom: 0;">
        <strong>Need more countries for meaningful regional/continental analysis.</strong><br>
        Regional statistics work best with <strong>at least 3-5 countries</strong> from different continents or regions.
        </p>
        <p style="color: #856404; margin-bottom: 0; margin-top: 10px;">
        <strong>Current selection:</strong> {countries} countries from {regions} continents/regions<br>
        <strong>Try:</strong> Expanding your continent/region selection or choosing a different disease with more data coverage.
        </p>
        </div>
        """.format(countries=total_countries, regions=unique_regions), unsafe_allow_html=True)
    elif unique_regions < 2:
        region_name = region_list[0] if region_list else "selected region"
        st.markdown("""
        <div style="background-color: #e1f5fe; border: 1px solid #81d4fa; border-radius: 5px; padding: 15px; margin: 15px 0;">
        <h4 style="color: #0277bd; margin-top: 0;">💡 Continental Comparison Tip</h4>
        <p style="color: #0277bd; margin-bottom: 0;">
        You're viewing data from <strong>{region_name}</strong> with <strong>{countries} countries</strong>.<br>
        For continental/regional <em>comparisons</em>, try selecting multiple continents/regions from the sidebar.<br>
        <em>Example: Compare Asia + Europe + Africa for global perspective</em>
        </p>
        </div>
        """.format(countries=total_countries, region_name=region_name), unsafe_allow_html=True)
    elif unique_regions < 3:
        regions_str = " + ".join(region_list)
        st.markdown("""
        <div style="background-color: #fff7ed; border: 1px solid #fed7aa; border-radius: 5px; padding: 15px; margin: 15px 0;">
        <h4 style="color: #c2410c; margin-top: 0;">📊 Good Continental Coverage</h4>
        <p style="color: #c2410c; margin-bottom: 0;">
        <strong>Comparing:</strong> {regions_str} ({countries} countries)<br>
        This is good for <strong>regional comparison</strong>! For broader global analysis, consider adding more continents.
        </p>
        </div>
        """.format(countries=total_countries, regions_str=regions_str), unsafe_allow_html=True)
    else:
        regions_str = ", ".join(region_list)
        st.markdown("""
        <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 5px; padding: 15px; margin: 15px 0;">
        <h4 style="color: #166534; margin-top: 0;">🌍 Excellent Global Coverage</h4>
        <p style="color: #166534; margin-bottom: 0;">
        <strong>Analyzing:</strong> {countries} countries across {regions} continents/regions<br>
        <strong>Continents:</strong> {regions_str}<br>
        ✅ Perfect for comprehensive <strong>global continental analysis</strong>!
        </p>
        </div>
        """.format(countries=total_countries, regions=unique_regions, regions_str=regions_str), unsafe_allow_html=True)
    
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
    
    # Add reliability disclaimer
    st.markdown("""
    <div style="background-color: #fef3c7; border: 1px solid #f59e0b; border-radius: 5px; padding: 15px; margin: 20px 0;">
    <h4 style="color: #92400e; margin-top: 0;">⚠️ Data Usage Disclaimer</h4>
    <p style="color: #92400e; margin-bottom: 0;">
    <strong>For educational and research purposes only.</strong> This visualization uses historical epidemic data and should not be used for:
    </p>
    <ul style="color: #92400e; margin-bottom: 0;">
    <li>Current health decision making</li>
    <li>Real-time outbreak monitoring</li>
    <li>Clinical or policy guidance</li>
    </ul>
    <p style="color: #92400e; margin-bottom: 0; margin-top: 10px;">
    Always consult official health authorities and current medical sources for up-to-date information.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
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