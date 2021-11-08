def minimum_index(non_negative_integer_list, starting_index):
	minimum = "NA"
	flag = ""

	for i in range(starting_index, len(non_negative_integer_list)):
		if non_negative_integer_list[i] < 0:
			print("No negative integers are allowed in this list. Please try again.")
			flag = "not able to run"
			
	if flag == "not able to run":
		pass
	else:
		for i in range(starting_index, len(non_negative_integer_list)):
			if i == starting_index:
				minimum = non_negative_integer_list[i]
			else:
				if non_negative_integer_list[i] < minimum:
					minimum = non_negative_integer_list[i]

	return minimum
