import random

#Stages represented in ASCII Graphics. Made in a list. 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Assigning variables for whether end_of_game is True or False.
# Made a list of words (word_list) that will be randomly chosen by the random module (chosen_word).
# (Word_length) will determine the amount of chars in randomly chosen word to reach all correct chances taken.

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Made difficulty level which determines how many chances the player gets before win or lose.

difficulty_level = input("Please choose your difficulty level:\n 1. Easy\n 2. Normal\n 3. Hard\n ")

if difficulty_level == '1':
  chances = 6
elif difficulty_level == '2':
  chances = 4
else:
  chances = 2

# This is just to see what word has been chosen by the random module.

print(f'Pssst, the solution is {chosen_word}.')

# Created blank list corresponding to the amount of chars in the chosen_word.

display = []
for _ in range(word_length):
    display += "_"

#Creating the condition that determines whether the game is over.
#Player chooses letter which is automatically lowercased with the lower() function.

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checks position of the word_length of chosen word. 
    for position in range(word_length):
        letter = chosen_word[position]

        # Checks if the guess matches any of the letters in the chosen_word to replace with correct letter.
      
        if letter == guess:
            display[position] = letter

    # If the guess is not any of the letters in the chosen word it reduces the amount of chances.
    # If chances run out. It's game over.
  
    if guess not in chosen_word:
      chances -= 1
      if chances == 0:
        end_of_game = True
        print("Haha loser!")
        print("Game over!")
  
    # Prints the hangman with "_" and correct guesses.
    print(f"{' '.join(display)}")

    # Checks to see if all blanks have been filled which if it has the user wins changing the condition of end of game to true. 
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Prints the ASCII Graphics corresponding to the stage of the hanged man depending on right or wrong guesses.
  
    print(stages[chances])