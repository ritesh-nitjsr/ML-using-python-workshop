a = lambda x : x*2
print a(4)
b = lambda x,y : x*y
print b(5,3)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#'b' contains only those element of 'a' which are didvisible by 2
b = filter(lambda x : x%2,a)
print b

#'b' contains squares of all values of 'a'
b = map(lambda x : x**2, a)
print b

#'b' contains the summation of all values of a
b = reduce(lambda x,y : x+y, a)
print b

#Seive Implementation
from math import sqrt
arr = range(2,100)
for i in range(2,int(sqrt(100))+1):
    arr = filter(lambda x : x%i!=0 or x==i, arr)
print arr
