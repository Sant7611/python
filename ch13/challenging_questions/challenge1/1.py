employees = [
    {"name": "Alice", "department": "IT", "salary": 75000},
    {"name": "Bob", "department": "HR", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 65000},
    {"name": "Dave", "department": "Finance", "salary": 90000},
    {"name": "Eve", "department": "IT", "salary": 45000}
]

# 1. Use a list comprehension to extract the salaries of all "IT" employees.

salaries = [i['salary'] for i in employees if i['department'] == 'IT' ]
print(salaries)

