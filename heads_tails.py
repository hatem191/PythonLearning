import random

print("This program is a randomized program that will print out heads or tails\n")

heads = 1
tails = 2

selection=''

start = input("Type start on this line to begin the random selection: ")
if start == 'start':
    random_selection = random.randint(1,2)
    print("The random selection is " + str(random_selection))
    if random_selection == 1:
        selection = 'heads'
    else:
        selection = 'tails'
    print("The random selection is " + selection)
else:
    print("You didn't type start, so the program ended. Goodbye and have a nice day!")
