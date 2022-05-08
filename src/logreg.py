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
    
    def setupWidget(self):
        self.setWindowTitle('Login')
        self.setGeometry(0, 0, 1920, 1080)

        self.centralwidget = appCore.widgetClass()
        self.centrallayout = QGridLayout(self.centralwidget)
        self.widget = appCore.widgetClass(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(400, 200))
        self.setCentralWidget(self.centralwidget)
        self.gridlayout = QGridLayout(self.widget)

        self.widget.createLabel(name = "login", text = "Login")
        self.widget.login_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget.login_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.gridlayout.addWidget(self.widget.login_label, 0, 0, 1, 1)
        self.centrallayout.addWidget(self.widget, 0, 0, 1, 1)

        self.user_input = QLineEdit(self.widget)
        self.gridlayout.addWidget(self.user_input, 1, 0, 1, 1)
        self.pass_input = QLineEdit(self.widget)
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.gridlayout.addWidget(self.pass_input, 2, 0, 1, 1)
        self.user_input.setPlaceholderText("Username")
        self.pass_input.setPlaceholderText("Password")

        self.createBtn(name = "node_3", text = "Login")
        self.createBtn(name = "node_2", text = "Register")
        self.horlayout = QHBoxLayout()
        self.horlayout.addWidget(self.node_3_btn)
        self.horlayout.addWidget(self.node_2_btn)
        self.centrallayout.addLayout(self.horlayout, 1, 0, 1, 1)

    def loginButtonAction(self, window1, window2, *args, **kwargs):
        self.data = self.loginList()
        userCredential, passCredential = self.user_input.text(), self.pass_input.text()
        if self.data.get(userCredential) != passCredential or userCredential == "" or passCredential == "":
            def temp():
                self.createMsg('Error', "Invalid login credentials")
                self.node_3_btn.setText("Try again")
            return temp() 
        else:
            return args[0](window1, window2) 

    def resetWindow(self):
        self.node_3_btn.setText("Login")
        self.node_2_btn.setText("Register")
        self.user_input.clear()
        self.pass_input.clear()

class regWidget(appCore.windowClass, loginData):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        super(loginData, self).__init__()
        self.data = self.loginList()
        self.createNode()

    def setupWidget(self):
        self.setWindowTitle('Registration')
        self.setGeometry(0, 0, 1920, 1080)

        self.centralwidget = appCore.widgetClass()
        self.centrallayout = QGridLayout(self.centralwidget)
        self.widget= appCore.widgetClass(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(400, 200))
        self.buttonField = appCore.widgetClass(self.centralwidget)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.centrallayout)
        self.gridLayout_2 = QGridLayout(self.widget)

        self.widget.createLabel(name = "reg", text = "Register")
        self.widget.reg_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget.reg_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.gridLayout_2.addWidget(self.widget.reg_label, 0, 0, 1, 1)
        self.centrallayout.addWidget(self.widget, 0, 0, 1, 1)

        self.user_input, self.pass_input, self.confirm_input = QLineEdit(self), QLineEdit(self), QLineEdit(self)
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.user_input.setPlaceholderText("Username")
        self.pass_input.setPlaceholderText("Password")
        self.confirm_input.setPlaceholderText("Confirm Password")
        self.gridLayout_2.addWidget(self.user_input, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.pass_input, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.confirm_input, 3, 0, 1, 1)

        self.createBtn(name = "reg", text = "Register") 
        self.createBtn(name = "node_1", text = "Back")
        self.horLayout = QHBoxLayout()
        self.horLayout.addWidget(self.reg_btn)
        self.horLayout.addWidget(self.node_1_btn)
        self.centrallayout.addLayout(self.horLayout, 1, 0, 1, 1)
        self.reg_btn.clicked.connect(self.regButtonAction)

    def registrationSuccessful(self, user, pw):
        self.updateLogin(user, pw)
        self.reg_btn.setText("Registered")

    def regButtonAction(self):
        self.data = self.loginList()
        userCredential, passCredential, confirmCredential = self.user_input.text(), self.pass_input.text(), self.confirm_input.text()
        if userCredential == "" or passCredential == "":
            self.createMsg('Error', "Invalid credentials")
            return
        if self.data.get(userCredential) != None:
            self.createMsg('Error', "User already exists")
            return
        if passCredential != confirmCredential:
            self.createMsg('Error', "Passwords do not match")
            return
        self.registrationSuccessful(userCredential, passCredential)

    def resetWindow(self):
        self.reg_btn.setText("Register")
        self.node_1_btn.setText("Back")
        self.user_input.clear()
        self.pass_input.clear()
        self.confirm_input.clear()