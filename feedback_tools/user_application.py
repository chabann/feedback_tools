import os

from PyQt6.QtWidgets import QMainWindow, QGridLayout,QPushButton
from PyQt6 import uic

from connection import Connection
from builders.list_builder import ListBuilder


class UserApplication(QMainWindow):        
    def __init__(self):
        super().__init__()

        uic.loadUi('design.ui', self)
        layout = QGridLayout()
        self.setLayout(layout)

    def update(self):
        uic.loadUi('design2.ui', self)
