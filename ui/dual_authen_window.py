# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dual_authen_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(217, 107)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 196, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_token = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_token.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_token.setObjectName("lineEdit_token")
        self.verticalLayout.addWidget(self.lineEdit_token)
        self.pushButton_confirm = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.verticalLayout.addWidget(self.pushButton_confirm)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">请输入双重验证口令：</span></p></body></html>"))
        self.pushButton_confirm.setText(_translate("Dialog", "确认"))
