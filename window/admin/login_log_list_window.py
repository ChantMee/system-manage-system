from ui import login_log_list_window
from PyQt5.QtWidgets import *
from my_library.tool import connect_to_mysql, get_SQL_statement

class LoginLogListWindow(QDialog, login_log_list_window.Ui_Dialog):
    def __init__(self, parent = None):
        super(LoginLogListWindow, self).__init__(parent)
        self.setupUi(self)
        self.show_student_list()

    def __get_request_list(self):
        sql = get_SQL_statement.select(get_SQL_statement(),
                                       ['*'], 'login_log')
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

    def show_student_list(self):
        list = self.__get_request_list()
        print(list)
        num = len(list)
        num = int(num)
        # id 时间 身份 账号 双重认证 是否成功 详情
        title = ['id', '时间', '身份', '账号', '双重认证', '是否成功', '详情']
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(num)
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 7):
                # 学生 老师 辅导员 门卫 管理员 超级管理员
                # 0	 1		2     3   4     5
                t = list[i][j]
                if j == 2:
                    map = ['学生', '老师', '辅导员', '门卫', '管理员', '超级管理员']
                    t = int(t)
                    item = QTableWidgetItem('%s' % str(map[t]))
                elif j == 4:
                    map = ['未打开', '打开']
                    t = int(t)
                    item = QTableWidgetItem('%s' % str(map[t]))
                elif j == 5:
                    map = ['未成功', '成功']
                    t = int(t)
                    item = QTableWidgetItem('%s' % str(map[t]))
                elif j == 6:
                    detail = ['账号不存在', '密码错误', '账号被禁用', '登陆成功', '双重验证未通过', '双重验证通过，登陆成功']
                    t = int(t)
                    item = QTableWidgetItem('%s' % str(detail[t]))
                else:
                    item = QTableWidgetItem('%s' % str(t))
                self.tableWidget.setItem(i, j, item)

        # 一些小设置。。。
        self.tableWidget.resizeColumnsToContents()

