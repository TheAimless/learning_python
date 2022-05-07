#Imports
from typing import Type
from varname import nameof
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
#Variables
NODE_COUNT = 1

class windowClass(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

    def createNode(self):
        global NODE_COUNT
        self.id = f"node_{str(NODE_COUNT)}"
        NODE_COUNT += 1

    def createBtn(self, name, text, xpos, ypos):
        lst = [f"self.{name}_btn = QPushButton(self)", f"self.{name}_btn.setText('{text}')", f"self.{name}_btn.move({xpos}, {ypos})"] 
        for i in lst:
            exec(i)

    def createLabel(self, name, text, xpos, ypos):
        lst = [f"self.{name}_label = QLabel(self)", f"self.{name}_label.setText('{text}')", f"self.{name}_label.move({xpos}, {ypos})"]
        for i in lst:
            exec(i)

    def createMsg(self, name, text):
        msg = QMessageBox()
        msg.setWindowTitle(name)
        msg.setText(text)
        msg.exec_()
    
class window_rootClass:
    def __init__(self, *args):
        self.windows = args
        for i in self.windows:
            i.setupWidget()

    def switchWindow(window1, window2):
        window1.hide()
        window2.resetWindow()
        window2.showMaximized()

    def addEdge(self, id1, id2, func, *args, **kwargs):
        getattr(self.windows[id1], f"{self.windows[id2].id}_btn").clicked.connect(lambda: func(self.windows[id1], self.windows[id2], *args, **kwargs))

    def addEdges(self, *args):
        for i in args:
            self.addEdge(*i)