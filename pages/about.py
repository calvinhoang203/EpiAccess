# About EpiAccess - Smarter Public Health Decisions
import streamlit as st

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
    }
    
    .about-subtitle {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.9) !important;
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
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .user-item {
        background: white;
        padding: 0.8rem 1.2rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #374151;
        font-weight: 500;
    }
    
    .dataset-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
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
        margin-bottom: 0.8rem;
    }
    
    .dataset-description {
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .dataset-meta {
        display: flex;
        gap: 1rem;
        font-size: 0.9rem;
        color: #9ca3af;
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
        background: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 300px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .team-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(45deg, #3b82f6, #2563eb);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    .team-name {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        color: #3b82f6;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .team-description {
        color: #6b7280;
        font-size: 0.95rem;
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
        <div class="about-title">About EpiAccess</div>
        <div class="about-subtitle">Empowering Public Health Through Data-Driven Insights</div>
    </div>
    """, unsafe_allow_html=True)

def mission_section():
    st.markdown("""
    <div class="mission-card">
        <h2 style="color: #1f2937; font-size: 1.8rem; font-weight: 600; margin-bottom: 1.5rem;">Our Mission</h2>
        <p class="mission-text">
            EpiAccess democratizes access to critical public health data and insights. In a world where 
            infectious diseases know no borders, we believe that every organization – from local NGOs to 
            international health agencies – deserves access to the same powerful analytics that drive 
            evidence-based decision making.
        </p>
        <p class="mission-text">
            Our platform transforms complex epidemiological data into actionable insights, enabling 
            faster response times, better resource allocation, and more effective public health interventions. 
            We bridge the gap between raw data and real-world impact.
        </p>
        
        <div class="target-users">
            <h3 class="target-title">Designed For</h3>
            <ul class="user-list">
                <li class="user-item">🏥 Non-Governmental Organizations (NGOs)</li>
                <li class="user-item">🌍 International Health Organizations</li>
                <li class="user-item">👥 Community Health Leaders</li>
                <li class="user-item">📊 Public Health Researchers</li>
                <li class="user-item">🏛️ Government Health Agencies</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

def datasets_section():
    st.markdown('<h2 class="section-title">Our Data Sources</h2>', unsafe_allow_html=True)
    
    datasets = [
        {
            "title": "COVID-19 Global Dataset",
            "description": "Comprehensive daily tracking of COVID-19 cases, deaths, and recoveries across 190+ countries. Updated continuously with WHO and national health ministry data.",
            "timespan": "2020 - Present",
            "records": "2.1M+ records",
            "source": "WHO, Johns Hopkins, National Health Ministries"
        },
        {
            "title": "Monkeypox Surveillance Data",
            "description": "Real-time monitoring of monkeypox cases with detailed geographic and demographic breakdowns. Essential for outbreak response planning.",
            "timespan": "2022 - Present", 
            "records": "50K+ records",
            "source": "WHO Global Health Observatory"
        },
        {
            "title": "SARS Historical Dataset",
            "description": "Complete epidemiological record of the 2003 SARS outbreak. Critical for understanding coronavirus transmission patterns and response effectiveness.",
            "timespan": "2003 - 2004",
            "records": "8K+ records", 
            "source": "WHO SARS Archives"
        },
        {
            "title": "World Bank Health Expenditure",
            "description": "Healthcare spending patterns and economic capacity indicators for 180+ countries. Essential for understanding healthcare access disparities.",
            "timespan": "2000 - 2022",
            "records": "15K+ records",
            "source": "World Bank Open Data"
        }
    ]
    
    cols = st.columns(2)
    for i, dataset in enumerate(datasets):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="dataset-card">
                <h3 class="dataset-title">{dataset['title']}</h3>
                <p class="dataset-description">{dataset['description']}</p>
                <div class="dataset-meta">
                    <span>📅 {dataset['timespan']}</span>
                    <span>📊 {dataset['records']}</span>
                </div>
                <p style="margin-top: 1rem; font-size: 0.9rem; color: #6b7280;">
                    <strong>Source:</strong> {dataset['source']}
                </p>
            </div>
            """, unsafe_allow_html=True)

def team_section():
    st.markdown('<h2 class="section-title">Meet Our Team</h2>', unsafe_allow_html=True)
    
    team_members = [
        {
            "name": "Dr. Sarah Chen",
            "role": "Lead Data Scientist", 
            "avatar": "👩‍🔬",
            "description": "Epidemiologist with 10+ years experience in infectious disease modeling and WHO outbreak response."
        },
        {
            "name": "Marcus Rodriguez",
            "role": "Full-Stack Engineer",
            "avatar": "👨‍💻", 
            "description": "Software architect specializing in healthcare systems and real-time data processing pipelines."
        },
        {
            "name": "Priya Patel",
            "role": "UX/UI Designer",
            "avatar": "🎨",
            "description": "Design lead focused on making complex health data accessible and actionable for diverse user groups."
        },
        {
            "name": "Dr. James Wright",
            "role": "Public Health Advisor",
            "avatar": "🏥", 
            "description": "Former CDC epidemiologist with field experience in outbreak response across 20+ countries."
        }
    ]
    
    cols = st.columns(2)
    for i, member in enumerate(team_members):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="team-card">
                <div class="team-avatar">{member['avatar']}</div>
                <h3 class="team-name">{member['name']}</h3>
                <p class="team-role">{member['role']}</p>
                <p class="team-description">{member['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def main():
    load_about_css()
    about_header()
    mission_section()
    datasets_section() 
    team_section()

if __name__ == "__main__":
    main()