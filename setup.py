# This is the setup script which will install the software package into the
# wherever it's meant to be.

import sys, uuid, random, os
import httplib

Dependancies = True

# Check that the user has PyQt installed
try:
    import PyQt4.QtCore
except ImportError:
    print("You do not have the correct version of PyQt installed :(")
    Depedancies = False
    # TODO: Automatically download the PyQt installation file for the
    # detected OS

# Check that the user has access to SQLite

try:
    import sqlite3
except ImportError:
    print("You are unable to use databases because you're a spaz")
    Dependancies = False

# The dependencies checks are done, now for the 

if Dependancies:
    pass
# TODO: Implement the PyPacker code to unpack the squashed project code.
