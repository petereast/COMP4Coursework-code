from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

from MeetingWidget import *
from NewMeetingDialog import *
from Meetings import Meeting
from RespondToPendingRequestsDialog import *
from IndicatorBadge import *

class DiaryView(QWidget):
    def __init__(self, user = None):
        super().__init__()
        self.user = user
        print("[INFO] Created MainScreenGuiDiaryView")

        self.main_layout = QVBoxLayout()

        self.title = QLabel("Upcoming Meetings & Appointments")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.title)

        self.middle_widget = QWidget()
        self.middle_layout = QHBoxLayout()

        # Define the left-side stuff
        self.left_side_widget = QWidget()
        self.left_side_layout = QVBoxLayout()

        self.meetings_widget = QWidget()
        self.meetings_layout = QVBoxLayout()

        # Start to do a slightly more indepth meetings code
        # Get meetings from the database
        # Enumerate these meetings
        # have an array of meetingss objects

        #Get a list of meetings
        meetings_list = MeetingsInfo(None).get_meetings_by_owner(user.id)
        print("{0} Meeting(s) found.".format(len(meetings_list)))
        meetings_widgets = []
        for m in meetings_list:
            meetings_widgets.append(MeetingOverview(Meeting(meeting_id=m[0])))
            self.meetings_layout.addWidget(meetings_widgets[-1])

        self._update_meeting_list()


        self.meetings_widget.setLayout(self.meetings_layout)
        #self.meetings_widget.setMinimumSize(300, 700)


        self.meetings_container_widget = QScrollArea()
        self.meetings_container_widget.setWidget(self.meetings_widget)
        self.meetings_container_widget.setVerticalScrollBarPolicy(2)
        self.left_side_layout.addWidget(self.meetings_container_widget)

        self.left_side_widget.setLayout(self.left_side_layout)
        self.middle_layout.addWidget(self.left_side_widget)

        # End of left side
        # Define the right side stuff

        self.right_side_widget = QWidget()
        self.right_side_layout = QVBoxLayout()#

        # Right side widgets...
        self.button_container = QWidget()
        self.button_container_layout = QVBoxLayout()

        self.add_new_appointment_button = QPushButton("New Appointment")
        self.add_new_appointment_button.clicked.connect(self.display_new_meeting_dialog)
        self.button_container_layout.addWidget(self.add_new_appointment_button)

        # TODO: Add some kind of indicator to show the amound of unread pending meetings

        self.response_container = QWidget()
        self.response_layout = QHBoxLayout()

        self.respond_to_pending_appointments_button = QPushButton("Respond to Pending Appointments")
        self.respond_to_pending_appointments_button.clicked.connect(self.display_respond_to_meetings_dialog)
        self.respond_to_pending_appointments_button.setFixedHeight(30)
        self.response_layout.addWidget(self.respond_to_pending_appointments_button)

        self.pending_number = Indicator(len(MeetingsInfo().get_outstanding_meetings(self.user.id)))
        self.response_layout.addWidget(self.pending_number)

        self.response_container.setLayout(self.response_layout)
        self.button_container_layout.addWidget(self.response_container)

        self.button_container.setLayout(self.button_container_layout)
        self.right_side_layout.addWidget(self.button_container)

        self.spacer1 = QLabel(" ")
        self.spacer1.setFixedHeight(270)
        self.right_side_layout.addWidget(self.spacer1)


        self.right_side_widget.setLayout(self.right_side_layout)
        self.middle_layout.addWidget(self.right_side_widget)

        self.middle_widget.setLayout(self.middle_layout)
        self.main_layout.addWidget(self.middle_widget)
        self.setLayout(self.main_layout)

    def _update_meeting_list(self):
        del self.meetings_widget

        self.meetings_widget = QWidget()
        self.meetings_layout = QVBoxLayout()

        # Start to do a slightly more indepth meetings code
        # Get meetings from the database
        # Enumerate these meetings
        # have an array of meetingss objects

        #Get a list of meetings
        meetings_list = MeetingsInfo(None).get_meetings_by_owner(self.user.id)
        print("{0} Meeting(s) found.".format(len(meetings_list)))
        meetings_widgets = []
        for m in meetings_list:
            meetings_widgets.append(MeetingOverview(Meeting(meeting_id=m[0])))
            self.meetings_layout.addWidget(meetings_widgets[-1])



    def display_new_meeting_dialog(self):
        new_meeting_dialog = NewMeetingDialog(self.user)
        new_meeting_dialog.exec_()
        self._update_meeting_list()

    def display_respond_to_meetings_dialog(self):
        self.pending_number.update(self.pending_number.getValue()-1)
        respond_to_meetings_dialog = RespondToPendingMeetingDialog(self.user)
        respond_to_meetings_dialog.exec_()
