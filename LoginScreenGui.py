import sys

# import Qt depenencies
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MainScreenGui import *
from GlobalResources import *

from LoginAction import *
from DatabaseInit import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("[INFO] Created Login window")

        self.setWindowTitle("[CMS] Login")

        self.main_title = QLabel("Welcome.")


        self.main_title.setFont(GTitleFont)

        # Create a labeled username feild:

        self.username_item = QWidget()

        self.username_layout = QHBoxLayout()


        self.username_label = QLabel("Username:")
        self.username_label.setFont(GBodyFont)
        self.username_label.setFixedWidth(150)

        self.username_input = QLineEdit()

        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)

        self.username_item.setLayout(self.username_layout)


        # Create a password feild

        self.password_item = QWidget()

        self.password_layout = QHBoxLayout()

        self.password_label = QLabel("Password:")
        self.password_label.setFont(GBodyFont)
        self.password_label.setFixedWidth(150)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)

        self.password_item.setLayout(self.password_layout)

        self.button_layout = QHBoxLayout()

        self.submit_button = QPushButton("Login")
        self.submit_button.clicked.connect(self.login_action)

        self.help_button = QPushButton("?")
        self.help_button.setFixedWidth(30)

        self.quit_button = QPushButton("Quit")

        self.button_layout.addWidget(self.submit_button)

        self.button_layout.addWidget(self.help_button)
        self.button_layout.addWidget(self.quit_button)

        # Add actions to the buttons within buttons_widget

        self.quit_button.clicked.connect(lambda: sys.exit(1))

        self.buttons_widget = QWidget()
        self.buttons_widget.setFixedWidth(300)
        self.buttons_widget.setLayout(self.button_layout)
        # TODO:
        # - include interactions with the user/pass entry
        # - Make the title bigger/change the font?
        # - Anything else?

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.main_title)
        self.layout.addWidget(self.username_item)
        self.layout.addWidget(self.password_item)
        self.layout.addWidget(self.buttons_widget)
        #self.layout.addWidget()

        self.widget = QWidget()
        self.widget.setFixedWidth(600)
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def login_action(self):

        userid = UsersInfo().get_uid_by_username(self.username_input.text())
        print(userid)

        user = User(userid)

        if user.password_hash_cmp(self.password_input.text()):
            pass


        self.main_screen = MainScreen()
        self.main_screen.show()
        self.main_screen.raise_()
        self.hide()
