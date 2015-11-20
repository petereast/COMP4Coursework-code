# NewTaskDialogGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class NewTaskDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setWindowTitle("Add new task")
        self.title = QLabel("New Task")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.title)

        self.setLayout(self.main_layout)
