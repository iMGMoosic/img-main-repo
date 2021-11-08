def longest_substring(string):
	length_substring = 0
	length_substring_temp = 0
	substring = ""
	substring_temp = ""

	for i in range(0, len(string)):
		if string[i] not in substring_temp:
			substring_temp += string[i]
		else:
			length_substring_temp = len(substring_temp)
			if length_substring_temp > length_substring:
				length_substring = length_substring_temp
				substring = substring_temp
				substring_temp = string[i]
				length_substring_temp = 1

	return substring