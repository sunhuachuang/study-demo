# -*- coding: utf-8 -*-

import os, sys, re

class Test:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


t = Test('Tom')
j = Test('Jack')
print(t)

print(t.get_name())
print(j.get_name())

t.get_name = lambda s: s.name

print(t.get_name(t))

exit()
def a(name, **kwargs):
    print(kwargs)


a('a', **{'aa': 'bbb', 'cc': 'ccc'})

exit(0)


class A:
    def __init__(a, b):
        a.name = b

    def get_name(self):
        return self.name


a = A('aaaaaa')
print(a.get_name())
print(memoryview(a))

exit(0)



print( False == 0 ) # True
print( False > -1 ) # True

print( None == False ) # False
print( None == 0 )     # False
print( None == '' )    # False
print( False == '' )   # False
print( True == '' )    # False
print( '' == 0 )       # False
# print( [] > 0 )
print( [] == False ) # False
print( [] == 0 )     # False
# print({} > [])
print( {} == False ) # False
print( {} == 0 )  # False
print( {} == [] ) # False
# print( False < ' ' )

'''
bool 值可以与数字比较大小(转成0或1), 其他比较大小， 必须同类型
相等比较： 除了bool值与数字（0， 1）， 其他不同类型均为 False

Objects of different types, except different numeric types, never compare equal.

'''

exit(0)

a = {'aa': 123, 'bb': 234}

print(a['aaa'] if 'aaa' in a else 'cc')
exit(0)

import bcrypt

def encrypt(password, salt=None):
    return bcrypt.hashpw(password.encode('utf-8'), salt if salt else bcrypt.gensalt())

def decrypt(password, hashed):
    if bcrypt.hashpw(password.encode('utf-8'), hashed) == hashed:
        return True
    else:
        return False

h = encrypt('123456')
print(h)
print(decrypt('12345', h))

exit(0)


from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/todos/<int:id>')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)

exit(0)


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')




class A:
    def hello(self):
        print('A')

class B(A):
    name = 'aaa'
    id = 123
    def hello(self):
        A.hello(self)
        print('B')

    def get_id(self):
        return self.id

    def __dict__(self):
        return {'id': self.id, 'name': self.name}

b = B()

b.hello()
print(b.get_id())
print(id(b))
print(dir(b))

print(b)

exit(0)



for i in range(8, -1, -1):
    print(i)


def test():
    print(a+1)

a = 10
test()
exit(0)





class A:
    def __call__(self):
        print('call from class')

a = A()
a()
a.__call__ = lambda: print('calll from lambda')
a()
a.__call__()

exit(0)

import time
class Time:
    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kws):
        start_time = time.time()
        result = self._wrapped(*args, **kws)
        print('all time is :', time.time()-start_time)
        return result

    def __get__(self, instance, owner): #针对class method 必须有self参数
        start_time = time.time()
        result = lambda *args, **kwargs: self._wrapped(instance, *args, **kwargs)
        print('all time is :', time.time()-start_time)
        return result

@Time
def func():
    time.sleep(1)
    print('func ok!')

func()

class Test:
    @Time
    def method(self):
        time.sleep(1)
        print('method ok!')

    @staticmethod
    def method2(): # no self is ok
        time.sleep(1)
        print('method2 ok!')

a = Test()
a.method()
Test.method2()

exit(0)

import math

x = 1
a = (lambda x: x+1)(x)

print(a)

exit(0)

x = 1
s = (x for _ in range(10))

print(list(s))

class A:
    x = 2
    g = x * 2
    gg = (x for _ in range(10)) # x = 1 generator 作用范围在用到生成器的地方
    ggg = (lambda x: (x for _ in range(10)))(x) # x = 2
    #g = (1 for _ in range(10))

print(A.g)
print(list(A.gg))
print(list(A.ggg))

exit(0)

a = [(1, 2), (3, 4), (0, 0), (1, 1)]
b = [(1, 2), (0, 0), (4, 8)]

print(a[1:])
print(a[0:-1])

exit(0)
b.sort(key=lambda u: u[0])
print(b)



exit(0)

def get_line_all_points(point1, point2):
    if point1 == point2:
        return
    line = [point1, point2]
    a = (point1[1] - point2[1])/(point1[0] - point2[0])
    b = (point1[0]*point2[1] - point1[1]*point2[0])/(point1[0] - point2[0])
    for x in range(0, 7):
        if (x != point1[0]) and (x != point2[0]):
            y = a*x + b
            if math.ceil(y) == int(y) and int(y) <= 5:
                line.append((x, int(y)))
    if (len(line) > 2):
        return line
    return

print(get_line_all_points((1, 2), (2, 4)))

exit(0)


print('0' * 2)

exit(0)

a = 0

for n in range(0, 65):
    a += 1
    print(bin(a))

exit(0)

print(not False)
print(bin(0))


def suma():
    a = [123, 123]
    return a

print(suma())
exit();

print ('\n'.join([''.join([('SunHuachuang'[(x-y)%8] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ' ) for x in range(-30,30)])for y in range(15,-15,-1)] ))

exit()

for i in range(4, 20):
    print("test"+str(i)+";test"+str(i)+"@example.com;"+str(i))



exit()
print ("aaaaaa")
with open('aaa') as o:
    print (o.readlines())
