from ui import modify_account_window
from my_library.user import get_account_inf, modify_account_inf
from PyQt5.QtWidgets import *

class ModifyAccountWindow(QDialog, modify_account_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(ModifyAccountWindow, self).__init__(parent)
        self.identifier = identifier
        self.setupUi(self)
        self.pushButton_confirm.clicked.connect(self.confirm)
        self.pushButton_close_dual_auth.clicked.connect(self.close_dual_authen)
        self.pushButton_modify_account.clicked.connect(self.modify_account)
        self.pushButton_modify_password.clicked.connect(self.modify_password)
        self.pushButton_modify_token.clicked.connect(self.open_dual_authen_or_modift_token)

    def open_dual_authen_or_modift_token(self):
        new_token = self.lineEdit_new_token.text()
        is_open_dual_auth = get_account_inf.is_opened_dual_auth(get_account_inf(), self.identifier)
        if is_open_dual_auth:
            modify_account_inf.modify_dual_auth_token(modify_account_inf(), self.identifier, new_token)
            self.label_state.setText('成功修改口令')
        else:
            modify_account_inf.change_dual_auth_state(modify_account_inf(), self.identifier, 1, new_token)
            self.label_state.setText('成功打开双重认证')

    def close_dual_authen(self):
        is_open_dual_auth = get_account_inf.is_opened_dual_auth(get_account_inf(), self.identifier)
        if is_open_dual_auth:
            modify_account_inf.change_dual_auth_state(modify_account_inf(), self.identifier, 0)
            self.label_state.setText('成功关闭双重认证')
        else:
            self.label_state.setText('关闭失败，此账号没有开通双重认证')

    def modify_account(self):
        new_account = self.lineEdit_new_account.text()
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), new_account)
        account_exist = get_account_inf.account_exist(get_account_inf(), new_account)
        if identifier_exist == 1 or account_exist == 1:
            self.label_state.setText('修改失败，该账号已存在于账号或标识码')
        else:
            modify_account_inf.modify_account(modify_account_inf(), self.identifier, new_account)
            self.label_state.setText('账号修改成功')

    def modify_password(self):
        new_password = self.lineEdit_new_password.text()
        modify_account_inf.modify_password(modify_account_inf(), self.identifier, new_password)
        self.label_state.setText('密码修改成功')

    def confirm(self):
        self.reject()
