from ui import student_list_window
from PyQt5.QtWidgets import *
from my_library.user import get_account_inf
from my_library.tool import get_SQL_statement, connect_to_mysql

class RequestListWindow(QDialog, student_list_window.Ui_Dialog):
    def __init__(self, parent = None):
        super(RequestListWindow, self).__init__(parent)
        self.setupUi(self)
        self.show_student_list()

    def __get_student_list(self):
        sql = get_SQL_statement.select(get_SQL_statement(),
                                       ['*'], 'student_inf')
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

    def show_student_list(self):
        list = self.__get_student_list()
        num = len(list)
        num = int(num)
        # id '学号', '专业', '姓名', '班级', '入学时间'
        title = ['学号', '专业', '姓名', '班级', '入学时间']
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(num)
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i in range(0, num):
            for j in range(0, 6):
                if j == 0:
                    continue
                t = list[i][j]
                item = QTableWidgetItem('%s' % t)
                self.tableWidget.setItem(i, j, item)

        # 一些小设置。。。
        self.tableWidget.resizeColumnsToContents()