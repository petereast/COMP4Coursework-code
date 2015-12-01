# DatabaseInit
# main program

import SqlDictionary #this tidies all the SQL queries into another namespace
import sqlite3

class Database:
    """This is the general database wrapper that I'll use throughout the system"""
    def __init__(self, database_name):
        print("[INFO] Created database")

        self.db_name = database_name

    def _connect_and_execute(self, sql="", database_name=self.db_name):
        with sqlite3.connect(database_name) as dbcon:
            cursor = dbcon.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
        return results

class UsersInfo(Database):
    def __init__(self):
        super().__init__(self, "Users")

    # NB: all input MUST be sanitized at this point.

    def get_all_users(self, condition = ""): #Add a SQL condition? maybe? TODO: refactor this bit
        self._connect_and_execute(SqlDictionary.GET_ALL_USERS.format(condition))

    def add_user(self, values):
        #Values as SQL string? TODO: reqrite this bit when a definite list of attributes is determined
        self._connect_and_execute(SqlDictionary.ADD_USER.format(values))

main()
