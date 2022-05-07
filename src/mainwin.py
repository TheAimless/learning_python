import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import appCore

class mainScreen(appCore.windowClass):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        self.createNode()

    def setupWidget(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(0, 0, 1920, 1080)
        self.centralwidget = QWidget(self)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(0, 0, 1920, 1080))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1918, 1078))
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QRect(1900, 0, 16, 1080))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.setCentralWidget(self.centralwidget)
        self.createBtn(name = "node_1", text = "Logout", xpos = "540", ypos = "720")

    def resetWindow(self):
        pass