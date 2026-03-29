# AI Personal Assistant Agent

A modular AI Personal Assistant implemented in Python using **Google Gemini API**. This agent maintains conversation memory, reasons about user requests, and can autonomously call external tools like Calculator, Weather, Translator, File Reader, and more.

---

## Features

- **Interactive CLI**: Chat with the AI in natural language.
- **Contextual Memory**: Remembers conversation within a session.
- **Tool Integration**:
  - Calculator
  - Time
  - Translator
  - File Reader
  - Weather (requires WeatherAPI API key)
- **Adaptive Execution**: Decides when to answer directly or call an external tool.
- **Robust Error Handling**: Handles API errors, invalid inputs, and unknown tool requests.
- **Modular & Extensible**: Follows SOLID principles and Design Patterns (Strategy, Factory/Registry, Observer optional).

---

## Prerequisites

- Python 3.10+
- Required Python packages:
pip install google-genai requests

## Setup

1. **Add your Gemini API Key** in agent.py:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
2.Add your WeatherAPI API Key in weather_tool.py

## Running the Agent
1. python main.py
   
## Example result 
You: what is 12 * 8

Agent: 12 * 8 = 96


You: what is the weather in Riga, Latvia

Agent: Weather in Riga, Latvia: 7°C, Overcast


You: what time is it now

Agent: Current time: 14:35


You: read_file filename="tools/example.txt"

Agent: Hello! This is a test file.
It has multiple lines.
FileReaderTool should read all of this.
