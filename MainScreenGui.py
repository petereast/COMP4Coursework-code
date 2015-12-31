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
    from GlobalResources import *
except ImportError:
    print("[ERROR] Error loading modules")
    sys.exit(-1)



# Requires seperate widgets for each view in the tabbed layout
# Implementation of the tabbed layout could use a QStackedLayout

class MainScreen(QMainWindow):
    def __init__(self, user=None):
        super().__init__()
        print("[INFO] Created MainScreenGui")

        self.setWindowTitle("[CMS] Main View")

        self.main_layout = QVBoxLayout()

        self.central_widget = QWidget()
        # Define the topbar
        self.topbar = QWidget()

        self.topbar_layout = QHBoxLayout()

        self.tb_help_button = QPushButton("?")
        self.tb_help_button.setFixedWidth(30)

        self.tb_spacer = QLabel("  ")
        self.tb_spacer.setFixedWidth(600)

        self.tb_logout_button = QPushButton("Logout")
        self.tb_logout_button.setFixedWidth(100)

        self.topbar_layout.addWidget(self.tb_help_button)
        self.topbar_layout.addWidget(self.tb_spacer)
        self.topbar_layout.addWidget(self.tb_logout_button)

        self.topbar.setLayout(self.topbar_layout)

        self.main_layout.addWidget(self.topbar)

        # Finish defining the topbar


        # Define the views for the view_switcher
        # Diary View

        diary_view = DiaryView(user)

        # Task View
        task_view = TaskView(user)

        # Resources view
        resources_view = ResourcesView()


        # Define the view switcher

        self.view_switcher = QTabWidget()
        self.view_switcher.addTab(diary_view, "Planner")
        self.view_switcher.addTab(task_view, "Tasks")
        self.view_switcher.addTab(resources_view, "Resources")

        self.view_switcher.setFont(GBodyFont)

        # End the definitions for the view swtich
        # Add the task view to the window
        self.main_layout.addWidget(self.view_switcher)


        # Fill in the window
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
