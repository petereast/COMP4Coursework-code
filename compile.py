# PyPackager - a simple utility designed to compile and decompile a set of 
# python files.

# Program stages
# Iterate through a python file, searching for import statements
# get the module name from those statements and check if it's in the
# module's directory
# open that file & find repeat the process

# once a list of filenames (&paths)  has been collected,
# open the files
# remove whitespace and comments
# (maybe) rename the variables to one or two character names
# write the squashed code to a (binary?) file or database ready for
# extraction

import os, sys
import re as regex

def parse_file(file_data, filenames_set):
	pattern = regex.compile("from +[a-zA-Z\_]* import +[a-zA-Z\*]*\n") 
	for string in pattern.findall(file_data):
		filename = string[string.find(" ")+1:string.find(" ", string.find(" ")+1)]+".py"
		filenames_set.add(filename)
		parse_file(open(filename).read(), filenames_set)
		del filename
	pattern = regex.compile("import +[a-zA-Z\_]*\n")
	for string in pattern.findall(file_data):
		# find all the instances where the user uses import not from 
		# whatever import class
		# This will also include all the imports of builtin classes
		# so we're going to have to do some error handling! yay
		filename = string[string.find(" ")+1:-1]+".py"
		try:
			open(filename)
			filenames_set.add(filename)
			parse_file(open(filename).read(), filenames_set)
		except FileNotFoundError:
			pass 
def squash_file(filename):
	# returns a string of the squashed file
	f = open(filename)
	lines = f.readlines()
	f.close()
	outlines = ['@@@{0}@@@\n'.format(filename)]
	for l in lines:
		tmpl = l.strip()
		if tmpl == "":
			pass
		elif tmpl[0] == "#":
			pass
		else:
			outlines+=l
	return "".join(outlines)
def conjoin_files(filenames_set):
	# returns a string of the conjoined file
	outfiles = []
	for f in filenames_set:
		outfiles.append(squash_file(f))
	return "\n".join(outfiles)
	
def unconjoin_files(conjoined_file_data):
	# creates a directory containing the various files that have been squashed
	inlines = conjoined_file_data.split("\n")
	startline, endline, alternator = 0, 0, False
	for index, line in enumerate(inlines):
		if line[:3] == "@@@":
			filename = line[3:line.find("@@@", 4)]
			if not alternator:
				startline = index
			else:
				endline = index
				print(startline, endline)
print(squash_file("main.py"))
#Testing stuff
filenames_set = {"main.py"}
f = open("main.py")
parse_file(f.read(), filenames_set)
print(filenames_set)
print(len(filenames_set))
for f in filenames_set:
	print(f)
c = conjoin_files(filenames_set)
print(c, file=open("allc.py", "w"))
unconjoin_files(c)
