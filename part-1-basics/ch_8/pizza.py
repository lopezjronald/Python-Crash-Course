def make_pizza(size, *toppings):
    print(f'Making a {size}-size pizza with the following toppings')
    for topping in toppings:
        print(f'- {topping}')

def slice_pizza(size):
    print(f"Slicing a {size}-size pizza")