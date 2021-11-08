from turtle import *
from math import *

turtle1 = Turtle()
turtle1.penup()
turtle1.setpos(-960, -540)
turtle1.pendown()
previous_close = 0.0
file = open("AAPL.csv", "r")
file.readline()
for i in range(1, 254):
	current_line = file.readline()
	current_line = current_line.split(",")
	current_close = float(current_line[3])
	if previous_close != 0 and current_close - previous_close >= 0:
		diff = current_close - previous_close
		turtle1.left(degrees(atan(diff / 5)))
		turtle1.forward(((diff ** 2) + 25) ** 0.5)
		turtle1.right(degrees(atan(diff / 5)))
	elif previous_close != 0 and current_close - previous_close <= 0:
		diff = current_close - previous_close
		turtle1.right(degrees(atan(diff / 5)))
		turtle1.forward(((diff ** 2) + 25) ** 0.5)
		turtle1.left(degrees(atan(diff / 5)))
	else:
		turtle1.left(90)
		turtle1.forward(current_close)
		turtle1.right(90)
	previous_close = current_close