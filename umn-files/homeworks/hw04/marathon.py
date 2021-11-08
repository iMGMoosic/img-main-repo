# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 4

#==========================================
# Purpose: This function checks a csv file and returns the amount of miles a particular person has ran
# Input Parameter(s): file_name, which is the name of the csv file, and member, which is who you're searching for
# Return Value(s): returns an integer of the number of miles the member ran, or -1 if the file isn't found
#==========================================

def miles_run(file_name, member):
	miles = 0

	try:
		file = open(file_name, "r")
	
	except FileNotFoundError:
		try:
			file = open(file_name + ".csv", "r")
		
		except FileNotFoundError:
			print("File does not exist.")
			return -1
	
	lines = file.readlines()
	
	for line in lines:
		split_line = line.split(",")
		
		if split_line[0] == member:
			miles += int(split_line[1])
	
	return miles
