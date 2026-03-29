from tools.base_tool import BaseTool

class FileReaderTool(BaseTool):

    def name(self):
        return "read_file"

    def description(self):
        return "Read a local text file"

    def execute(self, filename):

        try:
            with open(filename, "r") as f:
                return f.read()

        except Exception as e:
            return str(e)

    def get_declaration(self):
        return {
            "name": "read_file",
            "description": "Read contents of a file",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "filename": {"type": "STRING"}
                },
                "required": ["filename"]
            }
        }