
#second version

typed_password=input("Please type your password \n")
correct_password="I LOVE PYTHON"
typed_username=input("Please type your username \n")
correct_username="SNAKE"
if typed_password == "I LOVE PYTHON" and typed_username == "SNAKE":
    print("Welcome to the app")
else:
    print("Sorry, wrong user name or password. TRY AGAIN")

#first version 

typed_password=input("Please type your password \n")
correct_password="I LOVE PYTHON"
if typed_password == correct_password:
    print("Welcome to the app")
else:
    print("Incorrect password, try again")
