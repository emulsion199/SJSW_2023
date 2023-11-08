

from controller.main import DrawingController
from model.main import DrawingModel
from view.main import DrawingView


def main():
    view = DrawingView()
    view.mainloop()  # Tkinter 애플리케이션 시작

if __name__ == "__main__":
    main()