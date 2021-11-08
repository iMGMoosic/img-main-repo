def min_max_nums(string):
	small_num = 0
	big_num = 0
	word_lst = string.split()

	for i in range(0, len(word_lst)):
		if len(word_lst[i]) < small_num or small_num == 0:
			small_num = len(word_lst[i])
		if len(word_lst[i]) > big_num or big_num == 0:
			big_num = len(word_lst[i])

	min_max_lst = [small_num, big_num]
	return min_max_lst
