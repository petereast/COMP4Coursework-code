from PyQt4.QtCore import *
from PyQt4.QtGui import *

from NewTaskDialog import *

from GlobalResources import *
from Tasks import *

class TaskView(QWidget):
    def __init__(self, user = None):
        super().__init__()
        self.user = user

        self.main_layout = QVBoxLayout()


        self.title = QLabel("Outstanding Tasks")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.title)

        # Set up the two-pane view

        self.pane_container = QWidget()
        self.pane_layout = QHBoxLayout()

        # Left side
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        ##Task list

        self.task_list_view = QListView()

        # Add some example data
        data = QStandardItemModel()

        # This will be fetched from a database using different code in another class        
        exampleItems = [Task("Hello world", "Testing 123", 2), Task("Hello again world :)","This is a demo", 2)]

        for item in exampleItems:
            tmp = QStandardItem(item.text)

            tmp.setCheckable(True)

            data.appendRow(tmp)

        self.task_list_view.setModel(data)

        self.left_layout.addWidget(self.task_list_view)
        self.left_widget.setLayout(self.left_layout)

        self.pane_layout.addWidget(self.left_widget)
        # End Left pane
        # Start right pane

        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout()

        self.add_new_task_button = QPushButton("Add new Task")
        self.add_new_task_button.setFixedWidth(150)
        self.add_new_task_button.clicked.connect(self.display_new_task_dialog)
        self.right_layout.addWidget(self.add_new_task_button)

        self.spacer = QLabel(" ")
        self.spacer.setFixedHeight(300)
        self.right_layout.addWidget(self.spacer)

        self.right_widget.setLayout(self.right_layout)
        self.pane_layout.addWidget(self.right_widget)
        # End right pane


        self.pane_container.setLayout(self.pane_layout)
        self.main_layout.addWidget(self.pane_container)

        self.setLayout(self.main_layout)

    def display_new_task_dialog(self):
        new_task_dialog = NewTaskDialog()

        new_task_dialog.exec_()
