# part 1 of ica
# values that could cause ValueError: anything not an integer (float, string, etc.)
# values that could cause ZeroDivisionError: 0

def word_count(fname):
	try:
		file = open(fname, "r")
		contents = file.read()
		word_lst = contents.split()
		file.close()
		return len(word_lst)
	except FileNotFoundError:
		print("Bad file name.")
		return -1
