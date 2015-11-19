from PyQt4.QtCore import *
from PyQt.QtGui import *

# Requires seperate widgets for each view in the tabbed layout
# Implementation of the tabbed layout could use a QStackedLayout

class MainScreenGui(QMainWindow):
    def __init__(self):
        super().__init__()
        print("[INFO] Created MainScreenGui")

        self.title = QLabel("Whut up bitches")
