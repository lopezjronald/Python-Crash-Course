def addition():
    num1 = input("First Number to add:\n")
    try:
        num1 = int(num1)
    except ValueError:
        print(f"Sorry, {num1} is not a number.")

    num2 = input("Second Number to add:\n")
    try:
        num2 = int(num2)
    except ValueError:
        print(f"Sorry, {num2} is not a number.")
    try:
        return num1 + num2
    except Exception:
        return "Couldn't add entries."


response = True
while response:
    print(addition())
    add_more = input("Would you like to continue ('q' to quit):\n")
    if add_more.lower() == 'q':
        response = False
