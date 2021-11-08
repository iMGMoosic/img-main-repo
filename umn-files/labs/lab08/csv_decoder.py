min_val = 0
max_val = 0

fname = input("Please input the name of the file you would like to create (leave off extension): ")
try:
	file = open((fname + ".csv"), "r")
	contents = file.read()
	line_lst = contents.split("\n")
	for i in range(len(line_lst)):
		line_lst[i] = line_lst[i].split(",")
	line_lst.pop(100)
	for i in range(len(line_lst)):
		if int(line_lst[i][1]) <= min_val or min_val == 0:
			min_val = int(line_lst[i][1])
		if int(line_lst[i][1]) >= max_val or max_val == 0:
			max_val = int(line_lst[i][1])
	print("Minimum value:", min_val)
	print("Maximum value:", max_val)
	file.close()
except FileNotFoundError:
	print("Bad file name.")
