# DatabaseInit
# main program

import SqlDictionary #this tidies all the SQL queries into another namespace
import sqlite3

class Database:
    """This is the general database wrapper that I'll use throughout the system"""
    def __init__(self, database_name):
        print("[INFO] Created database")

        self.db_name = database_name

    def _connect_and_execute(self, sql="", database_name=None):
        if database_name == None:
            database_name = self.db_name

        with sqlite3.connect(database_name) as dbcon:
            cursor = dbcon.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
        return results

class UsersInfo(Database):
    def __init__(self):
        super().__init__(self, "Users")
        self.create_table()

    # NB: all input MUST be sanitized at this point.
    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_USERS)

    def get_all_users(self, condition = ""): #Add a SQL condition? maybe? TODO: refactor this bit
        return self._connect_and_execute(SqlDictionary.GET_ALL_USERS.format(condition))

    def add_user(self, values):
        #Values as SQL string? TODO: reqrite this bit when a definite list of attributes is determined
        return self._connect_and_execute(SqlDictionary.ADD_USER.format(values))

    # TODO: Add more features as they become necessary.

class TasksInfo(Database):

    def __init__(self):
        super().__init__(self, "Tasks")
        self.create_table()

    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_TASKS)


class MeetingsInfo(Database):
    def __init__(self):
        super().__init__(self, "Meetings")
        self.create_table()

    def create_table(self):
        self._connect_and_execute(SqlDictionary.CREATE_MEETINGS)
