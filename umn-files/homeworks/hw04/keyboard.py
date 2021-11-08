# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 4

#==========================================
# Purpose: this function detects repeated characters and if they pass a certain threshold, returns them to the user
# Input Parameter(s): phrase (the phrase to be checked), and the maximum amount of times a letter can be repeated (it's automatically set to 2 but can be changed by the user)
# Return Value(s): a list of letters repeated more than the max_repeat value
#==========================================

def flag_keys(phrase, max_repeat=2):
	char_list = []
	current_char = ""
	repeat_occur = 1

	for i in range(len(phrase)):
		if current_char != phrase[i] or current_char == "":
			current_char = phrase[i]
			repeat_occur = 1
		
		else:
			repeat_occur += 1

			if repeat_occur > max_repeat and current_char not in char_list:
				char_list.append(current_char)

	return char_list

if __name__ == '__main__': # I honestly can't think of any edge cases, so I used the cases provided in the instructions
	flag_keys('Heeellooo Wooorld', 2)
	flag_keys('Heeeellooo Wooorllld', 3)
	flag_keys('Iii aaam bbbattmmman', 2)
	flag_keys('Heeellooo Wooorllld')