class Student:
    
    def __init__(self):
       print("this is student's constructor")

class job(Student):
    def __init__(self):
       super().__init__() #tis calls parent's constructor that is student.
       print("this is jobs's constructor")

class multiple(job):
    def __init__(self):
       super().__init__() #this calls it's prents' constructor that is job.
       print("this is multiple's constructor")


# student = Student()
# jobs = job()
multiples = multiple()
