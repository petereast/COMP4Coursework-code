from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *


class ResourcesView(QWidget):
    def __init__(self, user):

        self.user = user
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.title =  QLabel("Resources")
        self.title.setFont(GTitleFont)
        self.main_layout.addWidget(self.title)

        self.pane_container = QWidget()
        self.pane_container_layout = QHBoxLayout()

        self.left_pane_container = QWidget()
        self.left_pane_layout = QVBoxLayout()


        self.placeholder = QLabel(" placeholder ")
        self.placeholder.setFixedSize(400, 400)
        self.left_pane_layout.addWidget(self.placeholder)
        # This is where I'll define the tabular view.
        # there also needs to be some code for getting sections of information
        # from the database - otherwise it won't work.

        self.left_pane_container.setLayout(self.left_pane_layout)
        self.pane_container_layout.addWidget(self.left_pane_container)
        self.right_pane_container = QWidget()
        self.right_pane_layout = QVBoxLayout()

        self.add_items_button = QPushButton("Add Resource")
        self.right_pane_layout.addWidget(self.add_items_button)

        self.view_urgent_requirements_button = QPushButton("View urgent requirements")
        self.right_pane_layout.addWidget(self.view_urgent_requirements_button)

        self.right_pane_container.setLayout(self.right_pane_layout)
        self.pane_container_layout.addWidget(self.right_pane_container)

        self.pane_container.setLayout(self.pane_container_layout)
        self.main_layout.addWidget(self.pane_container)

        self.setLayout(self.main_layout)
