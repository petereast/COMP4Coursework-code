

# import Qt depenencies
from PyQt4.Core import *
from PyQt4.Gui import *

class LoginWindow:
    def __init__(self):
        super().__init__()
        print("[INFO] Created Login window")

        self.main_title = QLabel("Welcome.")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.submit_button = QPushButton("Login")
        self.help_button = QPushButton("?")


        # TODO:
        # - include interactions with the user/pass entry
        # - Make the title bigger/change the font
        # - Anything else?

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.main_title)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.help_button)
        #self.layout.addWidget()

        self.setLayout(self.layout)
