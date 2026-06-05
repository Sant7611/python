class Student:
    name = 'Santosh'
    role='student'
    def about(self):
        print(f'my name is {self.name}. i work as a {self.role}')

class job:
    role='job'
    def jobs(self):
        print(f'my role is {self.role}')

class multiple(Student, job):
    def everything(self):
        print("This is the class that has multiple classes inherited.")


b=multiple()
b.jobs()
b.everything()
b.about()