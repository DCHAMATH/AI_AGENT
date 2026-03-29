from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):

    def name(self):
        return "calculator"

    def description(self):
        return "Performs basic math calculations"

    def execute(self, expression):
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Evaluate a math expression",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "expression": {
                        "type": "STRING"
                    }
                },
                "required": ["expression"]
            }
        }