#! /usr/bin/python3
import sys
import io
import math
import time
import operator
import weakref
import collections
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial, total_ordering
from abc import ABCMeta, abstractmethod

sys.exit(0)

# 25 创建缓存实例


class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


class CachedSpamManager2:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam3._new(name)  # Modified creation
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam3:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

# 24 让类支持比较操作 functools.total_ordering()


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                                              self.living_space_footage,
                                              self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage

# 23 循环引用数据结构的内存管理 weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

# 21 实现访问者模式


class HTTPHandler:
    def handler(self, request):
        method = 'do' + request.request_method
        getattr(self, method)(request)

    def do_GET(self, request):
        pass

    def do_POST(self, request):
        pass

# 20 通过字符串调用对象方法 getattr(cls, 'stringfunc')(params) & operator.methodcaller('string', params)(cls)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'point({}, {})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
print(getattr(p, 'distance')(0, 0))  # 3.605551275463989

points = [
    Point(2, 3),
    Point(1, 1),
    Point(4, 3),
    Point(2, 5),
]
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)  # [point(1, 1), point(2, 3), point(4, 3), point(2, 5)]

# 19 实现状态对象或者状态机 (状态模式)


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def colse(self):
        return self._state.close(self)


class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def wirte(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing {}'.format(data))

    @staticmethod
    def open(conn):
        raise RuntimeError('Already opened')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


c = Connection()
print(c._state)  # <class '__main__.ClosedConnectionState'>
# c.read() RuntimeError: Not open
c.open()
print(c._state)  # <class '__main__.OpenConnectionState'>
c.read()  # reading
c.write('hello')  # writing hello
# c.open() RuntimeError: Already opened
c.colse()  # <class '__main__.ClosedConnectionState'>
print(c._state)

# 18 利用 Mixins 扩展类的功能


class LoggedMappingMixins:
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting {} value.'.format(key))
        return super().__getitem__(key)

    def __setitem(self, key, value):
        print('Setting {} value is {}.'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deling {}'.format(key))
        return super().__delitem__(key)


class OnceMappingMinxins:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('{} already setted.'.format(key))
        return super().__setitem__(key, value)


class StringKeysMappingMinxins:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('This key must string')
        return super().__setitem__(key, value)

# 17 创建不掉用ｉｎｉｔ方法的实例


class Date:
    def __init__(self, year, mouth, day):
        self.year = year
        self.mouth = mouth
        self.day = day


a = Date.__new__(Date)
print(a)  # <__main__.Date object at 0x7f6a11ff3128>
# a.year #AttributeError: 'Date' object has no attribute 'year'

# 16 在类中定义多个构造器


class Date:
    def __init__(self, year, mouth, day):
        self.year = year
        self.mouth = mouth
        self.day = day

    def getDate(self):
        return str(self.year) + '-' + str(self.mouth) + '-' + str(self.day)

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(2016, 6, 18)
print(d.getDate())

a = Date.today()
print(a.getDate())

# 15 属性的代理访问


class A:
    def foo():
        pass

    def bar():
        pass


class B:
    def __init__(self):
        self._a = A()

    def hello():
        pass

    def __getattr__(self, name):
        return getattr(self._a, name)

# 14 实现自定义容器 collections


class DryIter(collections.Iterable):
    def __iter__(self):
        pass


a = DryIter()

# 13 实现数据模型的类型约束


class Descriptor():
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('value must < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('Sun', 24, 45.5)
print(s.name)
# s.name = '1234567890' ValueError: value must < 8
# s.price = 'aa' #TypeError: expected <class 'float'>


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate

# Example


@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)

# Example


class Stock3(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# Best way


def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for unsigned values
def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for allowing sized values
def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass

# 12 定义接口或抽象基类


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


IStream.register(io.IOBase)
f = open('test.txt')
print(isinstance(f, IStream))

# 11 简化数据结构的初始化


class Structurel:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Excepted {} argument.'.format(self._fields))
        else:
            for name, value in zip(self._fields, args):
                setattr(self, name, value)


class Test1(Structurel):
    _fields = ['name', 'age']


class Test2(Structurel):
    _fields = ['aa', 'bb', 'cc']


t1 = Test1('sun', 24)
print(vars(t1))  # {'age': 24, 'name': 'sun'}
t2 = Test2('a', 'b', 'c')
print(vars(t2))  # {'bb': 'b', 'cc': 'c', 'aa': 'a'}
# t22 = Test2('a', 'b') #TypeError: Excepted ['aa', 'bb', 'cc'] argument.

# 10 使用延迟计算属性


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)  # 4.0
print(c.area)  # computing area 50.26548245743669
print(c.area)  # 50.26548245743669
print(c.area)  # 50.26548245743669
print(c.perimeter)  # computing perimeter 25.132741228718345
print(c.perimeter)  # 25.132741228718345
print(c.perimeter)  # 25.132741228718345

# 9 创建新的类或实例对象 描述器（__get__ __set__ __delete__） 只能作为类中已定义的变量


class Person:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cla):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Must is string')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Firelds:
    x = Person('x')
    y = Person('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


f = Firelds('aaa', 'bbb')
print(f.x)  # aaa
print(f.y)  # bbb
# f.x = 20 #TypeError: Must is string
f.x = 'ccc'
print(f.x)  # ccc
del f.x
# print(f.x) #KeyError: 'x'

# 8 子类中扩展property


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot delete attribute')


class SubPerson(Person):
    @property
    def name(self):
        print('get name')
        return super().first_name

    @name.setter
    def name(self, value):
        print('set name: ', value)
        super(SubPerson, SubPerson).first_name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete this name')
        super(SubPerson, SubPerson).first_name.__delete__(self)


s = SubPerson('sun')
print(s.name)

# s.name = 20 #TypeError: Excepted a string
# del s.name #AttributeError: cannot delete attribute

# 7 调用父类的方法 super()


class A:
    def __init__(self, x):
        self.x = x

    def get_name(self):
        return self.x


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def get_name(self):
        return self.y

    def get_all_name(self):
        return super().get_name() + self.get_name()


b = B(1, 2)
print(b.get_all_name())  # 3


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


c = C()  # Base.__init__   B.__init__  A.__init__  C.__init__

# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
print(C.__mro__)

# 6 创建可管理的属性 @property


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot delete attribute')


a = Person('aaa')
print(a.first_name)  # aaa
# a.first_name = 24 #TypeError: Excepted a string
# del a.first_name #AttributeError: cannot delete attribute

# 5 在类中封装属性名 _开头都是类的保护属性（习惯）　私有属性__开头则会自动转化为_(类名)__() 不会被继承


class A:
    def __init__(self):
        self._protect_variable = 0

    def _protect_method():
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method():
        pass

    def public_method():
        pass


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # 不会区覆盖

    def __private_method():
        pass  # 不会覆盖

# 重名内部函数名　后下划线 lambda_

# 4 创建大量对象时节省内存 __slote__ 只是单纯内存优化工具　适用于生成几百万的实例要求时


class Date:
    __slote__ = ['year', 'month', 'day']

    def __init__(self):
        self.year = year
        self.month = month
        self.day = day

# 3 让对象支持上下文管理协议 (with) __enter__() __exit__()


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Alreay connected!')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)


class LazyConnections:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


conn = LazyConnections(('www.python.org', 80))
with conn as s:
    pass
    with conn as s2:
        pass

# 2 自定义字符串的格式化　__format__
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        code = 'ymd' if code == '' else code
        fmt = _formats[code]
        return fmt.format(d=self)


date = Date(2016, 5, 31)
print(format(date, 'mdy'))  # 5/31/2016
print(format(date))  # 2016-5-31
print('the date is {:dmy}'.format(date))  # the date is 31/5/2016

# 1 改变对象的字符串输出　__str__ and  __repr__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name is {0.name!s}, age is {0.age!s}'.format(self)

    def __repr__(self):
        return 'Person({0.name!r}, {0.age!r})'.format(self)


sun = Person('sun', 24)
sun  # Person('sun', 24)
print(sun)  # name is sun, age is 24
print('{0!r}'.format(sun))  # Person('sun', 24)
print('{0}'.format(sun))  # name is sun, age is 24
