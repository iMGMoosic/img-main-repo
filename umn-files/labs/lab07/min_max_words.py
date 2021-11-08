def min_max_words(string):
	small_num = 0
	small_word_lst = []
	big_num = 0
	big_word_lst = []
	word_lst = string.split()

	for i in range(0, len(word_lst)):
		if len(word_lst[i]) <= small_num or small_num == 0:
			small_num = len(word_lst[i])
			small_word_lst.append(word_lst[i])
		if len(word_lst[i]) >= big_num or big_num == 0:
			big_num = len(word_lst[i])
			big_word_lst.append(word_lst[i])

	for i in range(0, len(small_word_lst)):
		if len(small_word_lst[i]) != small_num:
			small_word_lst[i] = ""

	for i in range(0, len(big_word_lst)):
		if len(big_word_lst[i]) != big_num:
			big_word_lst[i] = ""

	small_word_lst_new = [i for i in small_word_lst if i != ""]
	big_word_lst_new = [i for i in big_word_lst if i != ""]

	min_max_lst = [small_word_lst_new, big_word_lst_new]
	return min_max_lst
