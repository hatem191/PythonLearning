import random

# This is a list of words used for this hangman game
list_of_words = ["goat", "cow", "donkey", "lion", "car", "train", "cat", "dog","house", "street"]
word_as_list = []
selected_word = ""
random_word = ""

def make_a_guess():
    return input("Guess one of the characters in the list, enter it to check: ")

def chose_a_random_word():
    return random.choice(list_of_words)

def check_the_guess(guess, word_as_list):
    print("The guess is " + guess)
    length_of_guess = len(guess)
    count = 0
    if length_of_guess > 1 and count < 3:
        print("You can only guess one character at a time")
        count+=1
    else:
        if guess in word_as_list:
            print("You guessed a correct letter!")
            return guess
        else:
            print("You guessed incorrectly")

def print_selected_word(verify_random_letter):
    number_of_letters = len(verify_random_letter)
    print("The selected word is " + verify_random_letter)
    print("The number of letters in the word is " + str(number_of_letters))
    print("Thank you!")

def create_a_list():
    return list(selected_word)

# Function to check the guess
#make_a_guess()
check_the_guess(make_a_guess())
print_selected_word()

