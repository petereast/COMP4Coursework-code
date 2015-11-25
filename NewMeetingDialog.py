# New Meeting Dialog

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class NewMeetingDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.setWindowTitle("Add New Meeting")

        self.title = QLabel("Add New Meeting")
        self.title.setFont(GTitleFont)
        self.main_layout.addWidget(self.title)


        self.meeting_title_label = QLabel("Meeting Title:")
        self.main_layout.addWidget(self.meeting_title_label)
        self.meeting_title_entry = QLineEdit()
        self.main_layout.addWidget(self.meeting_title_entry)

        self.attendees_label = QLabel("Attendees:")
        self.main_layout.addWidget(self.attendees_label)
        self.attendees_entry = QLineEdit()
        self.main_layout.addWidget(self.attendees_entry)

        self.where_label = QLabel("Where")
        self.main_layout.addWidget(self.where_label)
        self.where_entry = QLineEdit()
        self.main_layout.addWidget(self.where_entry)

        self.button_container_widget = QWidget()
        self.button_container_layout = QHBoxLayout()

        self.save_button = QPushButton("Save")
        self.button_container_layout.addWidget(self.save_button)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        self.button_container_layout.addWidget(self.cancel_button)

        self.button_container_widget.setLayout(self.button_container_layout)
        self.main_layout.addWidget(self.button_container_widget)

        self.setLayout(self.main_layout)
