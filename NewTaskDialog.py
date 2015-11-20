# NewTaskDialogGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class NewTaskDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setWindowTitle("Add new task")
        self.smalltitle = QLabel("Create new task")
        self.smalltitle.setFont(GBodyFont)
        self.title = QLabel("New Task")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.smalltitle)
        self.main_layout.addWidget(self.title)

        self.title_entry_label = QLabel("Title:")
        self.main_layout.addWidget(self.title_entry_label)
        self.title_entry = QLineEdit("")
        self.title_entry.textChanged.connect(self.update_window_title)
        self.main_layout.addWidget(self.title_entry)

        self.people_entry_label = QLabel("With whom:")
        self.main_layout.addWidget(self.people_entry_label)

        self.people_entry = QLineEdit()
        self.people_entry.textChanged.connect(self.check_names)


        self.setLayout(self.main_layout)

    def update_window_title(self):
        newtext = self.title_entry.text().title()[0:45]
        if newtext == "":
            self.title.setText("New Task")
        else:
            self.title.setText(newtext)
        self.title_entry.setText(newtext)
        self.setWindowTitle(newtext)


        self.title_entry.setFixedWidth(self.title.width())

    def check_names(self):
        # Add some name checking functionality
        pass
