# abstract factory
from abc import abstractmethod


class DrawingFactory:
    def create_shape(self,props):
        pass
# concrete factory 1
class LineFactory(DrawingFactory):
    @abstractmethod
    def create_shape(self,props):
        return Line(props)
# concrete factory 2
class RectangleFactory(DrawingFactory):
    @abstractmethod
    def create_shape(self,props):
        return Rectangle(props)
# concrete factory 3
class CircleFactory(DrawingFactory):
    @abstractmethod
    def create_shape(self,props):
        return Circle(props)
    
# abstract product
class Shape:
    def draw(self,canvas,props):
        pass

# concrete product 1
class Line(Shape):
    def draw(self,canvas,props):
        canvas.create_line([props['start'], props['end']],fill="black")
# concrete product 2
class Rectangle(Shape):
    def draw(self,canvas,props):
        canvas.create_rectangle(props['start'][0],props['start'][1],props['end'][0],props['end'][1], outline = "black")
# concrete product 3
class Circle(Shape):
    def draw(self,canvas,props):
        canvas.create_oval(props['start'][0],props['start'][1],props['end'][0],props['end'][1], outline = "black")
    