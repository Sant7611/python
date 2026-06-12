# #lambda arguments:expressions
# #anonymous function just like in js.
# square = lambda x:x*x

# print(square(6))


# #with map:
# lst = [1,2,3,4,5]

# sqnum = list(map(lambda x: x*x, lst))
# print(sqnum)


# #with filter:
# evens = list(filter(lambda x: x%2 ==0, lst ))
# print(evens)


# #with sorted:
# dictio = {'a':1, 'b':3, 'c':5, 'd':9}

# #this sorts based on values. .items() returns tuple, and x[1] accesses value for that tuple
# sortedItems = sorted(dictio.items(), key=lambda x:x[1])

# print(sortedItems)


# from functools import reduce
# cart = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 25},
#     {"product": "Keyboard", "price": 75}
# ]
# # Your code here using sorted() and lambda

# sorted_list = sorted(cart, key=lambda x: x['price'],reverse=True)
# print(sorted_list)



# # Question 2: Data Filtering (The Active Users list)
# # Imagine you serialized a queryset of users, but now you only want to extract the users who are both is_active AND strictly over age 18.
# users = [
#     {"username": "alice", "is_active": True, "age": 22},
#     {"username": "bob", "is_active": False, "age": 19},
#     {"username": "charlie", "is_active": True, "age": 17},
#     {"username": "dave", "is_active": True, "age": 30}
# ]
# # Your code here using filter() and lambda

# filtered_users = list(filter(lambda x:x['is_active'] == True and x['age'] > 18 , users))
# print(filtered_users)



# # Question 3: Data Transformation (The Email Extractor)
# # You have a list of user profiles. Use map() to create a simple list that contains only the email addresses in lowercase.

# profiles = [
#     {"name": "Alice", "email": "ALICE@example.com"},
#     {"name": "Bob", "email": "bob@DOMAIN.com"}
# ]
# # Your code here using map() and lambda (Remember to cast to list()!)

# new_email = list(map(lambda x:x['email'].lower(), profiles))
# print(new_email)


# Question 4: The Combo Challenge (Filter + Map)
# You have a list of transactions.

# Use filter() to find only the "completed" transactions.
# Use map() to extract just the "amount" from those completed transactions.

transactions = [
    {"id": 1, "status": "pending", "amount": 100},
    {"id": 2, "status": "completed", "amount": 250},
    {"id": 3, "status": "failed", "amount": 50},
    {"id": 4, "status": "completed", "amount": 90}
]
# Your code here

completed_transaction = list(filter(lambda x:x['status'] == 'completed', transactions))

amt_of_compl_trans = list(map(lambda x:x['amount'], completed_transaction))

print(amt_of_compl_trans)