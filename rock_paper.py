import random

play = ["rock", "paper", "scissors"]
player_status = ""
rock_picture = '''    
    _______
---'   ____)____
          ______)
 rock    _______)
         _______)
---.__________)
'''

scissors_picture='''    
    _______
---'   ____)_________
 scissors ______)____
       __________)___
      (____)_________
---.__(___)
'''

paper_picture='''    
    _______
---'   ____)____
          ______)
paper     _______)
         _______)
---.__________)
'''



opponent_random_selection = random.choice(play)
print("Welcome to the game rock, paper, or scissors!\n\n")
player_selection = input("Please enter your selection of either rock, paper, or scissors: ")

if player_selection not in play:
    print("Invalid Selection: Only choose rock, paper, or scissors.")
else:
    if player_selection == opponent_random_selection:
        player_status="It is a tie."
    else:
        if opponent_random_selection == "rock" and player_selection == "paper":
            player_status = "You win!"
        elif opponent_random_selection == "rock" and player_selection == "scissors":
            player_status = "You lose!"
        elif opponent_random_selection == "paper" and player_selection == "rock":
            player_status = "You lose!"
        elif opponent_random_selection == "paper" and player_selection == "scissors":
            player_status = "You win!"
        elif opponent_random_selection == "scissors" and player_selection == "paper":
            player_status = "You lose!"
        elif opponent_random_selection == "scissors" and player_selection == "rock":
            player_status = "You win!"
        else:
            print("Invalid Selection: Only chose rock, paper, or scissors.")


print("Your opponent selected " + opponent_random_selection + " and you chose " + player_selection + "\n")

print("Opponent Selection\n")
if opponent_random_selection == "rock":
    print(rock_picture)
elif opponent_random_selection == "paper":
    print(paper_picture)
elif opponent_random_selection == "scissors":
    print(scissors_picture)
else:
    print("Invalid Selection\n")

print("Your Selection\n")
if player_selection == "rock":
    print(rock_picture)
elif player_selection == "paper":
    print(paper_picture)
elif player_selection == "scissors":
    print(scissors_picture)
else:
    print("Invalid Selection\n")

print("\n\n" + "Your Final Status is: " + player_status)
