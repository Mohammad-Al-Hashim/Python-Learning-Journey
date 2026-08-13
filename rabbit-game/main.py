#NOTE: This file tracks my code evolution. The active version is at the bottom.
# You will see the struggle story behind this project in this folder.

#V1
if False:
    print("Welcome to (Place the rabbit.)")
    total_list = [
    ["🌿","🌿","🌿"],
    ["🌿","🌿","🌿"],
    ["🌿","🌿","🌿"],
    ]
    print(f"{total_list[0]}\n{total_list[1]}\n{total_list[2]} \nwhere should the rabbit go?")
    user_number = [input("Please choose a row and a column: \n")]
    if user_number[0] == 1 or user_number[0] == 2 or user_number[0] == 3:
        if user_number[1] == 1 or user_number[1] == 2 or user_number[1] ==3:
            total_list.insert(user_number[0] and user_number[1], "🐇")
            print(total_list)
    else:
        print("The first number or the second number must be (1 OR 2 OR 3)")

#V2
if False:
    print("Welcome to (Place the rabbit.)")
    list=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"],]
    print(f"{list[0]}\n{list[1]}\n{list[2]} \nwhere should the rabbit go?")
    user_number = int(input("Please choose a row and a column: \n"))
    row = user_number[0]
    column = user_number[1]
    if user_number[0] == 1 or user_number[0] == 2 or user_number[0] ==3:
        if user_number[1] == 1 or user_number[1] == 2 or user_number[1] ==3:
            list[row-1][column-1] = "🐇"
            print(list)
    else:
        print("The first number or the second number must be (1 OR 2 Or 3)")

#V3
if False:
    print("Welcome to (Place the rabbit.)")
    list=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"],]
    print(f"{list[0]}\n{list[1]}\n{list[2]} \nwhere should the rabbit go?")
    user_number = (input("Please choose a row and a column: \n"))
    row = int(user_number[0])
    column = int(user_number[1])
    if user_number[0] == 1 or user_number[0] == 2 or user_number[0] ==3:
        if user_number[1] == 1 or user_number[1] == 2 or user_number[1] ==3:
            list[row-1][column-1] = "🐇"
            print(list)
    else:
        print("The first number or the second number must be (1 OR 2 Or 3)")

#V4
if False:
    print("Welcome to (Place the rabbit.)")
    list=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"],]
    print(f"{list[0]}\n{list[1]}\n{list[2]} \nwhere should the rabbit go?")
    user_number = (input("Please choose a row and a column: \n"))
    row = int(user_number[0])
    column = int(user_number[1])
    if user_number[0] == "1" or user_number[0] == "2" or user_number[0] =="3":
        if user_number[1] == "1" or user_number[1] == "2" or user_number[1] =="3":
            list[row-1][column-1] = "🐇"
            print(list)
    else:
        print("The first number or the second number must be (1 OR 2 Or 3)")

#V5 
if False:
    print("Welcome to (Place the rabbit.)")
    list=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"],]
    print(f"{list[0]}\n{list[1]}\n{list[2]} \nwhere should the rabbit go?")
    user_number = (input("Please choose a row and a column: \n"))
    row = int(user_number[0])
    column = int(user_number[1])
    if user_number[0] == "1" or user_number[0] == "2" or user_number[0] =="3":
        if user_number[1] == "1" or user_number[1] == "2" or user_number[1] =="3":
            list[row-1][column-1] = "🐇"
            print(f"{list[0]}\n{list[1]}\n{list[2]}")
    else:
        print("The first number or the second number must be (1 OR 2 Or 3)")

#V6 
if False:
    print("Welcome to (Place the rabbit)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if number[0] =="1" or number[0] =="2" or number[0] =="3" and number[1] =="1" or number[1] =="2" or number[1] =="3":
        row = int(number[0])
        column = int(number [1])
        field[row-1][column-1]="🐇"
        print(f"{field[0]}\n{field[1]}\n{field[2]}")
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number: {number}")

#V7 
if False:
    print("Welcome to (Place the rabbit)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if (number[0] =="1" or number[0] =="2" or number[0] =="3") and (number[1] =="1" or number[1] =="2" or number[1] =="3"):
        row = int(number[0])
        column = int(number [1])
        field[row-1][column-1]="🐇"
        print(f"{field[0]}\n{field[1]}\n{field[2]}")
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number: {number}")

#V8 
if False:
    print("WELCOME to (PLACE THE RABBIT)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if len(number) == "2" and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
        field=[int(number[0])-1][int(number[1])-1]
        print(f"{field[0]}\n{field[1]}\n{field[2]}")
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number is: {number}")

#V9 
if False:
    print("WELCOME to (PLACE The RABBIT)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if len(number) == 2 and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
        row = int(field[0])
        column = int(field[1])
        field = [row-1][column-1] = "🐇"
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number is: {number}")

#V10 
if False:
    print("WELCOME to (PLACE The RABBIT)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if len(number) == 2 and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
        row = int(number[0])
        column = int(number[1])
        field [row-1 and column-1] = "🐇"
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number is: {number}")

#V11 
if False:
    print("WELCOME to (PLACE The RABBIT)")
    field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
    print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
    number = input("Please choose a row and a column \n")
    if len(number) == 2 and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
        row = int(number[0])
        column = int(number[1])
        field [row-1][column-1] = "🐇"
        print(f"{field[0]}\n{field[1]}\n{field[2]}")
    else:
        print(f"The first number and the second number must be 1 OR 2 OR 3. Your number is: {number}")

#V12 
print("WELCOME to (PLACE THE RABBIT)")
field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}\nWhere should the rabbit go?")
number = input("Please choose a row and a column \n")
if len(number) == 2 and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
    row = int(number[0])
    column = int(number[1])
    field [row-1][column-1] = "🐇"
    print(f"{field[0]}\n{field[1]}\n{field[2]}")
else:
    print(f"The first number and the second number must be 1 OR 2 OR 3. Your number is: {number}")
