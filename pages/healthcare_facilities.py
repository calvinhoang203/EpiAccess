import streamlit as st

st.set_page_config(
    page_title="🏥 Healthcare Facilities",
    page_icon="🏥",
    layout="wide"
)

# Add consistent styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main > div {
    padding-top: 2rem;
}

footer {visibility: hidden;}

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

st.title("🏥 Healthcare Facilities Dashboard")
st.markdown("**Facility distribution, capacity, and resource planning**")

st.info("🚧 **Coming Soon!** This dashboard is under development.")

st.markdown("""
This dashboard will feature:
- 🏥 Hospital and clinic locations
- 📊 Capacity and resource utilization
- 🚑 Emergency service coverage
- 📈 Resource allocation optimization
""")

# Navigation
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Back to Home"):
        st.switch_page("epiaccess_app.py")

with col2:
    if st.button("📊 Epidemic Dashboard"):
        st.switch_page("pages/epidemic_dashboard.py")

with col3:
    if st.button("🎯 Access Clustering"):
        st.switch_page("pages/access_clustering.py") 