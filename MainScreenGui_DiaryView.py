from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class DiaryView(QWidget):
    def __init__(self):
        super().__init__()

        print("[INFO] Created MainScreenGuiDiaryView")

        self.main_layout = QVBoxLayout()

        self.title = QLabel("Upcoming Meetings & Appointments")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.title)


        self.setLayout(self.main_layout)
