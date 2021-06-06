from ui import teacher_main_window
from PyQt5.QtWidgets import *
from window.modify_account_window import ModifyAccountWindow
from my_library.leave_request import teacher, leave_inf

class TeacherMainWindow(QDialog, teacher_main_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(TeacherMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.identifier = identifier
        self.pushButton_confirm_read.clicked.connect(self.confirm_read)
        self.pushButton_modify_account.clicked.connect(self.modify_account)
        self.show_table()

    def show_table(self):
        # id 是否撤回 是否已读 学号 请假类型 开始时间 结束时间 是否通过
        text = teacher.get_request_list(teacher(), self.identifier)
        num_request = len(text)
        num = int(num_request)
        title = ['id', '是否撤回', '是否已读', '学号', '请假类型', '开始时间', '结束时间', '辅导员是否通过']
        self.tableWidget_list.setColumnCount(8)
        self.tableWidget_list.setRowCount(num)
        self.tableWidget_list.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 8):
                t = text[i][j]
                if j == 4:
                    # 0事假 1病假
                    type = ['事假', '病假']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 7:
                    # 0未阅 1同意 2拒绝
                    type = ['未阅', '同意', '拒绝']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 1:
                    type = ['未撤回', '撤回']
                    item = QTableWidgetItem('%s' % type[int(t)])
                elif j == 2:
                    type = ['未读', '已读']
                    item = QTableWidgetItem('%s' % type[int(t)])
                else:
                    item = QTableWidgetItem('%s' % str(t))
                self.tableWidget_list.setItem(i, j, item)

        # 一些小设置。。。
        self.tableWidget_list.resizeColumnsToContents()

    def modify_account(self):
        ModifyAccountWindow_ = ModifyAccountWindow(self.identifier)
        ModifyAccountWindow_.exec()

    def confirm_read(self):
        id = self.lineEdit_confirm_read_request_id.text()
        if id == '':
            self.label_state.setText('假条编号不合法')
            return
        id = int(id)
        if leave_inf.id_exist(leave_inf(), id):
            if leave_inf.read_by_teacher(leave_inf(), id):
                self.label_state.setText('修改失败，%s号假条已经为已读状态'%id)
            else:
                teacher.confirm_read(teacher(), id)
                self.label_state.setText('成功修改%d号假条为已读状态'%id)
        else:
            self.label_state.setText('%d号假条不存在'%id)
        self.show_table()

