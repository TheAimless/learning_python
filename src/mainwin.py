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

        self.scrollWidgetContents = appCore.widgetClass()
        self.scrollObj = QScrollArea()
        self.layoutObj = appCore.layoutClass()

        self.layoutObj.createBtn(name = "node_1", text = "Logout")
        self.scrollWidgetContents.setLayout(self.layoutObj)

        self.scrollObj.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollObj.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollObj.setWidgetResizable(True)
        self.scrollObj.setWidget(self.scrollWidgetContents)
        self.scrollObj.setGeometry(QRect(0, 0, 1920, 1080))

        self.setCentralWidget(self.scrollObj)

    def resetWindow(self):
        pass