
class DrawingModel:
    def __init__(self):
        self.shapes = []  # 그려진 도형들을 저장할 리스트
        self.selected_shapes = []
        self.select_box ={}
        self.selected_box = {"type":"selected", "start":[1e9,0], "end":[1e9,0]}
        self.tool = 'SELECT'
        self.current_line = None

        ##OBSERVER
        self.observers = []

    #OBSERVER : SHAPES#
    def notify_all(self):
        for observer in self.observers:
            observer.update()

    def add_shapes(self,shape):
        self.shapes.append(shape)
        self.notify_all()
        
    def update_shapes(self,idx,pos):
        self.shapes[idx]['end'] = pos
        self.notify_all()
    
    def remove_shapes(self, idx):
        del self.shapes[idx]
        self.notify_all()


    def set_tool(self,tool):
        self.tool = tool
    

