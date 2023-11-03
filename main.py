

from controller.main import DrawingController
from model.main import DrawingModel
from view.main import DrawingView


def main():
    model = DrawingModel()
    view = DrawingView(model)
    controller = DrawingController(model, view)
    view.mainloop()  # Tkinter 애플리케이션 시작

if __name__ == "__main__":
    main()