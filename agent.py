import os
from google import genai
from google.genai import errors  

# to run this add your gemini api key here
GEMINI_API_KEY = "" 

class Agent:
    def __init__(self, memory, registry):
        self.memory = memory
        self.registry = registry
        
        if not GEMINI_API_KEY:
            raise ValueError("API Key not found. Please set the GEMINI_API_KEY environment variable.")
        
        # Initialize the Google GenAI client
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def run(self, user_input):
        self.memory.add_user_message(user_input)

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=user_input,
                config={"temperature": 0.2}
            )
            text = response.text
            
        except errors.ClientError as e:
            # Checking for rate limits or other API-specific failures
            if "429" in str(e):
                text = "Error: Quota exceeded. Please check your billing or wait a few minutes."
            elif "404" in str(e):
                text = "Error: Model not found. Try updating the model name string."
            else:
                text = f"An API error occurred: {e}"
        except Exception as e:
            text = f"An unexpected error occurred: {e}"

        self.memory.add_agent_message(text)
        return text