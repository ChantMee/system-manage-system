from window.login_window import LoginWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    LoginWindow_ = LoginWindow()
    LoginWindow_.show()
    sys.exit(app.exec_())