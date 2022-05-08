#Imports
from PyQt5.QtWidgets import *
#Variables
NODE_COUNT = 1

class widgetClass(QWidget):
    def __init__(self, *args):
        super(QWidget, self).__init__(*args)

    def createBtn(self, name, text):
        lst = [f"self.{name}_btn = QPushButton()", f"self.{name}_btn.setText('{text}')"] 
        for i in lst:
            exec(i)

    def createLabel(self, name, text):
        lst = [f"self.{name}_label = QLabel()", f"self.{name}_label.setText('{text}')"]
        for i in lst:
            exec(i)

    def createMsg(self, name, text):
        msg = QMessageBox()
        msg.setWindowTitle(name)
        msg.setText(text)
        msg.exec_()

class windowClass(QMainWindow, widgetClass):
    def __init__(self):
        super(QMainWindow, self).__init__()
        super(widgetClass, self).__init__()

    def createNode(self):
        global NODE_COUNT
        self.id = f"node_{str(NODE_COUNT)}"
        NODE_COUNT += 1

class window_rootClass:
    def __init__(self, *args):
        self.windows = args
        for i in self.windows:
            i.setupWidget()

    def switchWindow(window1, window2):
        window1.hide()
        window2.resetWindow()
        window2.showMaximized()

    def addEdge(self, id1, id2, obj_list, func, *args, **kwargs):
        temp = self.windows[id1]
        for i in obj_list:
            temp = getattr(temp, i)
        getattr(temp, f"{self.windows[id2].id}_btn").clicked.connect(lambda: func(self.windows[id1], self.windows[id2], *args, **kwargs))

    def addEdges(self, *args):
        for i in args:
            self.addEdge(*i)