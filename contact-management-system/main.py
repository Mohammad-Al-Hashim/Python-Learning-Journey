if False:
    contacts = {}
    while True:
        print("-----------------------------------------")
        print("\nContact management \n")
        print("1-Add a contact")
        print("2-View a contact")
        print("3-Edit a contact")
        print("4-exit \n")
        user_choice = int(input("Please choose a number from 1-4: "))
        right = 1,2,3,4
        if user_choice in right:
            if user_choice == 4:
                print("\n    Exiting the program......")
                break
            elif user_choice == 1:
                ID = input("\nEnter the contact ID: ")
                name = input("Please type a name: ")
                while True:
                    phone = input("Please type a phone number: ")
                    if phone.isdigit():
                        break
                    else:
                        print("You must enter numbers")
                contacts["ID"] = ID
                contacts["name"] = name
                contacts["phone"] = phone
                print(f"\n {name} was added successfully")
            elif user_choice == 2:
                if contacts:
                    print("\n",contacts)
                else:
                    print("\nThe contacts are empty, please add new contacts")
            elif user_choice == 3:
                if contacts:
                    ID_to_edit = input("\nPlease type the ID of the contact that you want to edit: ")
                    if ID_to_edit in contacts["ID"]:
                        new_ID = input("\nPlease type the new ID of the contact: ")
                        new_name = input("Enter a new name: ")
                        while True:
                            new_phone = input("Enter a new number: ")
                            if new_phone.isdigit():
                                break
                            else:
                                print("You must enter numbers")
                        contacts["ID"] = new_ID
                        contacts["name"] = new_name
                        contacts["phone"] = new_phone
                        print("\n     Success ....")
                    else:
                        print(f"\nSorry, there is no contact that have this ID: {ID_to_edit}")
                else:
                    print("\nThe contacts are empty, please add new contacts")
        else:
            print("\nInvalid number, please type a number between 1-4")


contacts = {}
while True:
    print("-----------------------------------------")
    print("\nContact management \n")
    print("1-Add a contact")
    print("2-View a contact")
    print("3-Edit a contact")
    print("4-exit \n")
    user_choice = int(input("Please choose a number from 1-4: "))
    right = 1,2,3,4
    if user_choice in right:
        if user_choice == 4:
            print("\n    Exiting the program......")
            break
        elif user_choice == 1:
            while True:
                ID = input("\nEnter the contact ID: ")
                if ID in contacts:
                    print("This ID is already used, type another one")
                else:
                    break
            name = input("Please type a name: ")
            while True:
                phone = input("Please type a phone number: ")
                if phone.isdigit():
                    break
                else:
                    print("You must enter numbers")
            contacts[ID] = {"ID": ID, "name": name, "phone": phone,}
            print(f"\n {name} was added successfully")
        elif user_choice == 2:
            if contacts:
                print("\n",contacts)
            else:
                print("\nThe contacts are empty, please add new contacts")
        elif user_choice == 3:
            if contacts:
                ID_to_edit = input("\nPlease type the ID of the contact that you want to edit: ")
                while True:
                    if ID_to_edit not in contacts:
                        print("This ID isn't in the contacts, you must edit an existing contact. Or: add a new contact")
                        ID_to_edit = input("\nPlease type the ID of the contact that you want to edit: ")
                    else:
                        break
                new_ID = input("Enter a new ID: ")
                new_name = input("Enter a new name: ")
                while True:
                    new_phone = input("Enter a new number: ")
                    if new_phone.isdigit():
                        break
                    else:
                        print("You must enter numbers")
                contacts[ID_to_edit] = {"ID": new_ID, "name": new_name, "phone": new_phone,}
                print("\n     Success ....")
            else:
                print("\nThe contacts are empty, please add new contacts")
    else:
        print("\nInvalid number, please type a number between 1-4")
