class Restaurant():
    def __init__(self, restaurant_name, type_cuisine):
        self.restaurant_name = restaurant_name
        self.type_cuisine = type_cuisine

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a {self.type_cuisine} cuisine type.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')
