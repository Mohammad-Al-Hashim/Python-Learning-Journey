age=int(input("How old are you? \n"))
if age >= 18:
    status=input("Type wether you are a student or employee or unemployed \n").lower()
    if status == "student":
        print("Your ticket price is: 15$")
    elif status == "unemployed":
        print("Your ticket price is 10$")
    elif status == "employee":
        print("Your ticket price is 20$")
    else:
        print("You must choose (student) or (employee) or (unemployed)")
else:
    print("Your ticket price is: 5$")
