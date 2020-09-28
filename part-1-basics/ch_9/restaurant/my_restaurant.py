# from restaurant import Restaurant
#
# my_restaurant = Restaurant(restaurant_name='McDonalds', type_cuisine="American")
# my_restaurant.describe_restaurant()

from ice_cream_stand import IceCreamStand
my_stand = IceCreamStand('Baskin Robbins', 'Desserts', ['chocolate', 'strawberry', 'vanilla'])
my_stand.describe_restaurant()
print(my_stand.flavors)