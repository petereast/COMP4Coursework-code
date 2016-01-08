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
        #print(sql)
        if database_name == None:
            database_name = self.db_name

        with sqlite3.connect(self.db_name) as dbcon:
            cursor = dbcon.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()

        #print("[INFO] Executed SQL query \"{0}\"".format(sql))
        return results

class UsersInfo(Database):
    def __init__(self, uid = 0):
        super().__init__(self)
        self.create_table()

    # NB: all input MUST be sanitized at this point.
    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_USERS)

    def get_all_users(self, condition = ""): # Add a SQL condition? maybe? TODO: refactor this bit
        return self._connect_and_execute(SqlDictionary.GET_ALL_USERS.format(condition))

    def get_uid_by_username(self, username=""):
        return self._connect_and_execute((SqlDictionary.GET_USER_ID.format(username)))[0][0]

    def get_username_by_uid(self, uid=None):
        return self._connect_and_execute(SqlDictionary.GET_USERNAME_BY_UID.format(uid))[0][0]

    def add_user(self, info):
        #info follows the format {"SQL value":Data value}
        values = "`{0}`, `{1}`, `{2}`, {3}".format(info["Name"], info["Username"], info["Password"], info["Permissions"])

        return self._connect_and_execute(SqlDictionary.ADD_USER.format(values))

    # TODO: Add more features as they become necessary.

class TasksInfo(Database):

    def __init__(self):
        super().__init__(self)
        self.create_table()

    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_TASKS)
        self._connect_and_execute(SqlDictionary.CREATE_TASKATTENDEE)

    def get_info_by_id(self, task_id):
        sql = SqlDictionary.GET_TASK.format("WHERE (TaskID = {0})".format(task_id))
        raw = self._connect_and_execute(sql)[0]
        return {"TaskID":raw[0], "Title":raw[1], "Description":raw[2], "OwnerID":raw[3], "Attendees":raw[4]}

    def get_ids_by_owner(self, owner_id):
        sql = SqlDictionary.GET_TASK_ID_LIST.format("WHERE Owner = {0}".format(owner_id))
        output_ids = []
        for row in self._connect_and_execute(sql):
            output_ids.append(row[0])
        return output_ids

    def add_task(self, info):
        SQL_DATA = """'{0}', '{1}', {2}, {3}""".format(info["Title"], info["Description"], info["OwnerID"], info["Attendees"])
        self._connect_and_execute(SqlDictionary.ADD_TASK.format(SQL_DATA))



class MeetingsInfo(Database):
    def __init__(self, meeting_info = None):
        super().__init__(self)
        self.create_table()
        self.meeting_info = meeting_info
        self.id = None

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
        self.id = self._connect_and_execute("SELECT Max(MeetingID) FROM Meetings;")[0][0]

    def get_meeting_info(self):
        sql_condition = "WHERE (MeetingID = {0})".format(self.meeting_info['MeetingID'])
        q = SqlDictionary.GET_MEETING.format(sql_condition)
        results = self._connect_and_execute(q)
        return results[0]

    def add_meeting_attendee(self, user_id):
        sql_values = """{0}, {1}, 0""".format(self.id, user_id)
        return self._connect_and_execute(SqlDictionary.ADD_MEETING_ATTENDEE.format(sql_values))


    def get_meetings_by_owner(self, OwnerID):
        sql_condition = "WHERE (OwnerID = {0})".format(OwnerID)
        q = SqlDictionary.GET_MEETING_ID_LIST.format(sql_condition)
        return self._connect_and_execute(q)

    def get_outstanding_meetings(self, OwnerID):
        results = self._connect_and_execute(SqlDictionary.GET_OUTSTANDING_MEETINGS_TO_BE_ATTENDED.format(OwnerID))
        return results

    def get_meeting_attendees(self, MeetingID):
        return self._connect_and_execute(SqlDictionary.GET_MEETING_ATTENDEES.format(MeetingID))
