from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restuarant_name, type_cuisine, flavors):
        super().__init__(restuarant_name, type_cuisine)
        self.flavors = flavors
