from PyQt5.QtWidgets import *
from ui import login_window, dual_authen_window
from my_library.user import *
import sys

from window.student.student_window import StudentMainWindow
from window.teacher.teacher_window import TeacherMainWindow
from window.counselor.counselor_window import CounselorMainWindow
from window.admin.admin_window import AdminMainWindow

class LoginWindow(QDialog, login_window.Ui_Dialog):
    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        account = self.lineEdit_account.text()
        account = str(account)
        password = self.lineEdit_password.text()
        password = str(password)
        state = authentication.login(authentication(), account, password)
        # 0 账号不存在
        # 1 密码错误
        # 2 账号被禁用
        # 3 登陆成功
        # 4 验证账号密码正确但是需要双重认证
        message = ['账号不存在', '密码错误', '账号被禁用', '登陆成功', '验证成功，等待双重验证']
        self.label.setText(message[state])
        if state == 3:
            self.close()
            identifier = get_account_inf.get_identifier(get_account_inf(), account)
            LoadMainWindow(identifier)

        elif state == 4:
            self.close()
            identifier = get_account_inf.get_identifier(get_account_inf(), account)
            LoginDualAuthen_ = LoginDualAuthen(identifier)
            LoginDualAuthen_.exec()


class LoginDualAuthen(QDialog, dual_authen_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(LoginDualAuthen, self).__init__(parent)
        self.identifier = identifier
        self.setupUi(self)
        self.identifier = identifier
        self.pushButton_confirm.clicked.connect(self.confirm)

    def confirm(self):
        self.token = self.lineEdit_token.text()
        state = authentication.dual_auth(authentication(), self.identifier, self.token)
        if state == 1:
            self.close()
            LoadMainWindow(self.identifier)


class LoadMainWindow():
    def __init__(self, identifier):
        self.identifier = identifier
        identity = get_account_inf.get_identity(get_account_inf(), self.identifier)
        # 学生 老师 辅导员 门卫 管理员 超级管理员
        # 0	  1		2     3   4     5
        if identity == 0:
            StudentMainWindow_ = StudentMainWindow(identifier)
            StudentMainWindow_.exec()
        elif identity == 1:
            TeacherMainWindow_ = TeacherMainWindow(identifier)
            TeacherMainWindow_.exec()
        elif identity == 2:
            CounselorMainWindow_ = CounselorMainWindow(identifier)
            CounselorMainWindow_.exec()
        elif identity == 3:
            None
        elif identity == 4:
            AdminMainWindow_ = AdminMainWindow(identifier)
            AdminMainWindow_.exec()
        elif identity == 5:
            None