import random

play = ["rock", "paper", "scissors"]

opponent_random_selection = random.choice(play)
print("Welcome to the game rock, paper, or scissors!\n\n")
player_selection = input("Please enter your selection of either rock, paper, or scissors: ")

if player_selection == opponent_random_selection:
    print("It is a tie.")
else:
    if opponent_random_selection == "rock" and player_selection == "paper":
        print("You win!")
    elif opponent_random_selection == "rock" and player_selection == "scissors":
        print("You lose!")
    elif opponent_random_selection == "paper" and player_selection == "rock":
        print("You lose!")
    elif opponent_random_selection == "paper" and player_selection == "scissors":
        print("You win!")
    elif opponent_random_selection == "scissors" and player_selection == "paper":
        print("You lose!")
    elif opponent_random_selection == "scissors" and player_selection == "rock":
        print("You win!")
    else:
        print("Invalid Selection: Only chose rock, paper, or scissors.")
print("Your opponent selected " + opponent_random_selection + " and you chose " + player_selection)
