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

word_list = ["avocado", "apple", "tomato", "orange", "nectarine", "lemon", "pineapple", "grapes", "strawberry",
             "blueberry", "raspberry"]

random.shuffle(word_list)
word_chosen = word_list.pop()

misses = 0
incorrect_guesses = ["Incorrect Guesses: "]


used_letters = ["Used Letters: "]

done = False

while not done:
    print("Welcome to Hangman!! :) ")
    print(gallows[0])
    print(used_letters)

    for letter in word_chosen:
        if letter in used_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    word_guess = str(input("What letter could it be? "))
    if word_guess in used_letters:
        print("Sorry, you've already used that letter.")

    elif word_guess in word_chosen:
        used_letters.append(word_guess)
        print("Yay! You guessed a correct letter!")

    else:
        print("Sorry, that's not in the word.")
        misses += 1
        incorrect_guesses.append(word_guess)
        print(incorrect_guesses)
        print(gallows)  # print one more than what you currently have

    if used_letters == word_chosen:
        print("Wow, you guessed the whole word! Good job!")
        print("Thanks for playing!")
        done = True

    if misses >= 10 or gallows[6]:
        print("You ran out of all your guesses, sorry :( ")
        done = True

    # things we still need to include: end game checks to see if the user has gotten all of the letters in the
    # word, check to see if the user has too many misses, and properly end the game or allow user to replay















