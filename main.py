
# import core depenencies
import sys, time, random

# import Qt depenencies
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import custom classes
from LoginScreenGui import LoginWindow

# Main Program

def main():

    print("[INFO] Startup")

    application = QApplication(sys.argv)
    login_window = LoginWindow()


    login_window.show()
    login_window.raise_()

    application.exec_()


    print("[INFO] Execution complete")


if __name__ == "__main__":
    main()
