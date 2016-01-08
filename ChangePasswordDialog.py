# The dialog for changing a user's password

from PyQt4 import QtCore
from PyQt4 import QtGui

from DatabaseInit import UsersInfo
from GlobalResources import *


class ChangePasswordDialog(QDialog):
    def __init__(self, user):
        self.user = user
        
        self.setWindowTitle("Change your password")
               
        self.layout = QVBoxLayout()
        
        self.title = QLabel("Change your password")
        self.title.setFont(GTitleFont)
        self.layout.addWidget(self.title)
        
        
        self.setLayout(self.layout)
    




