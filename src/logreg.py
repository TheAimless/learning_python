from operator import truediv
from logdetails import loginData
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import appCore

class loginWidget(appCore.windowClass, loginData):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        super(loginData, self).__init__()
        self.data = self.loginList()
        self.createNode()
        self.flag = False
    
    def setupWidget(self):
        self.setWindowTitle('Login')
        self.setGeometry(0, 0, 1920, 1080)

        self.createLabel(name = "login", text = "Login", xpos = "960", ypos = "0")
        self.createLabel(name = "user", text = "Username", xpos = "480", ypos = "200")
        self.createLabel(name = "pass", text = "Password", xpos = "480", ypos = "400")

        self.user_input = QLineEdit(self)
        self.user_input.move(720, 200)
        self.pass_input = QLineEdit(self)
        self.pass_input.move(720, 400)

        self.createBtn(name = "node_3", text = "Login", xpos = "480", ypos = "540")
        self.createBtn(name = "node_2", text = "Register", xpos = "1440", ypos = "540")

    def loginButtonAction(self, window1, window2, *args, **kwargs):
        userCredential, passCredential = self.user_input.displayText(), self.pass_input.displayText()
        if self.data.get(userCredential) != passCredential:
            def temp():
                self.errorLogin()
                self.node_3_btn.setText("Try again")
            return temp() 
        else:
            return args[0](window1, window2) 

    def errorLogin(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText("Invalid login credentials")
        msg.exec_()

class regWidget(appCore.windowClass):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        self.createNode()

    def setupWidget(self):
        self.setWindowTitle('Registration')
        self.setGeometry(0, 0, 1920, 1080)

        self.createLabel(name = "reg", text = "Register", xpos = "960", ypos = "0")
        self.createLabel(name = "user", text = "Username", xpos = "480", ypos = "200")
        self.createLabel(name = "pass", text = "Password", xpos = "480", ypos = "400")
        self.createLabel(name = "confirm", text = "Confirm Password", xpos = "480", ypos = "600")

        self.user_input, self.pass_input, self.confirm_input = QLineEdit(self), QLineEdit(self), QLineEdit(self)
        self.user_input.move(720, 200)
        self.pass_input.move(720, 400)
        self.confirm_input.move(720, 600)

        self.createBtn(name = "reg", text = "Register", xpos = "480", ypos = "540")
        self.createBtn(name = "node_1", text = "Back", xpos = "1440", ypos = "540")
        self.reg_btn.clicked.connect(self.regButtonAction)

    def errorRegisterNotSame(self):
        pass

    def errorRegisterUserExist(self):
        pass

    def regButtonAction(self):
        userCredential, passCredential, confirmCredential = self.user_input.displayText(), self.pass_input.displayText(), self.confirm_input.displayText()
        if passCredential != confirmCredential:
            self.errorRegisterNotSame()
            return
        if self.data.get(userCredential) != None:
            self.btn_login.setText("Logined")
        else:
            self.errorLogin()
            self.btn_login.setText("Try again")

    def backButtonAction(self):
        pass
