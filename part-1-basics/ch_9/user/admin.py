from user import User
from privilege import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

    def show_privileges(self):
        print("List of Privileges:")
        for privilege in self.privileges.privileges:
            print(f'- {privilege}')