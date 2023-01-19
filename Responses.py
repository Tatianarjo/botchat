from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi", "what's good", "hey"):
        return "Hey! How are you?"
    
    if user_message in ("hello", "hi", "what's good", "hey"):
        return "Hey! How are you?"