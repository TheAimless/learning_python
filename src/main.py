import sys, psutil
from PyQt5.QtWidgets import *
from logreg import loginWidget, regWidget
from mainwin import mainScreen
from lessons import learnWindow
from appCore import window_rootClass as wrc

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    mainUI = wrc(loginWidget(), regWidget(), mainScreen(), learnWindow())
    mainUI.windows[3].showMaximized()

    #Adds linking method between different windows 
    mainUI.addEdges((1, 0, (), wrc.switchWindow), (0, 1, (), wrc.switchWindow), 
    (0, 2, (), mainUI.windows[0].loginButtonAction, wrc.switchWindow), (2, 0, ("frame",), wrc.switchWindow),
    (2, 3, ("widget_2",), wrc.switchWindow), (3, 2, ("widget",), wrc.switchWindow))

    #Runs app
    sys.exit(app.exec_())