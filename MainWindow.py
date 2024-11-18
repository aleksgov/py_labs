from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QWidget, QLabel, QFrame, QVBoxLayout
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.setMinimumSize(1440, 810)

        # Кнопки и вкладки из interface.ui
        self.firstLabButton : QPushButton = self.findChild(QPushButton, 'FirstLabButton')
        self.theoryFirstLabButton : QPushButton = self.findChild(QPushButton, 'TheoryFirstLabButton')
        self.exampleFirstLabButton : QPushButton = self.findChild(QPushButton, 'ExampleFirstLabButton')
        self.variantsFirstLabButton : QPushButton = self.findChild(QPushButton, 'VariantsFirstLabButton')
        self.tab_widget : QTabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab : QWidget = self.findChild(QWidget, 'FirstLabTab')
        self.htmlViewTab : QWidget = self.findChild(QWidget, 'TheoryFirstLabTab')
        self.exampleFirstLabTab : QWidget = self.findChild(QWidget, 'ExampleFirstLabTab')
        self.variantsFirstLabTab : QWidget = self.findChild(QWidget, 'VariantsFirstLabTab')
        self.tasksFrame : QFrame = self.findChild(QFrame, "TasksFrame")
        self.colorButtonsLayout : QVBoxLayout = self.findChild(QVBoxLayout, "verticalLayout")

        self.tasksFrame.setLayout(QVBoxLayout())

        self.tab_widget.setFocusPolicy(Qt.NoFocus)

        buttons = self.findChildren(QPushButton, QRegExp(".+Button"))
        for button in buttons:
            button.setFocusPolicy(Qt.NoFocus)

        labels = self.findChildren(QLabel, QRegExp("^label.+"))
        for label in labels:
            label.setAttribute(Qt.WA_TransparentForMouseEvents)