# Copyright (c) 2015 Copyright Holder All Rights Reserved.

from DatabaseInit import TasksInfo

class Task:
    def __init__(self, title="", subtitle="", priority=1, databaseid=None):
        if databaseid == None:
            self.title = title
            self.priority = priority
            self.subtitle = subtitle
            self.text  = self.title + "\n  " + self.subtitle
        else:
            #Load the info from the database.
            pass

    def load_task_from_database(self, taskid):
        pass

    def complete(self):
        self.title+= " [Done]"
        self.priority = -1
