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