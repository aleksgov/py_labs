import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    controller = MainController()
    window = controller.mainWindow
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()