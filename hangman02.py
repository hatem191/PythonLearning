import random

# This is a list of words used for this hangman game
list_of_words = ["goat", "cow", "donkey", "lion", "car", "train", "cat", "dog", "house", "street"]
selected_word = ""
word_as_list = []
guessed_letters = []
attempts_remaining = 6

def make_a_guess():
    return input("Guess one of the characters in the word: ").lower()

def choose_a_random_word():
    return random.choice(list_of_words)

def check_the_guess(guess, word_as_list):
    if len(guess) > 1:
        print("You can only guess one character at a time")
        return False
    elif guess in guessed_letters:
        print("You already guessed that letter!")
        return False
    else:
        guessed_letters.append(guess)
        if guess in word_as_list:
            print("You guessed a correct letter!")
            return True
        else:
            print("You guessed incorrectly")
            return False

def print_selected_word(word_as_list, guessed_letters):
    display_word = [letter if letter in guessed_letters else '_' for letter in word_as_list]
    print("Current word: " + " ".join(display_word))

def create_a_list(selected_word):
    return list(selected_word)

def has_won(word_as_list, guessed_letters):
    return all(letter in guessed_letters for letter in word_as_list)

# Main game logic
selected_word = choose_a_random_word()
word_as_list = create_a_list(selected_word)
print("Welcome to Hangman!")
print_selected_word(word_as_list, guessed_letters)

while attempts_remaining > 0 and not has_won(word_as_list, guessed_letters):
    guess = make_a_guess()
    if check_the_guess(guess, word_as_list):
        print_selected_word(word_as_list, guessed_letters)
    else:
        attempts_remaining -= 1
        print(f"Incorrect guess! Attempts remaining: {attempts_remaining}")
        print_selected_word(word_as_list, guessed_letters)

# Check win or lose condition
if has_won(word_as_list, guessed_letters):
    print(f"Congratulations! You've guessed the word: {selected_word}")
else:
    print(f"Game over! The word was: {selected_word}")
