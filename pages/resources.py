# Resources & Methodology - EpiAccess
import streamlit as st

st.set_page_config(
    page_title="📚 Resources",
    page_icon="📚",
    layout="wide"
)

def load_resources_css():
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
    
    .resources-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .resources-title {
        font-size: 3rem;
        font-weight: 700;
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    .resources-subtitle {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.9);
        font-weight: 400;
    }
    
    .methodology-card {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border-left: 6px solid #3b82f6;
    }
    
    .method-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    .method-description {
        font-size: 1rem;
        line-height: 1.7;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    
    .code-block {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 1.5rem;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        margin: 1rem 0;
        overflow-x: auto;
    }
    
    .download-card {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .download-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(16, 185, 129, 0.3);
    }
    
    .download-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .download-description {
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .download-button {
        background: rgba(255, 255, 255, 0.2);
        border: 2px solid white;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .download-button:hover {
        background: white;
        color: #059669;
        text-decoration: none;
    }
    
    .reference-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin: 1rem 0;
        border-left: 4px solid #6366f1;
    }
    
    .reference-title {
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .reference-authors {
        color: #6b7280;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    
    .reference-link {
        color: #3b82f6;
        text-decoration: none;
        font-weight: 500;
    }
    
    .reference-link:hover {
        text-decoration: underline;
    }
    
    .flowchart-box {
        background: linear-gradient(45deg, #f0f9ff, #e0f2fe);
        border: 2px solid #0ea5e9;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        text-align: center;
    }
    
    .process-step {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        display: inline-block;
        min-width: 150px;
    }
    
    .arrow {
        font-size: 1.5rem;
        color: #0ea5e9;
        margin: 0 1rem;
    }
    
    .persona-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-top: 4px solid #8b5cf6;
    }
    
    .persona-name {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .persona-role {
        color: #8b5cf6;
        font-weight: 500;
        margin-bottom: 1rem;
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

def resources_header():
    st.markdown("""
    <div class="resources-header">
        <h1 class="resources-title">📚 Resources & Methodology</h1>
        <p class="resources-subtitle">Technical documentation, research methods, and downloadable guides</p>
    </div>
    """, unsafe_allow_html=True)

def forecast_methodology_tab():
    st.markdown("## 📊 How We Predict Epidemic Trends")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Simple Time Series Forecasting</h3>
        <p class="method-description">
            We use proven statistical methods to predict where disease trends might go next. Think of it like 
            looking at a graph of cases over time and drawing a line to show what might happen in the next few months.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **What We Look For:**
        - **Patterns**: Does the disease spread faster in winter? 
        - **Trends**: Are cases going up, down, or staying steady?
        - **Cycles**: Do outbreaks repeat every few months?
        
        **Real Example:**
        If COVID-19 cases have been rising by 100 per week for the past month, 
        our model might predict they'll keep rising at a similar rate.
        """)
    
    with col2:
        st.markdown("""
        **Why This Works:**
        - Disease spread often follows predictable patterns
        - People's behavior (like travel, gatherings) is somewhat consistent
        - Seasonal factors (weather, holidays) repeat each year
        
        **When It Doesn't Work:**
        - New virus variants appear
        - Major policy changes happen
        - Unexpected events occur
        """)
    
    st.markdown("""
    <div class="flowchart-box">
        <h4>How We Make Predictions</h4>
        <div>
            <div class="process-step">Look at Past Data</div>
            <span class="arrow">→</span>
            <div class="process-step">Find Patterns</div>
            <span class="arrow">→</span>
            <div class="process-step">Project Forward</div>
            <span class="arrow">→</span>
            <div class="process-step">Show Confidence Level</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def clustering_methodology_tab():
    st.markdown("## 🎯 How We Group Countries by Healthcare Access")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Grouping Similar Countries Together</h3>
        <p class="method-description">
            We look at how much countries spend on healthcare and group those with similar patterns. 
            This helps us understand which countries face similar challenges in fighting diseases.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **What We Measure:**
        - **Money per person**: How much each country spends on healthcare per citizen
        - **Percentage of economy**: What portion of their total economy goes to health
        - **Economic strength**: Overall wealth of the country
        
        **Simple Example:**
        - USA: High spending per person, large economy
        - Denmark: Medium spending per person, but high percentage of economy
        - Kenya: Low spending per person, but trying hard (higher percentage)
        """)
    
    with col2:
        st.markdown("""
        **The Four Groups We Found:**
        
        1. **🟢 High Access**: Rich countries with lots of healthcare spending
        2. **🟡 Growing Access**: Countries investing heavily in health improvements  
        3. **🔵 Health-Focused**: Countries that prioritize health despite limited money
        4. **🔴 Limited Access**: Countries with significant healthcare challenges
        """)
    
    st.markdown("""
    **Why This Matters:**
    - Countries in the same group often have similar disease response capabilities
    - We can compare how different groups handle outbreaks
    - It helps identify where international support might be most needed
    """)

def data_sources_tab():
    st.markdown("## 🔧 Where Our Data Comes From")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Trusted Health Organizations</h3>
        <p class="method-description">
            We only use data from official sources that health experts trust worldwide. 
            This ensures our information is accurate and reliable.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simplified data sources - only the ones we actually use
    st.markdown("""
    **🏥 World Health Organization (WHO)**
    - Global disease tracking and surveillance data
    - Official outbreak reports and case counts
    - Updated regularly by health professionals worldwide
    
    **🏦 World Bank**
    - Healthcare spending data for most countries
    - Economic indicators like GDP and population
    - Helps us understand each country's healthcare capacity
    
    **🏛️ Government Health Ministries**
    - Country-specific disease surveillance
    - Local outbreak reports and case tracking
    - Provides detailed regional information
    """)
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">How We Clean and Check the Data</h3>
        <p class="method-description">
            Raw data often has mistakes or missing information. We carefully clean and verify everything 
            before using it in our analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Common Problems We Fix:**
        - Missing dates or duplicate entries
        - Different countries using different formats
        - Obvious data entry errors (like negative cases)
        - Inconsistent country names or spellings
        """)
    
    with col2:
        st.markdown("""
        **How We Fix Them:**
        - Fill small gaps using nearby data points
        - Standardize all formats to be consistent
        - Remove or correct obvious errors
        - Cross-check with multiple sources when possible
        """)

def why_this_matters_tab():
    st.markdown("## 💡 Why These Methods Matter")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Making Complex Data Simple</h3>
        <p class="method-description">
            Public health data can be overwhelming. Our goal is to turn thousands of data points 
            into clear, actionable insights that help people make better health decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Real examples from the platform
    examples = [
        {
            "scenario": "NGO Planning Emergency Response",
            "problem": "A health NGO needs to know where to send medical supplies during an outbreak",
            "solution": "Use our clustering analysis to identify countries with similar healthcare limitations",
            "outcome": "Supplies go to countries most likely to need them based on spending patterns"
        },
        {
            "scenario": "Government Preparing for Seasonal Flu",
            "problem": "Health officials want to know when flu cases might peak this winter",
            "solution": "Look at our trend forecasts to see predicted case increases",
            "outcome": "Hospitals can prepare beds and staff before the peak hits"
        },
        {
            "scenario": "Researcher Studying Global Health Equity",
            "problem": "Academic needs to compare healthcare access across different regions",
            "solution": "Use our country clustering to see which nations face similar challenges",
            "outcome": "Research identifies patterns and potential solutions for health equity"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        st.markdown(f"""
        **Example {i}: {example['scenario']}**
        - *Problem*: {example['problem']}
        - *How EpiAccess Helps*: {example['solution']}
        - *Result*: {example['outcome']}
        """)
        if i < len(examples):
            st.markdown("---")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Limitations and Important Notes</h3>
        <p class="method-description">
            No analysis is perfect. Here's what you should know about the limits of our methods.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **What Our Forecasts Can Do:**
        - Show likely trends based on current patterns
        - Help with general planning and preparation
        - Compare different scenarios and outcomes
        - Identify potential problems before they happen
        """)
    
    with col2:
        st.markdown("""
        **What Our Forecasts Cannot Do:**
        - Predict exact numbers with 100% accuracy
        - Account for unexpected events or policy changes
        - Replace expert medical judgment
        - Guarantee specific outcomes will occur
        """)

def main():
    load_resources_css()
    resources_header()
    
    # Simplified tabs - removed downloads
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Disease Forecasting", 
        "🎯 Country Grouping", 
        "🔧 Data Sources", 
        "💡 Why This Matters"
    ])
    
    with tab1:
        forecast_methodology_tab()
    
    with tab2:
        clustering_methodology_tab()
    
    with tab3:
        data_sources_tab()
    
    with tab4:
        why_this_matters_tab()

if __name__ == "__main__":
    main()