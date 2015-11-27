from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *


class ResourcesView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.title =  QLabel("Resources")
        self.title.setFont(GTitleFont)
        self.main_layout.addWidget(self.title)

        self.pane_container = QWidget()
        self.pane_container_layout = QHBoxLayout()

        self.left_pane_container = QWidget()
        self.left_pane_layout = QVBoxLayout()


        self.setLayout(self.main_layout)
