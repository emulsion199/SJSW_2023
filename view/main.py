import tkinter as tk
from controller.main import DrawingController

from model.main import DrawingModel

from view.tool import Tool
from view.canvas import Canvas
from view.property import Property


class DrawingView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.model = DrawingModel()
        self.controller = DrawingController(self.model, self)
        ##도구
        tool = Tool(self.controller)
        tool.pack(side = "left")
        # self.model.observers.append(tool)
        ##캔버스
        canvas = Canvas(self.controller,self.model)
        canvas.pack()
        self.model.observers.append(canvas)
        ##속성창
        property = Property(self.controller)
        property.pack()
        # self.model.observers.append(property)
