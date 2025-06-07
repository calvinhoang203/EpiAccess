import streamlit as st

st.set_page_config(
    page_title="Access Clustering - EpiAccess",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Access Clustering Dashboard")
st.markdown("**Healthcare access patterns and equity analysis**")

st.info("🚧 **Coming Soon!** This dashboard is under development.")

st.markdown("""
This dashboard will feature:
- 🎯 Healthcare access clustering analysis
- 📊 Equity and disparity identification
- 🗺️ Access pattern visualization
- 💡 Intervention recommendations
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
    if st.button("🗺️ Disease Map"):
        st.switch_page("pages/disease_map.py") 