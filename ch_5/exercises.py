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