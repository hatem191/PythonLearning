import random

# This is a list of words used for this hangman game
list_of_words = ["goat", "cow", "donkey", "lion", "car", "train", "cat", "dog", "house", "street"]
selected_word = ""
word_as_list = []

def make_a_guess():
    return input("Guess one of the characters in the word: ")

def choose_a_random_word():
    return random.choice(list_of_words)

def check_the_guess(guess, word_as_list):
    print("The guess is: " + guess)
    if len(guess) > 1:
        print("You can only guess one character at a time")
    else:
        if guess in word_as_list:
            print("You guessed a correct letter!")
            return guess
        else:
            print("You guessed incorrectly")

def print_selected_word(verify_random_word):
    number_of_letters = len(verify_random_word)
    print("The selected word is: " + verify_random_word)
    print("The number of letters in the word is: " + str(number_of_letters))

def create_a_list(selected_word):
    return list(selected_word)

# Main game logic
selected_word = choose_a_random_word()
word_as_list = create_a_list(selected_word)
print_selected_word(selected_word)

# Function to check the guess
guess = make_a_guess()
check_the_guess(guess, word_as_list)


