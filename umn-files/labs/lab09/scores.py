def make_dictionary(list1, list2):
	dictionary = {}
	if len(list1) != len(list2):
		print("Lists are not equal in length.")
		return -1
	else:
		for i in range(len(list1)):
			dictionary[list1[i]] = list2[i]
		return dictionary

names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10,23,13,18,12]

score_dict = make_dictionary(names, scores)
print(score_dict["barb"])
score_dict["john"] = 19

score_dict = {"joe": 10, "sally": 12, "barb": 13, "sue": 18, "john": 19, "tom": 23}

del score_dict["tom"]

score_dict["sally"] = 13

def get_score(name, dictionary):
	if dictionary.has_key(name):
		return dictionary[name]
	else:
		print("Name does not exist in dictionary.")
		return -1