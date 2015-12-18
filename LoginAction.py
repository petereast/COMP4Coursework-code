#Login action:
#   The code and database actions performed when the user attempts to log into the system.

import hashlib

from DatabaseInit import *
import SqlDictionary

class User:
    def __init__(self, uid=0):
        self.info = {} # info to be retrieved from the database
        self.user_id = uid

    def _password_hash_cmp(self, password_input):
        currenthash = self.info["Password"]

        phash = hashlib.md5()
        phash.update(bytes(password_input, "UTF-8"))

        return currenthash == phash.hexdigest()

    def add_user(self, info=None):

        if info == None:
            info = self.info

        dbinterface = UsersInfo()
        dbinterface.add_user(info)

    def update_user_info(self):
        pass

class UserSession(User):
    def __init__(self):
        print("[USER] [INFO] Session start")
