print("Welcome to tip calculator")
price = float(input("Please type the price \n"))
recommended_tip_poor = price*(10/100)
recommended_tip_good = price*(15/100)
recommended_tip_perfect = price*(20/100)
service = input("Please estimate the service, type: (POOR) OR (GOOD) OR (PERFECT) \n").upper()
if service == "POOR" or service == "GOOD" or service == "PERFECT":
    if service == "POOR":
        print(f"The recommended tip is: {recommended_tip_poor}")
    elif service == "GOOD":
        print(f"The recommended tip is: {recommended_tip_good}")
    else:
        print(f"The recommended tip is: {recommended_tip_perfect}")
else:
    print("You must type: (POOR) OR (GOOD) OR (PERFECT), try again")
