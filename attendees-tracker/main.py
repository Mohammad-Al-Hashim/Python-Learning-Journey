attendees = input("Please enter the names of attendees separated by a coma. \n").split(", ")
for person in attendees:
    print(person)
    user_typed = input("\nIs this person attending? type (yes or no) \n").lower()
    if user_typed == "yes" or user_typed == "no":
        if user_typed == "yes":
            print("Attendance confirmed")
            print("--------------------")
            print("                     ")
        else:
            print("Attendance not confirmed")
            print("--------------------")
            print("                     ")
    else:
        print("Please type either (yes or no). you typed: ",user_typed,".","Try again")
        break
