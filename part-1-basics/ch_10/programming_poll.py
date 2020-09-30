def ask_name():
    return input("What is your name:\n")


def why_programming():
    return input("Why do you like programming?\n")


def exit_app():
    return input("Would you like to continue ('q' to quit):\n")

filename = 'programming_poll.txt'
with open(filename, 'w') as file_object:
    file_object.write('Programming Poll\n\n')

start_app = True
programming_poll = {}
while start_app:
    name = ask_name()
    reason = why_programming()
    programming_poll[name] = reason

    for name, reason in programming_poll.items():
        with open(filename, 'a') as file_object:
            file_object.write(f'Name: {name}\nReason: {reason}\n')

    new_name = exit_app()
    if new_name.lower() == 'q':
        start_app = False