from turtle import *

draw_finish_line = Turtle()
draw_finish_line.penup()
draw_finish_line.setpos(150,-20)
draw_finish_line.pendown()
draw_finish_line.left(90)
draw_finish_line.forward(60)
turtle1 = Turtle()
turtle2 = Turtle()
turtle1.setpos(0,0)
turtle2.setpos(0,20)

player_1_first_jump = int(input("Please enter Player 1's first jump: "))
player_2_first_jump = int(input("Please enter Player 2's first jump: "))

turtle1.forward(player_1_first_jump)
turtle2.forward(player_2_first_jump)

player_1_second_jump = int(input("Please enter Player 1's second jump: "))
player_2_second_jump = int(input("Please enter Player 2's second jump: "))

turtle1.forward(player_1_second_jump)
turtle2.forward(player_2_second_jump)

player_1_third_jump = int(input("Please enter Player 1's third jump: "))
player_2_third_jump = int(input("Please enter Player 2's first jump: "))

turtle1.forward(player_1_third_jump)
turtle2.forward(player_2_third_jump)

print("Game over.")
