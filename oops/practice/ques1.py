# 1. Data Validation with Encapsulation & @property
# Real-world use case: Sanitizing and validating data models (e.g., in a web backend).

# The Scenario: You're building a user management system.
# The Task: Create a User class. It should take a username and password on initialization.
# Make the internal password attribute private (e.g., _password).
# Create a @property for password that only returns a masked version of the password (e.g., "********").
# Create a .setter for password that checks if the new password is at least 8 characters long and contains at least one number. If it doesn't, raise a ValueError. If it does, update the hidden _password.

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
    
    @property
    def password(self):
        return '*' * len(self._password)
    
    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("The password has length less than 8")
        if not any(i.isdigit() for i in new_password):
            raise ValueError('Digit is missing...')
        self._password = new_password

user = User('uname', 'santosh')
print(user.password)