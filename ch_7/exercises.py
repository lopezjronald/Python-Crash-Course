from pip._vendor.distlib.compat import raw_input

# exercise 7-1
input = raw_input("What care would you like to drive? ")
print(f'Let me see if I can find you a {input}.')

# exercise 7-2

group = raw_input("How many people will be sitting with you tonight? ")
group = int(group)
if group > 8:
    print("you will need to wait until we find you a table")
else:
    print("table is ready")

# exercise 7-3
multiple_of_ten = raw_input("Please enter a number: ")
if (int(multiple_of_ten) % 10 == 0):
    print(f"{multiple_of_ten} is a multiple of ten")

# exercise 7-4
toppings = []
order_pizza = True
while order_pizza:
    topping = raw_input("What topping would you like to add (enter 'quit' to exit): ")
    if topping.lower() == 'quit':
        order_pizza = False
    else:
        toppings.append(topping)
print(toppings)

# exercise 7-5
order_ticket = True
prices = [0, 10, 15]
cost = []
while order_ticket:
    age = raw_input("Age: ")
    age = int(age)
    if age < 3:
        cost.append(prices[0])
    elif age <= 12:
        cost.append(prices[1])
    else:
        cost.append(prices[2])
    response = raw_input("Would you like to order more tickets (enter 'n' for no)? ")
    if response.lower() == 'n':
        order_ticket = False
print(f"Total will be {sum(cost)}")

# exercise 7-6
count = 0
while count < 10:
    print(count)
    count += 1

# exercise 7-8
ordered_sandwiches = ['salami', 'meatball', 'tuna', 'blt', 'salami', 'salami']
finished_sandwiches = []
print("Ordered Sandwiches: ")
while ordered_sandwiches:
    completed_sandwich = ordered_sandwiches.pop()
    print(f"- {completed_sandwich}")
    finished_sandwiches.append(completed_sandwich)

print("Completed Sandwiches: ")
while finished_sandwiches:
    print(f'- {finished_sandwiches.pop()}')

print()
print(ordered_sandwiches)
print(finished_sandwiches)

ordered_sandwiches = ['salami', 'meatball', 'tuna', 'blt', 'salami', 'salami']
while 'salami' in ordered_sandwiches:
    ordered_sandwiches.remove('salami')
print(ordered_sandwiches)

# exercise 7-10
vacation_spots = {}
vacation_request = True
while vacation_request:
    name = raw_input("Name: ")
    vacation_location = raw_input("Vacation Spot: ")
    vacation_spots[name] = vacation_location
    response = raw_input("Another location? ('n' to quit)")
    if response.lower() == 'n':
        vacation_request = False

for name, location in vacation_spots.items():
    print(f'{name}: {location}')
