# -*- coding: utf-8 -*-
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="🏥 EpiAccess",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional healthcare theme
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main > div {
        padding-top: 2rem;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit elements (keep header for deploy button) */
    footer {visibility: hidden;}
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-tagline {
        font-size: 1.5rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 2.5rem;
        font-weight: 400;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(45deg, #2563eb, #3b82f6);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        margin: 0 1rem;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.6);
        text-decoration: none;
        color: white;
    }
    
    .cta-button.secondary {
        background: linear-gradient(45deg, #10b981, #059669);
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
    
    .cta-button.secondary:hover {
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.6);
    }
    
    /* Hero Button Styling - Production Safe */
    button[kind="primary"] {
        background: linear-gradient(45deg, #2563eb, #3b82f6) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4) !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        height: 3rem !important;
    }
    
    button[kind="secondary"] {
        background: linear-gradient(45deg, #10b981, #059669) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4) !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        height: 3rem !important;
    }
    
    button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.6) !important;
    }
    
    button[kind="secondary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.6) !important;
    }
    
    /* Default button styling for Disease Map */
    button:not([kind]) {
        background: linear-gradient(45deg, #f59e0b, #d97706) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4) !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        height: 3rem !important;
    }
    
    button:not([kind]):hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.6) !important;
    }
    
    /* More specific targeting for Disease Map button */
    button[data-testid*="map_btn"],
    div[data-testid*="map"] button,
    .stButton button:nth-of-type(2) {
        background: linear-gradient(45deg, #e97444, #dc2626) !important;
        box-shadow: 0 4px 15px rgba(233, 116, 68, 0.4) !important;
    }
    
    button[data-testid*="map_btn"]:hover,
    div[data-testid*="map"] button:hover,
    .stButton button:nth-of-type(2):hover {
        box-shadow: 0 8px 25px rgba(233, 116, 68, 0.6) !important;
    }
    
    /* Target Disease Map button through container */
    .map-button-container button {
        background: linear-gradient(45deg, #8b5cf6, #7c3aed) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4) !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        height: 3rem !important;
    }
    
    .map-button-container button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6) !important;
    }
    
    /* Center buttons in their columns */
    .stButton {
        display: flex !important;
        justify-content: center !important;
    }
    
    .stButton > button {
        width: auto !important;
        margin: 0 auto !important;
    }
    
    /* Light Mode Warning Banner */
    .warning-banner {
        background: linear-gradient(45deg, #f3f4f6, #e5e7eb);
        color: #4b5563;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        margin: 1rem auto;
        max-width: 600px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #d1d5db;
        animation: fadeInOut 6s ease-in-out forwards;
    }
    
    @keyframes fadeInOut {
        0% {
            opacity: 0;
            transform: translateY(-10px);
            height: 0;
            margin: 0;
            padding: 0;
        }
        5% {
            height: auto;
            margin: 1rem auto;
            padding: 0.75rem 1.5rem;
        }
        10% {
            opacity: 1;
            transform: translateY(0);
        }
        80% {
            opacity: 1;
            transform: translateY(0);
        }
        95% {
            opacity: 0;
            transform: translateY(-10px);
            height: auto;
            margin: 1rem auto;
            padding: 0.75rem 1.5rem;
        }
        100% {
            opacity: 0;
            transform: translateY(-10px);
            visibility: hidden;
            height: 0;
            margin: 0;
            padding: 0;
        }
    }
    
    .warning-title {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        color: #6b7280;
    }
    
    .warning-text {
        font-size: 0.9rem;
        line-height: 1.4;
        color: #6b7280;
    }
    
    .warning-steps {
        margin-top: 0.25rem;
        font-weight: 400;
        font-style: italic;
        font-size: 0.85rem;
        color: #9ca3af;
    }
    
    /* Zoom Level Warning Banner */
    .zoom-warning-banner {
        background: linear-gradient(45deg, #f3f4f6, #e5e7eb);
        color: #4b5563;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        margin: 0.5rem auto;
        max-width: 600px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #d1d5db;
        animation: fadeInOutDelayed 6s ease-in-out forwards;
    }
    
    @keyframes fadeInOutDelayed {
        0% {
            opacity: 0;
            transform: translateY(-10px);
            height: 0;
            margin: 0;
            padding: 0;
        }
        5% {
            height: auto;
            margin: 0.5rem auto;
            padding: 0.75rem 1.5rem;
        }
        10% {
            opacity: 1;
            transform: translateY(0);
        }
        80% {
            opacity: 1;
            transform: translateY(0);
        }
        95% {
            opacity: 0;
            transform: translateY(-10px);
            height: auto;
            margin: 0.5rem auto;
            padding: 0.75rem 1.5rem;
        }
        100% {
            opacity: 0;
            transform: translateY(-10px);
            visibility: hidden;
            height: 0;
            margin: 0;
            padding: 0;
        }
    }
    
    .zoom-warning-title {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        color: #6b7280;
    }
    
    .zoom-warning-text {
        font-size: 0.9rem;
        line-height: 1.4;
        color: #6b7280;
    }
    
    .zoom-warning-steps {
        margin-top: 0.25rem;
        font-weight: 400;
        font-style: italic;
        font-size: 0.85rem;
        color: #9ca3af;
    }
    
    /* Value Proposition Cards */
    .value-card {
        background: white;
        padding: 2.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(226, 232, 240, 0.8);
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .value-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .value-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
    }
    
    .value-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    .value-description {
        color: #6b7280;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* How It Works Section */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        color: #1f2937;
        margin-bottom: 3rem;
    }
    
    .step-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .step-card:hover {
        border-color: #3b82f6;
        transform: scale(1.02);
    }
    
    .step-number {
        background: linear-gradient(45deg, #3b82f6, #2563eb);
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.5rem;
        margin: 0 auto 1rem auto;
    }
    
    .step-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .step-description {
        color: #6b7280;
        font-size: 0.95rem;
    }
    
    /* Featured Dashboards */
    .dashboard-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 2px solid transparent;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .dashboard-card:hover {
        border-color: #3b82f6;
        transform: scale(1.02);
    }
    
    .dashboard-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .dashboard-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    .dashboard-description {
        color: #6b7280;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    .preview-button {
        background: linear-gradient(45deg, #f59e0b, #d97706);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .preview-button:hover {
        transform: scale(1.05);
    }
    
    /* Footer */
    .footer {
        background: #1f2937;
        color: white;
        padding: 3rem 2rem 2rem 2rem;
        border-radius: 20px 20px 0 0;
        margin-top: 4rem;
        text-align: center;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .footer-link {
        color: #d1d5db;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer-link:hover {
        color: white;
        text-decoration: none;
    }
    
    .footer-text {
        color: #9ca3af;
        font-size: 0.9rem;
    }
    
    /* Style About button to match footer links perfectly */
    .footer .stButton > button {
        background: transparent !important;
        border: none !important;
        color: #d1d5db !important;
        text-decoration: none !important;
        transition: color 0.3s ease !important;
        font-size: 1rem !important;
        padding: 0 !important;
        height: auto !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }
    
    .footer .stButton > button:hover {
        background: transparent !important;
        color: white !important;
        border: none !important;
        text-decoration: none !important;
        transform: none !important;
    }
    
    .footer .stButton > button:focus {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    .footer .stButton > button:active {
        background: transparent !important;
        border: none !important;
        color: white !important;
        transform: none !important;
    }
    
    .footer .stButton {
        display: inline !important;
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

# Light Mode Warning Banner
def light_mode_warning():
    st.markdown("""
    <div class="warning-banner">
        <div class="warning-title">
            ⚠️ Light Mode Required
        </div>
        <div class="warning-text">
            This application is optimized for light mode. For the best experience, please switch to light mode.
        </div>
        <div class="warning-steps">
            Instructions: Click the three dots (⋮) at the top right → Settings → Change "App theme" to "Light"
        </div>
    </div>
    """, unsafe_allow_html=True)

# Zoom Level Warning Banner
def zoom_warning():
    st.markdown("""
    <div class="zoom-warning-banner">
        <div class="zoom-warning-title">
            🔍 100% Zoom Required
        </div>
        <div class="zoom-warning-text">
            This application is designed for 100% browser zoom. Layout may break at other zoom levels.
        </div>
        <div class="zoom-warning-steps">
            Press Ctrl+0 (Cmd+0 on Mac) to reset zoom to 100%, or use browser zoom controls
        </div>
    </div>
    """, unsafe_allow_html=True)

# Hero Section
def hero_section():
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🏥 EpiAccess</div>
        <div class="hero-title">Smarter Public Health Decisions</div>
        <div class="hero-tagline">Track disease trends. Understand access. Improve outcomes.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Three-button centered layout
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1.2, 0.3, 1.2, 0.3, 1.2, 1])
    
    with col2:
        # Custom HTML button for Disease Trends with inline styling
        st.markdown("""
        <div style="display: flex; justify-content: center;">
            <button onclick="window.location.href='?page=epidemic_dashboard'" style="
                background: linear-gradient(45deg, #2563eb, #3b82f6);
                color: white;
                border: none;
                padding: 0.75rem 2rem;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1rem;
                box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
                transition: all 0.3s ease;
                font-family: 'Inter', sans-serif;
                height: 3rem;
                cursor: pointer;
                white-space: nowrap;
            " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 25px rgba(37, 99, 235, 0.6)';" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(37, 99, 235, 0.4)';">
                📈 Explore Disease Trends
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if this button was clicked using query params
        if st.query_params.get("page") == "epidemic_dashboard":
            st.switch_page("pages/epidemic_dashboard.py")

    with col4:
        # Custom HTML button for Disease Map with inline styling
        st.markdown("""
        <div style="display: flex; justify-content: center;">
            <button onclick="window.location.href='?page=disease_map'" style="
                background: linear-gradient(45deg, #8b5cf6, #7c3aed);
                color: white;
                border: none;
                padding: 0.75rem 2rem;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1rem;
                box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
                transition: all 0.3s ease;
                font-family: 'Inter', sans-serif;
                height: 3rem;
                cursor: pointer;
                white-space: nowrap;
            " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 25px rgba(139, 92, 246, 0.6)';" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(139, 92, 246, 0.4)';">
                🌍 View Disease Map
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if this button was clicked using query params
        if st.query_params.get("page") == "disease_map":
            st.switch_page("pages/disease_map.py")
    
    with col6:
        # Custom HTML button for Healthcare Access with inline styling
        st.markdown("""
        <div style="display: flex; justify-content: center;">
            <button onclick="window.location.href='?page=access_clustering'" style="
                background: linear-gradient(45deg, #10b981, #059669);
                color: white;
                border: none;
                padding: 0.75rem 2rem;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1rem;
                box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
                transition: all 0.3s ease;
                font-family: 'Inter', sans-serif;
                height: 3rem;
                cursor: pointer;
                white-space: nowrap;
            " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 25px rgba(16, 185, 129, 0.6)';" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(16, 185, 129, 0.4)';">
                🏥 Compare Healthcare Access
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if this button was clicked using query params
        if st.query_params.get("page") == "access_clustering":
            st.switch_page("pages/access_clustering.py")

# Value Proposition Section
def value_proposition():
    st.markdown('<div class="section-title">Why Choose EpiAccess?</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="value-card">
            <div class="value-icon">📈</div>
            <div class="value-title">Real-time Epidemic Forecasting</div>
            <div class="value-description">
                Advanced analytics and machine learning models predict disease outbreaks 
                and trends to help you stay ahead of public health challenges.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="value-card">
            <div class="value-icon">🏥</div>
            <div class="value-title">Health Access Insights</div>
            <div class="value-description">
                Clustering algorithms reveal healthcare access patterns and inequities, 
                enabling targeted interventions for underserved populations.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="value-card">
            <div class="value-icon">🗺️</div>
            <div class="value-title">Facility Visibility & Planning</div>
            <div class="value-description">
                Interactive maps and resource allocation tools help optimize healthcare 
                infrastructure and improve service delivery.
            </div>
        </div>
        """, unsafe_allow_html=True)

# How It Works Section
def how_it_works():
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">Select a Region</div>
            <div class="step-description">
                Choose your area of interest - from global views to local communities
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">View Analysis</div>
            <div class="step-description">
                Explore disease trends, access patterns, and facility distributions
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">Take Action</div>
            <div class="step-description">
                Use insights to make informed decisions and improve health outcomes
            </div>
        </div>
        """, unsafe_allow_html=True)

# Featured Dashboards Section
def featured_dashboards():
    st.markdown('<div class="section-title">Featured Dashboards</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-icon">🌍</div>
            <div class="dashboard-title">Disease Map</div>
            <div class="dashboard-description">
                Geographic visualization of disease incidence and risk levels
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-icon">📊</div>
            <div class="dashboard-title">Epidemic Trends</div>
            <div class="dashboard-description">
                Forecasting and trend analysis for disease outbreaks
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-icon">🏢</div>
            <div class="dashboard-title">Healthcare Facilities</div>
            <div class="dashboard-description">
                Facility distribution, capacity, and resource planning
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-icon">🎯</div>
            <div class="dashboard-title">Access Clustering</div>
            <div class="dashboard-description">
                Healthcare access patterns and equity analysis
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer Section
def footer():
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding: 2rem; color: #6b7280;">
        © 2025 EpiAccess. Empowering smarter public health decisions through data-driven insights.
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Load custom CSS
    load_css()
    
    # Light mode compatibility warning
    light_mode_warning()
    
    # Zoom level warning
    zoom_warning()
    
    # Landing Page Sections
    hero_section()
    
    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    value_proposition()
    
    # Add spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    how_it_works()
    
    # Add spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    featured_dashboards()
    
    # Footer
    footer()

if __name__ == "__main__":
    main() 