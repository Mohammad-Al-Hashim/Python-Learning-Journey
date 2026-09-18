#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1
if False:
    print("Welcome to the multiplication table.")
    number = int(input("Enter a number less than 10: \n"))
    operate = print(f"{number}x{range(0,11)}={number*range(0,11)}")
    if number > 10:
        print("You must enter a number less than 10, Try again")
    else:
        print(operate)

#V2
print("Welcome to the multiplication table.")
number = int(input("Enter a number less than 10: "))
if number > 10:
    print("You must enter a number less than 10. Try again")
else:
    for i in range(0,11):
        print(f"{number} x {i} = {number*i}")
