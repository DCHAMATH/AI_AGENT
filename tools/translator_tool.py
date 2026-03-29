from tools.base_tool import BaseTool

class TranslatorTool(BaseTool):

    def name(self):
        return "translate"

    def description(self):
        return "Translate text into another language"

    def execute(self, text, language):
        return f"Translated '{text}' to {language}"

    def get_declaration(self):
        return {
            "name": "translate",
            "description": "Translate text into another language",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "text": {"type": "STRING"},
                    "language": {"type": "STRING"}
                },
                "required": ["text", "language"]
            }
        }