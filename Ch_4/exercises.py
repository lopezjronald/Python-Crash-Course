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
