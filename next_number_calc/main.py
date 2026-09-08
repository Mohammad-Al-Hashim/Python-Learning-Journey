#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1:
if False:
    user_numbers = [(input("Please enter the numbers separated by a comma. \n"))]
    total = 0
    for i in int(user_numbers):
        print("Let's add each number to the next")
        print(total+i)
        print(f"----{total}")
    print(total)

#V2:
user_numbers = input("Please enter the numbers separated by a comma.").split(",")
total = 0
for i in user_numbers:
    print("Let's add each number to the next")
    total += int(i)
    print(f"----{total}")
print(f"The whole sum of the numbers is: {total}")
