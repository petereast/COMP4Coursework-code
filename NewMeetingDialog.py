# New Meeting Dialog

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

from DatabaseInit import MeetingsInfo

class NewMeetingDialog(QDialog):
    def __init__(self, user = None):
        super().__init__()
        self.user = user
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

        self.when_label = QLabel("When")
        self.main_layout.addWidget(self.when_label)
        self.when_entry = QLineEdit()
        self.main_layout.addWidget(self.when_entry)

        self.button_container_widget = QWidget()
        self.button_container_layout = QHBoxLayout()

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.add_meeting)
        self.button_container_layout.addWidget(self.save_button)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        self.button_container_layout.addWidget(self.cancel_button)

        self.button_container_widget.setLayout(self.button_container_layout)
        self.main_layout.addWidget(self.button_container_widget)

        self.setLayout(self.main_layout)

    def add_meeting(self):
        info = {"OwnerID": self.user.id, # This is where to do the username lookup
            "Title":self.meeting_title_entry.text(),
            "ISOTime":self.when_entry.text(),
            "Location":self.where_entry.text(),
            "Attendees": 0 # This will work someday
        }
        meeting = MeetingsInfo(info)
        meeting.add_meeting()
        self.close()
