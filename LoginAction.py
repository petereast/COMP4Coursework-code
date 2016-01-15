#Login action:
#   The code and database actions performed when the user attempts to log into the system.

import hashlib

from DatabaseInit import *
import SqlDictionary

class User:
    def __init__(self, uid=0):
        self.info = {} # info to be retrieved from the database
        self.permissions = {}
        self.user_id = uid

        self.dbinterface = UsersInfo()

        self.update_user_info()

    def gen_pw_hash(self, password):
        phash = hashlib.md5()
        phash.update(bytes(password, "UTF-8"))
        return phash.hexdigest()

    def password_hash_cmp(self, password_input):
        currenthash = self.info["Password"]
        print(currenthash)
        print(self.gen_pw_hash(password_input))
        return currenthash == self.gen_pw_hash(password_input)

    def add_user(self, info=None):

        if info == None:
            info = self.info

        dbinterface = UsersInfo()
        dbinterface.add_user(info)

    def update_user_info(self):
        raw_info = self.dbinterface.get_all_users("WHERE(UserID = {0})".format(self.user_id))[0]
        self.info["UserID"] =  self.user_id
        self.info["Name"] = raw_info[1]
        self.info["Username"] = raw_info[2]
        self.info["Password"] =  raw_info[3]
        self.info["Permissions"] = raw_info[4]
        self.gen_permissions()
        self.id = self.info["UserID"]

    def gen_permissions(self):
        perm = self.info["Permissions"]
        blist = [False, False, False, False, False]
        for index, digit in enumerate(bin(int(perm))[2:]):
            blist[index] = (bool(digit))
        permissions = {}
        permissions["Meetings"] = blist[0]
        permissions["Tasks"] = blist[1]
        permissions["Resources"] = blist[2]
        permissions["ChangeOwnData"] = blist[3]
        permissions["Admin"] = blist[4]
        self.permissions = permissions
        return permissions

class UserSession(User):
    def __init__(self):
        print("[USER] [INFO] Session start")
