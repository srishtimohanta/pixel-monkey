"""
 Help Page - Documentation and FAQ
"""
import streamlit as st
st.set_page_config(
    page_title="Help - FinanceAI",
    page_icon="❓",
    layout="wide"
)
st.title("❓ Help Center")
st.markdown("Everything you need to know about using FinanceAI")
# Quick Start Guide
st.markdown("""
<div>
    <h2>Quick Start Guide</h2>
    <p>Get started in 4 simple steps</p>
</div>
""", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
steps = [
    {"num": "1", "title": "Get API Token", "icon": "", "desc": "Sign up at huggingface.co and create an API token for authentication."},
    {"num": "2", "title": "Configure Settings", "icon": "⚙ ", "desc": "Enter your token in chat settings and customize your preferences."},
    {"num": "3", "title": "Start Chatting", "icon": "", "desc": "Ask financial questions and get personalized AI-powered responses."},
    {"num": "4", "title": "Explore Features", "icon": "", "desc": "Use analytics and research hub for deeper financial insights."}
]
for col, step in zip([col1, col2, col3, col4], steps):
    with col:
        st.markdown(f"""
        <div>
            <div>{step['num']}</div>
            <div>{step['icon']}</div>
            <h4>{step['title']}</h4>
            <p>{step['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
# Platform Features
st.markdown("##  Platform Features")
col1, col2 = st.columns(2)

features = [
    {
        "icon": "",
        "title": "AI-Powered Chat",
        "description": "Get personalized financial advice through natural conversation with IBM Granite AI.",
        "color": "#10B981"
    },
    {
        "icon": "",
        "title": "Financial Analytics",
        "description": "Visualize your financial data with interactive charts and AI-generated insights.",
        "color": "#3B82F6"
    },
    {
        "icon": "",
        "title": "Research Hub",
        "description": "Store and organize your financial research topics with tagging and search.",
        "color": "#F59E0B"
    },
    {
        "icon": "",
        "title": "Personalized Experience",
        "description": "Adaptive communication based on your profile (student vs professional).",
        "color": "#8B5CF6"
    }
]

for i, feature in enumerate(features):
    with [col1, col2][i % 2]:
        st.markdown(f"""
        <div>
            <div>{feature['icon']}</div>
            <h3>{feature['title']}</h3>
            <p>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# FAQ Section
st.markdown("## ❓ Frequently Asked Questions")
faqs = [
    {
        "question": "How do I get started with FinanceAI?",
        "answer": "Create a free Hugging Face account, generate an API token with Read permissions, then ensure you configure the app to use that token."
    },
    {
        "question": "What is the Hugging Face API token and how do I get one?",
        "answer": "It's a free authentication key for accessing the AI model. Go to huggingface.co → Settings → Access Tokens, then create a token with Read permissions."
    },
    {
        "question": "Is my financial data secure?",
        "answer": "Yes! All data is stored locally in your browser session only. We don't store any personal data on our servers."
    },
    {
        "question": "Do I need a GPU or powerful computer?",
        "answer": "No! The AI model runs on Hugging Face's servers via API. Your computer only needs to support a browser and internet access."
    },
    {
        "question": "Is this service free to use?",
        "answer": "Yes! Hugging Face Inference API is free for personal use. There may be rate limits or usage caps depending on your plan."
    },
    {
        "question": "Can I customize the AI model or responses?",
        "answer": "Yes! You can modify the model parameters in utils/ai_model.py or even use a different model as long as it's compatible with the API."
    },
    {
        "question": "What if I get an error or the app is slow?",
        "answer": "Check that your token is valid, you have internet connectivity, and Hugging Face services are operational. Review logs for any API error messages."
    },
    {
        "question": "Can I export my financial data or research topics?",
        "answer": "Currently, data is session-based. You can copy content manually or enable future export capabilities as an enhancement."
    }
]

for i, faq in enumerate(faqs):
    with st.expander(f"**{faq['question']}**"):
        st.write(faq['answer'])
st.markdown("<br>", unsafe_allow_html=True)
# Troubleshooting
st.markdown("##  Troubleshooting")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ** Token Error**
    - Verify token is valid and starts with `hf_`
    - Ensure token has Read permissions
    - Check token hasn't expired
    - Try generating a new token
    
    ** Slow Response**
    - First load downloads model (~2GB)
    - Subsequent responses should be faster
    - Check your internet connection
    - Try reducing max_tokens in settings
    """)
with col2:
    st.markdown("""
    ** Memory Error**
    - Close other applications
    - Model needs ~4GB RAM minimum
    - Restart the application
    - Check system resources
    
    ** Connection Issues**
    - Verify internet connection
    - Check Hugging Face status
    - Try refreshing the page
    - Clear browser cache
    """)
st.markdown("<br>", unsafe_allow_html=True)
# Resources
st.markdown("##  Additional Resources")
st.markdown("""
<div>
    <h3>Useful Links</h3>
    
    <ul>
        <li><strong>Streamlit Documentation:</strong> <a href="https://docs.streamlit.io">docs.streamlit.io</a></li>
        <li><strong>Hugging Face Hub:</strong> <a href="https://huggingface.co/docs">huggingface.co/docs</a></li>
        <li><strong>IBM Granite Model:</strong> <a href="https://huggingface.co/ibm-granite">huggingface.co/ibm-granite</a></li>
        <li><strong>Plotly Charts:</strong> <a href="https://plotly.com/python/">plotly.com/python</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Support Section
st.markdown("""
<div>
    <h2>Still Need Help?</h2>
    <p>Can't find what you're looking for? Our support team is here to help.</p>
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.info(" **Tip:** Check the sidebar on the Chat page for quick prompts to get started!")
