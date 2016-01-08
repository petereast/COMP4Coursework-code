# The dialog for changing a user's password

from PyQt4 import QtCore
from PyQt4 import QtGui

from DatabaseInit import UsersInfo
from GlobalResources import *


class ChangePasswordDialog(QDialog):
    def __init__(self, user):
        super().__init__()

        INPUT_WIDTH = 400
        LABEL_WIDTH = 200
        
        self.user = user
        
        self.setWindowTitle("Change your password")
               
        self.layout = QVBoxLayout()
        
        self.title = QLabel("Change your password")
        self.title.setFont(GTitleFont)
        self.layout.addWidget(self.title)

        self.pw_current_container = QWidget()
        self.pw_current_entry = QLineEdit()
        self.pw_current_entry.setFixedWidth(INPUT_WIDTH)
        self.pw_current_entry_label = QLabel("Enter your current password:")
        self.pw_current_entry_label.setFixedWidth(LABEL_WIDTH)
        
        self.pw_container_layout = QHBoxLayout()
        self.pw_container_layout.addWidget(self.pw_current_entry_label)
        self.pw_container_layout.addWidget(self.pw_current_entry)

        self.pw_current_container.setLayout(self.pw_container_layout)
        self.layout.addWidget(self.pw_current_container)

        self.new_pw_container = QWidget()
        self.new_pw_label = QLabel("Enter your new password:")
        self.new_pw_label.setFixedWidth(LABEL_WIDTH)
        self.new_pw_entry = QLineEdit()
        self.new_pw_entry.setFixedWidth(INPUT_WIDTH)

        self.new_pw_layout = QHBoxLayout()
        self.new_pw_layout.addWidget(self.new_pw_label)
        self.new_pw_layout.addWidget(self.new_pw_entry)

        self.new_pw_container.setLayout(self.new_pw_layout)
        self.layout.addWidget(self.new_pw_container)

        self.confirm_pw_container = QWidget()
        self.confirm_pw_label = QLabel("Confirm your new password:")
        self.confirm_pw_label.setFixedWidth(LABEL_WIDTH)
        self.confirm_pw_entry = QLineEdit()
        self.confirm_pw_entry.setFixedWidth(INPUT_WIDTH)

        self.confirm_pw_layout = QHBoxLayout()
        self.confirm_pw_layout.addWidget(self.confirm_pw_label)
        self.confirm_pw_layout.addWidget(self.confirm_pw_entry)

        self.confirm_pw_container.setLayout(self.confirm_pw_layout)
        self.layout.addWidget(self.confirm_pw_container)

        self.setFont(GBodyFont)
        
        self.setLayout(self.layout)
    
