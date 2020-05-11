# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

print(gallows[4])
word_list = ["avocado", "apple", "tomato", "orange", "nectarine", "lemon", "pineapple", "grapes",
                          "strawberry",
                          "blueberry", "raspberry"]
random.shuffle(word_list)
word_chosen = word_list.pop()  # chooses a random word from the word list

incorrect_guesses = " "

used_letters = " "

misses = 0
done = False  # initializes variables

print("Welcome to Hangman!! :) ")

while not done:  # while loop
    print(gallows[misses])   # prints the gallows according to how many misses the user has
    print()
    print("Incorrect Guesses: ", end=" ")
    for guess in incorrect_guesses:
        print(guess, end=" ")  # prints amount of incorrect guesses
    print()
    print("Used Letters: ", end=" ")
    for letter in used_letters:
        print(letter, end=" ")  # prints amount of used letters that are correct
    print()

    for letter in word_chosen:
        if letter in used_letters:
            print(letter, end=" ")

        else:
            print("_", end=" ")  # if letter is present in used_letters, prints letter, but if not, an underscore
            # appears
            
    print()

    word_guess = str(input("What letter could be in this word? "))
    word_guess = word_guess.lower()
    if word_guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please try again, that's not a letter.")  # only lets the player enter a letter
    elif len(word_guess) > 1:
        print("Please enter a single letter.")  # doesn't let the user enter more than one letter

    else:
        if word_guess in used_letters:
            print("Sorry, you've already used that letter.")  # doesn't let the user enter a letter they've already
            # entered
        elif word_guess in word_chosen:
            used_letters = used_letters + word_guess
            print("Yay! You guessed a correct letter!")  # if player correctly guessed, adds it to used_letters

        elif word_guess not in word_chosen:
            incorrect_guesses = incorrect_guesses + word_guess
            print("Sorry, that's not in the word")
            misses += 1  # if player incorrectly guessed, adds letter to misses and incorrect_guesses

    for letter in word_chosen:
        if letter not in used_letters:
            break
    else:
        print("Wow! You guessed the whole word, which was", word_chosen + ".", "Thanks for playing!")
        done = True  # checks if user guessed the whole word then ends game if that is true
    if misses >= 6:
        print("You ran out of all your guesses, sorry :( ")
        done = True  # if misses are more than 6, game ends and player has lost

    if done is True:
        play_again = str(input("Do you want to play again? "))
        play_again = play_again.lower()
        if play_again == "yes":
            word_list = ["avocado", "apple", "tomato", "orange", "nectarine", "lemon", "pineapple", "grapes",
                          "strawberry",
                          "blueberry", "raspberry"]
            random.shuffle(word_list)
            word_chosen = word_list.pop()
            misses = 0
            incorrect_guesses = " "
            used_letters = " "
            done = False

        else:
            print("Cool, thanks for playing!")
            done = True  # allows for game replay if done is true
