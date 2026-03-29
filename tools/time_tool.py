from tools.base_tool import BaseTool
from datetime import datetime

class TimeTool(BaseTool):

    def name(self):
        return "time"

    def description(self):
        return "Get current system time"

    def execute(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_declaration(self):
        return {
            "name": "time",
            "description": "Get current time",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }