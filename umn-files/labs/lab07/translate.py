def pig_latin(string):
	vowels = ["a", "e", "i", "o", "u"]
	pig_latin_string = ""
	word_lst = string.split()
	for i in range(0, len(word_lst)):
		if word_lst[i][0].lower() in vowels:
			word_lst[i] = word_lst[i] + "way"
		else:
			first_letter = word_lst[i][0]
			word_lst[i] = word_lst[i][1:]
			word_lst[i] += str(first_letter.lower()) + "ay"

	for i in range(0, len(word_lst)):
		pig_latin_string += word_lst[i] + " "
		pig_latin_string = pig_latin_string.capitalize()

	return pig_latin_string
