travel_list = input("Please type the names of the countries separated by a comma: \n").split(", ")
for country in travel_list:
    print("\n",country,"\n")
    visited = input(f"Have you ever visited {country} before? Type yes or no \n").lower()
    if visited in ["yes","no"] :
        if visited == "yes":
            print("I hope you had a wonderful time")
        else:
            print("I hope you get to visit it soon")
    else:
        print("You must type either yes or no. Try again")
        break
