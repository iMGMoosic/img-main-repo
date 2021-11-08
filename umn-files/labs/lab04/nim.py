flag = ""

while flag == "":
    answer = input("Would you like to go first? (y/n) ")
    if answer == "y" or answer == "Y":
        flag = "Player 1"
    elif answer == "n" or answer == "N":
        flag = "Player 2"
    else:
        flag = ""
        print("That is not a valid input. Please try again.")

objects = 21
take_away = 0

while flag == "Player 1" or flag == "Player 2":
    while flag == "Player 1":
        take_away = int(input(str(objects) + " objects remain, choose 1, 2, or 3: "))
        if take_away in range(1,4):
            objects -= take_away
        else:
            print("That is not a valid input. Please try again.")
            
        if objects <= 3 and flag == "Player 1":
            print("There are 3 or fewer objects remaining. The computer wins!")
            flag = "Win!"
        else:
            flag = "Player 2"
            
    while flag == "Player 2":
        if objects % 4 == 1:
            print(objects, "objects remain, I'll take 1.")
            objects -= 1
        elif objects % 4 == 2:
            print(objects, "objects remain, I'll take 2.")
            objects -= 2
        else:
            print(objects, "objects remain, I'll take 3.")
            objects -= 3
            
        if objects <= 3 and flag == "Player 2":
            print("There are 3 or fewer objects remaining. You win!")
            flag = "Win!"
        else:
            flag = "Player 1"
        
