# A little script for totalling up the number of lines of code in a directory

import os

def code_list():
    total = 0
    dir = os.listdir(os.getcwd())
    for file in dir:
        if file[-2:] == "py" and file != "linecounter.py":
            with open(file) as f:
                total += len(f.readlines())
                print("Read {0}".format(file))
    return total
print(code_list(), "Lines of code")