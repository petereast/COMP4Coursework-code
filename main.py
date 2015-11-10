
# import core depenencies
import sys, time, random

# import Qt depenencies
from PyQt4.Core import *
from PyQt4.Gui import *

# import custom classes
from LoginScreenGui import LoginWindow

# Main Program

def main():

    application = QApplication(sys.argv)
    login_window = LoginWindow()

    login_window.show()
    login_window._raise_()
    login_window.exec_()


    print("Execution complete")


if __name__ == "__main__":
    main()
