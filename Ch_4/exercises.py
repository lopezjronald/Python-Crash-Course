# Exercise 4.1
pizzas = ['pepperoni', 'combo', 'extra cheese']
print(f'Favorite pizzas: ', end='')
for index in range(len(pizzas)):
    if index == len(pizzas)-1:
        print(pizzas[index])
    else:
        print(pizzas[index], end=', ')
print("I love pizza")