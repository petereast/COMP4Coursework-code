# Meetings.py - Class definition for use with meetings stuff

from GlobalResources import *

class Meeting:
    def __init__(self, title="[Blank Meeting]", place="[Nowhere]", attendees=["[Demo Person 1]", "[Demo Person 2]"], when="[Sometime]"):
        #Attendees to be a list of people objects

        self.title = title
        self.place = place
        self.attendees = attendees
        self.when = when