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
    st.markdown("## 📈 How We Predict Disease Trends")
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Multiple Forecasting Approaches</h3>
        <p class="method-description">
            We offer two different forecasting methods to analyze epidemic patterns and project trends:
            <strong>Exponential Smoothing</strong> (traditional statistical approach) and 
            <strong>PyTorch Neural Network</strong> (machine learning approach). This dual approach
            provides educational value by comparing different forecasting techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual flowchart showing the prediction process
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">How We Make Predictions</h3>
        <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0; flex-wrap: wrap; gap: 1rem;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px 20px; border-radius: 12px; text-align: center; min-width: 140px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <strong>📊 Look at<br/>Past Data</strong>
            </div>
            <div style="color: #667eea; font-size: 24px; font-weight: bold;">→</div>
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px 20px; border-radius: 12px; text-align: center; min-width: 140px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <strong>🔍 Find<br/>Patterns</strong>
            </div>
            <div style="color: #667eea; font-size: 24px; font-weight: bold;">→</div>
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px 20px; border-radius: 12px; text-align: center; min-width: 140px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <strong>📈 Project<br/>Forward</strong>
            </div>
            <div style="color: #667eea; font-size: 24px; font-weight: bold;">→</div>
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px 20px; border-radius: 12px; text-align: center; min-width: 140px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <strong>📊 Show Confidence<br/>Level</strong>
            </div>
        </div>
        <p class="method-description" style="text-align: center; margin-top: 1rem;">
            Our transparent 4-step process makes forecasting easy to understand and perfect for learning epidemiological modeling.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for the two forecasting methods
    tab1, tab2 = st.tabs(["Exponential Smoothing", "PyTorch Neural Network"])
    
    with tab1:
        st.markdown("""
        <div class="methodology-card">
            <h3 class="method-title">Exponential Smoothing for Epidemic Forecasting</h3>
            <p class="method-description">
                We use a proven statistical method called exponential smoothing to analyze epidemic patterns 
                and project trends. This method is perfect for educational purposes because it's transparent, 
                understandable, and widely used in epidemiology.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **What Exponential Smoothing Does:**
            - **Weighs recent data more heavily** - Last week's cases matter more than last month's
            - **Smooths out random noise** - Ignores daily fluctuations to see real trends
            - **Adapts to changes** - Quickly responds when outbreak patterns shift
            - **Provides confidence intervals** - Shows uncertainty ranges around predictions
            
            **Real Example:**
            If COVID-19 cases in Brazil were:
            - Week 1: 1,000 cases
            - Week 2: 1,200 cases  
            - Week 3: 1,500 cases
            
            The model sees an upward trend (+25% per week) and might predict Week 4: ~1,800 cases
            """)
        
        with col2:
            st.markdown("""
            **Why This Method for Epidemics:**
            - **Epidemic-specific** - Designed for disease spread patterns
            - **Educational value** - Easy to understand and explain step-by-step
            - **Proven track record** - Used by epidemiologists for decades
            - **Handles uncertainty** - Shows confidence ranges, not false precision
            
            **What Makes It Different from ML:**
            - Transparent calculations (you can see how it works)
            - Works with smaller datasets (doesn't need millions of data points)
            - Focuses on recent trends (more relevant for outbreaks)
            - Educational focus (great for learning forecasting concepts)
            """)
        
        st.markdown("""
        <div class="methodology-card">
            <h3 class="method-title">Step-by-Step: How Our Exponential Smoothing Works</h3>
            <p class="method-description">Here's exactly how we turn historical case data into educational forecasts:</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Step 1: Data Preparation**
        - Clean historical case numbers (remove obvious errors)
        - Organize by date and country
        - Identify the timeframe for analysis
        
        **Step 2: Trend Detection**
        - Calculate recent growth/decline rates
        - Measure how volatile the data is (lots of ups and downs?)
        - Assess data quality (more data = higher confidence)
        
        **Step 3: Apply Exponential Smoothing**
        - Give more weight to recent observations
        - Calculate smoothed trend line
        - Project trend forward for 6 months maximum
        
        **Step 4: Add Epidemic Context**
        - Apply dampening to prevent unrealistic endless growth
        - Account for typical epidemic curve patterns
        - Generate uncertainty bands (confidence intervals)
        """)
        
        st.markdown("""
        **🎯 Specific Use Case Example:**
        
        **Learning Scenario**: Understanding SARS 2003 patterns
        - **Input**: Daily SARS cases in Singapore (March-June 2003)
        - **Model Output**: Shows the typical epidemic curve with peak in April
        - **Educational Value**: Students learn how outbreaks rise, peak, and decline
        - **Key Insight**: Even with limited data, you can see clear patterns
        
        **What Students Learn:**
        - How to identify epidemic phases (growth, peak, decline)
        - Why recent data matters more than old data
        - How to interpret confidence intervals and uncertainty
        - When forecasting works well vs. when it doesn't
        """)
    
    with tab2:
        st.markdown("""
        <div class="methodology-card">
            <h3 class="method-title">PyTorch Neural Network for Complex Pattern Recognition</h3>
            <p class="method-description">
                We also offer a machine learning approach using PyTorch, a popular deep learning framework.
                This method can capture more complex patterns in the data, though it requires more computational
                resources and is less transparent than traditional statistical methods.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **What PyTorch Neural Network Does:**
            - **Learns complex patterns** - Can identify non-linear relationships in the data
            - **Adapts to changing conditions** - Adjusts to new patterns as they emerge
            - **Handles irregular data** - Works well with datasets that have unusual patterns
            - **Provides confidence intervals** - Shows uncertainty ranges around predictions
            
            **Real Example:**
            If COVID-19 cases in Brazil had irregular patterns:
            - Week 1: 1,000 cases
            - Week 2: 800 cases (unexpected drop)
            - Week 3: 1,500 cases (sudden spike)
            
            The neural network might better capture this irregular pattern than simple smoothing
            """)
        
        with col2:
            st.markdown("""
            **Why This Method for Complex Epidemics:**
            - **Pattern recognition** - Can identify complex relationships in the data
            - **Educational value** - Shows how machine learning can be applied to epidemiology
            - **Modern approach** - Demonstrates cutting-edge techniques in public health
            - **Handles uncertainty** - Shows confidence ranges, not false precision
            
            **What Makes It Different from Traditional Methods:**
            - More complex calculations (less transparent)
            - Can work with irregular patterns (better for some datasets)
            - Requires more computational resources (slower)
            - Educational focus (great for learning ML concepts)
            """)
        
        st.markdown("""
        <div class="methodology-card">
            <h3 class="method-title">Step-by-Step: How Our PyTorch Forecasting Works</h3>
            <p class="method-description">Here's how our neural network approach processes time series data:</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Step 1: Data Preparation**
        - Clean historical case numbers (remove obvious errors)
        - Organize by date and country
        - Create input sequences (e.g., 7 days of data to predict the next day)
        
        **Step 2: Model Architecture**
        - EpidemicTimeSeriesModel: A specialized neural network for epidemic data
        - Input layer: Takes a sequence of past values (e.g., 7 days)
        - Hidden layer: Processes the input to identify patterns
        - Output layer: Predicts the next value in the sequence
        
        **Step 3: Training Process**
        - Split data into training sequences
        - Train the model to minimize prediction error
        - Use Adam optimizer and mean squared error loss
        - Train for a fixed number of epochs (iterations)
        
        **Step 4: Forecasting**
        - Use the trained model to predict future values
        - Generate confidence intervals based on model error
        - Apply constraints to ensure realistic predictions
        """)
        
        st.markdown("""
        **🎯 Specific Use Case Example:**
        
        **Learning Scenario**: Understanding irregular COVID-19 patterns
        - **Input**: Daily COVID-19 cases in a country with irregular reporting
        - **Model Output**: Captures the underlying pattern despite reporting irregularities
        - **Educational Value**: Students learn how machine learning can handle noisy data
        - **Key Insight**: Neural networks can identify patterns that traditional methods miss
        
        **What Students Learn:**
        - How machine learning differs from traditional statistics
        - The trade-offs between transparency and complexity
        - When to use different forecasting approaches
        - The importance of data quality in all forecasting methods
        """)
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">Why Multiple Methods are Perfect for Learning</h3>
        <p class="method-description">
            By offering both traditional statistical methods and modern machine learning approaches,
            we provide a comprehensive educational experience that shows the strengths and limitations
            of different forecasting techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Excellent for Teaching:**
        - **Method comparison** - Students can see how different approaches perform
        - **Immediate feedback** - See how changing parameters affects results
        - **Real-world relevance** - Both methods are used by health professionals
        - **Appropriate complexity** - From simple to more advanced techniques
        
        **Limitations to Discuss:**
        - Cannot predict sudden policy changes
        - Assumes patterns will continue (often unrealistic)
        - Works best with consistent data quality
        - 6-month limit for reasonable accuracy
        """)
    
    with col2:
        st.markdown("""
        **Learning Outcomes:**
        - **Statistical thinking** - Understanding trends vs. noise
        - **Critical analysis** - When to trust vs. doubt predictions
        - **Data literacy** - Reading charts and confidence intervals
        - **Scientific reasoning** - How models work and their limits
        
        **Real Skills Developed:**
        - Pattern recognition in time series data
        - Understanding forecasting uncertainty
        - Interpreting epidemic curves
        - Evaluating model reliability
        """)

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
        <h3 class="method-title">Reliable Public Datasets for Education</h3>
        <p class="method-description">
            We use well-documented, publicly available datasets that are perfect for learning 
            data analysis and epidemiological concepts. All sources are properly attributed and verifiable.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Epidemic Disease Datasets**
        - **COVID-19**: 44,785 records (2020-2022)
          - Source: Kaggle dataset by Bolkonsky
          - Coverage: 212 countries
          - Best for: Pandemic pattern analysis
        
        - **SARS**: 2,538 records (March-July 2003)
          - Source: Kaggle dataset by imdevskp
          - Coverage: 37 affected countries
          - Best for: Historical outbreak study
        
        - **Monkeypox**: 15,792 records (2022)
          - Source: Kaggle dataset by deepcontractor
          - Coverage: 109 countries
          - Best for: Emerging disease patterns
        """)
    
    with col2:
        st.markdown("""
        **💰 Healthcare Access Data**
        - **World Bank Health Expenditure**
          - Source: World Bank Open Data Platform
          - Coverage: 175+ countries (2015-2022)
          - Metrics: Per capita spending, % of GDP
        
        - **Economic Indicators**
          - GDP, population, development indices
          - Multi-year averages for stability
          - Used for clustering analysis
        
        **✅ Data Quality Features:**
        - Officially published datasets
        - Proper attribution to creators
        - Consistent formatting and cleaning
        - Documented limitations and gaps
        """)
    
    st.markdown("""
    <div class="methodology-card">
        <h3 class="method-title">How We Process Raw Data for Education</h3>
        <p class="method-description">
            Raw datasets often have inconsistencies. We clean and standardize everything 
            while documenting our process for educational transparency.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Quality Improvements:**
        - **Standardize country names** (USA vs United States vs US)
        - **Fix date formats** (MM/DD/YYYY vs DD/MM/YYYY)
        - **Remove obvious errors** (negative cases, impossible dates)
        - **Fill small gaps** using interpolation methods
        - **Document assumptions** made during cleaning
        """)
    
    with col2:
        st.markdown("""
        **Educational Benefits:**
        - **Real data experience** - Learn with authentic datasets
        - **Data cleaning skills** - See how raw data gets processed
        - **Quality awareness** - Understand data limitations
        - **Reproducible methods** - All steps documented and explainable
        - **Critical thinking** - Learn to question data quality
        """)
    
    st.markdown("""
    **⚠️ Important Educational Context**
    
    - **Historical focus**: All data is from past outbreaks for learning purposes
    - **Not real-time**: These are educational datasets, not current surveillance
    - **Properly attributed**: All original creators and sources are credited
    - **Transparent processing**: Cleaning steps are documented for learning
    - **Educational use only**: Not suitable for clinical or policy decisions
    """)

def why_this_matters_tab():
    st.markdown("## 💡 Educational Value and Learning Goals")
    
    st.markdown("""
    ### What You Can Learn
    This platform is designed as an educational tool to help users understand:
    """)
    
    # Focus on educational value
    learning_goals = [
        {
            "topic": "📈 Epidemic Patterns",
            "description": "How diseases spread over time and what epidemic curves look like",
            "skills": "Pattern recognition, trend analysis, data visualization"
        },
        {
            "topic": "🔮 Forecasting Concepts", 
            "description": "How statistical models make predictions and their limitations",
            "skills": "Understanding uncertainty, confidence intervals, model reliability"
        },
        {
            "topic": "🌍 Global Health Equity",
            "description": "How healthcare access varies worldwide and why it matters",
            "skills": "Data clustering, comparative analysis, health economics basics"
        },
        {
            "topic": "📊 Data Analysis Skills",
            "description": "How to interpret charts, understand data quality, and draw conclusions",
            "skills": "Critical thinking, data literacy, scientific reasoning"
        }
    ]
    
    for goal in learning_goals:
        st.markdown(f"""
        **{goal['topic']}**
        - *What you'll learn*: {goal['description']}
        - *Skills developed*: {goal['skills']}
        """)
        st.markdown("---")
    
    st.markdown("""
    ### Educational Use Cases
    
    **👨‍🎓 For Students:**
    - Learn data science and public health concepts
    - Practice interpreting visualizations and statistics
    - Understand how models work and their limitations
    
    **👩‍🏫 For Educators:**
    - Teaching tool for epidemiology and data analysis
    - Real-world examples of statistical concepts
    - Discussion starter about health equity and global health
    
    **🔬 For Researchers:**
    - Example of data cleaning and visualization techniques
    - Understanding clustering and forecasting methods
    - Learning about data limitations and uncertainty
    """)
    
    st.markdown("""
    ### Important Disclaimers
    
    **🚨 This is an Educational Tool**
    - Not for medical, clinical, or policy decisions
    - Historical data may not reflect current conditions
    - Simplified analysis for learning purposes
    - Always consult official health authorities for real health information
    
    **📚 Learning Focus**
    - Designed to teach concepts, not provide authoritative analysis
    - Emphasizes understanding methods and limitations
    - Encourages critical thinking about data and models
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