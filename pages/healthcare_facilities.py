import streamlit as st

st.set_page_config(
    page_title="Healthcare Facilities - EpiAccess",
    page_icon="🏥",
    layout="wide"
)

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