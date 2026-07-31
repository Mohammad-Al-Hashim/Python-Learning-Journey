"""
I built a PIN Code Guessing Game and learned a new concept:
how to make the computer randomly choose any digit number using random.randint() — in this case, a 4-digit PIN number is between 1000 and 9999.
Fun fact: the probability of actually guessing the right PIN is nearly impossible (1 in 9000!) 😅 
But that wasn't really the point — I built this to practice coding and apply what I've learned. On to the next project. 🚀
"""
import random
user_pin = int(input("Please type 4-digit PIN code: "))
computer_pin = random.randint(1000,9999)
if len(str(user_pin)) != 4:
    print("Sorry, you must enter 4-digit PIN code")
else:
    if user_pin == computer_pin:
        print("Success! PIN code matched!")
    else:
        print("Failure! PIN code didn't match.")
        print(f"The computer generated this PIN: {computer_pin}")
