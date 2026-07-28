age=int(input("How old are you? \n"))
license_possession=input("Do you have a license? Enter Yes or No \n")
if license_possession.lower() == "yes" and age >= 18:
    print("You can drive a car")
elif license_possession.lower() == "no" or age < 18:
    print("You cannot drive a car")
else:
    print("You must choose either Yes or No")
