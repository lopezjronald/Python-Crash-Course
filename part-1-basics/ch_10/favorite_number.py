import json


def ask_number():
    favorite_num = input("What is your favorite number:\n")
    try:
        favorite_num = int(favorite_num)
    except ValueError:
        print(f"Sorry, {favorite_num} is not a valid number.")
    else:
        return favorite_num


def store_number():
    filename = 'favorite_number.json'
    favorite_number = ask_number()
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


def get_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def display_favorite_number():
    favorite_number = get_favorite_number()
    if favorite_number:
        print(f"Your favorite number is {favorite_number}")
    else:
        favorite_number = store_number()
        print(f"Your favorite number is {favorite_number}. We will remember for next time")


display_favorite_number()
