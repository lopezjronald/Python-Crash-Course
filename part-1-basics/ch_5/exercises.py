# exercise 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print()
print('monkey' == 'banana')
print('monkey' == 'MONKEY')
print(3.5 == 3)
print(type('hello') == type(22))
print('33' == 33)

print()
print('monkey' == 'MONKEY'.lower())
print(type('33') == type('hello'))
print(int('33') == 33)
print(int('27') >= 25)
print(len('four') == 4)

# exercise 5-2
print()
names = ['JOYCE', 'VIOLET', 'AMBER', 'JULIET', 'ROMEO', 'JEFF', 'CHRIS', 'MIKE']
for name in range(len(names)):
    names[name] = names[name].lower()
print(names)
print(len('seven') == 5 and type('seven') == str)
print('violet'.lower() in names)
print('pumpkin' not in names)

# exercise 5-3
points = 0
alien_color = ['green', 'yellow', 'red']
color = 'blue'
if color in alien_color:
    points += 5
    print(f'Adding 5 points for having green: {points}')
else:
    print(f'Points: {points}')

# exercise 5-4
points = 0
color = 'lime'
if color.lower() == 'green':
    points += 5
else:
    points += 10
print(f'Points: {points}')

# exercise 5-5
points = 0
color = 'red'
if (color == 'green'):
    points += 5
elif (color == 'yellow'):
    points += 10
elif (color == 'red'):
    points += 15
print(f'Points: {points}')

# exercise 5-6
age = 34
role = None
if (age < 2):
    role = 'baby'
elif (age < 4):
    role = 'toddler'
elif (age < 13):
    role = 'kid'
elif (age < 20):
    role = 'teenager'
elif (age < 65):
    role = 'adult'
elif (age >= 65):
    role = 'elder'
print(f'The person is {age} years old and is considered as: {role.title()}.')

# exercise 5-8
names.append('admin'.lower())
username = 'admin'
if names:
    message = None
    for name in names:
        if name == username:
            message = 'Would you like to see a status report?'
        else:
            message = 'Thank you for logging in again.'
        print(f'Hello, {name.title()}. {message}')

# exercise 5-9
names = []
if names:
    print("There are names.")
else:
    print("There are no names")

# exercise 5-10
current_users = ['JEFF', 'DONALD', 'DWAYNE', 'BAbloa', 'COOKie']
for index in range(len(current_users)):
    current_users[index] = current_users[index].lower()

new_users = ['JeFf', 'DonALD', 'mcdonald', 'ronald', 'lopes']
for index in range(len(current_users)):
    new_users[index] = new_users[index].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry. Username {new_user} is taken.")
    else:
        print(f"Username {new_user} is available.")

# exercise 5-11
nums = []
[nums.append(i) for i in range(1, 10)]
if nums:
    for i in range(len(nums)):
        end = None
        if nums[i] == 1:
            end = 'st'
        elif nums[i] == 2:
            end = 'nd'
        elif nums[i] == 3:
            end =  'rd'
        else:
            end = 'th'
        print(str(nums[i]) + end, end=' ')

