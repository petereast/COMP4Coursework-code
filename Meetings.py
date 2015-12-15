# Meetings.py - Class definition for use with meetings stuff

from GlobalResources import *
from DatabaseInit import MeetingsInfo

class Meeting:
    def __init__(self, title="[Blank Meeting]", place="[Nowhere]", attendees=["[Demo Person 1]", "[Demo Person 2]"], when="[Sometime]", meeting_id=1):
        #Attendees to be a list of people objects

        self.title = title
        self.place = place
        self.attendees = attendees
        self.when = when
        self.meeting_id = meeting_id

        self.info = {"Title":title, "Location":place, "Attendees":attendees, "ISOTime":when, "MeetingID":meeting_id}

        self.load_meeting_from_database()

        self._update_info()

    def load_meeting_from_database(self, info=None):
        #provide functionality to get an individual meeting from a database.


        if info == None:
            info = self.info

        dbmeeting = MeetingsInfo(info)

        raw_info = dbmeeting.get_meeting_info()
        print(raw_info)
        self.info = {"Title":raw_info[2], "Location":raw_info[4], "ISOTime":raw_info[3], "MeetingID":raw_info[0]}

        # TODO: Add code to get the attendees from the MeetingAttendee table

        pass

    def _update_info(self):
        self.title = self.info["Title"]
        self.place = self.info["Location"]
        self.attendees = ['TODO', 'TODO'] # this'll be the entry point for the DB query
        self.when = self.info["ISOTime"]
        self.meeting_id = self.info["MeetingID"]
