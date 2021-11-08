# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 3

#==========================================
# Purpose: This function finds the values that are in all lists passed to the function, in this case, the students that are in every club
# Input Parameter(s): student_list, which is a list of lists of students in clubs
# Return Value(s): returns a list with the values that occur in all n sublists
#==========================================

def busybody(student_list):
	unique_values = []
	busybodies = []
	merged_list = [j for i in student_list for j in i]

	for i in range(0, len(merged_list)): # adds unique values to unique_values for comparison
		if merged_list[i] not in unique_values:
			unique_values.append(merged_list[i])

# since busybodies would be in all clubs, and the student list includes a list for each club
# if the amount of times a name occurs is equal to the amount of lists in the student_list
# that person is a busybody

	for i in range(0, len(unique_values)):
		if merged_list.count(unique_values[i]) == len(student_list):
			busybodies.append(unique_values[i])

	return busybodies