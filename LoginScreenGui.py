

# import Qt depenencies
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LoginWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        print("[INFO] Created Login window")

        self.main_title = QLabel("Welcome.")

        # Create a labeled username feild:

        self.username_item = QWidget()

        self.username_layout = QHBoxLayout()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.username_layout.addWidget(self.username_label)

        self.username_item.setLayout(self.username_layout)


        self.password_input = QLineEdit()
        self.submit_button = QPushButton("Login")
        self.help_button = QPushButton("?")


        # TODO:
        # - include interactions with the user/pass entry
        # - Make the title bigger/change the font
        # - Anything else?

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.main_title)
        self.layout.addWidget(self.username_item)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.help_button)
        #self.layout.addWidget()

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
