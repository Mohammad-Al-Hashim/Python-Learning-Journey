user_typed=input("Please enter (YES) or (NO) or (MAYBE) \n")
if user_typed == "YES":
    print("You typed: YES, correct choice!")
elif user_typed == "NO":
    print("You typed: NO, correct choice!")
elif user_typed == "MAYBE":
    print("You typed: MAYBE, correct choice!")
else:
    print(f"You typed: {user_typed}, which isn't one of the choices. Try again")
    