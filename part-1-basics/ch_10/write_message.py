filename = 'guest.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("Guest List\n")

# with open(filename, 'a') as file_object:
#     response = True
#     while response:
#         file_object.write(input("Please enter the name of your guest: "))
#         file_object.write('\n')
#         continue_app = input("Continue? ('q' to quit): ")
#         if continue_app.lower() == 'q':
#             response = False

with open('guest.txt') as file_object:
    for content in file_object:
        print(content.strip())