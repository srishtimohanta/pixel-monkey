"""
Analytics Page - Financial Dashboard
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import sys
sys.path.append('..')
from utils.financial_advisor import FinancialAdvisor

st.set_page_config(
    page_title="Analytics - FinanceAI",
    page_icon="📊",
    layout="wide"
)

# Enhanced CSS
st.markdown("""
<style>
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.12);
    }
    
    .chart-container {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize financial data in session state
if 'financial_data' not in st.session_state:
    st.session_state.financial_data = {
        'monthly_income': 5000,
        'monthly_expenses': 3500,
        'monthly_savings': 1000,
        'total_debt': 500,
        'spending': {
            'Housing': 1200,
            'Food': 600,
            'Transportation': 400,
            'Entertainment': 300,
            'Healthcare': 200,
            'Utilities': 250,
            'Shopping': 350,
            'Other': 200
        }
    }

data = st.session_state.financial_data

# Title
st.title("📊 Financial Analytics")
st.markdown("Visualize your financial data and get AI-powered insights")

# Calculate metrics
savings_rate = FinancialAdvisor.calculate_savings_rate(
    data['monthly_income'], 
    data['monthly_expenses']
)
debt_ratio = FinancialAdvisor.calculate_debt_ratio(
    data['total_debt'], 
    data['monthly_income']
)

# Top metrics row
col1, col2, col3, col4 = st.columns(4)
metrics = [
    {
        "label": "💰 Monthly Income",
        "value": f"${data['monthly_income']:,}",
        "color": "#10B981"
    },
    {
        "label": "💸 Monthly Expenses",
        "value": f"${data['monthly_expenses']:,}",
        "color": "#3B82F6"
    },
    {
        "label": "📈 Savings Rate",
        "value": f"{savings_rate:.1f}%",
        "color": "#8B5CF6"
    },
    {
        "label": "📉 Debt Ratio",
        "value": f"{debt_ratio:.1f}%",
        "color": "#F59E0B"
    }
]

for col, metric in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 0.9rem; color: #6B7280; margin-bottom: 0.5rem;">{metric['label']}</div>
            <div style="font-size: 2rem; font-weight: 700; color: {metric['color']};">{metric['value']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts row
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🍰 Spending Breakdown")
    
    # Donut chart
    categories = list(data['spending'].keys())
    values = list(data['spending'].values())
    colors = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444', '#14B8A6', '#EC4899', '#6B7280', '#8B5CF6']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=.4,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig.update_layout(
        showlegend=True,
        height=400,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("💡 Get AI Insights", use_container_width=True):
        st.info("**AI Insight:** Your housing costs are 34% of income. Consider keeping it under 30% for better financial health.")

with col2:
    st.markdown("### 📊 Financial Overview")
    
    # Bar chart
    categories = ['Income', 'Expenses', 'Savings', 'Debt']
    values = [
        data['monthly_income'],
        data['monthly_expenses'],
        data['monthly_savings'],
        data['total_debt']
    ]
    colors_bar = ['#10B981', '#3B82F6', '#8B5CF6', '#EF4444']
    
    fig = go.Figure(data=[go.Bar(
        x=categories,
        y=values,
        marker=dict(color=colors_bar),
        text=values,
        texttemplate='$%{text:,}',
        textposition='outside'
    )])
    
    fig.update_layout(
        height=400,
        margin=dict(t=20, b=0, l=0, r=0),
        yaxis_title="Amount ($)",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("📋 Generate Summary", use_container_width=True):
        advice = FinancialAdvisor.get_budget_advice(
            data['monthly_income'], 
            data['monthly_expenses']
        )
        st.success(f"**Summary:** {advice}")

st.markdown("<br>", unsafe_allow_html=True)

# Update Financial Data Form
st.markdown("### ⚙️ Update Your Financial Data")

with st.form("financial_data_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        income = st.number_input("Monthly Income ($)", value=data['monthly_income'], min_value=0, step=100)
        savings = st.number_input("Monthly Savings ($)", value=data['monthly_savings'], min_value=0, step=5)
    
    with col2:
        housing = st.number_input("Housing ($)", value=data['spending']['Housing'], min_value=0, step=50)
        food = st.number_input("Food ($)", value=data['spending']['Food'], min_value=0, step=50)
        transportation = st.number_input("Transportation ($)", value=data['spending']['Transportation'], min_value=0, step=50)
    
    with col3:
        entertainment = st.number_input("Entertainment ($)", value=data['spending']['Entertainment'], min_value=0, step=50)
        healthcare = st.number_input("Healthcare ($)", value=data['spending']['Healthcare'], min_value=0, step=50)
        debt = st.number_input("Total Debt ($)", value=data['total_debt'], min_value=0, step=50)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        utilities = st.number_input("Utilities ($)", value=data['spending']['Utilities'], min_value=0, step=50)
    with col2:
        shopping = st.number_input("Shopping ($)", value=data['spending']['Shopping'], min_value=0, step=25)
    with col3:
        other = st.number_input("Other ($)", value=data['spending']['Other'], min_value=0, step=25)
    with col4:
        st.empty()  # Placeholder for alignment
    
    submitted = st.form_submit_button("✅ Update Data", use_container_width=True)
    
    if submitted:
        total_expenses = housing + food + transportation + entertainment + healthcare + utilities + shopping + other
        
        st.session_state.financial_data = {
            'monthly_income': income,
            'monthly_expenses': total_expenses,
            'monthly_savings': savings,
            'total_debt': debt,
            'spending': {
                'Housing': housing,
                'Food': food,
                'Transportation': transportation,
                'Entertainment': entertainment,
                'Healthcare': healthcare,
                'Utilities': utilities,
                'Shopping': shopping,
                'Other': other
            }
        }
        st.success("✅ Financial data updated successfully!")
        st.rerun()
