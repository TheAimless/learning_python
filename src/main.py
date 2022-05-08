import sys
from PyQt5.QtWidgets import *
from logreg import loginWidget, regWidget
from mainwin import mainScreen
from appCore import window_rootClass as wrc

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    mainUI = wrc(loginWidget(), regWidget(), mainScreen())
    mainUI.windows[0].showMaximized()

    #Adds linking method between different windows 
    mainUI.addEdges((1, 0, (), wrc.switchWindow), (0, 1, (), wrc.switchWindow), 
    (0, 2, (), mainUI.windows[0].loginButtonAction, wrc.switchWindow), (2, 0, (), wrc.switchWindow))

    #Runs app
    sys.exit(app.exec_())