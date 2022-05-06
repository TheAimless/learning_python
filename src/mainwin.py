from PyQt5.QtWidgets import *
import appCore

class mainScreen(appCore.windowClass):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        self.createNode()

    def setupWidget(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(0, 0, 1920, 1080)

        self.createBtn(name = "node_1", text = "Logout", xpos = "540", ypos = "720")