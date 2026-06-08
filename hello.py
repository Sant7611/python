student_info = {}
student_name = input("Enter your name: ")
subnum = int(input("Enter the number of subjects: "))
subjects = []
def add_student():
    for i in range(1, subnum+1):
        subMark = input(f"Enter the marks in no.{i} subject")
        subjects.append(subMark)
    
    student_info[student_name] = subjects
    return student_info
add_student()
print(student_info)
