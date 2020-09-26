motorcycles = ['honda', 'yamaha', 'suzuki']
count = 1
for temp_motorcycle in motorcycles:
    print(f'Bike {count}: {temp_motorcycle}')
    count += 1
print()

# change element
motorcycles[0] = 'ducati'
count = 1
for temp_motorcycle in motorcycles:
    print(f'Bike {count}: {temp_motorcycle}')
    count += 1
print()

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print()

# Insert an element into the list
motorcycles.insert(1, 'ducati')
print(motorcycles)
print()

# Delete an element from the list, doesn't allow you to store it in a variable
del motorcycles[1]
print(motorcycles)
print()

# removes last element from the list and allows you to store it in a variable
pop_motorcycle = motorcycles.pop()
print(pop_motorcycle)
print(f"The last motorcycle I owned was a {pop_motorcycle.title()}.")
print()

# pop allows removal in specific index and lets you work with that element if stored in variable
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
length_moto_list = len(motorcycles)
for index in range(len(motorcycles)):
    print(f"{index + 1}: The last motorcycle I owned was a {motorcycles[index]}.")
print()

# Remove allows you to remove it based on requirement 'filter' in a way
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'suzuki', 'ducati']
print(motorcycles)
remove_motorcycle = 'ducati'
for temp_motorcycle in motorcycles:
    if temp_motorcycle == remove_motorcycle:
        motorcycles.remove(remove_motorcycle)
print(motorcycles)
print()

# sort a list in alphabetal order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars, '\n')

# sort a list in reverse alphabetal order
cars.sort(reverse=True)
print(cars, '\n')

# sorted function without changing it permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'List {cars}')
print(f'Sorted List Alphabetical: {sorted(cars)}')
print(f'Sorted List Reverse Alphabetical: {cars.reverse()}')
print(f'Original List: {cars}')

