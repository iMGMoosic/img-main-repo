file = open("2.5_day.csv", "r")
line = file.readline()
line = line.split(",")
for i in range(len(line)):
	print(i, line[i])
for i in range(1, 50):
	line = file.readline()
	line = line.split(",")
	mag = line[4]
	location = line[14]
	location.strip()
	location = location.replace("\"", "")
	print(mag, location)