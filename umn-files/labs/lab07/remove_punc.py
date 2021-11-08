def remove_punc(text, punc):
	punc_list = []
	new_text = ""
	for i in range(0, len(punc)):
		punc_list.append(punc[i])
	for i in range(0, len(text)):
		if text[i] not in punc_list:
			new_text += text[i]

	return new_text
