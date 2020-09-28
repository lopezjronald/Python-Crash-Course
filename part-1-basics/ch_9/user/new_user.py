from admin import Admin

new_admin = Admin('Jeff', 'Lopez')

print(new_admin.first_name)
print(new_admin.last_name)
new_admin.show_privileges()