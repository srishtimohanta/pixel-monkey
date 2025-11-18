"""
 Chat Page - Interactive Financial Assistant
"""
import streamlit as st
import sys
sys.path.append('..')
from utils.ai_model import load_ai_model

st.set_page_config(
    page_title="Chat - FinanceAI",
    page_icon="💬",
    layout="wide"
)

# Enhanced CSS with 3D Sidebar
st.markdown("""
<style>
    /* 3D Animated Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, 
            rgba(20, 184, 166, 0.15) 0%, 
            rgba(59, 130, 246, 0.15) 100%);
        backdrop-filter: blur(20px);
        perspective: 1000px;
        box-shadow: 5px 0 30px rgba(0, 0, 0, 0.1),
                    inset -1px 0 10px rgba(255, 255, 255, 0.5);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding: 2rem 1rem;
        transform: perspective(1000px) rotateY(-2deg);
        animation: sidebarFloat 6s ease-in-out infinite;
    }
    
    @keyframes sidebarFloat {
        0%, 100% {
            transform: perspective(1000px) rotateY(-2deg) translateY(0px);
        }
        50% {
            transform: perspective(1000px) rotateY(-2deg) translateY(-5px);
        }
    }
    
    /* Glassmorphism Settings Card */
    .settings-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1),
                    inset 0 1px 0 rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 1rem;
    }
    
    /* Quick Prompt Cards with 3D Effect */
    .prompt-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid #E5E7EB;
    }
    
    .prompt-card:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 12px 24px rgba(20, 184, 166, 0.2);
        border-color: #14B8A6;
    }
    
    /* Chat Messages */
    .stChatMessage {
        animation: slideIn 0.4s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Connection Status */
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .status-connected {
        background: #10B981;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    .status-disconnected {
        background: #EF4444;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'hf_token' not in st.session_state:
    st.session_state.hf_token = ""
if 'user_type' not in st.session_state:
    st.session_state.user_type = "Professional"

# Sidebar with 3D effect
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Token input
    token = st.text_input(
        "🔐 Hugging Face API Token",
        value=st.session_state.hf_token,
        type="password",
        help="Get your token from https://huggingface.co/settings/tokens"
    )
    
    if token:
        st.session_state.hf_token = token
    
    # User type selection
    user_type = st.radio(
        "👤 User Type",
        ["Student", "Professional"],
        index=0 if st.session_state.user_type == "Student" else 1
    )
    st.session_state.user_type = user_type
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    
    # Quick Prompts
    st.markdown("### 💡 Quick Prompts")
    
    prompts = [
        "Help me create a monthly budget",
        "What are the best investment options for beginners?",
        "How can I reduce my monthly expenses?",
        "Explain tax deductions I might be missing",
        "Should I pay off debt or invest first?",
        "How much should I save for an emergency fund?"
    ]
    
    for idx, prompt in enumerate(prompts):
        if st.button(prompt, key=f"prompt_{idx}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()

# Main chat interface
st.title("💬 FinanceAI Assistant")

# Connection status
status_class = "status-connected" if st.session_state.hf_token else "status-disconnected"
status_text = "Connected" if st.session_state.hf_token else "Not Connected"
status_color = "#10B981" if st.session_state.hf_token else "#EF4444"

st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: rgba(255,255,255,0.5); border-radius: 12px; margin-bottom: 1rem;">
    <div>
        <h3 style="margin: 0;">FinanceAI Assistant</h3>
        <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">Powered by IBM Granite 3.2 2B • {user_type} Mode</p>
    </div>
    <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: {status_color}; box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);"></span>
        <span style="font-weight: 600;">{status_text}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Check for token
if not st.session_state.hf_token:
    st.warning("⚠️ Please enter your Hugging Face API token in the sidebar to start chatting.")
    st.info("""
    **How to get your token:**
    1. Go to [huggingface.co](https://huggingface.co)
    2. Sign up or log in
    3. Go to Settings → Access Tokens
    4. Create a new **Read** token
    5. Copy and paste it in the sidebar
    """)
else:
    # Load model
    try:
        model = load_ai_model(st.session_state.hf_token)
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()
    
    # Welcome message
    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>👋 Welcome to FinanceAI!</h2>
            <p>
                I'm here to help you with personalized financial guidance. 
                Ask me about budgeting, investments, taxes, or any financial questions you have.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about your finances..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
