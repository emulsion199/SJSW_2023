class DrawingModel:
    def __init__(self):
        self.shapes = []  # 그려진 도형들을 저장할 리스트
        self.selected_shapes = []
        self.select_box ={}
        self.selected_box = {"type":"selected", "start":[1e9,0], "end":[1e9,0]}

        self.tool = 'SELECT'
        self.current_line = None
    # 다양한 메서드들로 도형을 조작하는 로직 추가

    #도구
    def set_tool(self,tool):
        self.tool = tool
    

