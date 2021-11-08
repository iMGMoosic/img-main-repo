# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 3

#==========================================
# Purpose: This function finds the unique values that when added together equal the target
# Input Parameter(s): num_list is a list of numbers to check and target is the number that the user wants to add up to
# Return Value(s): the function prints each triple and then returns the amount of triples
#==========================================

def triples(num_list, target):
	num_list.sort()
	triples_count = 0
	used_numbers = []

	for i in range(0, len(num_list)):
		for j in range(1, len(num_list)):
			for k in range(2, len(num_list)):
				if i == j or i == k or j == k: # basically checks to make sure there aren't duplicate numbers in the triple calc
					pass
				elif num_list[i] in used_numbers and num_list[j] in used_numbers and num_list[k] in used_numbers: # also checks to make sure the triple hasn't been used before
					pass
				elif num_list[i] + num_list[j] + num_list[k] == target: # adds numbers to used_list and then prints the triple before incrementing the triple count
					used_numbers.append(num_list[i])
					used_numbers.append(num_list[j])
					used_numbers.append(num_list[k])
					print(str(num_list[i]) + " + " + str(num_list[j]) + " + " + str(num_list[k]) + " = " + str(target))
					triples_count += 1

	return triples_count
