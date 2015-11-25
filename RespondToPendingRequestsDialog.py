# Respond to meeting requests

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *
from Meetings import Meeting
from MeetingWidget import *

class RespondToPendingMeetingDialog(QDialog):
    def __init__(self):
        super().__init__()

        #Respond to meeting request,
        # two panes, one for a list of pending meetings,
        # another for a tools and controls to deal with those
        # pending meetings
        self.setWindowTitle("Respond to Pending Requests")
        self.main_layout = QVBoxLayout()

        self.title = QLabel("Respond to Pending Requests")
        self.title.setFont(GTitleFont)
        self.main_layout.addWidget(self.title)

        self.pane_container = QWidget()
        self.pane_container_layout = QHBoxLayout()
        self.left_pane = QWidget()
        self.left_pane_layout = QVBoxLayout()

        self.meetings_list_view = QListView()
        data = QStandardItemModel()

        # All of the following code is to be replaced with database intergration
        test_data = [Meeting(), Meeting(), Meeting()]

        for meeting in test_data:
            tmp = QStandardItem(meeting.title+"\n"+meeting.place+"\n"+meeting.when)

            data.appendRow(tmp)

        self.meetings_list_view.setModel(data)
        # End of 'following code'
        self.left_pane_layout.addWidget(self.meetings_list_view)


        self.left_pane.setLayout(self.left_pane_layout)

        self.right_pane = QWidget()
        self.right_pane_layout = QVBoxLayout()



        self.pane_container_layout.addWidget(self.left_pane)
        self.pane_container_layout.addWidget(self.right_pane)
        self.pane_container.setLayout(self.pane_container_layout)
        self.main_layout.addWidget(self.pane_container)


        self.setLayout(self.main_layout)
