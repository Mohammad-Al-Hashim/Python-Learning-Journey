import random
import sys

print("Welcome to Hangman game!")
words = ["history", "bad" , "ugly", "computer", "good" , "fantastic"]
computer_word = random.choice(words)
space = ["_"] * len(computer_word)
lives = 6
hangman_stages = [
    '''
  +---+
  |   |
      |
      |
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
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
tries = []
print(hangman_stages[0])
while "_" in space and lives > 0:
    print(" ".join(space))
    user_guess = input("Please guess a letter ").lower()
    if user_guess in tries:
        print(f"You guessed that before, guess another one. You have {lives} tries.")
        continue
    else:
        tries.append(user_guess)
        if user_guess not in computer_word:
            lives -= 1
            if lives > 0:
                print(f"Oops! You guessed an incorrect letter. Try again. You have {lives} tries.")
                print(hangman_stages[6-lives])
            else:
                print("Oops! You guessed an incorrect letter. And You used all your tries.")
                print(hangman_stages[6-lives])
        else:
            for position in range(len(computer_word)):
                if computer_word[position] == user_guess:
                    space[position] = user_guess
            print(f"You have {lives} tries")
print(" ".join(space))

if lives == 0:
    print("Game over. Try again")
    sys.exit()
else:
    print("Congratulations! You win!")
