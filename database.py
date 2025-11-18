"""Research topic storage using session state"""
import streamlit as st
from datetime import datetime


class ResearchDatabase:
    """Manage research topics stored in Streamlit session state."""
    
    @staticmethod
    def initialize():
        """Initialize research topics list in session state if it doesn't exist."""
        if 'research_topics' not in st.session_state:
            st.session_state.research_topics = []
    
    @staticmethod
    def add_topic(title: str, content: str, tags: list = None) -> bool:
        """
        Add a new research topic.
        
        Args:
            title: Topic title
            content: Topic content/notes
            tags: List of tags (optional)
            
        Returns:
            bool: True if topic was added successfully
        """
        ResearchDatabase.initialize()
        
        if not title or not content:
            return False
        
        topic = {
            'id': len(st.session_state.research_topics) + 1,
            'title': title.strip(),
            'content': content.strip(),
            'tags': tags or [],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        st.session_state.research_topics.append(topic)
        return True
    
    @staticmethod
    def get_all_topics() -> list:
        """
        Get all research topics.
        
        Returns:
            list: All research topics stored in session state
        """
        ResearchDatabase.initialize()
        return st.session_state.research_topics
    
    @staticmethod
    def delete_topic(topic_id: int) -> bool:
        """
        Delete a research topic by ID.
        
        Args:
            topic_id: ID of the topic to delete
            
        Returns:
            bool: True if topic was found and deleted
        """
        ResearchDatabase.initialize()
        
        original_length = len(st.session_state.research_topics)
        st.session_state.research_topics = [
            t for t in st.session_state.research_topics if t['id'] != topic_id
        ]
        
        return len(st.session_state.research_topics) < original_length
    
    @staticmethod
    def update_topic(topic_id: int, title: str = None, content: str = None, tags: list = None) -> bool:
        """
        Update an existing research topic.
        
        Args:
            topic_id: ID of the topic to update
            title: New title (optional)
            content: New content (optional)
            tags: New tags (optional)
            
        Returns:
            bool: True if topic was found and updated
        """
        ResearchDatabase.initialize()
        
        for topic in st.session_state.research_topics:
            if topic['id'] == topic_id:
                if title:
                    topic['title'] = title.strip()
                if content:
                    topic['content'] = content.strip()
                if tags is not None:
                    topic['tags'] = tags
                topic['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                return True
        
        return False
    
    @staticmethod
    def search_topics(keyword: str) -> list:
        """
        Search topics by keyword in title or content.
        
        Args:
            keyword: Search keyword
            
        Returns:
            list: Topics matching the search keyword
        """
        ResearchDatabase.initialize()
        keyword_lower = keyword.lower()
        
        return [
            t for t in st.session_state.research_topics
            if keyword_lower in t['title'].lower() or keyword_lower in t['content'].lower()
        ]
    
    @staticmethod
    def get_topic_by_id(topic_id: int) -> dict:
        """
        Get a specific topic by ID.
        
        Args:
            topic_id: ID of the topic
            
        Returns:
            dict: Topic if found, None otherwise
        """
        ResearchDatabase.initialize()
        
        for topic in st.session_state.research_topics:
            if topic['id'] == topic_id:
                return topic
        
        return None
