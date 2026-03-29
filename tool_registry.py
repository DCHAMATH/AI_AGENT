class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name()] = tool

    def get_tool(self, name):
        return self.tools.get(name)

    def execute(self, name, **kwargs):
        tool = self.get_tool(name)

        if not tool:
            raise Exception(f"Tool {name} not found")

        return tool.execute(**kwargs)

    def get_declarations(self):
        return [tool.get_declaration() for tool in self.tools.values()]