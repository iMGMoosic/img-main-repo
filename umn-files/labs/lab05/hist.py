import random

lst = []

for i in range(1,10000):
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	die_sum = die1 + die2
	lst.append(die_sum)

print(format(2, "2d") + ": " + format(lst.count(2), "5d"))
print(format(3, "2d") + ": " + format(lst.count(3), "5d"))
print(format(4, "2d") + ": " + format(lst.count(4), "5d"))
print(format(5, "2d") + ": " + format(lst.count(5), "5d"))
print(format(6, "2d") + ": " + format(lst.count(6), "5d"))
print(format(7, "2d") + ": " + format(lst.count(7), "5d"))
print(format(8, "2d") + ": " + format(lst.count(8), "5d"))
print(format(9, "2d") + ": " + format(lst.count(9), "5d"))
print(format(10, "2d") + ": " + format(lst.count(10), "5d"))
print(format(11, "2d") + ": " + format(lst.count(11), "5d"))
print(format(12, "2d") + ": " + format(lst.count(12), "5d"))