# exercise 6-1
person = {
    'first_name': 'ronald',
    'last_name': 'lopez',
    'age': 34,
    'city': 'honolulu',
}

for key, value in person.items():
    print(f'{key.title()}: {value}')

# exercise 6-2
print()
favorite_numbers = {
    'joyce': 9,
    'ronald': 3,
    'Boo': 33,
    'Stew': 22,
    'Clue': 100,
}

favorite_numbers['jason'] = 13
favorite_numbers['violet'] = 2
for key, value in favorite_numbers.items():
    print(key, ": ", value)

# exercise 6-3
glossary = {
    'algorithm': 'An algorithm is a set of instructions or rules designed to solve a definite problem. The problem '
                 'can be simple like adding two numbers or a complex one, such as converting a video file from one '
                 'format to another.',
    'program': 'A computer program is termed as an organized collection of instructions, which when executed perform '
               'a specific task or function. A program is processed by the central processing unit (CPU) of the '
               'computer before it is executed. An example of a program is Microsoft Word, which is a word processing '
               'application that enables users to create and edit documents. The browsers that we use are also '
               'programs created to help us browse the internet.',
    'api': 'Application Programming Interface (API) is a set of rules, routines, and protocols to build software '
           'applications. APIs help in communication with third party programs or services, which can be used to '
           'build different software. Companies such as Facebook and Twitter actively use APIs to help developers '
           'gain easier access to their services.',
    'argument': 'Argument or arg is a value that is passed into a command or a function. For example, if SQR is a '
                'routine or function that returns the square of a number, then SQR(4) will return 16. Here, '
                'the value 4 is the argument. Similarly, if the edit is a function that edits a file, then in edit '
                'myfile.txt, ‘myfile.txt’ is the argument.',
    'ascii': 'American Standard Code for Information Interexchange (ASCII) is a standard that assigns letters, '
             'numbers and other characters different slots, available in the 8-bit code. The total number of slots '
             'available is 256. The ASCII decimal number is derived from binary, which is assigned to each letter, '
             'number, and character. For example, the ‘$’ sign is assigned ASCII decimal number 036, '
             'while the lowercase ‘a’ character is assigned 097.',
}

for key, value in glossary.items():
    print(f"{key.title()}:\n{value}\n")

# exercise 6-5
major_rivers = {
    'mississippi': 'mississippi river',
    'egypt': 'niles',
    'israel': 'jordan',
}

for place, river in major_rivers.items():
    print(f'{place.title()}: {river.title()}')

print()
for place in major_rivers.keys():
    print(place.title())

print()
for river in major_rivers.values():
    print(river.title())

# exercise 6-6
print()
voters = ['jen', 'sarah']
non_voters = ['ronald', 'violet']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for name in favorite_languages.keys():
    if name not in voters:
        print(f'{name.title()}, you need to vote!')
    else:
        print(f'{name.title()}, thank you for voting :)')

print()
for name in favorite_languages.keys():
    if name in non_voters:
        print(f'{name.title()}, you need to vote!')
    else:
        print(f'{name.title()}, thank you for voting :)')


# exercise 6-7
print()
person_0 = {
    'first_name': 'ronald',
    'last_name': 'lopez',
    'age': 34,
    'city': 'honolulu',
}
person_1 = {
    'first_name': 'donald',
    'last_name': 'trump',
    'age': 70,
    'city': 'new york',
}

person_2 = {
    'first_name': 'bears',
    'last_name': 'grills',
    'age': 45,
    'city': 'alaska',
}

people = [person_0, person_1, person_2]
for person in people:
    print()
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])

# exercise 6-8
print()
pet_0 = {
    'type': 'cat',
    'breed': 'house cat',
    'name': 'whiskers',
    'owner': 'steve austin',
}

pet_1 = {
    'type': 'dog',
    'breed': 'husky',
    'name': 'pudding',
    'owner': 'hanky',
}

pet_2 = {
    'type': 'fish',
    'breed': 'blue',
    'name': 'dora',
    'owner': 'nemo',
}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print()
    for key, value in pet.items():
        print(key.title(), ": ", value.title())

# exercise 6-9

# exercise 6-10
print()
favorite_numbers = {
    'joyce': [22, 33, 35],
    'ronald': [232, 22, 139],
    'mcfee': [33, 233, 3566223345],
}

for name, numbers in favorite_numbers.items():
    print()
    print(f"{name.title()}'s favorite number(s):")
    for number in numbers:
        print(f"- {number}")

# exercise 6-11
print()

states = {
    'california': {
        "nickname": "the golden state",
        "capital": "sacramento",
        "population": 39_144_818,
        "abbreviation": "ca",
    },
    'alabama': {
        "nickname": "the heart of dixie",
        "capital": "montgomery",
        "population": 4_858_979,
        "abbreviation": "al",
    },
    'florida': {
        "nickname": "the sunshine state",
        "capital": "tallahassee",
        "population": 20_271_272,
        "abbreviation": "fl",
    },
}
for state, state_info in states.items():
    print()
    print(state.title())
    for key, value in state_info.items():
        if (type(value) == int):
            print(key.title(), ":", value)
        else:
            print(key.title(), ":", value.title())


# exercise 6-12
