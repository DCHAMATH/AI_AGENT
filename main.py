from agent import Agent
from memory_manager import MemoryManager
from tool_registry import ToolRegistry

from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.translator_tool import TranslatorTool
from tools.file_reader_tool import FileReaderTool
from tools.weather_tool import WeatherTool

memory = MemoryManager()
registry = ToolRegistry()

registry.register(CalculatorTool())
registry.register(TimeTool())
registry.register(TranslatorTool())
registry.register(FileReaderTool())
registry.register(WeatherTool())

agent = Agent(memory, registry)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    response = agent.run(user_input)
    print("\nAgent:", response)