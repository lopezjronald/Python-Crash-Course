# Exercise 4.1
pizzas = ['pepperoni', 'combo', 'extra cheese']
print(f'Favorite pizzas: ', end='')
for index in range(len(pizzas)):
    if index == len(pizzas) - 1:
        print(pizzas[index])
    else:
        print(pizzas[index], end=', ')
print("I love pizza")

# exercise 4-3
[print(value, end=' ') for value in range(1, 21)]

# exercise 4-4
[print(num, end=' ') for num in range(1_000)]

# exercise 4-5
nums = []
[nums.append(value) for value in range(1_000)]
print()
print(min(nums))
print(max(nums))
print(sum(nums))

# exercise 4-6
[print(value, end=' ') for value in range(0, 21) if value % 2 == 1]
print()

# exercise 4-7
[print(value, end=' ') for value in range(21) if value % 3 == 0]
print()

# exercise 4-8
for i in range(11):
    print(i ** 3, end=' ')
print()

# exercise 4-9
[print(value ** 3, end=' ') for value in range(11)]
print()

# exercise 4-10
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'charles', 'martina', 'michael', 'florence', 'eli']
print(f'The first three items on the list our: {foods[:3]}')
print(f'The first three items on the list our: {foods[5:8]}')
print(f'The last three items on the list our: {foods[-3:]}')

# exercise 4-11
pizzas = ['pepperoni', 'combo', 'extra cheese']
friend_pizzas = pizzas[:]
pizzas.append('feta cheese')
print(friend_pizzas)
print(pizzas)

# exercise 4-12
[print(f'Friend pizzas are: {pizza}', end=' ') for pizza in friend_pizzas]
print()
print("My pizzas are: ")
[print(pizza, end=', ') for pizza in pizzas]
print()

# exercise 4-13
essentials = ('chicken', 'steak', 'vegetables', 'water', 'bread')
[print(essential, end=' ') for essential in essentials]
print()
# essentials[1] = 'lamb'
essentials = ('burger', 'fries', 'vegetables', 'water', 'bread')
[print(food, end=' ') for food in essentials]












