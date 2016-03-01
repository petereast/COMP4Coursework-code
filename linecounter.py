# A little script for totalling up the number of lines of code in a directory

import os

def code_list():
    complete_code = []
    total = 0
    dir = os.listdir(os.getcwd())
    for file in dir:
        if file[-2:] == "py" and file != "linecounter.py":
            with open(file) as f:
                c = f.readlines()
                complete_code += c
                total += len(c)
                print("Read {0}".format(file))
    print("".join(complete_code), file=open("all.py", "w"))
    return total
print(code_list(), "Lines of code")
