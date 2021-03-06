# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Pipe import conn
#from Pipe.inputfileold import *
from  PyQt5.QtGui import *

class Ui_LoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(640, 430)
        #Form.setStyleSheet("background-image:url(imges/bc1.png)")
        #Form.set
#用户名Label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 100, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

#密码Label
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

#登录button
        self.Button_Login = QtWidgets.QPushButton(Form)
        self.Button_Login.setGeometry(QtCore.QRect(170, 250, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Login.sizePolicy().hasHeightForWidth())
        self.Button_Login.setSizePolicy(sizePolicy)
        self.Button_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_Login.setObjectName("Button_Login")

#取消button
        self.button_exit = QtWidgets.QPushButton(Form)
        self.button_exit.setGeometry(QtCore.QRect(365, 250, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        self.button_exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_exit.setObjectName("button_exit")

#账号输入框
        self.inputText_username = QtWidgets.QLineEdit(Form)
        self.inputText_username.setGeometry(QtCore.QRect(240, 100, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputText_username.sizePolicy().hasHeightForWidth())
        self.inputText_username.setSizePolicy(sizePolicy)
        self.inputText_username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputText_username.setObjectName("inputText_username")

#密码输入框
        self.Text_password = QtWidgets.QLineEdit(Form)
        self.Text_password.setGeometry(QtCore.QRect(240, 150, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text_password.sizePolicy().hasHeightForWidth())
        self.Text_password.setSizePolicy(sizePolicy)
        self.Text_password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Text_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Text_password.setObjectName("Text_password")

#选择按钮
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(355, 200, 85, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label.setStyleSheet("font-size:16px")
        self.label_2.setText(_translate("Form", "密  码:"))
        self.label_2.setStyleSheet("font-size:16px")
        self.Button_Login.setText(_translate("Form", "登录"))
        self.Button_Login.setStyleSheet("font-size:16px")
        self.button_exit.setText(_translate("Form", "退出"))
        self.button_exit.setStyleSheet("font-size:16px")
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.checkBox.setStyleSheet("font-size:16px")
