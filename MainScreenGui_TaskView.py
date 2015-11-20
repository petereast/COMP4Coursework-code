from PyQt4.QtCore import *
from PyQt4.QtGui import *


from GlobalResources import *
from Tasks import *

class TaskView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()


        self.title = QLabel("Outstanding Tasks")
        self.title.setFont(GTitleFont)

        self.main_layout.addWidget(self.title)


        ##Task list

        self.task_list_view = QListView()

        # Add some example data
        data = QStandardItemModel()

        exampleItems = [Task("Hello world", "Testing 123", 2)]

        for item in exampleItems:
            tmp = QStandardItem(item.text)

            tmp.setCheckable(True)

            data.appendRow(tmp)

        self.task_list_view.setModel(data)

        self.main_layout.addWidget(self.task_list_view)

        self.setLayout(self.main_layout)
