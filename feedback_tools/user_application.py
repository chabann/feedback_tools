import os

from connection import Connection
from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtCore import QSize


class UserApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Feedback Tools")
        button = QPushButton("Press Me!")

        self.setMinimumSize(QSize(1000, 800))
        self.setCentralWidget(button)

        connection = Connection()
        if not os.path.isfile('./db/app_database.db'):
            connection.create_database()