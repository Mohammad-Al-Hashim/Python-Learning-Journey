typed_text=input("Enter the text \n")
user_choice=input("Convert to (lowercase) or (uppercase)? \n")
if user_choice == "lowercase":
    print(typed_text.lower())
elif user_choice == "uppercase":
    print(typed_text.upper())
else:
    print("You must type either lowercase or uppercase")
