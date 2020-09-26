# exercise 3-4

guests = ['Tony', 'Brandon', 'Jim Rohn']
print("Guest List", end=': ')
for guest in guests:
    print(guest, end=' ')
print("\n")

# exercise 3-5
new_guest = "Eric the 'Hip-Hop' Preacher"
guest_not_attending = 'Tony'
guests.remove(guest_not_attending)
print(guests, "\n")

guests.append(new_guest)
print(guests, "\n")

# exercise 3-6
print("Found a bigger table. 3 more attendees")
guest1 = 'John Maxwell'
guest2 = 'Dwayne Johnson'
guest3 = "'Stone Cold' Steve Austin"
guests.insert(0, guest1)
print(guests, '\n')
guests.insert(int(len(guests)/2), guest2)
print(guests)
guests.append(guest3)
print(guests, '\n')

# exercise 3-7
print("Sorry peeps! Table not arriving. Only 2 are able to come.", '\n')
table_size = 2

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f'Sorry, {removed_guest}, the table is too small and I\'m unable to invite you this time :(')
print(guests, '\n')

for guest in guests:
    print(f'{guest}, you are still invited to the "PARTAYYYYYY"!')
print()

while(len(guests) > 0):
    del guests[len(guests)-1]

print(guests)

# exercise 3-8
vacation_spots = ['polynesian islands', 'south america', 'canada', 'germany', 'hawaii islands']
print()
print('Location spots: ', end='')
print(vacation_spots, '\n')

print(f"Alphabetical: ", end='')
print(sorted(vacation_spots))
print("Original form: ", end='')
print(vacation_spots, end='\n\n')

print(f"Reverse Alphabetical: ", end='')
print(sorted(vacation_spots, reverse=True))
print("Original form: ", end='')
print(vacation_spots, end='\n\n')

vacation_spots.reverse()
print('Reverse order: ', end='')
print(vacation_spots, end='\n')

vacation_spots.reverse()
print("Original form: ", end='')
print(vacation_spots,end='\n\n')

vacation_spots.sort()
print("Permanent Alpha Order: ", end='')
print(vacation_spots)

vacation_spots.sort(reverse=True)
print("Permanent Reverse Alpha Order: ", end='')
print(vacation_spots)