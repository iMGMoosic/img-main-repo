import random # for if computer_flag = True

def play_odds_evens():
	computer_flag = "" # initilization of flags
	player_flag = ""
	round_flag = 0

	com_choice = ""
	odd_even_choice = ""

	p1_state = ""
	p2_state = ""

	p1_choice = ""
	p2_choice = ""

	round_winner = ""
	p1_points = 0
	p2_points = 0

	while com_choice == "":
		com_choice = input("Would you like to play against the (c)omputer or another (h)uman? ")

		if com_choice != "c" and com_choice != "h":
			print("That is not a valid choice. Please try again.")
			com_choice = ""
		else:
			if com_choice == "c":
				computer_flag = True
			else:
				computer_flag = False

	while odd_even_choice == "":
		odd_even_choice = input("Would you like (o)dds or (e)vens? ")

		if odd_even_choice != "o" and odd_even_choice != "e":
			print("That is not a valid choice. Please try again.")
			odd_even_choice = ""
		else:
			if odd_even_choice == "o":
				p1_state = "Odd"
				p2_state = "Even"
			else:
				p1_state = "Even"
				p2_state = "Odd"

			round_flag += 1
			player_flag = "Player 1"

	while round_flag > 0 and round_flag <= 5:
		print("Round " + str(round_flag) + ":")

		print("Player 1 (" + p1_state + ") is up!")

		while player_flag == "Player 1":
			p1_choice = input("Please pick a number between 1 and 3: ")

			if int(p1_choice) < 1 or int(p1_choice) > 3:
				print("That is not a valid choice. Try again.")
			else:
				player_flag = "Player 2"

		if computer_flag == False:
			print("Player 2 (" + p2_state + ") is up!")
		else:
			print("The computer is thinking...")

		while player_flag == "Player 2":
			if computer_flag:
				p2_choice = random.randint(1, 3)
				player_flag = "Decision"
			else:
				p2_choice = input("Please pick a number between 1 and 3: ")

				if int(p2_choice) < 1 or int(p2_choice) > 3:
					print("That is not a valid choice. Try again.")
				else:
					player_flag = "Decision"

		while player_flag == "Decision":
			sum = int(p1_choice) + int(p2_choice)

			if sum % 2 == 0 and p1_state == "Even":
				p1_points += 1
				round_winner = "Player 1"
			elif sum % 2 == 0 and p2_state == "Even":
				p2_points += 1
				round_winner = "Player 2"
			elif sum % 2 == 1 and p1_state == "Odd":
				p1_points += 1
				round_winner = "Player 1"
			else:
				p2_points += 1
				round_winner = "Player 2"

			print("The sum of both players' choices is " + str(sum))
			print("The winner of this round is " + round_winner + "!")
			print("Player 1 currently has " + str(p1_points) + " point(s).")
			print("Player 2 currently has " + str(p2_points) + " point(s).")
			
			round_flag += 1
			round_winner = ""
			player_flag = "Player 1"

	if p1_points > p2_points:
		print("Player 1 wins!")
	else:
		print("Player 2 wins!")
