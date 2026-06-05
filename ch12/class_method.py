class parent:
    num = 5
    @classmethod
    def class_method(cls):
        print(f"this is a class method and the value of num is {cls.num}")

parent.num = 50   #the instance attribute is created and assigned 50 but class attribute is not changed.
print(parent.num)

parent.class_method()