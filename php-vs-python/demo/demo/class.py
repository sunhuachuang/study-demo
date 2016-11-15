#! /usr/bin/python3

class A:
    __private = 'aa'

    def __init__(self, name, age, say):
        self.name = name
        self._age = age
        self.__say = say

    def getAge(self):
        return self._age

    def getSay(self):
        return self.__say

    def getPrivate(self):
        return self.__private

a = A('sun', 2, 'hello')
print(a.name)
print(a._age)
# print(a.__say)
print(a.getSay())
print(a.getPrivate())

class B(A):
    def __init__(self, name, age, say):
        super().__init__(name, age, say)

    @staticmethod
    def getstatic():
        print('static method')

    @classmethod
    def getclassmethod(cls):
        print('class method')

b = B('hua', 4, 'world')

print(b.name)
print(b._age)
print(b.getSay())
print(b.getPrivate())

B.getstatic()
B.getclassmethod()
