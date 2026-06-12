# Feature	            Instance Method	    Class Method	Static Method
# Decorator	            None	            @classmethod	@staticmethod
# First parameter	    self	            cls	            none
# Access instance data	Yes	                No	            No
# Access class data	Yes	                    Yes	            No
# Can modify class state	Yes	            Yes	            No
# Requires object	    Yes	                    No          	No

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    # instance method
    def show(self):
        return self.name

    # class method
    @classmethod
    def change_company(cls, name):
        cls.company = name

    # static method
    @staticmethod
    def is_working_day(day):
        return day not in ["Saturday", "Sunday"]