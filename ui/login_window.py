# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(325, 228)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 190, 291, 20))
        self.label.setObjectName("label")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(90, 140, 141, 32))
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setEnabled(True)
        self.label_title.setGeometry(QtCore.QRect(60, 10, 221, 31))
        self.label_title.setObjectName("label_title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 241, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_account = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_account.setObjectName("label_account")
        self.horizontalLayout.addWidget(self.label_account)
        self.lineEdit_account = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.horizontalLayout.addWidget(self.lineEdit_account)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 100, 241, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_assword = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_assword.setObjectName("label_assword")
        self.horizontalLayout_2.addWidget(self.label_assword)
        self.lineEdit_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#fc0107;\">等待登陆...</span></p></body></html>"))
        self.pushButton_login.setText(_translate("Dialog", "登陆"))
        self.label_title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">学生请假&amp;管理系统</span></p></body></html>"))
        self.label_account.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">账号：</span></p></body></html>"))
        self.label_assword.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">密码：</span></p></body></html>"))