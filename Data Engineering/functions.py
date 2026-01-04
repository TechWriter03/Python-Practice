def sum(a,b,c=30):
    print("sum :",a+b+c)
    return a+b+c

val = sum(10,20)
print("returned value :",val)
print(sum(10,20,40))


def my_func(*x):
    print(x,type(x))

my_func(10,20,30)


def func(**x):
    print(x,type(x))

func(x=10,y=20,z=30)

multiply = lambda x,y : x*y
mul = multiply(20,30)
print(mul)

def square(x):
    return x*x

my_list = [1,2,3,4,5]
result = list(map(square,my_list))
print(result)

def square(x):
    if (x%2==0):
        return x*x
    
result = list(filter(square,my_list))
print(result)

from functools import reduce

def add(x,y):
    return x+y

result = reduce(add,my_list)
print(result)
print()

for index,value in enumerate(my_list):
    print(index,value)