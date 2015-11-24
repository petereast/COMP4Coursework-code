# Meeting overview widget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class MeetingOverview(QFrame):
    def __init__(self, title="[Blank Meeting]", place="[Nowhere]", attendees=["[Demo Person 1]", "[Demo Person 2]"]):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setFrameStyle(QFrame.Raised)

        # Define the widgets

        self.title = QLabel(title)
        self.title.setFont(GTitleFont)
        self.layout.addWidget(self.title)

        self.place_title = QLabel("At: "+place)
        self.layout.addWidget(self.place_title)

        self.attendees_title = QLabel("Attendees:")
        self.layout.addWidget(self.attendees_title)

        self.attendees_list = []
        for index, person in enumerate(attendees):
            self.attendees_title.setText(self.attendees_title.text()+"\n"+person)

        #self.setMinimumHeight(100)
        self.edit_button = QPushButton("Edit")
        self.edit_button.setFixedWidth(150)
        self.layout.addWidget(self.edit_button)


        self.setLayout(self.layout)
