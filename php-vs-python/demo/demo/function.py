#! /usr/bin/python3

def add(x, y):
    return x + y

def get(x, y):
    return x, y

a, b = get(1, 2)
print(a, b)

def add2(x, y, *xs):
    print(xs)

add2(1, 2, 3, 4, 5)

def add3(x, y, **kwxs):
    print(kwxs)

add3(1, 2, name='sun', age=2)

# map/reduce
def add_one(x):
    return x + 1

l = [1, 2, 3, 4, 5]

ll = map(add_one, l)
print(ll)

lll = list(ll)
print(lll)

from functools import reduce

lr = reduce(add, l)
print(lr)

def more_zero(x):
    if x > 0:
        return x

l = [1, 2, 3, 0, -1, -2]
lf = filter(more_zero, l)
print(lf)
print(list(lf))

l = ['F', 'a', 'Aaa', 'D', 'B', 'Ccc']
ls = sorted(l, key=str.lower)
print(list(ls))

a = lambda x: x + 1
b = a(2)
print(b)
