from pip._vendor.distlib.compat import raw_input


# exercise 8-1
def display_message():
    # message = raw_input("Tell people what you are learning: ")
    message = 'python'.title()
    print(f"I am learning {message}")


display_message()


# exercise 8-2
def favorite_book(book):
    print(f'One of my favorite books is {book}')


favorite_book("High Performance Habits")


# exercise 8-3
def make_shirt(size, shirt_message):
    print(f'Size of the shirt: {size}\nMessage on the shirt: {shirt_message}')


make_shirt('M', "Savage")
make_shirt(size="XL", shirt_message="STAY HARD")


# exercise 8-4
def make_shirt(size="Large", message="I love Python"):
    print(f"Size of the shirt: {size}\nMessage: {message}")


make_shirt()
make_shirt("XS")
make_shirt(message="You had me at 'Hello World'")


# exercise 8-5
def describe_city(city, country='the united states'):
    print(f'{city.title()} is located in {country.title()}')


describe_city('Sacramento')
describe_city('Paris', 'France')
describe_city(country='Iceland', city='Reykjavik')


# exercise 8-6
def city_country(city, country):
    return f'{city}, {country}'


print(city_country("Sac Town", "USA"))
print(city_country("Paris", "France"))
print(city_country("San Pao", "Brazil"))


# exercise 8-7
def make_album(name, artist):
    return {name: artist}


all_albums = {}
albums = [make_album('Mi amor', 'Mark Anthony'), make_album("Eres Tu", "J-Lo"), make_album("All Eyes on Me", "Tupac")]
for index in range(len(albums)):
    all_albums[f'album_{index}'] = albums[0]
print(all_albums)

# exercise 8-8
making_album = True
while making_album:
    response = raw_input("Would you like to add an album (press 'q' to quit")
    if response.lower() == 'q':
        making_album = False
    else:
        artist = raw_input("Artist name: ")
        album = raw_input("Album name: ")
        all_albums[f'album_{len(all_albums)}'] = make_album(artist=artist, name=album)
print(all_albums)


# exercise 8-9
def print_messages(messages):
    for message in messages:
        print(message)


text_messages = ["Hello there", "Text you later", "Working out"]
print_messages(text_messages)

# exercise 8-10
messages_sent = []


def sent_messages(messages):
    while messages:
        messages_sent.append(messages.pop())


sent_messages(text_messages)
print(text_messages)
print(messages_sent)

# exercise 8-11
messages_sent = []
text_messages = ["Hello there", "Text you later", "Working out"]
print_messages(text_messages)
sent_messages(text_messages[:])
print(text_messages)
print(messages_sent)


# exercise 8-12
def make_sandwich(*items_in_sandwich):
    return list(items_in_sandwich)


items = make_sandwich('lettuce', 'tomato', 'mustard', 'ham')
print(type(items))
print("Items in sandwich: ")
for item in items:
    print(f'- {item}')


# exercise 8-13
def user_profile(**user_info):
    return user_info


first = "Jeff"
last = "Lopez"
hobby = ['Reading', "MMA", "Traveling", "Working out", "Movies"]
location = 'CA'

user_1 = user_profile(name=f'{first} {last}', hobby=hobby, location=location)
print(user_1)


# exercise 8-14
def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info


make = "Toyota"
model = "Prius"
color = 'Charcoal'
doors = 4
print(make_car(make, model, color=color, doors=doors))

# exercise 8-15
# Done

import printing_models

user = 'Jeff'
printing_models.say_hello()
printing_models.say_hello_user(user)

import printing_models as pm

pm.say_hello()

from printing_models import say_hello

say_hello()

from printing_models import say_hello_user as shu

shu(user)
