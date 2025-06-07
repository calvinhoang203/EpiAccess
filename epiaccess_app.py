# -*- coding: utf-8 -*-
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="EpiAccess: Smarter Public Health Decisions",
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
        cursor: pointer;
        border: 2px solid transparent;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .dashboard-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .dashboard-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .dashboard-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .dashboard-description {
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 1rem;
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
    </style>
    """, unsafe_allow_html=True)

# Hero Section
def hero_section():
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🏥 EpiAccess</div>
        <div class="hero-title">Smarter Public Health Decisions</div>
        <div class="hero-tagline">Track disease trends. Understand access. Improve outcomes.</div>
        <div>
            <button class="cta-button">
                📈 Explore Disease Trends
            </button>
            <button class="cta-button secondary">
                🏥 Compare Healthcare Access
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            <div class="dashboard-icon">🗺️</div>
            <div class="dashboard-title">Disease Map</div>
            <div class="dashboard-description">
                Geographic visualization of disease incidence and risk levels
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗺️ View Disease Map", key="disease_map"):
            st.switch_page("pages/disease_map.py")
    
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
        if st.button("📊 View Epidemic Dashboard", key="epidemic_trends"):
            st.switch_page("pages/epidemic_dashboard.py")
    
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
        if st.button("🏥 View Healthcare Facilities", key="healthcare_facilities"):
            st.switch_page("pages/healthcare_facilities.py")
    
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
        if st.button("🎯 View Access Clustering", key="access_clustering"):
            st.switch_page("pages/access_clustering.py")

# Footer Section
def footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-links">
            <a href="#" class="footer-link">About</a>
            <a href="#" class="footer-link">Resources</a>
            <a href="#" class="footer-link">Contact</a>
            <a href="#" class="footer-link">Language Selector</a>
            <a href="#" class="footer-link">Accessibility Mode</a>
        </div>
        <div class="footer-text">
            © 2025 EpiAccess. Empowering smarter public health decisions through data-driven insights.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Load custom CSS
    load_css()
    
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