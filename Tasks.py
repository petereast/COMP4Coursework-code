# Copyright (c) 2015 Copyright Holder All Rights Reserved.

class Task:
    def __init__(self, title="", subtitle="", priority=1):
        self.title = title
        self.priority = priority
        self.subtitle = subtitle
        self.text  = self.title + "\n  " + self.subtitle

    def complete(self):
        self.title+= " [Done]"
        self.priority = -1
