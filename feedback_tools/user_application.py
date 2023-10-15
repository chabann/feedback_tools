import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from connection import Connection
from builders.list_builder import ListBuilder
from feedback_tools.design import Ui_UserApplication


class UserApplication(QMainWindow):        
    # def __init__(self):
    #     super().__init__()

    #     connection = Connection()
    #     if not os.path.isfile('./db/app_database.db'):
    #         connection.create_database()

    #     # builder = ListBuilder(self, connection)
    #     # builder.build()

    #     self.setupUi(self)
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        # QMainWindow.__init__(self)
        # Ui_UserApplication.__init__(self)
        super().__init__()
        # self.setupUi(self)
        # self.ui=Ui_UserApplication()
        # self.ui.setupUi(self)

        uic.loadUi("/home/anna/projects/development/feedback_tools/design.ui", self)

        # layout = QGridLayout()
        # self.setLayout(layout)
