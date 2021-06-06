from PyQt5.QtWidgets import *
from ui import issue_leave_request_window
from PyQt5.QtCore import Qt
from my_library.leave_request import student

class IssueLeaveRequestWindow(QDialog, issue_leave_request_window.Ui_Dialog):
    def __init__(self, identifier, parent = None):
        super(IssueLeaveRequestWindow, self).__init__(parent)
        self.identifier = identifier
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(self.submit)
        self.comboBox_request_type.addItems(['事假', '病假'])

    def __get_data_time(self, wid):
        date = wid.date()
        time = wid.time()
        text = date.toString(Qt.ISODate)
        text += ' ' + time.toString(Qt.ISODate)
        return text

    def submit(self):
        time_start = self.__get_data_time(self.dateTimeEdit_start)
        time_end = self.__get_data_time(self.dateTimeEdit_end)
        selected = self.comboBox_request_type.currentText()
        map = {'事假': 0, '病假': 1}
        request_type = map[selected]
        leave_reason = self.lineEdit_leave_reason.text()
        student.issue_request(student(), self.identifier, request_type, time_start, time_end, leave_reason)
        self.reject()


# import sys
# app = QApplication(sys.argv)
# win = IssueLeaveRequestWindow('student')
# win.show()
# sys.exit(app.exec_())