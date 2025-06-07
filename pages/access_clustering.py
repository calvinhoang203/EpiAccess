# Healthcare Access Clustering Analysis
# This page analyzes countries based on their healthcare spending patterns
# and economic capacity to identify different healthcare access groups

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
import os
warnings.filterwarnings('ignore')

# Page setup
st.set_page_config(
    page_title="🎯 Access Clustering",
    page_icon="🎯",
    layout="wide"
)

@st.cache_data
def load_health_expenditure_data():
    """
    Load World Bank health expenditure data and prepare it for clustering.
    We use 2020-2022 averages to smooth out pandemic-related volatility.
    """
    try:
        # Read the Excel file with health spending data
        df = pd.read_excel("data/cleaned_health_expenditure.xlsx")
        
        # Define column names for recent years (more stable than single year)
        recent_cols_pct = ['2020 H.E.(% of GDP)', '2021 H.E.(% of GDP)', '2022 H.E.(% of GDP)']
        recent_cols_per_capita = ['2020 H.E. per capita (USD)', '2021 H.E. per capita (USD)', '2022 H.E. per capita (USD)']
        recent_cols_gdp = ['2020 GDP(USD) by mil', '2021 GDP(USD) by mil', '2022 GDP(USD) by mil']
        
        # Start with basic country info
        clustering_data = df[['Country Name', 'Country Code']].copy()
        
        # Calculate 3-year averages for more stable clustering
        # Fix: Convert decimal percentages to actual percentages (0.07 becomes 7%)
        clustering_data['avg_he_pct_gdp'] = df[recent_cols_pct].mean(axis=1) * 100
        
        # Average spending per person in USD
        clustering_data['avg_he_per_capita'] = df[recent_cols_per_capita].mean(axis=1)
        
        # Convert GDP from millions to billions (easier to work with)
        clustering_data['avg_gdp_billions'] = df[recent_cols_gdp].mean(axis=1) / 1000
        
        # Clean up the data - keep countries with health spending info
        initial_count = len(clustering_data)
        clustering_data = clustering_data.dropna(subset=['avg_he_pct_gdp', 'avg_he_per_capita'])
        final_count = len(clustering_data)
        
        # Debug info for troubleshooting
        print(f"Data loaded: {initial_count} countries initially, {final_count} countries after cleaning")
        print(f"Sample data ranges:")
        print(f"Health Exp % GDP: {clustering_data['avg_he_pct_gdp'].min():.1f}% to {clustering_data['avg_he_pct_gdp'].max():.1f}%")
        print(f"Health Exp per capita: ${clustering_data['avg_he_per_capita'].min():.0f} to ${clustering_data['avg_he_per_capita'].max():.0f}")
        
        return clustering_data, df
        
    except Exception as e:
        st.error(f"Error loading health expenditure data: {e}")
        return None, None

def perform_health_access_clustering(data, n_clusters=4):
    """
    Group countries into 4 healthcare access clusters using K-means.
    Each cluster represents a different healthcare access pattern.
    """
    # The three key metrics for healthcare access
    features = ['avg_he_pct_gdp', 'avg_he_per_capita', 'avg_gdp_billions']
    clustering_features = data[features].copy()
    
    # Handle any missing values (use median as sensible default)
    for col in features:
        clustering_features[col] = clustering_features[col].fillna(clustering_features[col].median())
    
    # Standardize all features so they're on the same scale
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(clustering_features)
    
    # Run K-means clustering to find 4 groups
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    data['cluster'] = kmeans.fit_predict(scaled_features)
    
    # Calculate average characteristics of each cluster
    cluster_stats = data.groupby('cluster')[features].mean()
    
    # Give each cluster a meaningful name based on its spending patterns
    cluster_labels = {}
    for cluster_id in range(n_clusters):
        stats = cluster_stats.loc[cluster_id]
        he_per_capita = stats['avg_he_per_capita']
        he_pct_gdp = stats['avg_he_pct_gdp']
        gdp = stats['avg_gdp_billions']
        
        # Label clusters based on spending patterns (thresholds from global data analysis)
        if he_per_capita > 1500 and gdp > 100:  # Rich countries with high absolute spending
            cluster_labels[cluster_id] = "High Access - Advanced Economy"
        elif he_per_capita > 300 and he_pct_gdp > 6.0:  # Good spending with health priority
            cluster_labels[cluster_id] = "Medium-High Access - Developing"
        elif he_pct_gdp > 6.5 and he_per_capita < 400:  # High priority but limited resources
            cluster_labels[cluster_id] = "High Priority - Limited Resources"
        else:  # Lower spending across the board
            cluster_labels[cluster_id] = "Low Access - Resource Constrained"
    
    # Add the cluster names to our data
    data['cluster_label'] = data['cluster'].map(cluster_labels)
    
    # Show what we found (useful for debugging)
    print(f"Cluster distribution:")
    for cluster_id in range(n_clusters):
        cluster_data = data[data['cluster'] == cluster_id]
        label = cluster_labels[cluster_id]
        print(f"  {label}: {len(cluster_data)} countries")
        print(f"    Avg spending/capita: ${cluster_data['avg_he_per_capita'].mean():.0f}")
        print(f"    Avg spending % GDP: {cluster_data['avg_he_pct_gdp'].mean():.1f}%")
    
    return data, cluster_stats, scaler, kmeans

def create_cluster_bar_chart(data, metric, title):
    """Make a bar chart comparing clusters on a specific metric"""
    # Calculate averages and counts for each cluster
    cluster_summary = data.groupby('cluster_label')[metric].agg(['mean', 'count']).reset_index()
    cluster_summary.columns = ['Cluster', 'Average', 'Countries']
    
    # Use consistent colors across all visualizations
    color_map = {
        'High Access - Advanced Economy': '#2ecc71',
        'Medium-High Access - Developing': '#f39c12', 
        'High Priority - Limited Resources': '#3498db',
        'Low Access - Resource Constrained': '#e74c3c'
    }
    
    # Create the bar chart with improved scaling
    fig = px.bar(
        cluster_summary,
        x='Cluster',
        y='Average',
        color='Cluster',
        color_discrete_map=color_map,
        title=title,
        text='Countries'
    )
    
    # Calculate better y-axis range for optimal scaling
    max_val = cluster_summary['Average'].max()
    min_val = cluster_summary['Average'].min()
    
    # Add 20% padding to top for better text visibility
    y_range_top = max_val * 1.25
    
    # Make it look nice with improved scaling
    fig.update_layout(
        title=dict(
            text=title,
            font_size=18,
            x=0.47,
            y=0.95,
            xanchor='center',
            yanchor='top'
        ),
        xaxis_title="Healthcare Access Cluster",
        yaxis_title=metric.replace('_', ' ').title(),
        height=500,  # Increased height for better visibility
        showlegend=False,  # Don't need legend since x-axis shows cluster names
        plot_bgcolor='rgba(248,248,248,0.8)',
        paper_bgcolor='white',
        margin=dict(l=60, r=60, t=100, b=120),  # Better margins for labels
        yaxis=dict(
            range=[0, y_range_top],  # Set optimal range
            gridcolor='lightgray',
            gridwidth=1
        ),
        xaxis=dict(
            tickangle=-35,  # Better angle for readability
            tickfont=dict(size=12),
            automargin=True
        )
    )
    
    # Add country counts on top of bars with better positioning
    fig.update_traces(
        texttemplate='%{text} countries',
        textposition='outside',
        textfont=dict(size=13, color='black', family='Arial'),
        marker=dict(
            line=dict(color='white', width=2)  # Add border for better definition
        ),
        hovertemplate='<b>%{x}</b><br>' +
                     f'{metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                     'Countries: %{text}<br>' +
                     '<extra></extra>'
    )
    
    # Format y-axis appropriately for different metrics
    if 'per_capita' in metric:
        fig.update_yaxes(tickformat='$,.0f')
    elif 'pct_gdp' in metric:
        fig.update_yaxes(tickformat='.1f', title='Health Expenditure (% of GDP)')
    elif 'gdp' in metric:
        fig.update_yaxes(tickformat=',.0f')
    
    return fig

def create_scatter_plot(data, x_metric, y_metric, title):
    """Create scatter plot colored by cluster"""
    fig = px.scatter(
        data,
        x=x_metric,
        y=y_metric,
        color='cluster_label',
        hover_name='Country Name',
        title=title,
        color_discrete_sequence=['#e74c3c', '#f39c12', '#2ecc71', '#3498db'],  # More distinct colors
        size='avg_gdp_billions',  # Size points by GDP for extra dimension
        size_max=15  # Limit maximum size
    )
    
    # Update layout with better formatting
    fig.update_layout(
        title=dict(
            text=title,
            font_size=18,
            x=0.47,
            y=0.92,
            xanchor='center',
            yanchor='top'
        ),
        xaxis_title=x_metric.replace('_', ' ').title(),
        yaxis_title=y_metric.replace('_', ' ').title(),
        height=600,  # Increased height for better visibility
        legend_title="Access Cluster",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1.01,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="rgba(0,0,0,0.2)",
            borderwidth=1
        ),
        plot_bgcolor='rgba(248,248,248,0.8)',  # Light background
        paper_bgcolor='white'
    )
    
    # Update traces for better visibility
    fig.update_traces(
        marker=dict(
            opacity=0.7,  # Add transparency to show overlapping points
            line=dict(width=1, color='white')  # White outline for better separation
        ),
        hovertemplate='<b>%{hovertext}</b><br>' +
                     f'{x_metric.replace("_", " ").title()}: %{{x:,.0f}}<br>' +
                     f'{y_metric.replace("_", " ").title()}: %{{y:,.0f}}<br>' +
                     'Cluster: %{marker.color}<br>' +
                     '<extra></extra>'
    )
    
    # Improve axis formatting
    if x_metric == 'avg_gdp_billions':
        fig.update_xaxes(title='GDP (Billions USD)', tickformat=',.0f')
    elif x_metric == 'avg_he_per_capita':
        fig.update_xaxes(title='Health Expenditure per Capita (USD)', tickformat='$,.0f')
    elif x_metric == 'avg_he_pct_gdp':
        fig.update_xaxes(title='Health Expenditure (% of GDP)', tickformat='.1f')
        
    if y_metric == 'avg_gdp_billions':
        fig.update_yaxes(title='GDP (Billions USD)', tickformat=',.0f')
    elif y_metric == 'avg_he_per_capita':
        fig.update_yaxes(title='Health Expenditure per Capita (USD)', tickformat='$,.0f')
    elif y_metric == 'avg_he_pct_gdp':
        fig.update_yaxes(title='Health Expenditure (% of GDP)', tickformat='.1f')
    
    return fig

def display_cluster_insights(data, cluster_stats):
    """Display insights about each cluster"""
    st.subheader("🔍 Cluster Analysis & Insights")
    
    # Overall statistics
    total_countries = len(data)
    avg_he_per_capita = data['avg_he_per_capita'].mean()
    avg_he_pct_gdp = data['avg_he_pct_gdp'].mean()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total Countries Analyzed",
            f"{total_countries}",
            help="Countries with complete health expenditure data (2020-2022)"
        )
    
    with col2:
        st.metric(
            "Global Avg Health Spending",
            f"${avg_he_per_capita:.0f}",
            help="Average health expenditure per capita across all countries"
        )
    
    with col3:
        st.metric(
            "Global Avg as % of GDP",
            f"{avg_he_pct_gdp:.1f}%",
            help="Average health expenditure as percentage of GDP"
        )
    
    st.markdown("---")
    
    # Detailed cluster insights
    for cluster_id in sorted(data['cluster'].unique()):
        cluster_data = data[data['cluster'] == cluster_id]
        cluster_label = cluster_data['cluster_label'].iloc[0]
        
        # Calculate cluster statistics
        cluster_size = len(cluster_data)
        cluster_he_per_capita = cluster_data['avg_he_per_capita'].mean()
        cluster_he_pct_gdp = cluster_data['avg_he_pct_gdp'].mean()
        cluster_gdp = cluster_data['avg_gdp_billions'].mean()
        
        # Get sample countries
        sample_countries = cluster_data['Country Name'].head(5).tolist()
        countries_text = ", ".join(sample_countries)
        if len(cluster_data) > 5:
            countries_text += f" and {len(cluster_data) - 5} more"
        
        # Color coding for different cluster types
        if "High Access" in cluster_label:
            box_style = "background-color: #e8f5e8; border-left: 4px solid #28a745;"
            icon = "🟢"
        elif "Medium-High" in cluster_label:
            box_style = "background-color: #fff3cd; border-left: 4px solid #ffc107;"
            icon = "🟡"
        elif "High Priority" in cluster_label:
            box_style = "background-color: #e1ecf4; border-left: 4px solid #007bff;"
            icon = "🔵"
        else:
            box_style = "background-color: #f8d7da; border-left: 4px solid #dc3545;"
            icon = "🔴"
        
        st.markdown(f"""
        <div style="{box_style} padding: 15px; margin: 10px 0; border-radius: 5px;">
        <h4 style="margin-top: 0;">{icon} {cluster_label}</h4>
        <p><strong>Countries:</strong> {cluster_size} ({countries_text})</p>
        <p><strong>Avg Health Spending per Capita:</strong> ${cluster_he_per_capita:.0f}</p>
        <p><strong>Avg Health Spending (% GDP):</strong> {cluster_he_pct_gdp:.1f}%</p>
        <p><strong>Avg GDP:</strong> ${cluster_gdp:.0f} billion</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Enhanced header with styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(90deg, #6c5ce7, #a29bfe);
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
        st.title("🔬 Access Clusters")
        st.markdown('<p class="subtitle">View population clusters by healthcare usage and access patterns</p>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📊 Back to Dashboard", use_container_width=True, type="primary"):
            st.switch_page("pages/epidemic_dashboard.py")
    
    # Intro section
    st.markdown("""
    <div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin: 20px 0;">
    <h3 style="color: #2c3e50; margin-top: 0;">🧬 Healthcare Access Clustering Analysis</h3>
    <p style="color: #34495e; font-size: 16px; margin-bottom: 0;">
    We used <strong>data modeling to cluster countries with similar health access patterns</strong> based on:
    </p>
    <ul style="color: #34495e; margin-top: 10px;">
    <li><strong>Health expenditure per capita</strong> - Individual access indicator</li>
    <li><strong>Health expenditure as % of GDP</strong> - National health priority indicator</li>
    <li><strong>Economic capacity (GDP)</strong> - Resource availability indicator</li>
    <li><strong>Recent trends (2020-2022)</strong> - Current patterns including pandemic impact</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    data, raw_data = load_health_expenditure_data()
    
    if data is None:
        st.error("Failed to load health expenditure data.")
        return
    
    # Perform clustering
    with st.spinner("Performing healthcare access clustering analysis..."):
        clustered_data, cluster_stats, scaler, kmeans = perform_health_access_clustering(data)
    
    # Sidebar for filtering
    st.sidebar.header("🎛️ Cluster Analysis Controls")
    
    # Cluster selection
    available_clusters = sorted(clustered_data['cluster_label'].unique())
    selected_clusters = st.sidebar.multiselect(
        "Select Clusters to Compare",
        available_clusters,
        default=available_clusters,
        help="Choose which healthcare access clusters to display and compare"
    )
    
    # Comparison mode
    compare_mode = st.sidebar.checkbox(
        "Compare Multiple Clusters",
        value=True,
        help="Show comparative analysis across selected clusters"
    )
    
    # Filter data based on selection
    if selected_clusters:
        filtered_data = clustered_data[clustered_data['cluster_label'].isin(selected_clusters)]
    else:
        filtered_data = clustered_data
    
    if filtered_data.empty:
        st.warning("No data available for selected clusters.")
        return
    
    # Visualization Section
    st.markdown("---")
    st.subheader("📊 Healthcare Access Cluster Visualizations")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["💰 Health Spending", "🌍 Global Distribution", "📈 Economic Patterns"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Health expenditure per capita by cluster
            fig1 = create_cluster_bar_chart(
                filtered_data, 
                'avg_he_per_capita', 
                'Average Health Expenditure per Capita by Access Cluster'
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Health expenditure as % of GDP by cluster
            fig2 = create_cluster_bar_chart(
                filtered_data, 
                'avg_he_pct_gdp', 
                'Average Health Expenditure (% of GDP) by Access Cluster'
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        # Add controls for better visualization
        col1, col2 = st.columns([3, 1])
        
        with col2:
            st.markdown("**🎛️ Display Options**")
            use_log_scale = st.checkbox(
                "Use Log Scale", 
                value=False,
                help="Apply logarithmic scale to X-axis to better separate clustered data points"
            )
            
            show_cluster_centers = st.checkbox(
                "Show Cluster Centers",
                value=False,
                help="Display cluster center points for reference"
            )
            
            # Add point size control
            point_size_factor = st.slider(
                "Point Size",
                min_value=0.5,
                max_value=3.0,
                value=1.5,
                step=0.1,
                help="Adjust the size of data points for better visibility"
            )
            
            # Add jitter option
            add_jitter = st.checkbox(
                "Add Jitter",
                value=True,
                help="Add small random displacement to reduce point overlap"
            )
        
        with col1:
            # Enhanced scatter plot with better visibility
            data_for_plot = filtered_data.copy()
            
            # Add jitter if selected
            if add_jitter:
                import numpy as np  # Ensure numpy is available
                np.random.seed(42)  # For reproducible jitter
                jitter_x = np.random.normal(0, data_for_plot['avg_he_per_capita'].std() * 0.02, len(data_for_plot))
                jitter_y = np.random.normal(0, data_for_plot['avg_he_pct_gdp'].std() * 0.02, len(data_for_plot))
                data_for_plot['jittered_x'] = data_for_plot['avg_he_per_capita'] + jitter_x
                data_for_plot['jittered_y'] = data_for_plot['avg_he_pct_gdp'] + jitter_y
            else:
                data_for_plot['jittered_x'] = data_for_plot['avg_he_per_capita']
                data_for_plot['jittered_y'] = data_for_plot['avg_he_pct_gdp']
            
            # Create enhanced scatter plot
            fig3 = go.Figure()
            
            # Define enhanced colors for clusters
            cluster_colors = {
                'High Access - Advanced Economy': '#2E8B57',      # Dark green
                'Medium-High Access - Developing': '#FF6B35',     # Orange-red
                'High Priority - Limited Resources': '#4682B4',   # Steel blue
                'Low Access - Resource Constrained': '#DC143C'    # Crimson
            }
            
            # Add traces for each cluster
            for cluster_label in selected_clusters:
                cluster_data = data_for_plot[data_for_plot['cluster_label'] == cluster_label]
                
                # Calculate point sizes based on GDP (larger GDP = larger points)
                gdp_sizes = cluster_data['avg_gdp_billions']
                min_size = 8 * point_size_factor
                max_size = 25 * point_size_factor
                
                # Normalize sizes
                if gdp_sizes.max() > gdp_sizes.min():
                    normalized_sizes = (gdp_sizes - gdp_sizes.min()) / (gdp_sizes.max() - gdp_sizes.min())
                    sizes = min_size + (max_size - min_size) * normalized_sizes
                else:
                    sizes = [min_size] * len(gdp_sizes)
                
                fig3.add_trace(go.Scatter(
                    x=cluster_data['jittered_x'],
                    y=cluster_data['jittered_y'],
                    mode='markers',
                    name=cluster_label,
                    text=cluster_data['Country Name'],
                    hovertemplate='<b>%{text}</b><br>' +
                                 'Health Expenditure per Capita: $%{x:,.0f}<br>' +
                                 'Health Expenditure (% GDP): %{y:.1f}%<br>' +
                                 'GDP: $%{customdata:.0f}B<br>' +
                                 f'Cluster: {cluster_label}<br>' +
                                 '<extra></extra>',
                    customdata=cluster_data['avg_gdp_billions'],
                    marker=dict(
                        size=sizes,
                        color=cluster_colors.get(cluster_label, '#666666'),
                        opacity=0.8,
                        line=dict(width=1.5, color='white'),
                        symbol='circle'
                    )
                ))
            
            # Update layout for better visibility
            fig3.update_layout(
                title={
                    'text': 'Healthcare Access Patterns: Per Capita Spending vs National Priority',
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 16}
                },
                xaxis_title="Health Expenditure per Capita (USD)",
                yaxis_title="Health Expenditure (% of GDP)",
                height=650,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=1.01,
                    bgcolor="rgba(255,255,255,0.9)",
                    bordercolor="rgba(0,0,0,0.3)",
                    borderwidth=1
                ),
                plot_bgcolor='rgba(245,245,245,0.8)',
                paper_bgcolor='white',
                hovermode='closest'
            )
            
            # Apply formatting
            fig3.update_xaxes(
                tickformat='$,.0f',
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                zeroline=False
            )
            fig3.update_yaxes(
                tickformat='.1f',
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                zeroline=False
            )
            
            # Apply log scale if selected
            if use_log_scale:
                fig3.update_xaxes(type="log", title="Health Expenditure per Capita (USD) - Log Scale")
                fig3.update_layout(title_text="Healthcare Access Patterns: Per Capita Spending vs National Priority (Log Scale)")
            
            # Add cluster centers if selected
            if show_cluster_centers:
                for cluster_label in selected_clusters:
                    cluster_data = filtered_data[filtered_data['cluster_label'] == cluster_label]
                    center_x = cluster_data['avg_he_per_capita'].mean()
                    center_y = cluster_data['avg_he_pct_gdp'].mean()
                    
                    fig3.add_trace(go.Scatter(
                        x=[center_x],
                        y=[center_y],
                        mode='markers',
                        marker=dict(
                            size=30, 
                            symbol='diamond-x', 
                            color='black', 
                            line=dict(width=4, color='white')
                        ),
                        name=f'{cluster_label} Center',
                        showlegend=False,
                        hovertemplate=f'<b>{cluster_label} Center</b><br>' +
                                     'Avg Health Exp/Capita: $%{x:,.0f}<br>' +
                                     'Avg Health Exp (% GDP): %{y:.1f}%<br>' +
                                     '<extra></extra>'
                    ))
            
            st.plotly_chart(fig3, use_container_width=True)
        
        # Add summary statistics table
        st.markdown("### 📈 Cluster Summary Statistics")
        
        summary_stats = []
        for cluster_label in selected_clusters:
            cluster_data = filtered_data[filtered_data['cluster_label'] == cluster_label]
            stats = {
                'Cluster': cluster_label,
                'Countries': len(cluster_data),
                'Avg Health Spending/Capita': f"${cluster_data['avg_he_per_capita'].mean():.0f}",
                'Avg Health Spending (% GDP)': f"{cluster_data['avg_he_pct_gdp'].mean():.1f}%",
                'Avg GDP': f"${cluster_data['avg_gdp_billions'].mean():.0f}B",
                'Health Spending Range': f"${cluster_data['avg_he_per_capita'].min():.0f} - ${cluster_data['avg_he_per_capita'].max():.0f}",
                'GDP % Range': f"{cluster_data['avg_he_pct_gdp'].min():.1f}% - {cluster_data['avg_he_pct_gdp'].max():.1f}%"
            }
            summary_stats.append(stats)
        
        if summary_stats:
            summary_df = pd.DataFrame(summary_stats)
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
        
        # Countries by cluster table with better formatting
        st.subheader("🗺️ Countries by Healthcare Access Cluster")
        
        for cluster_label in selected_clusters:
            cluster_countries = filtered_data[filtered_data['cluster_label'] == cluster_label]['Country Name'].tolist()
            cluster_data = filtered_data[filtered_data['cluster_label'] == cluster_label]
            avg_spending = cluster_data['avg_he_per_capita'].mean()
            avg_gdp_pct = cluster_data['avg_he_pct_gdp'].mean()
            
            # Color coding for cluster headers
            if "High Access" in cluster_label:
                color = "#2E8B57"
                bg_color = "rgba(46, 139, 87, 0.1)"
            elif "Medium-High" in cluster_label:
                color = "#FF6B35"
                bg_color = "rgba(255, 107, 53, 0.1)"
            elif "High Priority" in cluster_label:
                color = "#4682B4"
                bg_color = "rgba(70, 130, 180, 0.1)"
            else:
                color = "#DC143C"
                bg_color = "rgba(220, 20, 60, 0.1)"
                
            st.markdown(f"""
            <div style="background-color: {bg_color}; border-left: 4px solid {color}; padding: 15px; margin: 10px 0; border-radius: 5px;">
            <h4 style="color: {color}; margin-top: 0;">{cluster_label}</h4>
            <p><strong>{len(cluster_countries)} Countries</strong> | <strong>Avg Spending:</strong> ${avg_spending:.0f}/capita | <strong>Avg % GDP:</strong> {avg_gdp_pct:.1f}%</p>
            <p style="color: #666; font-style: italic; line-height: 1.6;">{', '.join(cluster_countries)}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        # Enhanced Economic Patterns tab
        col1, col2 = st.columns([3, 1])
        
        with col2:
            st.markdown("**🎛️ Display Options**")
            econ_log_scale = st.checkbox(
                "Use Log Scale (GDP)", 
                value=True,
                help="Apply logarithmic scale to GDP axis for better visualization",
                key="econ_log"
            )
            
            econ_point_size = st.slider(
                "Point Size",
                min_value=0.5,
                max_value=3.0,
                value=1.8,
                step=0.1,
                help="Adjust point size for better visibility",
                key="econ_size"
            )
            
            show_trend_lines = st.checkbox(
                "Show Trend Lines",
                value=False,
                help="Add trend lines for each cluster"
            )
        
        with col1:
            # Create enhanced economic patterns scatter plot
            fig4 = go.Figure()
            
            # Define enhanced colors for clusters
            cluster_colors = {
                'High Access - Advanced Economy': '#2E8B57',      # Dark green
                'Medium-High Access - Developing': '#FF6B35',     # Orange-red
                'High Priority - Limited Resources': '#4682B4',   # Steel blue
                'Low Access - Resource Constrained': '#DC143C'    # Crimson
            }
            
            # Add traces for each cluster with enhanced visibility
            for cluster_label in selected_clusters:
                cluster_data = filtered_data[filtered_data['cluster_label'] == cluster_label]
                
                # Calculate point sizes based on health spending % of GDP
                he_pct_sizes = cluster_data['avg_he_pct_gdp']
                min_size = 10 * econ_point_size
                max_size = 30 * econ_point_size
                
                # Normalize sizes
                if he_pct_sizes.max() > he_pct_sizes.min():
                    normalized_sizes = (he_pct_sizes - he_pct_sizes.min()) / (he_pct_sizes.max() - he_pct_sizes.min())
                    sizes = min_size + (max_size - min_size) * normalized_sizes
                else:
                    sizes = [min_size] * len(he_pct_sizes)
                
                fig4.add_trace(go.Scatter(
                    x=cluster_data['avg_gdp_billions'],
                    y=cluster_data['avg_he_per_capita'],
                    mode='markers',
                    name=cluster_label,
                    text=cluster_data['Country Name'],
                    hovertemplate='<b>%{text}</b><br>' +
                                 'GDP: $%{x:,.0f} billion<br>' +
                                 'Health Expenditure per Capita: $%{y:,.0f}<br>' +
                                 'Health Exp (% GDP): %{customdata:.1f}%<br>' +
                                 f'Cluster: {cluster_label}<br>' +
                                 '<extra></extra>',
                    customdata=cluster_data['avg_he_pct_gdp'],
                    marker=dict(
                        size=sizes,
                        color=cluster_colors.get(cluster_label, '#666666'),
                        opacity=0.8,
                        line=dict(width=2, color='white'),
                        symbol='circle'
                    )
                ))
                
                # Add trend lines if selected
                if show_trend_lines and len(cluster_data) > 2:
                    import numpy as np
                    
                    # Calculate linear regression
                    x_vals = cluster_data['avg_gdp_billions'].values
                    y_vals = cluster_data['avg_he_per_capita'].values
                    
                    # Remove any infinite or NaN values
                    valid_mask = np.isfinite(x_vals) & np.isfinite(y_vals)
                    x_vals = x_vals[valid_mask]
                    y_vals = y_vals[valid_mask]
                    
                    if len(x_vals) > 1:
                        z = np.polyfit(x_vals, y_vals, 1)
                        p = np.poly1d(z)
                        
                        x_trend = np.linspace(x_vals.min(), x_vals.max(), 100)
                        y_trend = p(x_trend)
                        
                        fig4.add_trace(go.Scatter(
                            x=x_trend,
                            y=y_trend,
                            mode='lines',
                            name=f'{cluster_label} Trend',
                            line=dict(
                                color=cluster_colors.get(cluster_label, '#666666'),
                                width=2,
                                dash='dot'
                            ),
                            showlegend=False,
                            hoverinfo='skip'
                        ))
            
            # Update layout
            fig4.update_layout(
                title={
                    'text': 'Economic Capacity vs Healthcare Spending by Access Cluster',
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 16}
                },
                xaxis_title="GDP (Billions USD)",
                yaxis_title="Health Expenditure per Capita (USD)",
                height=650,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=1.01,
                    bgcolor="rgba(255,255,255,0.9)",
                    bordercolor="rgba(0,0,0,0.3)",
                    borderwidth=1
                ),
                plot_bgcolor='rgba(245,245,245,0.8)',
                paper_bgcolor='white',
                hovermode='closest'
            )
            
            # Format axes
            fig4.update_yaxes(
                tickformat='$,.0f',
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                zeroline=False
            )
            
            if econ_log_scale:
                fig4.update_xaxes(
                    type="log",
                    title="GDP (Billions USD) - Log Scale",
                    tickformat=',.0f',
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.1)',
                    zeroline=False
                )
            else:
                fig4.update_xaxes(
                    tickformat=',.0f',
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.1)',
                    zeroline=False
                )
            
            st.plotly_chart(fig4, use_container_width=True)
        
        # Economic insights section
        st.markdown("### 💡 Economic Pattern Insights")
        
        # Calculate correlations and insights
        insights_data = []
        for cluster_label in selected_clusters:
            cluster_data = filtered_data[filtered_data['cluster_label'] == cluster_label]
            
            if len(cluster_data) > 1:
                # Calculate correlation between GDP and health spending per capita
                gdp_he_corr = cluster_data['avg_gdp_billions'].corr(cluster_data['avg_he_per_capita'])
                
                insights_data.append({
                    'Cluster': cluster_label,
                    'Countries': len(cluster_data),
                    'GDP-Health Spending Correlation': f"{gdp_he_corr:.3f}",
                    'Efficiency Ratio': f"{(cluster_data['avg_he_per_capita'] / cluster_data['avg_he_pct_gdp']).mean():.0f}",
                    'Top Spender': cluster_data.loc[cluster_data['avg_he_per_capita'].idxmax(), 'Country Name'],
                    'Most Efficient (% GDP)': cluster_data.loc[cluster_data['avg_he_pct_gdp'].idxmax(), 'Country Name']
                })
        
        if insights_data:
            insights_df = pd.DataFrame(insights_data)
            st.dataframe(insights_df, use_container_width=True, hide_index=True)
            
            # Add explanatory text
            st.markdown("""
            **Key Metrics Explained:**
            - **GDP-Health Spending Correlation**: How strongly economic capacity correlates with health spending in each cluster
            - **Efficiency Ratio**: Average health spending per capita divided by % of GDP (higher = more absolute spending relative to GDP share)
            - **Top Spender**: Country with highest per capita health spending in each cluster
            - **Most Efficient (% GDP)**: Country dedicating the highest percentage of GDP to health in each cluster
            """)
    
    # Display insights
    display_cluster_insights(filtered_data, cluster_stats)
    
    # Data reliability disclaimer
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #fef3c7; border: 1px solid #f59e0b; border-radius: 5px; padding: 15px; margin: 20px 0;">
    <h4 style="color: #92400e; margin-top: 0;">⚠️ Data Usage & Methodology Disclaimer</h4>
    <p style="color: #92400e; margin-bottom: 0;">
    <strong>Clustering methodology:</strong> K-means clustering using standardized health expenditure and economic indicators (2020-2022 averages).<br>
    <strong>Data limitations:</strong> Based on national-level aggregate data; does not capture within-country variations or healthcare quality measures.<br>
    <strong>Intended use:</strong> Educational analysis and policy research only. Not for clinical or individual healthcare decisions.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗺️ Disease Map", use_container_width=True):
            st.switch_page("pages/disease_map.py")
    
    with col2:
        if st.button("🏥 Healthcare Facilities", use_container_width=True):
            st.switch_page("pages/healthcare_facilities.py")
    
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("epiaccess_app.py")

if __name__ == "__main__":
    main()
 