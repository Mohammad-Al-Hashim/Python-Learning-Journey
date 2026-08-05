#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1
if False:
    import random

    print("WElCOME to (Whose wallet)")
    print("You will give me a list of names, and I will pick a person to pay")
    names_string = input("Please enter the names separated by a comma: \n")
    names = names_string.split(", ")
    names_number = len(names)
    names_index = len(names) -1
    random_number = random.randint(0,names_index)
    random_person = names[random_number]
    print(f"Please ask {random_person} to take his wallet out. The dinner is on him.")

#V2
if False:
    import random

    print("""
    Welcome to (WHOSE WALLET). You will give me a list of names, and I will pick a person to pay.      
    """)
    names = input("Please enter the names separated by a comma: \n").split(", ")
    random_person = random.choice(names)
    print(f"Please ask {random_person} to take his wallet out. The dinner is on him.")

#V3
import random

print("WELCOME to (WHOSE WALLET) \nYou will give me a list of names, and I will pick a person to pay.")
print(f"Please ask {random.choice(input("Please enter the names separated by a comma: \n").split(", "))} to take his wallet out. The dinner is on him.")

