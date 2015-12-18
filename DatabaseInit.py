# DatabaseInit
# main program

import SqlDictionary
 #this tidies all the SQL queries into another namespace
import sqlite3

class Database:
    """This is the general database wrapper that I'll use throughout the system"""
    def __init__(self, child, database_name="cmsdb.db"):
        print("[INFO] Created database object")

        self.db_name = database_name

    def _connect_and_execute(self, sql="", database_name=None):
        if database_name == None:
            database_name = self.db_name

        with sqlite3.connect(self.db_name) as dbcon:
            cursor = dbcon.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()

        print("[INFO] Executed SQL query \"{0}\"".format(sql))
        return results

class UsersInfo(Database):
    def __init__(self):
        super().__init__(self)
        self.create_table()

    # NB: all input MUST be sanitized at this point.
    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_USERS)

    def get_all_users(self, condition = ""): # Add a SQL condition? maybe? TODO: refactor this bit
        return self._connect_and_execute(SqlDictionary.GET_ALL_USERS.format(condition))

    def get_uid_by_username(self, username=""):
        return self._connect_and_execute((SqlDictionary.GET_USER_ID.format(username)))[0][0]

    def add_user(self, info):
        #info follows the format {"SQL value":Data value}
        values = "`{0}`, `{1}`, `{2}`, {3}".format(info["Name"], info["Username"], info["Password"], info["Permissions"])

        return self._connect_and_execute(SqlDictionary.ADD_USER.format(values))

    # TODO: Add more features as they become necessary.

class TasksInfo(Database):

    def __init__(self):
        super().__init__(self, "Tasks")
        self.create_table()

    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_TASKS)


class MeetingsInfo(Database):
    def __init__(self, meeting_info):
        super().__init__(self)
        self.create_table()
        self.meeting_info = meeting_info

    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_MEETINGS)
        self._connect_and_execute(SqlDictionary.CREATE_MEETINGS_ATTENEDEES)

    def add_meeting(self):
        SQL_DATA = "{0}, '{1}', '{2}', '{3}', '{4}'".format(self.meeting_info["OwnerID"],
            self.meeting_info["Title"],
            self.meeting_info["ISOTime"],
            self.meeting_info["Location"],
            self.meeting_info["Attendees"])
        self._connect_and_execute(SqlDictionary.ADD_MEETING.format(SQL_DATA)) #TODO Sort out the formatting.

    def get_meeting_info(self):
        sql_condition = "WHERE (MeetingID = {0})".format(self.meeting_info['MeetingID'])
        q = SqlDictionary.GET_MEETING.format(sql_condition)
        results = self._connect_and_execute(q)
        return results[0]


    def get_meetings_by_owner(self, OwnerID):
        sql_condition = "WHERE (OwnerID = {0})".format(OwnerID)
        q = SqlDictionary.GET_MEETING_ID_LIST.format(sql_condition)
        return self._connect_and_execute(q)
