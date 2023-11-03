# 도구 클래스
class Tool:
    def __init__(self, name):
        self.name = name

    def use(self):
        pass

# 각 도구의 구체적인 구현
class SelectTool(Tool):
    def use(self):
        print("Select Tool")

class LineTool(Tool):
    def use(self):
        print("Line Tool")

class RectangleTool(Tool):
    def use(self):
        print("Rectangle Tool")

class CircleTool(Tool):
    def use(self):
        print("Circle Tool")

# 도구 팩토리
class ToolFactory:
    def create_tool(self, tool_name):
        if tool_name == "select":
            return SelectTool(tool_name)
        elif tool_name == "line":
            return LineTool(tool_name)
        elif tool_name == "rectangle":
            return RectangleTool(tool_name)
        elif tool_name == "circle":
            return CircleTool(tool_name)
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
