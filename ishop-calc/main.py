#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1:
if False:
    print("Welcome to i-shop calculator")
    number_typed = float(input("How many items are there in your basket today? "))
    items=range(1,number_typed+1)
    name_item_list = []
    price_item_list = []
    print("Lets get to counting them....")
    for item in items:
        name_item=input("Please tell me the name of item number:",item)
        name_item_list.append(name_item)
        price_item=input(f"What is the price of {name_item} ?")
        price_item_list.append(price_item)
        user_choice = input("Would you like to see your entire basket items? Type yes or no").lower()
        if user_choice not in ["yes","no"]:
            print("You must type either yes or no. You typed: ",user_choice)
        else:
            print(name_item_list)
            print("Would you like to see how much it'll cost? Type yes or no").lower()
            if user_choice not in ["yes","no"]:
                print("You must type either yes or no. You typed: ",user_choice)
            else:
                print("Buying these items will cost: ",sum(price_item_list))

#V2:
import sys

print("Welcome to i-shop calculator")
number_typed = int(input("How many items are there in your basket today? "))
if number_typed <=0:
    print("You must type a positive number. You typed: ",number_typed, "Try again")
    sys.exit()
items=range(1,number_typed+1)
name_item_list = []
price_item_list = []
print("Lets get to counting them....")
for item in items:
    name_item=input(f"Please tell me the name of item number: {item} \n")
    name_item_list.append(name_item)
    price_item=float(input(f"What is the price of {name_item} ? \n"))
    price_item_list.append(price_item)

user_choice = input("Would you like to see your entire basket items? Type yes or no \n").lower()
if user_choice not in ["yes","no"]:
    print("You must type either yes or no. You typed: ",user_choice)
else:
    print(name_item_list)
    user_choice = input("Would you like to see how much it'll cost? Type yes or no \n").lower()
    if user_choice not in ["yes","no"]:
        print("You must type either yes or no. You typed: ",user_choice)
    else:
        print("Buying these items will cost: ",sum(price_item_list))
