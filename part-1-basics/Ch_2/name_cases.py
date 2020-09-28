"""
2-3. Personal Message: Use a variable to represent a person’s name, and print a message to
that person. Your message should be simple, such as, “Hello Eric, would you like to learn some
Python today?”

2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s
name in lowercase, uppercase, and title case.

2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the
name of its author. Your output should look something like the following, including the
quotation marks:
Albert Einstein once said, “A person who never made a mistake
never tried anything new.”

2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name
using a variable called famous_person. Then compose your message and represent it with a
new variable called message. Print your message.

2-7. Stripping Names: Use a variable to represent a person’s name, and include some
whitespace characters at the beginning and end of the name. Make sure you use each character
combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name
using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

name = "Eric"
print(f"Hello, {name}! Would you like to learn some python today?")

first_name = "jEfF"
last_name = "LoPEz"
print(f"Lowercase: {first_name.lower()} {last_name.lower()}")
print(f"Uppercase: {first_name.upper()} {last_name.upper()}")
print(f"Title: {first_name.title()} {last_name.title()}")

author = "tony robbins"
print(f"Repetition is the mother of skill ~ {author.title()}")

famous_person = "kevin hart"
message = "is one hilarious dude!"
print(f"{famous_person.title()} {message}")

name = "\t\nRonald Lopez\t\t\n"
print(f"Left Strip function: {name.lstrip()}")
print(f"Strip function: {name.strip()}")
print(f"Right Strip function: {name.rstrip()}")

fav_num = 17
print(f'Favorite number is {fav_num}')