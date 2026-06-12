
#2. Use filter, map, and lambda to get a list of the names of "IT" employees who earn more than 60,000, and then use String join() to combine their names into a single string separated by | (e.g., "Alice | Charlie").

employees = [
    {"name": "Alice", "department": "IT", "salary": 75000},
    {"name": "Bob", "department": "HR", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 65000},
    {"name": "Dave", "department": "Finance", "salary": 90000},
    {"name": "Eve", "department": "IT", "salary": 45000}
]
# (a,b)=>{}

fltr = lambda x: x['salary']>60000 and x['department'] == 'IT'


fltrlst = list(filter(fltr, employees))
print(fltrlst)

names = list(map(lambda x: x['name'], fltrlst))
print(names)

res = "|".join(names)
print(res)