import tkinter as tk
class Tool(tk.Frame):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        tool_frame = tk.Frame(self)
        tool_frame.pack(side="left")  # 왼쪽에 정렬
        for tool in [{"icon":"↸", "name":'select'},{"icon":"⏤", "name":'line'},{"icon":"❏", "name":'rectangle'},{"icon":"❍", "name":'circle'}]:
            button = tk.Button(tool_frame, text=tool["icon"], command=lambda t=tool: self.select_tool(t["name"]), width = 1, height = 2)
            button.pack(side="top", anchor='n')  # 위에서 아래로 정렬
    def select_tool(self, tool):
        self.controller.use_tool(tool)
        