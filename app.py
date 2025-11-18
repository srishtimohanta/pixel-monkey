"""
 FinanceAI - Personal Finance Chatbot
 Main Entry Point
 """
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="FinanceAI - Your Personal Finance Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI with animations and 3D effects
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #E8F8F5 0%, #FFFFFF 100%);
    }
    
    /* Header Styling */
    header {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Sidebar Styling with 3D Effect */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, rgba(20, 184, 166, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 5px 0 20px rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding: 2rem 1rem;
    }
    
    /* Card Styling */
    .stCard {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        transition: all 0.3s ease;
    }
    
    .stCard:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.12);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #14B8A6 0%, #0D9488 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(20, 184, 166, 0.3);
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.4);
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #14B8A6, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Animation Keyframes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 3rem 2rem;
        animation: fadeInUp 0.8s ease;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #10B981 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        transition: all 0.3s ease;
        margin: 1rem;
        animation: fadeInUp 0.8s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        font-size: 0.95rem;
        color: #6B7280;
        line-height: 1.6;
    }
    
    /* CTA Section */
    .cta-section {
        background: linear-gradient(135deg, #14B8A6 0%, #3B82F6 100%);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        color: white;
        margin: 3rem 0;
        box-shadow: 0 10px 30px rgba(20, 184, 166, 0.3);
    }
    
    .cta-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .cta-description {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        opacity: 0.95;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #E5E7EB;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #14B8A6;
        box-shadow: 0 0 0 3px rgba(20, 184, 166, 0.1);
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: #F9FAFB;
        border-color: #14B8A6;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Your Personal Finance AI Assistant</h1>
    <p class="hero-subtitle">
        Harness the power of IBM Granite AI to get personalized financial guidance, 
        budget summaries, and spending insights tailored to your unique needs and goals.
    </p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("💬 Start Chatting Now", use_container_width=True):
        st.switch_page("pages/1__Chat.py")
    if st.button("📚 Learn How It Works", use_container_width=True):
        st.switch_page("pages/4_❓_Help.py")

st.markdown("<br>", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <h2>Powerful Features for Your Financial Success</h2>
    <p>Our AI-powered platform combines cutting-edge technology with personalized insights</p>
</div>
""", unsafe_allow_html=True)

# Feature Cards
col1, col2, col3 = st.columns(3)
features = [
    {
        "icon": "💰",
        "title": "Personalized Financial Guidance",
        "description": "Get customized advice on savings, taxes, and investments based on your profile." 
    },
    {
        "icon": "📊",
        "title": "AI-Generated Budget Summaries",
        "description": "Automatically generated detailed budget summaries to help you track and manage finances."
    },
    {
        "icon": "📈",
        "title": "Spending Insights",
        "description": "Actionable insights on spending habits with recommendations to optimize your expenses."
    },
    {
        "icon": "👥",
        "title": "Demographic-Aware Communication",
        "description": "Adaptive communication based on your profile (student vs professional)."
    },
    {
        "icon": "💬",
        "title": "Conversational AI Experience",
        "description": "Natural, fluid, and context-aware interactions powered by IBM Granite AI."
    },
    {
        "icon": "📉",
        "title": "Financial Analytics",
        "description": "Comprehensive charts and graphs to visualize your financial progress and trends."
    }
]

for i, feature in enumerate(features):
    with [col1, col2, col3][i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature['icon']}</div>
            <h3 class="feature-title">{feature['title']}</h3>
            <p class="feature-description">{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Get Started Section
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <h2>Get Started in Seconds</h2>
    <p>Choose your path to better financial management</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
steps = [
    {"icon": "💬", "title": "Start Chatting", "desc": "Get instant financial advice"},
    {"icon": "📊", "title": "View Analytics", "desc": "See your financial insights"},
    {"icon": "📚", "title": "Research Topics", "desc": "Explore financial topics"},
    {"icon": "❓", "title": "Get Help", "desc": "Learn how to use the platform"}
]

for col, step in zip([col1, col2, col3, col4], steps):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{step['icon']}</div>
            <h3 class="feature-title">{step['title']}</h3>
            <p class="feature-description">{step['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# CTA Footer Section
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Transform Your Financial Future?</h2>
    <p class="cta-description">
        Join thousands of users who are already making smarter financial decisions with our AI assistant.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Get Started Today", use_container_width=True):
        st.switch_page("pages/1__Chat.py")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; border-top: 1px solid #E5E7EB; margin-top: 2rem;">
    <p>© 2024 FinanceAI. All rights reserved. | Powered by IBM Granite AI</p>
</div>
""", unsafe_allow_html=True)
