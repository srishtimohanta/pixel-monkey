"""
Research Hub Page - Save and organize financial research
"""
import streamlit as st
import sys
sys.path.append('..')
from utils.database import ResearchDatabase

st.set_page_config(
    page_title="Research Hub - FinanceAI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Financial Research Hub")
st.markdown("Store and organize your financial research topics with tagging and search")

# Initialize database
ResearchDatabase.initialize()

# Sidebar - Topic List
with st.sidebar:
    st.markdown("## 📖 Research Topics")
    
    search_query = st.text_input("🔍 Search topics...", placeholder="Enter keywords")
    
    selected_tag = st.selectbox("🏷️ Filter by Tag", ["All Tags", "Savings", "Investment", "Tax", "Debt", "Budget"])
    
    st.markdown("---")
    st.markdown("### 📊 Statistics")
    st.metric("Total Topics", len(ResearchDatabase.get_all_topics()))

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # Add new topic
    with st.expander("➕ Add New Research Topic", expanded=False):
        with st.form("add_topic_form"):
            title = st.text_input("📝 Topic Title", placeholder="e.g., Emergency Fund Strategies")
            content = st.text_area("✍️ Content/Notes", placeholder="Write your research notes here...", height=150)
            tags_input = st.text_input("🏷️ Tags (comma-separated)", placeholder="e.g., savings, emergency, strategy")
            
            tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
            
            submitted = st.form_submit_button("💾 Save Topic", use_container_width=True)
            
            if submitted:
                if title and content:
                    ResearchDatabase.add_topic(title, content, tags)
                    st.success("✅ Topic saved successfully!")
                    st.rerun()
                else:
                    st.error("❌ Please fill in both title and content")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display topics
    st.markdown("### 📋 Saved Topics")
    
    topics = ResearchDatabase.get_all_topics()
    
    if not topics:
        st.info("📭 No topics saved yet. Add your first research topic above!")
    else:
        for topic in reversed(topics):  # Show newest first
            with st.expander(f"📌 {topic['title']}", expanded=False):
                st.markdown(f"**Content:**\n\n{topic['content']}")
                
                if topic['tags']:
                    tags_html = " ".join([f"<span style='background-color: #E0F2FE; padding: 0.25rem 0.75rem; border-radius: 12px; margin-right: 0.5rem; font-size: 0.85rem;'>{tag}</span>" for tag in topic['tags']])
                    st.markdown(f"**Tags:** {tags_html}", unsafe_allow_html=True)
                
                st.caption(f"🕐 Created: {topic['created_at']}")
                
                col_delete, col_edit = st.columns([1, 1])
                with col_delete:
                    if st.button(f"🗑️ Delete", key=f"delete_{topic['id']}", use_container_width=True):
                        ResearchDatabase.delete_topic(topic['id'])
                        st.success("✅ Topic deleted!")
                        st.rerun()

with col2:
    st.markdown("### 🚀 Quick Start")
    
    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.1); border-radius: 12px; padding: 1.5rem; border-left: 4px solid #10B981;">
        <h4 style="margin-top: 0;">Welcome to Research Hub!</h4>
        <p>
            Store and organize your financial research, insights, and notes. 
            Use tags to categorize topics for easy retrieval.
        </p>
        
        <h5>Suggested Topics:</h5>
        <ul>
            <li>Emergency Fund Strategies</li>
            <li>Investment Basics</li>
            <li>Tax Optimization</li>
            <li>Debt Reduction Plans</li>
            <li>Retirement Planning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sample topics for first-time users
    if len(topics) == 0:
        if st.button("📚 Add Sample Topics", use_container_width=True):
            ResearchDatabase.add_topic(
                "Emergency Fund Strategies",
                "Building and maintaining an emergency fund for financial security. Experts recommend 3-6 months of living expenses saved.",
                ["Emergency Fund", "Savings", "Financial Security"]
            )
            ResearchDatabase.add_topic(
                "Investment Basics for Beginners",
                "Understanding fundamental investment concepts: stocks, bonds, mutual funds, and ETFs. Diversification is key to managing risk.",
                ["Investing", "Stocks", "Bonds", "Beginner"]
            )
            st.success("✅ Sample topics added!")
            st.rerun()
