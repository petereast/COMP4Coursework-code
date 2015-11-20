import sys

from PyQt4.QtCore import *
from PyQt.QtGui import *

# Import custom classes for this project

try:
    from MainScreenGui_DiaryView import *
    from MainScreenGui_TaskView import *
    from MainScreenGui_ResourcesView import *
    from MainScreenGui_UserAdminView import *
except ImportError:
    print("[ERROR] Error loading modules")
    sys.exit(-1)



# Requires seperate widgets for each view in the tabbed layout
# Implementation of the tabbed layout could use a QStackedLayout

class MainScreenGui(QMainWindow):
    def __init__(self):
        super().__init__()
        print("[INFO] Created MainScreenGui")

        self.title = QLabel("Main Screen")
