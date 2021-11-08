import random

fname = input("Please input the name of the file you would like to create (leave off extension): ")
file = open((fname + ".csv"), "w")
for i in range(0, 100):
	file.write(str(i + 1) + "," + str(random.randint(-1000, 1000)) + "\n")
file.close()