import car
from battery import Battery

my_new_car = car.Car("BMW", "A4", 2019)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
new_battery = Battery()
new_battery.describe_battery()

