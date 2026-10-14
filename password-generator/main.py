#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1:
if False:
    import random
    import string
    import sys

    print("Welcome to the password generator!")
    password_length = int(input("Enter the total number of characters"))
    letters_number = int(input("Enter the number of letters \n"))
    numbers_number = int(input("Enter the number of numbers \n"))
    symbols_number = int(input("Enter the number of symbols \n"))
    if letters_number + numbers_number + symbols_number == password_length:
        pass
    else:
        print("Invalid inputs. Try again")
        sys.exit()
    letters_list = [random.choice(string.ascii_letters, k=letters_number)]
    numbers_list = [random.choice(string.digits, k=numbers_number)]
    symbols_list = [random.choice(string.punctuation, k=symbols_number)]
    password = []

#V2:
if False:
    import random
    import string
    import sys

    print("Welcome to the password generator!")
    password_length = int(input("Enter the total number of characters"))
    letters_number = int(input("Enter the number of letters \n"))
    numbers_number = int(input("Enter the number of numbers \n"))
    symbols_number = int(input("Enter the number of symbols \n"))
    if letters_number + numbers_number + symbols_number == password_length:
        pass
    else:
        print("Invalid inputs. Try again")
        sys.exit()
    letters_list = random.choices(string.ascii_letters, k=letters_number)
    numbers_list = random.choices(string.digits, k=numbers_number)
    symbols_list = random.choices(string.punctuation, k=symbols_number)
    letters_string = "".join(letters_list)
    numbers_string = "".join(numbers_list)
    symbols_string = "".join(symbols_list)
    password = []
    password.append(letters_string)
    password.append(numbers_string)
    password.append(symbols_string)
    password_string = "".join(password)
    generated_password = random.shuffle(password_string)
    print(generated_password)

#V3:
if False:
    import random
    import string
    import sys

    print("Welcome to the password generator!")
    password_length = int(input("Enter the total number of characters"))
    letters_number = int(input("Enter the number of letters \n"))
    numbers_number = int(input("Enter the number of numbers \n"))
    symbols_number = int(input("Enter the number of symbols \n"))
    if letters_number + numbers_number + symbols_number == password_length:
        pass
    else:
        print("Invalid inputs. Try again")
        sys.exit()
    letters_list = random.choices(string.ascii_letters, k=letters_number)
    numbers_list = random.choices(string.digits, k=numbers_number)
    symbols_list = random.choices(string.punctuation, k=symbols_number)
    letters_string = "".join(letters_list)
    numbers_string = "".join(numbers_list)
    symbols_string = "".join(symbols_list)
    password_list = letters_string + numbers_string + symbols_string
    random.shuffle(password_list)
    generated_password = "".join(password_list)
    print(generated_password)

#V4:
if False:
    import random
    import string
    import sys

    print("Welcome to the password generator!")
    password_length = int(input("Enter the total number of characters"))
    letters_number = int(input("Enter the number of letters \n"))
    numbers_number = int(input("Enter the number of numbers \n"))
    symbols_number = int(input("Enter the number of symbols \n"))
    if letters_number + numbers_number + symbols_number == password_length:
        pass
    else:
        print("Invalid inputs. Try again")
        sys.exit()
    letters_list = random.choices(string.ascii_letters, k=letters_number)
    numbers_list = random.choices(string.digits, k=numbers_number)
    symbols_list = random.choices(string.punctuation, k=symbols_number)
    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    generated_password = "".join(password_list)
    print(generated_password)

#V5:
import random
import string
import sys

print("Welcome to the password generator!")
password_length = int(input("Enter the total number of characters: \n"))
letters_number = int(input("Enter the number of letters: \n"))
numbers_number = int(input("Enter the number of numbers: \n"))
symbols_number = int(input("Enter the number of symbols: \n"))
if letters_number + numbers_number + symbols_number == password_length:
    pass
else:
    print("Invalid input. The sum of letters, numbers, symbols, doesn't match the password's total number of characters. Try again")
    sys.exit()
letters_list = random.choices(string.ascii_letters, k=letters_number)
numbers_list = random.choices(string.digits, k=numbers_number)
symbols_list = random.choices(string.punctuation, k=symbols_number)
password_list = letters_list + numbers_list + symbols_list
random.shuffle(password_list)
generated_password = "".join(password_list)
print(f"Generated password: {generated_password}")
