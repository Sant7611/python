num = [1,2,3,4,5,6]

#use1
# sq = list(map(lambda x:x*x, num))
# print(sq)


#use2
square = lambda x:x*x # this is a function

# map(function, iterable)
sqList = map(square, num)
print(list(sqList))


#2. filter

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, num)
print(list(onlyEven))


#3. Reduce

from functools import reduce
# def sum(a,b):
#     return a+b

sum = lambda a,b : a+b

print(reduce(sum, num))

max_value = reduce(lambda x,y: x if x>y else y, num)
print(max_value)