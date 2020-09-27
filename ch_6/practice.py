alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# adding position
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# adding speed
alien_0['speed'] = 'medium'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# BOOK EXAMPLE
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# removing keys in dictionaries
alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
del alien_0['speed']
print(alien_0)

print()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print(f"Sarah's favorite programming language is {favorite_languages['sarah']}")
print(favorite_languages.get("ronald", "Not a voter in the poll"))
print(favorite_languages.get('jen', 'not in the poll'))

print()
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f'{key}: {value}')

print()
for language in sorted(favorite_languages.values()):
    print(language)

print()
for name in sorted(favorite_languages.keys()):
    print(name)

# Nesting
print()
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms',
                 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print(f'- {topping}')

# dictionaries in dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, username_info in users.items():
    print()
    print(f'Username: {username}')
    print(f"First Name: {username_info['first'].title()}")
    print(f"Last Name: {username_info['last'].title()}")
    print(f"Location: {username_info['location'].title()}")
