list = [["apples","bananas"],["milk","water"]]
press = input("Press enter to change the content: ")
if press:
    print("You must press enter. Try again")
else:
    list[0].insert(0, "oranges")
    list[0].insert(3, "kiwi")
    list[1].insert(0, "Coffee")
    list[1].remove("water")
    list[1].insert(2, "tea")
    numbers=[1,2,3]
    list.append(numbers)
    print(list)
