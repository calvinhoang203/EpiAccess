# About EpiAccess - Smarter Public Health Decisions
import streamlit as st
import base64
import os

st.set_page_config(
    page_title="ℹ️ About",
    page_icon="ℹ️",
    layout="wide"
)

def load_about_css():
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

    .about-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .about-title {
        font-size: 3rem;
        font-weight: 700;
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    .about-subtitle {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.9);
        font-weight: 400;
    }
    
    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .mission-card {
        background: white;
        padding: 3rem 2.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 3rem;
        border-left: 6px solid #3b82f6;
    }
    
    .mission-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    
    .target-users {
        background: linear-gradient(45deg, #f0f9ff, #e0f2fe);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
    }
    
    .target-title {
        font-weight: 600;
        color: #1e40af;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    .user-list {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        padding: 0;
        margin: 0;
    }
    
    .user-item {
        background: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        color: #374151;
        font-weight: 500;
        font-size: 1rem;
        border-left: 4px solid #3b82f6;
        transition: all 0.3s ease;
    }
    
    .user-item:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
        border-left-color: #2563eb;
    }
    
    .dataset-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .dataset-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        border-color: #10b981;
    }
    
    .dataset-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
        min-height: 1.8rem;
    }
    
    .dataset-description {
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        flex-grow: 1;
        font-size: 0.95rem;
    }
    
    .dataset-meta {
        display: flex;
        gap: 1rem;
        font-size: 0.9rem;
        color: #9ca3af;
        margin-bottom: 1rem;
        flex-wrap: wrap;
    }
    
    .dataset-source {
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: auto;
        padding-top: 0.5rem;
        border-top: 1px solid #e5e7eb;
    }
    
    .dataset-link {
        color: #3b82f6;
        text-decoration: none;
        font-weight: 600;
    }
    
    .dataset-link:hover {
        color: #2563eb;
        text-decoration: underline;
    }
    
    .team-card {
        background: white !important;
        padding: 2rem !important;
        border-radius: 16px !important;
        text-align: center !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
        height: 400px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        margin-bottom: 2rem !important;
        border: 1px solid #f3f4f6 !important;
        position: relative !important;
        z-index: 1 !important;
        overflow: hidden !important;
    }
    
    .team-card:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
        border: 1px solid #3b82f6 !important;
        z-index: 2 !important;
    }
    
    .team-avatar {
        width: 120px !important;
        height: 120px !important;
        border-radius: 50% !important;
        object-fit: cover !important;
        border: 4px solid #e5e7eb !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        margin-bottom: 1.5rem !important;
        transition: all 0.3s ease !important;
        flex-shrink: 0 !important;
        display: block !important;
    }
    
    .team-card:hover .team-avatar {
        border-color: #3b82f6 !important;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3) !important;
    }
    
    .team-name {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
        margin-bottom: 0.5rem !important;
        text-align: center !important;
        line-height: 1.3 !important;
        flex-shrink: 0 !important;
        width: 100% !important;
    }
    
    .team-role {
        color: #3b82f6 !important;
        font-weight: 600 !important;
        margin-bottom: 1.2rem !important;
        font-size: 1.1rem !important;
        text-align: center !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        flex-shrink: 0 !important;
        width: 100% !important;
    }
    
    .team-description {
        color: #6b7280 !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
        text-align: center !important;
        margin: 0 !important;
        flex-grow: 1 !important;
        display: block !important;
        width: 100% !important;
        padding: 0 !important;
        overflow-wrap: break-word !important;
        word-wrap: break-word !important;
    }
    
    .team-container {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 2rem 0 !important;
        clear: both !important;
    }
    
    .team-section-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .team-section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .team-section-subtitle {
        font-size: 1.2rem;
        color: #6b7280;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.5;
    }
    
    .contact-card {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-top: 3rem;
    }
    
    .contact-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .contact-description {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        margin-top: 2rem;
        text-align: left;
    }
    
    .form-input {
        width: 100%;
        padding: 0.8rem;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-family: 'Inter', sans-serif;
    }
    
    .form-textarea {
        width: 100%;
        padding: 0.8rem;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-family: 'Inter', sans-serif;
        resize: vertical;
        min-height: 120px;
    }
    
    .submit-button {
        background: linear-gradient(45deg, #3b82f6, #2563eb);
        color: white;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .submit-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    }
    
    .persona-description {
        color: #4b5563;
        line-height: 1.6;
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

def about_header():
    st.markdown("""
    <div class="about-header">
        <h1 class="about-title">About EpiAccess</h1>
        <p class="about-subtitle">Empowering Public Health Through Data-Driven Insights</p>
    </div>
    """, unsafe_allow_html=True)

def mission_section():
    st.markdown("## Our Mission")
    
    st.markdown("""
    EpiAccess democratizes access to critical public health data and insights. In a world where 
    infectious diseases know no borders, we believe that every organization – from local NGOs to 
    international health agencies – deserves access to the same powerful analytics that drive 
    evidence-based decision making.
    """)
    
    st.markdown("""
    Our platform transforms complex epidemiological data into actionable insights, enabling 
    faster response times, better resource allocation, and more effective public health interventions. 
    We bridge the gap between raw data and real-world impact.
    """)
    
    st.markdown("### Designed For")
    
    # Create columns for the target users
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("• 🏥 **Non-Governmental Organizations (NGOs)**")
        st.markdown("• 🌍 **International Health Organizations**")
        st.markdown("• 👥 **Community Health Leaders**")
    
    with col2:
        st.markdown("• 📊 **Public Health Researchers**")
        st.markdown("• 🏛️ **Government Health Agencies**")
        st.markdown("• 🎓 **Students and Educators**")

def datasets_section():
    st.markdown('<h2 class="section-title">Our Data Sources</h2>', unsafe_allow_html=True)
    
    datasets = [
        {
            "title": "COVID-19 Global Dataset",
            "description": "Historical COVID-19 cases, deaths, and country-level tracking data from 2020-2022. Processed and cleaned for educational analysis of pandemic patterns.",
            "timespan": "2020 - 2022",
            "records": "44,785 records",
            "source": "Kaggle Public Dataset (Bolkonsky/COVID-19)"
        },
        {
            "title": "SARS Historical Dataset",
            "description": "Complete epidemiological record of the 2003 SARS outbreak covering 37 countries. Essential for understanding coronavirus transmission patterns and historical outbreak analysis.",
            "timespan": "March - July 2003",
            "records": "2,538 records", 
            "source": "Kaggle Public Dataset (imdevskp/SARS 2003)"
        },
        {
            "title": "Monkeypox Surveillance Data",
            "description": "Daily confirmed monkeypox cases by country during the 2022 outbreak. Provides insights into emerging disease patterns and transmission dynamics.",
            "timespan": "2022", 
            "records": "15,792 records",
            "source": "Kaggle Public Dataset (deepcontractor/Monkeypox)"
        },
        {
            "title": "World Bank Health Expenditure",
            "description": "Healthcare spending indicators and economic capacity data for 175+ countries. Used for clustering analysis to understand global healthcare access patterns.",
            "timespan": "2015 - 2022",
            "records": "175 countries",
            "source": "World Bank Open Data Platform"
        }
    ]
    
    cols = st.columns(2)
    for i, dataset in enumerate(datasets):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="dataset-card">
                <div>
                    <h3 class="dataset-title">{dataset['title']}</h3>
                    <p class="dataset-description">{dataset['description']}</p>
                </div>
                <div>
                    <div class="dataset-meta">
                        <span>📅 {dataset['timespan']}</span>
                        <span>📊 {dataset['records']}</span>
                    </div>
                    <div class="dataset-source">
                        <strong>Source:</strong> {dataset['source']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def team_section():
    st.markdown('<h2 class="section-title">Meet Our Team</h2>', unsafe_allow_html=True)
    
    team_members = [
        {
            "name": "Hieu (Calvin) Hoang",
            "role": "Lead Data Scientist", 
            "image": "info/hieu_pic.jpg",
            "description": "Data Scientist with experience in public health analytics, machine learning, and building community-driven tools for impact using Python, SQL, Streamlit, Firebase, and Scikit-learn. Obtained the Google Advanced Data Analytics Certificate."
        },
        {
            "name": "Marcos Escamilla",
            "role": "Data Analyst",
            "image": "info/marcos_pic.jpg", 
            "description": "Working for a non profit organization where I teach first year college students data analytic tools such as SQL, R and Excel"
        },
        {
            "name": "Theraune Casey",
            "role": "Product Designer and Strategist",
            "image": "info/theraune_pic.png",
            "description": "Specializing in creating data-driven, human-centered tools that promote equity in public health and community systems. With a background in data analysis, business strategy and UX design, Theraune designs intuitive digital experiences that bridge complex information with real-world needs."
        },
        {
            "name": "Soumana Dama",
            "role": "Full-Stack Engineer",
            "image": "info/soumana_pic.jpg", 
            "description": "Web and mobile developer, specialized in full-stack technologies, with a keen interest in artificial intelligence and data analysis. Holder of the Google Professional Data Analytics Certificate, obtained as part of the GWG Data Analytics Spring Cohort 25 (EMEAI Data Analytics) program."
        }
    ]
    
    # Create a centered container for the team cards with better deployment compatibility
    st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 2rem 0; clear: both;">', unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, member in enumerate(team_members):
        with cols[i % 2]:
            # Create a card container with inline styles to override any CSS conflicts
            st.markdown(f"""
            <div style="background: white; padding: 2rem; border-radius: 16px; text-align: center; 
                        box-shadow: 0 8px 25px rgba(0,0,0,0.1); transition: all 0.3s ease; 
                        height: 400px; display: flex; flex-direction: column; align-items: center; 
                        justify-content: flex-start; margin-bottom: 2rem; border: 1px solid #f3f4f6; 
                        position: relative; z-index: 1; overflow: hidden;">
                <img src="data:image/jpeg;base64,{get_image_base64(member['image'])}" 
                     style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; 
                            border: 4px solid #e5e7eb; box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
                            margin-bottom: 1.5rem; transition: all 0.3s ease; flex-shrink: 0; display: block;" 
                     alt="{member['name']}">
                <h3 style="font-size: 1.4rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem; 
                           text-align: center; line-height: 1.3; flex-shrink: 0; width: 100%;">{member['name']}</h3>
                <p style="color: #3b82f6; font-weight: 600; margin-bottom: 1.2rem; font-size: 1.1rem; 
                          text-align: center; text-transform: uppercase; letter-spacing: 0.5px; 
                          flex-shrink: 0; width: 100%;">{member['role']}</p>
                <p style="color: #6b7280; font-size: 0.95rem; line-height: 1.6; text-align: center; 
                          margin: 0; flex-grow: 1; display: block; width: 100%; padding: 0; 
                          overflow-wrap: break-word; word-wrap: break-word;">{member['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def get_image_base64(image_path):
    """Convert image to base64 string for embedding in HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        # Return a default placeholder if image fails to load
        return ""

def main():
    load_about_css()
    about_header()
    mission_section()
    datasets_section() 
    team_section()

if __name__ == "__main__":
    main()