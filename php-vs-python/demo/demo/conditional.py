#! /usr/bin/python3

for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i)

for i in range(2, 3):  # 2
    print(i)

a = ['a', 'b', 'c']

for i in a:
    print(i)  # a b c

s = 'abcd'

for i in s:
    print(i)

d = {'a': 'aa', 'b': 'bb'}

for key, value in d.items():
    print(key, '--', value)

s = set('a')
s.add('b')

for i in s:
    print(i)

t = (123, 345)
for i in t:
    print(i)

# collections.Iterable
from collections import Iterable

print(isinstance(s, Iterable))

# string list dict set tuple  __iter__(object)


# slice

s = 'abcdefgh'

print(s[1])    # b
print(s[1:])   # bcdefgh
print(s[-1:])  # h
print(s[:])    # abcdefgh
print(s[1:4])  # bcd
print(s[1::4])  # bf
