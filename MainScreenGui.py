# Copyright (c) 2015 Peter East All Rights Reserved.

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import custom classes for this project

try:
    from MainScreenGui_DiaryView import *
    from MainScreenGui_TaskView import *
    from MainScreenGui_ResourcesView import *
    from MainScreenGui_UserAdminView import *
except IOError:
    print("[ERROR] Error loading modules")
    sys.exit(-1)



# Requires seperate widgets for each view in the tabbed layout
# Implementation of the tabbed layout could use a QStackedLayout

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        print("[INFO] Created MainScreenGui")

        self.setWindowTitle("[CMS] Main View")

        self.main_layout

        titlefont = QFont("Quicksand", 36)
        bodyfont = QFont("Quicksand", 12)

        self.central_widget = QWidget()
        # Define the topbar
        self.topbar = QWidget()

        self.topbar_layout = QHBoxLayout()

        self.tb_help_button = QPushButton("?")
        self.tb_logout_button = QPushButton("Logout")

        self.topbar_layout.addWidget(self.tb_help_button)
        self.topbar_layout.addWidget(self.tb_logout_button)

        self.topbar.setLayout(self.topbar_layout)

        # Finish defining the topbar

        # Define the view switcher

        # Fill in the window

        self.setCentralWidget(self.central_widget)
