#3. Use functools.reduce and a lambda to calculate the total salary of all the IT employees combined.
employees = [
    {"name": "Alice", "department": "IT", "salary": 75000},
    {"name": "Bob", "department": "HR", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 65000},
    {"name": "Dave", "department": "Finance", "salary": 90000},
    {"name": "Eve", "department": "IT", "salary": 45000}
]

from functools import reduce 

filtered = lambda x:x['department'] == 'IT'

fltrlst = list(filter(filtered, employees))

namelst = list(map(lambda x: x['salary'], fltrlst))
print(namelst)

print(reduce(lambda x,y: x+y, namelst))