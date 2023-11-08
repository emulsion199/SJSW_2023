import tkinter as tk
class Property(tk.Frame):
    def __init__(self,controller):
        super().__init__()
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

    #     self.type_entry.bind("<Return>", self.on_type_change)
    #     self.x1_entry.bind("<Return>", self.on_x1_change)
    #     self.y1_entry.bind("<Return>", self.on_y1_change)
    #     self.x2_entry.bind("<Return>", self.on_x2_change)
    #     self.y2_entry.bind("<Return>", self.on_y2_change)
    # #속성창 이벤트
    # def on_type_change(self, event):
    #     new_type = self.type_entry_var.get()

    # def on_x1_change(self, event):
    #     new_x1 = int(self.x1_entry_var.get())
    #     self.model.shapes[self.model.selected_shapes[0]]["start"][0] = new_x1
    #     self.update_view()
        

    # def on_y1_change(self, event):
    #     new_y1 = int(self.y1_entry_var.get())
    #     self.model.shapes[self.model.selected_shapes[0]]["start"][1] = new_y1
    #     self.update_view()

    # def on_x2_change(self, event):
    #     new_x2 = int(self.x2_entry_var.get())
    #     self.model.shapes[self.model.selected_shapes[0]]["end"][0] = new_x2
    #     self.update_view()

    # def on_y2_change(self, event):
    #     new_y2 = int(self.y2_entry_var.get())
    #     self.model.shapes[self.model.selected_shapes[0]]["end"][1] = new_y2
    #     self.update_view()