# Indicator Badge -  a PyQt widget to display a numerical indicator Badge

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GlobalResources import *

class Indicator(QWidget):
    """docstring for """
    def __init__(self, value = 0):
        super().__init__()
        self.value = value

        # do some cool stuff here :-)
