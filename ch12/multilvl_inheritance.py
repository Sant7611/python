class Student:
    name = 'Santosh'
    role='student'
    def about(self):
        print(f'my name is {self.name}. i work as a {self.role}')

class job(Student):
    role='job'
    def jobs(self):
        print(f'my role is {self.role}')

class multiple(job):
    def everything(self):
        print("This is the class that has multilvl classes inherited.")


b=multiple()
b.jobs()
b.everything()
b.about()