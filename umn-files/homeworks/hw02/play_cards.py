# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 2

#==========================================
# Purpose: This function lets the user play cards with the computer using random number generation
# Input Parameter(s): No input parameters
# Return Value(s): Nothing is returned
#==========================================

import random

def play_cards():
    print("Game start!")
    
    card_1 = random.randint(1,9)
    card_2 = random.randint(1,9)
    card_3 = random.randint(1,9)
    
    print("Your cards are: " + str(card_1) + ", " + str(card_2) + ", & " + str(card_3))
    
    flag = "Player 1"
    rnd = 1
    p1_score = 0
    p2_score = 0

    while flag == "Player 1" or flag == "Player 2" or flag == "Determine": # catch all for when the game is still active
        while flag == "Player 1":
            print("Round " + str(rnd) + ":")
        
            p1_card_played = int(input("Enter the card index of the card you'd like to play: "))
        
            if p1_card_played in range(1,4):
                if p1_card_played == 1 and card_1 != "":
                    p1_card_played = card_1
                    card_1 = ""
                    flag = "Player 2"
                elif p1_card_played == 2 and card_2 != "":
                    p1_card_played = card_2
                    card_2 = ""
                    flag = "Player 2"
                elif p1_card_played == 3 and card_3 != "":
                    p1_card_played = card_3
                    card_3 = ""
                    flag = "Player 2"
                else:
                    print("That is not a valid card.")
            else:
                print("That is not a valid input. Index must be between (1-3).")

        while flag == "Player 2":
            p2_card_played = random.randint(1,9)
        
            print("You played: " + str(p1_card_played))
            print("The computer plays: " + str(p2_card_played))

            if p1_card_played > p2_card_played:
                p1_score += 1
                flag = "Determine"
            elif p2_card_played > p1_card_played:
                p2_score += 1
                flag = "Determine"
            else:
                p1_score += 1
                p2_score += 1
                flag = "Determine"

        while flag == "Determine":
            print("Score: Player " + str(p1_score) + ", Computer " + str(p2_score))

            if rnd == 3:
                flag = "End"
            else:
                rnd += 1
                flag = "Player 1"

    while flag == "End":
        if p1_card_played > p2_card_played:
            print("You win!")
            flag = ""
        elif p2_card_played > p1_card_played:
            print("The computer wins.")
            flag = ""
        else:
            print("It's a tie!")
            flag = ""

    return
