import sys
from PyQt5.QtWidgets import *
from ui import admin_main_window
from my_library.user import modify_account_inf, add_descr_member, get_account_inf
from my_library.list import insert_extern_list
from window import modify_account_window
from window.admin import student_list_window,  request_list_window, login_log_list_window

class AdminMainWindow(QDialog, admin_main_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(AdminMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.identifier = identifier
        self.comboBox_ban_enable.addItems(['封禁', '解封'])
        self.comboBox_identity.addItems(['老师', '辅导员', '门卫'])
        self.pushButton_ban_enable.clicked.connect(self.ban_enable_account)
        self.pushButton_add_account.clicked.connect(self.add_account)
        self.pushButton_init_account.clicked.connect(self.init_account)
        self.pushButton_teacher_manage_class.clicked.connect(self.add_teacher_manage_class)
        self.pushButton_add_counselor_manage_major.clicked.connect(self.counselor_manage_major)
        self.pushButton_get_request_list.clicked.connect(self.get_request_list)
        self.pushButton_get_student_list.clicked.connect(self.get_student_list)
        self.pushButton_get_login_log.clicked.connect(self.get_login_log)
        self.pushButton_modify_account.clicked.connect(self.modify_account)
        self.pushButton_add_student.clicked.connect(self.add_student)

    def ban_enable_account(self):
        text = self.comboBox_ban_enable.currentText()
        map = {'封禁':1, '解封':0}
        state = map[text]
        identifier = self.lineEdit_ban_enable_id.text()
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), identifier)
        if identifier_exist == 0:
            self.lineEdit_ban_enable_id.setText('该账号不存在')
            return
        cur_state = get_account_inf.account_is_banned(get_account_inf(), identifier)
        if cur_state == state:
            self.lineEdit_ban_enable_id.setText('该账号已处于%s状态'%text)
        else:
            modify_account_inf.ban_unban_account(modify_account_inf(), identifier, state)
            self.lineEdit_ban_enable_id.setText('已将该账号设置为%s状态' % text)

    def add_account(self):
        text = self.comboBox_identity.currentText()
        # 学生 老师 辅导员 门卫 管理员 超级管理员
        # 0	 1		2     3   4     5
        map = {'老师':1, '辅导员':2, '门卫':3}
        identity = map[text]
        identifier = self.lineEdit_add_account_identifier.text()
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), identifier)
        account_exist = get_account_inf.account_exist(get_account_inf(), identifier)
        if identifier_exist or account_exist:
            self.lineEdit_add_account_identifier.setText('该账号已存在')
        else:
            add_descr_member.add_user_but_student(add_descr_member(), identifier, identity)
            add_descr_member.add_inentity(add_descr_member(), identifier, identity)
            self.lineEdit_add_account_identifier.setText('成功添加%s账号' % text)

    def add_student(self):
        major = self.lineEdit_student_major.text()
        major = int(major)
        name = self.lineEdit_student_name.text()
        class_id = self.lineEdit_student_class.text()
        class_id = int(class_id)
        enro_time = self.lineEdit_student_enrollment_time.text()
        identifier = self.lineEdit_student_identifier.text()
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), identifier)
        account_exist = get_account_inf.account_exist(get_account_inf(), identifier)
        if identifier_exist or account_exist:
            self.lineEdit_student_major.setText('学号已存在')
        else:
            add_descr_member.add_student(add_descr_member(), identifier, major, name, class_id, enro_time)
            self.lineEdit_student_major.setText('添加成功')

    def init_account(self):
        identifier = self.lineEdit_init_identifier.text()
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), identifier)
        if identifier_exist == 0:
            self.lineEdit_init_identifier.setText('该账号不存在')
            return
        modify_account_inf.modify_account(modify_account_inf(), identifier, identifier)
        modify_account_inf.modify_password(modify_account_inf(), identifier, identifier)
        modify_account_inf.change_dual_auth_state(modify_account_inf(), identifier, 0)
        self.lineEdit_init_identifier.setText('初始化成功')

    def add_teacher_manage_class(self):
        teacher_id = self.lineEdit_teacher_id.text()
        teacher_id = teacher_id
        class_id = self.lineEdit_class_id.text()
        class_id = int(class_id)
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), teacher_id)
        if identifier_exist == 0:
            self.lineEdit_teacher_id.setText('该老师id不存在')
            return
        insert_extern_list.insert_teacher_list(insert_extern_list(), teacher_id, class_id)
        self.lineEdit_teacher_id.setText('添加成功')

    def counselor_manage_major(self):
        counselor_id = self.lineEdit_counselor_id.text()
        counselor_id = int(counselor_id)
        major_id = self.lineEdit_major_id.text()
        major_id = int(major_id)
        identifier_exist = get_account_inf.identifier_exist(get_account_inf(), counselor_id)
        if identifier_exist == 0:
            self.lineEdit_counselor_id.setText('该辅导员id不存在')
            return
        else:
            insert_extern_list.insert_counselor_list(insert_extern_list(), counselor_id, major_id)
            self.lineEdit_counselor_id.setText('添加成功')

    def get_request_list(self):
        RequestListWindow_ = request_list_window.RequestListWindow()
        RequestListWindow_.exec()

    def get_student_list(self):
        StudentListWindow = student_list_window.RequestListWindow()
        StudentListWindow.exec()

    def get_login_log(self):
        LoginLogListWindow_ = login_log_list_window.LoginLogListWindow()
        LoginLogListWindow_.exec()

    def modify_account(self):
        ModifyAccountWindow_ = modify_account_window.ModifyAccountWindow(self.identifier)
        ModifyAccountWindow_.exec()