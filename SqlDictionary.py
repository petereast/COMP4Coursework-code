# sql dictionary
# This file will contain all of the SQL references used throughout the system, with string formatting already
# added

#initialisation scripts

CREATE_USERS = """CREATE TABLE IF NOT EXISTS Users
                (UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Username TEXT,
                Password TEXT,
                Permissions INTEGER # A 5-bit permisions string
                );
"""

#Permissions: Like unix file permissions but using denary instead of octal
# and there are 5 bits rather than several.

# time to design databases - NOW!

CREATE_MEETINGS = """CREATE TABLE IF NOT EXISTS Meetings
                (MeetingID INTEGER PRIMARY KEY AUTOINCREMENT,
                OwnerID INTEGER,
                Title TEXT,
                ISOTime TEXT,
                Location TEXT,
                Confirmed BOOLEAN,
                Attendees INTEGER # Foreign Key -- see table -
                );

                CREATE TABLE IF NOT EXISTS MeetingAttendee
                (
                    #I NEED ANOTHER COMPOSITE KEEY!!
                );
"""

CREATE_TASKS = """CREATE TABLE IF NOT EXISTS Tasks
                (TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Description TEXT,
                Owner INTEGER, # Foreign Key to form a one to many with `users`
                Attendees INTEGER # Foreign Key to form a many to many with Users
                );

                CREATE TABLE IF NOT EXISTS TaskAttendee
                (
                    #HOW DO I COMPOSITE KEYY???
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
"
