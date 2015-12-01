# sql dictionary
# This file will contain all of the SQL references used throughout the system, with string formatting already
# added

#initialisation scripts

CREATE_USERS = """CREATE TABLE Users IF NOT EXISTS
                (UserID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,



                );

"""

# time to design databases - NOW!

CREATE_TASKS = """CREATE TABLE Tasks IF NOT EXISTS
                (TaskID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,



                );
"""

CREATE_RESOURCES = """CREATE TABLE Resources IF NOT EXISTS
                (ResourceID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,


);
"""


GET_ALL_USERS = """ SELECT * FROM Users {0}; """

ADD_USER = """INSERT INTO Users(null, other stuff) VALUES({0});"""
