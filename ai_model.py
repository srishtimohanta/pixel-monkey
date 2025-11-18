"""AI Model Integration Module"""
import streamlit as st
from huggingface_hub import InferenceClient


class GraniteAIModel:
    """AI model integration with Hugging Face Granite model."""
    
    def __init__(self, token: str):
        """
        Initialize the Granite AI Model.
        
        Args:
            token: Hugging Face API token
        """
        self.token = token
        self.client = None
        self.model_name = "ibm-granite/granite-3.2-2b-instruct"
    
    def load_model(self) -> bool:
        """
        Load the AI model client.
        
        Returns:
            bool: True if model loaded successfully, False otherwise
        """
        try:
            self.client = InferenceClient(token=self.token)
            return True
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return False
    
    def generate_response(
        self,
        messages: list,
        user_type: str = "professional",
        max_tokens: int = 512,
        temperature: float = 0.7
    ) -> str:
        """
        Generate a response from the AI model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_type: User type - "student" or "professional"
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0-1)
            
        Returns:
            str: Generated response text
        """
        if not self.client:
            if not self.load_model():
                return "Error: Failed to load model. Please check your API token."
        
        if not messages:
            return "Error: No messages provided."
        
        # Customize system prompt based on user type
        if user_type == "student":
            system_prompt = """You are a helpful financial advisor assistant for students.
Provide practical, beginner-friendly financial advice tailored to student circumstances.
Focus on budgeting, savings, and financial planning for their situation."""
        else:  # professional
            system_prompt = """You are a helpful financial advisor assistant for professionals.
Provide personalized financial advice for career professionals.
Consider topics like investments, tax optimization, and long-term financial planning."""
        
        # Build prompt from message history
        prompt = f"{system_prompt}\n\n"
        for msg in messages:
            role = msg.get('role', 'user').capitalize()
            content = msg.get('content', '')
            prompt += f"{role}: {content}\n"
        prompt += "Assistant: "
        
        try:
            response = self.client.text_generation(
                prompt=prompt,
                model=self.model_name,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True
            )
            
            # Handle response object - extract text if needed
            if hasattr(response, 'generated_text'):
                return response.generated_text
            elif isinstance(response, str):
                return response
            else:
                return str(response)
                
        except Exception as e:
            return f"Error generating response: {str(e)}"


@st.cache_resource
def load_ai_model(token: str) -> GraniteAIModel:
    """
    Load and cache the AI model.
    
    Args:
        token: Hugging Face API token
        
    Returns:
        GraniteAIModel: Initialized model instance
    """
    model = GraniteAIModel(token=token)
    if not model.load_model():
        st.error("Failed to initialize AI model. Check your token.")
    return model
