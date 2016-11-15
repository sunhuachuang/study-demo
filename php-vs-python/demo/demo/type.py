#! /usr/bin/python3

a = 1
print(type(a)) #<class 'int'>

b = 1.1
print(type(b)) #<class 'float'>

c = 'string'
print(type(c)) #<class 'str'>

d = True
print(type(d)) #<class 'bool'>

e = [1, 3, 4, 'aa', 3.33, 1]
print(type(e)) #<class 'list'>

f = {'a': 'aa', 'b': 'bb', 'c': 12345}
print(type(f)) #<class 'dict'>

g = None
print(type(g)) #<class 'NoneType'>

h = ('a', 123)
print(type(h)) #<class 'tuple'>

i = set('a')
i.add('a')
print(type(i)) #<class 'set'>
print(i) #{'a'} |(并集)　&(交集)　-(差集)
