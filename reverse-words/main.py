user_typed = input("Please type a sentence \n").split()
formula = user_typed[::-1]
reversed = " ".join(formula)
print(reversed)
