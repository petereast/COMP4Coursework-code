# New Meeting Dialog

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class NewMeetingDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()


        self.setLayout(self.main_layout)
