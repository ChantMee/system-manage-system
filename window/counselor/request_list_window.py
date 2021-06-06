from ui import request_list_window
from PyQt5.QtWidgets import *
from my_library.user import get_account_inf

class RequestListWindow(QDialog, request_list_window.Ui_Dialog):
    def __init__(self, parent = None):
        super(RequestListWindow, self).__init__(parent)
