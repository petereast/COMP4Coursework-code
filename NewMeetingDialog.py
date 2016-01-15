# New Meeting Dialog

import re

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

from DatabaseInit import *

class UsernameLookup(QDialog):
    def __init__(self):
        super().__init__()
        pass

    # This will contain a list widget 


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
        # self.attendees_entry.textChanged.connect(self._add_attendees)
        self.attendees_info_label = QLabel("A list of usernames seperated by semicolons")
        self.attendees_info_label.setFont(GSmallText)

        # Create a dialog with an index of usernames and users to include

        self.where_label = QLabel("Where")
        self.main_layout.addWidget(self.where_label)
        self.where_entry = QLineEdit()
        self.main_layout.addWidget(self.where_entry)

        self.when_label = QLabel("When")
        self.main_layout.addWidget(self.when_label)
        self.when_entry = QDateTimeEdit()
        self.when_entry.setMinimumDate(QDate.currentDate())
        self.when_entry.setMinimumTime(QTime.currentTime())
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
        self._add_attendees(meeting)
        self.close()

    def _add_attendees(self, meeting):
        raw_attendee_list = self.attendees_entry.text()
        #Parse this into a list of attendees, seperated by eiter semicolons or commas.
        pattern = re.compile("([a-zA-Z]+;?)")
        # Iterate through the list of attendees
        print(pattern.findall(raw_attendee_list))
        
        for string in pattern.findall(raw_attendee_list):
            
            if string[-1] == ";":
                string = string[0:-1]
            try:
                attendeeID = UsersInfo().get_uid_by_username(string)
            except IndexError:
                print("[WARN] Username '{0}' not recognised".format(string))
                attendeeID = 0
            if attendeeID:
                meeting.add_meeting_attendee(attendeeID)
                
        

        
