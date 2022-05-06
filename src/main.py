import sys
import appCore as ac
from PyQt5.QtWidgets import *
from logreg import loginWidget, regWidget
from mainwin import mainScreen

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    login = loginWidget()    
    reg = regWidget()
    mainwin = mainScreen()
    reg.setupWidget()
    login.setupWidget()
    mainwin.setupWidget()

    login.showMaximized()

    #Adds linking method between different windows 
    ac.addEdge(reg, login, ac.switchWindow)
    ac.addEdge(login, reg, ac.switchWindow)
    ac.addEdge(login, mainwin, login.loginButtonAction, ac.switchWindow)
    ac.addEdge(mainwin, login, ac.switchWindow)

    #Runs app
    sys.exit(app.exec_())