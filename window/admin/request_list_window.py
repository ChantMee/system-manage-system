from ui import request_list_window
from PyQt5.QtWidgets import *
from my_library.tool import connect_to_mysql, get_SQL_statement

class RequestListWindow(QDialog, request_list_window.Ui_Dialog):
    def __init__(self, parent = None):
        super(RequestListWindow, self).__init__(parent)
        self.setupUi(self)
        self.show_student_list()

    def __get_request_list(self):
        sql = get_SQL_statement.select(get_SQL_statement(),
                                       ['*'], 'leave_request')
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

    def show_student_list(self):
        list = self.__get_request_list()
        num = len(list)
        num = int(num)
        # id 请求时间 是否撤回 学号 班级id 请假类型 开始时间 结束时间 是否同意 审批者 老师已读 是否出校 出校时间 是否返校 返校时间 是否准时
        title = ['id', '请求时间', '是否撤回', '学号', '班级id', '请假类型', '开始时间', '结束时间', '是否同意',
                 '审批者', '老师已读', '是否出校', '出校时间', '是否返校', '返校时间', '是否准时']
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(num)
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 16):
                t = list[i][j]

                if j == 2:
                    map = ['未撤回', '已撤回']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 5:
                    map = ['事假', '病假']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 8:
                    map = ['未阅', '同意', '拒绝']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 10:
                    map = ['已读', '未读']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 11:
                    map = ['已出校', '未出校']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 13:
                    map = ['已返校', '未返校']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                if j == 15:
                    map = ['准时', '不准时']
                    t = int(t)
                    item = QTableWidgetItem('%s' % map[t])
                else:
                    item = QTableWidgetItem('%s' % str(t))
                self.tableWidget.setItem(i, j, item)

        # 一些小设置。。。
        self.tableWidget.resizeColumnsToContents()