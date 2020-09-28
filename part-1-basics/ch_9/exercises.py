# exercise 9-1
class Restaurant():
    def __init__(self, restaurant_name, type_cuisine):
        self.restaurant_name = restaurant_name
        self.type_cuisine = type_cuisine

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a {self.type_cuisine} cuisine type.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')


restaurant = Restaurant("McDonalds", "American")
print(restaurant.restaurant_name)
print(restaurant.type_cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# exercise 9-2
restaurants = ["McDonalds", "Burger King", "In-n-Out"]
restaurant_obj = []
for restaurant in restaurants:
    restaurant = Restaurant(restaurant, 'American')
    restaurant_obj.append(restaurant)
for restaurant in restaurant_obj:
    print(restaurant.restaurant_name)


# exercise 9-3

class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        user_info['first_name'] = self.first_name
        user_info['last_name'] = self.last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print(self.user_info)

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user = User('ron', 'lopez', age=25, fitness='excellent', hobby='MMA')

new_user.describe_user()
new_user.greet_user()

# exercise 9-4

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)


# exercise 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restuarant_name, type_cuisine, flavors):
        super().__init__(restuarant_name, type_cuisine)
        self.flavors = flavors


ice_cream_flavors = ['strawberry', 'chocolate', 'mint', 'vanilla']

ice_cream_store = IceCreamStand('Baskin Robbins', 'Ice Cream', ice_cream_flavors)
print(ice_cream_store.flavors)
print(ice_cream_store.restaurant_name)
print(ice_cream_store.type_cuisine)


# exercise 9-7
class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("List of Privileges:")
        for privilege in self.privileges:
            print(f'- {privilege}')


print()
admin = Admin('ron', 'lopez')
admin.show_privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

    def show_privileges(self):
        print("List of Privileges:")
        for privilege in self.privileges.privileges:
            print(f'- {privilege}')


print()
new_admin = Admin('Joyce', 'Lopez')
new_admin.show_privileges()


# exercise 9-8
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


import random

flavor = (random.choice(ice_cream_flavors))
print(flavor)