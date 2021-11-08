string = " "
lst = []

while string != "":
	string = input("Enter word: ")
	if string == "":
		pass
	else:
		lower_string = string.lower()
		first_char = lower_string[0]
		if lower_string.count(first_char) >= 2:
			lst.append(string)

print(*lst,sep='\n')
