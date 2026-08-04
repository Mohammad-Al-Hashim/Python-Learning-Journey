#1 paper 2 scissors  3 rock
import random
print("Welcome to rock paper scissors game")
user_choice = input("Type (Rock) Or (Paper) Or (Scissors) \n").lower()
computer_random_choice = random.randint(1,3)
if computer_random_choice == 1:
    computer_random_name = "paper"
elif computer_random_choice == 2:
    computer_random_name = "scissors"
else:
    computer_random_name = "rock"
if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    if user_choice == "rock" and computer_random_choice == 3 or user_choice == "scissors" and computer_random_choice == 2 or user_choice == "paper" and computer_random_choice == 1:
        print("It's a tie! We both chose the same thing.")
    elif user_choice == "rock" and computer_random_choice == 2 or user_choice == "scissors" and computer_random_choice == 1 or user_choice == "paper" and computer_random_choice == 3:
        print(f"CONGRATULATIONS! You win! [Your choice: {user_choice}] beats [computer's choice: {computer_random_name}]!")
    else:
        print(f"Sorry! You lose. [Computer's choice: {computer_random_name}] beats [your choice: {user_choice}]. Try again!")
else:
    print("You must enter (Paper) Or (Rock) Or (Scissors) Try again")
