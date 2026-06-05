class Employee:
    company = 'TTC'
    name ='Satosh'
    def show(self):
        print(f"The name is {self.name}")


# class Programmer:
#     company = 'TTC infotech'
#     def show(self):
#         print(f"The name of company is {self.company}")

#     def showLang(self):
#         print(f"I study {self.lang}")


#This is inheritance here.
class Programmer(Employee):
    def showLang(self):
        print(f"I study {self.lang}")

a = Programmer()
a.show()

