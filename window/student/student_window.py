from ui import student_main_window
from PyQt5.QtWidgets import *
from my_library.leave_request import student
from window.student.issue_request_window import IssueLeaveRequestWindow
from window.modify_account_window import ModifyAccountWindow
from my_library.leave_request import student

class StudentMainWindow(QDialog, student_main_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(StudentMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.identifier = identifier
        # resizeColumnsToContents()
        self.show_request_list()
        self.pushButton_issue_request.clicked.connect(self.issue_request)
        self.pushButton_modify_account.clicked.connect(self.modify_account)
        self.pushButton_withdraw.clicked.connect(self.withdraw_request)
        # self.tableWidget_request.doubleClicked.connect(self.get_detail_inf)

    def issue_request(self):
        IssueRequestWindow_ = IssueLeaveRequestWindow(self.identifier)
        IssueRequestWindow_.exec()
        self.show_request_list()

    def modify_account(self):
        ModifyAccountWindow_ = ModifyAccountWindow(self.identifier)
        ModifyAccountWindow_.exec()

    def show_request_list(self):
        text = student.get_request_list_simplify(student(), self.identifier)
        # id 请假时间 请假类型 是否批准 开始时间 结束时间 是否撤回
        num_request = len(text)
        num = int(num_request)
        title = ['id', '请假时间', '请假类型', '是否批准', '开始时间', '结束时间', '是否撤回', '老师是否已读']
        self.tableWidget_request.setColumnCount(8)
        self.tableWidget_request.setRowCount(num)
        self.tableWidget_request.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 8):
                t = text[i][j]
                if j == 2:
                    # 0事假 1病假
                    type = ['事假', '病假']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 3:
                    # 0未阅 1同意 2拒绝
                    type = ['未阅', '同意', '拒绝']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 6:
                    type = ['未撤回', '撤回']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 7:
                    type = ['未阅', '已阅']
                    item = QTableWidgetItem('%s' % type[int(t)])
                else:
                    item = QTableWidgetItem('%s' % str(t))
                self.tableWidget_request.setItem(i, j, item)


        # 一些小设置。。。
        self.tableWidget_request.resizeColumnsToContents()

    def withdraw_request(self):
        request_id = self.lineEdit_withdraw_request.text()
        request_id = int(request_id)
        # 0 失败，该假条已撤回
        # 1 失败，该假条已被批准
        # 2 成功
        state = student.withdraw_request(student(), request_id)
        if state == 0:
            self.lineEdit_withdraw_request.setText('失败，该假条已撤回')
        elif state == 1:
            self.lineEdit_withdraw_request.setText('失败，该假条已被批准')
        else:
            self.lineEdit_withdraw_request.setText('撤回成功')
        self.show_request_list()