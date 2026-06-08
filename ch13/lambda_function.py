#lambda arguments:expressions
#anonymous function just like in js.
square = lambda x:x*x

print(square(6))


#with map:
lst = [1,2,3,4,5]

sqnum = list(map(lambda x: x*x, lst))
print(sqnum)


#with filter:
evens = list(filter(lambda x: x%2 ==0, lst ))
print(evens)


#with sorted:
dictio = {'a':1, 'b':3, 'c':5, 'd':9}

#this sorts based on values. .items() returns tuple, and x[1] accesses value for that tuple
sortedItems = sorted(dictio.items(), key=lambda x:x[1])

print(sortedItems)