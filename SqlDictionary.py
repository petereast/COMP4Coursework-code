# sql dictionary
# This file will contain all of the SQL references used throughout the system, with string formatting already
# added

#initialisation scripts

CREATE_USERS = """CREATE TABLE IF NOT EXISTS Users
                (UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Username TEXT,
                Password TEXT,
                Permissions INTEGER
                );
"""

#Permissions: Like unix file permissions but using denary instead of octal
# and there are 5 bits rather than several.
# eg 0b11010 - will give the user permission to use the meetings, tasks and user admin, and not resources management or privac.

# time to design databases - NOW!

CREATE_MEETINGS = """CREATE TABLE IF NOT EXISTS Meetings
                (MeetingID INTEGER PRIMARY KEY AUTOINCREMENT,
                OwnerID INTEGER,
                Title TEXT,
                ISOTime TEXT,
                Location TEXT
                );
"""

CREATE_MEETINGS_ATTENEDEES = """CREATE TABLE IF NOT EXISTS MeetingAttendee(
    MeetingID INTEGER,
    UserID INTEGER,
    Confirmed BOOLEAN
);"""

CREATE_TASKS = """CREATE TABLE IF NOT EXISTS Tasks
                (TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Description TEXT,
                Owner INTEGER,
                Attendees INTEGER
                );

                CREATE TABLE IF NOT EXISTS TaskAttendee
                (
                TaskId INTEGER,
                UserId INTEGER
                );
"""

CREATE_RESOURCES = """CREATE TABLE IF NOT EXISTS Resources
                (ResourceID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Cost INTEGER,
                QuantityAvailable INTEGER,
                QuantityRequired INTEGER
);
"""


GET_ALL_USERS = """ SELECT * FROM Users {0}; """

ADD_USER = """INSERT INTO Users(Name, Username, Password, Permissions) VALUES({0});"""


ADD_MEETING = """INSERT INTO Meetings(OwnerID, Title, ISOTime, Location, Attendees) VALUES({0})"""

GET_MEETING = """SELECT * FROM Meetings {0};"""

GET_MEETING_ID_LIST = """SELECT MeetingID FROM Meetings {0};"""
