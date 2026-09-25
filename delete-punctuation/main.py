#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1
if False:
    import string

    user_typed = input("Please type your text \n")
    text = ""
    for x in user_typed:
        if x not in string.punctuation:
            text+=x
            print(text)

#V2
import string

user_typed = input("Please type your text \n")
text = ""
for x in user_typed:
    if x not in string.punctuation:
        text+=x
print(text)
