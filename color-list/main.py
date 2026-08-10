#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1
if False:
    colors = []
    first_color = input("Add the first color you like: ")
    user_choice = input("Do you want to add more colors? type Yes Or No: ").lower()
    if user_choice == "yes" or user_choice == "no":
        if user_choice == "yes":
            second_color = input("Add another color to the list: ")
            colors.append(first_color)
            colors.append(second_color)
            print(f"The colors you like are: {colors}")
        else:
            colors.append(first_color)
            print(f"The colors you like are: {colors}")
    else:
        print("You must type either yes or no. Try again")

#V2: (I applied the new concept that I realized:) (see my story behind this project in this folder)
colors = []
best_color = input("Add the first color you like: ")
colors.append(best_color)
user_choice = input("Do you want to add more colors? type Yes Or No: ").lower()
if user_choice == "yes" or user_choice == "no":
    if user_choice == "no":
        print(f"The colors you like are: {colors}")
    else:
        best_color = input("Add another color to the list: ")
        colors.append(best_color)
        print(f"The colors you like are: {colors}")
else:
    print("You must type either yes or no. Try again")



