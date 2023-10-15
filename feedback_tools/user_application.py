import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from connection import Connection
from builders.list_builder import ListBuilder


class UserApplication(QMainWindow):        
    def __init__(self):
        super().__init__()

        uic.loadUi("design.ui", self)
