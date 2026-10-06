abbreviations = []
names_list = input("Please enter the first and the last name of the persons, separated by a comma \n").split(", ")
print(names_list)
for name in names_list:
    name_parts = name.split()
    first_name = name_parts[0]
    second_name = name_parts[1]
    first_letter_first_name = first_name[0]
    first_letter_second_name = second_name[0]
    abbreviated_name = first_letter_first_name +"."+first_letter_second_name
    abbreviations.append(abbreviated_name)
for short_name in abbreviations:
    print(short_name)
