import tkinter as tk

class DrawingView(tk.Tk):
    def __init__(self,model):
        super().__init__()
        self.model = model
        # 도구창 Frame
        tool_frame = tk.Frame(self)
        tool_frame.pack(side="left")  # 왼쪽에 정렬

        for tool in [{"icon":"↸", "name":'select'},{"icon":"⏤", "name":'line'},{"icon":"❏", "name":'rectangle'},{"icon":"❍", "name":'circle'}]:
            button = tk.Button(tool_frame, text=tool["icon"], command=lambda t=tool: self.select_tool(t["name"]), width = 1, height = 2)
            button.pack(side="top", anchor='n')  # 위에서 아래로 정렬

        # 캔버스
        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack(side='top', fill='both', expand =True)
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)


        # 속성창
        self.type_label = tk.Label(self, text="type", fg="white")
        self.type_label.pack(side="left")
        self.type_entry_var = tk.StringVar()
        self.type_entry = tk.Entry(self, width=8, textvariable=self.type_entry_var, state = 'readonly')
        self.type_entry.pack(side="left")

        self.x1_label = tk.Label(self, text="x1", fg="white")
        self.x1_label.pack(side="left")
        self.x1_entry_var = tk.StringVar()
        self.x1_entry = tk.Entry(self, width=5, textvariable=self.x1_entry_var)
        self.x1_entry.pack(side="left")

        self.y1_label = tk.Label(self, text="y1", fg="white")
        self.y1_label.pack(side="left")
        self.y1_entry_var = tk.StringVar()
        self.y1_entry = tk.Entry(self, width=5, textvariable=self.y1_entry_var)
        self.y1_entry.pack(side="left")

        self.x2_label = tk.Label(self, text="x2", fg="white")
        self.x2_label.pack(side="left")
        self.x2_entry_var = tk.StringVar()
        self.x2_entry = tk.Entry(self, width=5, textvariable=self.x2_entry_var)
        self.x2_entry.pack(side="left")

        self.y2_label = tk.Label(self, text="y2", fg="white")
        self.y2_label.pack(side="left")
        self.y2_entry_var = tk.StringVar()
        self.y2_entry = tk.Entry(self, width=5, textvariable=self.y2_entry_var)
        self.y2_entry.pack(side="left")

        self.type_entry.bind("<Return>", self.on_type_change)
        self.x1_entry.bind("<Return>", self.on_x1_change)
        self.y1_entry.bind("<Return>", self.on_y1_change)
        self.x2_entry.bind("<Return>", self.on_x2_change)
        self.y2_entry.bind("<Return>", self.on_y2_change)
        
        
        
       
    #도구 선택
    def select_tool(self, tool):
        self.controller.set_selected_tool(tool)

    #도형 그리기
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
    def update_view(self):
        self.canvas.delete("all")  # 화면 지우고
        for shape in self.model.shapes:
            self.draw_shape(shape)  # 저장된 도형들을 다시 그림
        #SELECT BOX
        if(self.model.select_box):
            self.draw_shape(self.model.select_box)
        #SELECTED BOX
        if(self.model.selected_box):
            self.draw_shape(self.model.selected_box)

        selected_shape = self.model.selected_shapes  # 선택한 도형 가져오기
        if len(selected_shape)==1:
            shape = self.model.shapes[selected_shape[0]]
            self.type_entry_var.set(shape['type'])
            self.x1_entry_var.set(shape['start'][0])
            self.y1_entry_var.set(shape['start'][1])
            self.x2_entry_var.set(shape['end'][0])
            self.y2_entry_var.set(shape['end'][1])


    
    #마우스 이벤트
    def on_mouse_click(self, event):
        self.controller.start_draw(event.x, event.y)
    def on_mouse_drag(self, event):
        self.controller.update_draw(event.x, event.y)
    def on_mouse_release(self, event):
        self.controller.end_draw()


    #속성창 이벤트
    def on_type_change(self, event):
        new_type = self.type_entry_var.get()

    def on_x1_change(self, event):
        new_x1 = int(self.x1_entry_var.get())
        self.model.shapes[self.model.selected_shapes[0]]["start"][0] = new_x1
        self.update_view()
        

    def on_y1_change(self, event):
        new_y1 = int(self.y1_entry_var.get())
        self.model.shapes[self.model.selected_shapes[0]]["start"][1] = new_y1
        self.update_view()

    def on_x2_change(self, event):
        new_x2 = int(self.x2_entry_var.get())
        self.model.shapes[self.model.selected_shapes[0]]["end"][0] = new_x2
        self.update_view()

    def on_y2_change(self, event):
        new_y2 = int(self.y2_entry_var.get())
        self.model.shapes[self.model.selected_shapes[0]]["end"][1] = new_y2
        self.update_view()

    
        