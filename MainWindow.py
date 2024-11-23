from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QWidget, QLabel, QFrame, QVBoxLayout
from PyQt5 import uic
from PyQt5.QtGui import QFontDatabase


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.setMinimumSize(1440, 810)

        QFontDatabase.addApplicationFont("documentation/assets/centurygothic.ttf")
        QFontDatabase.addApplicationFont("documentation/assets/centurygothic_bold.ttf")

        # Кнопки и вкладки из interface.ui
        self.firstLabButton : QPushButton = self.findChild(QPushButton, 'FirstLabButton')
        self.secondLabButton: QPushButton = self.findChild(QPushButton, 'SecondLabButton')
        self.thirdLabButton: QPushButton = self.findChild(QPushButton, 'ThirdLabButton')
        self.fourthLabButton: QPushButton = self.findChild(QPushButton, 'FourthLabButton')
        self.theoryFirstLabButton : QPushButton = self.findChild(QPushButton, 'TheoryButton')
        self.exampleFirstLabButton : QPushButton = self.findChild(QPushButton, 'ExampleButton')
        self.variantsFirstLabButton : QPushButton = self.findChild(QPushButton, 'VariantsButton')
        self.tab_widget : QTabWidget = self.findChild(QTabWidget, 'TabWidget')
        self.LabTab : QWidget = self.findChild(QWidget, 'LabTab')
        self.htmlViewTab : QWidget = self.findChild(QWidget, 'TheoryTab')
        self.exampleTab : QWidget = self.findChild(QWidget, 'ExampleTab')
        self.variantsTab : QWidget = self.findChild(QWidget, 'VariantsTab')
        self.tasksFrame : QFrame = self.findChild(QFrame, "TasksFrame")
        self.colorButtonsLayout : QVBoxLayout = self.findChild(QVBoxLayout, "verticalLayout")
        self.LabChangeLabel : QLabel = self.findChild(QLabel, 'LabHeaderLabel')
        self.tasksFrame.setLayout(QVBoxLayout())

        self.tab_widget.setFocusPolicy(Qt.NoFocus)

        buttons = self.findChildren(QPushButton, QRegExp(".+Button"))
        for button in buttons:
            button.setFocusPolicy(Qt.NoFocus)

        labels = self.findChildren(QLabel, QRegExp("^label.+"))
        for label in labels:
            label.setAttribute(Qt.WA_TransparentForMouseEvents)