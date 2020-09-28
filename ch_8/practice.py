# def greet_user(name):
#     print(f'Hello {name}!')
#
#
# greet_user("Jeff")
#
#
# def creating_copy(rand_list):
#     rand_list.append("Hello there!")
#     print(rand_list)
#
#
# random_list = ['2323', 'dfadf', 'dfadfa']
# creating_copy(random_list[:])
# print(random_list)

## * allows many arguments to enter SO AWESOME
# def print_names(*names):
#     for name in names:
#         print(name.title())
#
# print_names('jeff', 'chris', 'mike', 'jason', 'edgar')

## ** builds an empty dictionary SUPER AWESOME
def build_profile(**user_info):
    return user_info
name = 'jeff'
location = 'sacramento'
major = 'finance'
profile = build_profile(name=name, location=location, major=major)
print(profile)