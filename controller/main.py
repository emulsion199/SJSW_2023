import copy

from controller.factory import ToolFactory

# 컨트롤러 (Controller)
class DrawingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self
        self.tool = ToolFactory()
        # self.selected_tool = self.tool.create_tool("select")
        # self.selected_tool = 
        ##LINE
        self.current = None
        self.init_shape = None
        self.init_sbox = None
        

    #도구창
    def set_selected_tool(self, tool):
        # self.selected_tool = self.tool.create_tool(tool)
        self.selected_tool = tool
        self.model.tool = tool
        self.view.update_view()
        return
    
    ###UTIL
    def calculate_select_box(self):
        minx,maxx,miny,maxy = 1e9,0,1e9,0
        for i in self.model.selected_shapes:
            shape = self.model.shapes[i]
            minx = min(minx, shape["start"][0], shape["end"][0])
            maxx = max(maxx,  shape["start"][0], shape["end"][0])
            miny = min(miny, shape["start"][1], shape["end"][1])
            maxy = max(maxy,  shape["start"][1],shape["end"][1])
        self.model.selected_box["start"] = [minx,miny]
        self.model.selected_box["end"] = [maxx,maxy]



    def is_in_selected_box(self,x,y):
        selected_box = self.model.selected_box
        if(selected_box["end"][0]-5<=x<=selected_box["end"][0]+5 and selected_box["end"][1]-5<=y<=selected_box["end"][1]+5):
            return 'resize'
        if(selected_box["start"][0]<=x<=selected_box["end"][0] and selected_box["start"][1]<=y<=selected_box["end"][1]):
            return 'select'
        return 'none'
    
    def is_selected(self,x,y):
        for i in range(len(self.model.shapes)-1,-1,-1):
            shape = self.model.shapes[i]
            start = [min(shape["start"][0], shape["end"][0]), min(shape["start"][1], shape["end"][1])]
            end = [max(shape["start"][0], shape["end"][0]), max(shape["start"][1], shape["end"][1])]
            if(start[0]<=x<=end[0] and start[1]<=y<=end[1]):
                return i
        return -1
    
    def is_multi_selected(self,x,y):
        startx = min(self.model.select_box["start"][0],x)
        endx = max(self.model.select_box["start"][0],x)
        starty = min(self.model.select_box["start"][1],y)
        endy = max(self.model.select_box["start"][1],y)
        target = []
        for i in range(0,len(self.model.shapes)):
            shape = self.model.shapes[i]
            if(startx<=shape["start"][0]<=endx and starty<=shape["start"][1]<=endy):
                target.append(i)
        return target

    def moderate_position(self, i):
        shape = self.model.shapes[i]
        if(shape["type"] in ["rectangle", "circle"]):
            shape["start"][0], shape["end"][0] = min(shape["start"][0], shape["end"][0]), max(shape["start"][0], shape["end"][0])
            shape["start"][1], shape["end"][1] = min(shape["start"][1], shape["end"][1]), max(shape["start"][1], shape["end"][1])




    ####도형 그리기 통합
    def start_draw(self,x,y):
        if(self.model.tool == 'select'):
            flag = self.is_in_selected_box(x,y)
            if(flag == 'select'): #박스 안에 있다면
                # self.set_shape_property()
                self.current = 'select'
            if(flag =='resize'):
                self.current = 'resize'
                self.init_sbox = [self.model.selected_box["start"][0:],self.model.selected_box["end"][0:]]
                self.init_shape = copy.deepcopy(self.model.shapes)

            
            if(flag=='none'):
                target = self.is_selected(x,y) 
                if(target == -1):
                    self.current = 'multiselect'
                    self.model.selected_shapes = []
                    self.model.select_box = {"type": "select", "start":[x,y]}
                else:
                    self.current = 'select'
                    self.model.selected_shapes = [target]
                    self.calculate_select_box()
                    self.view.update_view()

            if(self.current == 'select'): 
                self.init_shape = copy.deepcopy(self.model.shapes)
                self.init_mouse = [x,y]


   
        if(self.model.tool == 'line'):
            self.model.shapes.append({'type': 'line', 'start':[x,y], 'end':[x,y]})
            self.current = 'line'

        if(self.model.tool == 'rectangle'):
            self.model.shapes.append({'type': 'rectangle', 'start':[x,y], 'end':[x,y]})
            self.current = 'rectangle'

        if(self.model.tool == 'circle'):
            self.model.shapes.append({'type': 'circle', 'start':[x,y], 'end':[x,y]})
            self.current = 'circle'

    def update_draw(self,x,y):
        if self.current == 'select':
            for i in self.model.selected_shapes:
                shape = self.model.shapes[i]
                init_shape = self.init_shape[i]
                init_mouse = self.init_mouse
                gap = [x-init_mouse[0],y-init_mouse[1]]
                shape["start"][0] = init_shape["start"][0] + gap[0]
                shape["end"][0] = init_shape["end"][0] + gap[0]
                shape["start"][1] = init_shape["start"][1] + gap[1]
                shape["end"][1] = init_shape["end"][1] + gap[1]
            self.calculate_select_box()
            self.view.update_view()
        
        if self.current == 'multiselect':
            self.model.select_box["end"] = [x,y]
            selected_shapes = self.is_multi_selected(x,y)
            self.model.selected_shapes = selected_shapes
            self.calculate_select_box()
            self.view.update_view()

        if self.current == 'resize':
            
            ##비율 구하기
            init_width = max(self.init_sbox[1][0] - self.init_sbox[0][0],0.1)
            init_height = max(self.init_sbox[1][1] - self.init_sbox[0][1],0.1)
            next_width = x - self.init_sbox[0][0]
            next_height = y - self.init_sbox[0][1]
            ratio_width = next_width/init_width 
            ratio_height = next_height/init_height 

            ##크기 줄이기
            for i in self.model.selected_shapes:
                shape = self.model.shapes[i]
                init_shape = self.init_shape[i]
                init_width =  init_shape["end"][0] - init_shape["start"][0] 
                init_height = init_shape["end"][1] - init_shape["start"][1]
                init_gap = [init_shape["start"][0] - self.init_sbox[0][0], init_shape["start"][1] - self.init_sbox[0][1]]
                
                shape["start"][0] = self.init_sbox[0][0] + init_gap[0]*ratio_width
                shape["start"][1] = self.init_sbox[0][1] + init_gap[1]*ratio_height
                shape["end"][0] = shape["start"][0] + init_width*ratio_width
                shape["end"][1] = shape["start"][1] + init_height*ratio_height
                self.moderate_position(i)


            self.calculate_select_box()
            self.view.update_view()
            



        if self.current == 'line':
            self.model.shapes[-1]['end'] = [x,y]
            self.view.update_view()

        if(self.model.tool == 'rectangle'):
            self.model.shapes[-1]['end']=[x,y]
            self.view.update_view()

        if(self.model.tool == 'circle'):
            self.model.shapes[-1]['end']=[x,y]
            self.view.update_view()

    def modify_position(self):
        shape = self.model.shapes[-1]
        if (shape['start'][0] > shape['end'][0]):
            shape['start'][0], shape['end'][0] = shape['end'][0], shape['start'][0]
        if (shape['start'][1] > shape['end'][1]):
            shape['start'][1], shape['end'][1] = shape['end'][1], shape['start'][1]


    def end_draw(self):
        
        if self.current == 'select':
            self.current =None
        if self.current == 'multiselect':
            self.calculate_select_box()
            self.current = None
            self.model.select_box = None
            self.view.update_view()

        if self.current == 'line':
            shape = self.model.shapes[-1]
            if (shape['start'] == shape['end']):
                self.model.shapes.pop()
            self.current = None

        if(self.model.tool == 'rectangle'):
            shape = self.model.shapes[-1]
            if (shape['start'] == shape['end']):
                self.model.shapes.pop()
            self.modify_position()
            self.current = None

        if(self.model.tool == 'circle'):
            shape = self.model.shapes[-1]
            if (shape['start'] == shape['end']):
                self.model.shapes.pop()
            self.modify_position()
            
                
            self.current = None


    