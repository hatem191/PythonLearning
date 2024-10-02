import random

# This is an experimental version of the program to test some conditional statements.
play = ["rock", "paper", "scissors"]
art = {
    "rock": '''    
    _______
---'   ____)____
          ______)
rock     _______)
         _______)
---.__________)''',
    "paper": '''    
    _______
---'   ____)____
          ______)
paper    _______)
         _______)
---.__________)''',
    "scissors": '''    
    _______
---'   ____)_________
          ______)____
scissors _________)___
      (____)_________
---.__(___)'''
}

player = input("Enter rock, paper, or scissors: ").lower()
opponent = random.choice(play)

if player not in play:
    print("Invalid selection.")
else:
    print(f"Opponent chose: {opponent}\n{art[opponent]}\n")
    print(f"You chose: {player}\n{art[player]}\n")

    if player == opponent:
        result = "It's a tie!"
    elif (player == "rock" and opponent == "scissors") or \
         (player == "paper" and opponent == "rock") or \
         (player == "scissors" and opponent == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    print(result)
