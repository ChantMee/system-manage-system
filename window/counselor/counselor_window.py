from PyQt5.QtWidgets import *
from ui import counselor_window
from my_library.leave_request import counselor
from window import modify_account_window
from my_library.user import get_account_inf, modify_account_inf
from my_library.leave_request import leave_inf, counselor

class CounselorMainWindow(QDialog, counselor_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(CounselorMainWindow, self).__init__(parent)
        self.identifier = identifier
        self.setupUi(self)
        self.comboBox_request_type.addItems(['未阅', '同意', '拒绝'])
        self.pushButton_modify_account.clicked.connect(self.modify_account)
        self.pushButton_enable_account.clicked.connect(self.enable_account)
        self.pushButton_init_account.clicked.connect(self.init_account)
        self.pushButton_examine.clicked.connect(self.examine_request)
        self.show_table()

    def modify_account(self):
        modify_account_window_ = modify_account_window.ModifyAccountWindow(self.identifier)
        modify_account_window_.exec()

    def enable_account(self):
        account = self.lineEdit_enable_account.text()
        identifier1 = get_account_inf.get_identifier(get_account_inf(), account)
        state = get_account_inf.account_banned(get_account_inf(), identifier1)
        if state == 0:
            self.label_state.setText('解封失败，账号未处于封禁状态')
        else:
            modify_account_inf.ban_unban_account(modify_account_inf(), identifier1, 0)
            self.label_state.setText('解封成功')

    def init_account(self):
        account = self.lineEdit_init_account.text()
        identifier1 = get_account_inf.get_identifier(get_account_inf(), account)
        state = get_account_inf.identifier_exist(get_account_inf(), identifier1)
        if state == 0:
            self.label_state.setText('初始化失败，账号不存在')
        else:
            modify_account_inf.modify_account(modify_account_inf(), identifier1, identifier1)
            modify_account_inf.modify_password(modify_account_inf(), identifier1, identifier1)
            modify_account_inf.change_dual_auth_state(modify_account_inf(), identifier1, 0)
            self.label_state.setText('初始化成功')

    def show_table(self):
        # id 请假时间 是否撤回 学号 请假类型 开始时间 结束时间 是否同意 是否出校 是否返校
        text = counselor.get_request_list(counselor(), self.identifier)
        num_request = len(text)
        num = int(num_request)
        title = ['id', '请假时间', '是否撤回', '学号', '请假类型', '开始时间', '结束时间', '是否同意', '是否已出校', '是否已返校']
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(num)
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 10):
                t = text[i][j]
                if j == 4:
                    # 0事假 1病假
                    type = ['事假', '病假']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 7:
                    # 0未阅 1同意 2拒绝
                    type = ['未阅', '同意', '拒绝']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 2:
                    type = ['未撤回', '撤回']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 8:
                    type = ['否', '是']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 9:
                    type = ['否', '是']
                    item = QTableWidgetItem('%s' % type[int(t)])
                else:
                    item = QTableWidgetItem('%s' % str(t))
                self.tableWidget.setItem(i, j, item)

        # 一些小设置。。。
        self.tableWidget.resizeColumnsToContents()

    def examine_request(self):
        state = self.comboBox_request_type.currentText()
        map = {'未阅':0, '同意':1, '拒绝':2}
        approval = map[state]
        id = self.lineEdit_request_id.text()
        id = int(id)
        request_exists = leave_inf.id_exist(leave_inf(), id)
        if request_exists == 0:
            self.label_state.setText('审批失败，请假请求不存在')
        else:
            counselor.examine_request(counselor(), id, approval)
            self.label_state.setText('审批成功')
        self.show_table()