Today, I made my first real mistake in Python — and I'm glad it happened. (Project #1: Character Counter) 🐍🚀

I built a program that counts the number of characters entered by the user.

First error in my coding journey:
While building the character counter, I tried to write:

print("Your text contains: " + len(user_text) + " characters")

This gave me my very first real error. The problem: len(user_text) returns an integer — the count of characters — not text. Since + on strings requires every value being joined to be a string, mixing a string with an integer caused Python to reject it immediately, with a TypeError.

The fix:

print("Your text contains: " + str(len(user_text)) + " characters")

Wrapping len(user_text) in str() converts the integer into a string first, so + can join all three pieces correctly.
What I learned from the error: len() always returns a number, never text — and print() combined with + demands that everything being joined must already be a string. This is exactly why type conversion functions like str() exist: to bridge the gap between different data types before combining them.

It's a small fix — but it taught me something bigger: errors aren't a sign to slow down. They're simply part of the process, and every single one leaves me better than before. I am glad it happened because I learned new things about syntax and programming logic.

This won't be my last error, and I know that. But it won't shake my enthusiasm, and it won't hold me back. Hitting errors is one of the most common, most normal parts of learning to code — and I plan to keep hitting them, learning from them, and moving forward, no matter how many more show up.

Here is what I learned from the whole project. 👇

Data types and conversions: str(), int(), variables, values, the input() function, the len() function, and the special character \n.

Variables and values: A variable is a name that stores a value, so it can be reused throughout a program. Variable names must start with a letter or underscore (never a digit), can contain letters, numbers, and underscores, and cannot use spaces or Python's reserved keywords.

Data types: Every value has a type, such as integer (a whole number), float (a decimal number), string (text), and boolean (True/False).

Type conversion functions: int(), float(), and str() convert a value from one data type to another, such as turning text into a number.

The input() function: asks the user to type something, and returns it as text.

The len() function: counts the number of characters in a piece of text and returns it from string type into integer type.

Special character: \n — inserts a line break inside text, used to format output in a clearer and organized way.

The + operator: in Python, + behaves differently depending on the data type. With numbers, it merges them mathematically (adds them together). With strings, it places them side by side, joining them into one longer piece of text — this is called concatenation. Because of this, print() cannot mix types when using +: every piece being joined must already be a string, or Python won't know whether you mean "add" or "join."

I'm a recent high school graduate, and I'm determined to keep building harder, deeper Python projects — reaching an advanced level and sharpening my skills before university begins. Hard problems and repeated failures won't stop me. I'll keep standing back up and pushing forward, one project at a time. 💪
