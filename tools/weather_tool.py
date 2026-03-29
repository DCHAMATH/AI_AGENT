# weather_tool.py
from tools.base_tool import BaseTool
import requests

class WeatherTool(BaseTool):

    def name(self):
        return "weather"

    def description(self):
        return "Get current weather of a city"

    def execute(self, city):
        try:
            API_KEY = " "  # to run this add your WeatherAPI API key here
            if API_KEY:
                url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
                response = requests.get(url).json()
                if "current" in response:
                    temp = response["current"]["temp_c"]
                    desc = response["current"]["condition"]["text"]
                    return f"Weather in {city}: {temp}°C, {desc}"
                else:
                    return f"Could not find weather for {city}"
            else:
                # Simulate weather if API key not provided
                return f"Weather in {city}: 25°C, clear sky"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "weather",
            "description": "Get current weather of a city",
            "parameters": {
                "type": "OBJECT",  
                "properties": {
                    "city": {"type": "STRING"}
                },
                "required": ["city"]
            }
        }