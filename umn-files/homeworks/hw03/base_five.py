# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 3

#==========================================
# Purpose: This function takes a number num and changes it from base10 to base5 using modulo and integer division operators
# Input Parameter(s): num, which is the number that you would like to convert into base 5
# Return Value(s): the number in base 5 notation
#==========================================

def base_five(num):
	remainder = num
	new_num = ""
	digit_list = []
	while remainder >= 5: # remainder is the value left, not the remainder of the division
		digit_list.append(remainder % 5)
		remainder //= 5
	
	if remainder != 0:
		digit_list.append(remainder)
	
	digit_list.reverse()

	for i in range(0, len(digit_list)): # this converts the digit list into an actual integer for use in other parts of a program
		new_num += str(digit_list[i])
	
	return int(new_num)
