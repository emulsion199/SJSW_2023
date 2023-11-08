import tkinter as tk
class Canvas(tk.Frame):
    def __init__(self,controller,model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack(side='top', fill='both', expand =True)
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

    def on_mouse_click(self, event):
        self.controller.start_draw(event.x, event.y)
    def on_mouse_drag(self, event):
        self.controller.update_draw(event.x, event.y)
    def on_mouse_release(self, event):
        self.controller.end_draw()

    def draw_shape(self, shape):
        if shape['type'] == 'line':
            self.canvas.create_line([shape['start'], shape['end']],fill="black")
        if shape['type'] == 'rectangle':
            self.canvas.create_rectangle(shape['start'][0],shape['start'][1],shape['end'][0],shape['end'][1], outline = "black")
        if shape['type'] == 'circle':
            self.canvas.create_oval(shape['start'][0],shape['start'][1],shape['end'][0],shape['end'][1], outline = "black")
        if shape['type'] == 'select':
            self.canvas.create_rectangle(shape['start'][0],shape['start'][1],shape['end'][0],shape['end'][1], outline = "blue")
        if shape['type'] == 'selected':
            self.canvas.create_rectangle(shape['start'][0],shape['start'][1],shape['end'][0],shape['end'][1], dash=(5,1), outline = "blue")
            self.canvas.create_oval(shape['end'][0]-5,shape['end'][1]-5,shape['end'][0]+5,shape['end'][1]+5, outline = "blue", fill = "white")
    #뷰 업데이트
    def update(self):
        self.canvas.delete("all")  # 화면 지우고
        for shape in self.model.shapes:
            self.draw_shape(shape)  # 저장된 도형들을 다시 그림
        # #SELECT BOX
        # if(self.model.select_box):
        #     self.draw_shape(self.model.select_box)
        # #SELECTED BOX
        # if(self.model.selected_box):
        #     self.draw_shape(self.model.selected_box)

        selected_shape = self.model.selected_shapes  # 선택한 도형 가져오기
        # if len(selected_shape)==1:
        #     shape = self.model.shapes[selected_shape[0]]
        #     self.type_entry_var.set(shape['type'])
        #     self.x1_entry_var.set(shape['start'][0])
        #     self.y1_entry_var.set(shape['start'][1])
        #     self.x2_entry_var.set(shape['end'][0])
        #     self.y2_entry_var.set(shape['end'][1])