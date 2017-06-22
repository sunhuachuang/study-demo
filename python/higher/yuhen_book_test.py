class User:
    def __init__(self):
        self._data = []

    def add(self, d):
        self._data.append(d)

    def data(self):
        return iter(self._data)

    def __iter__(self):
        return iter(self._data)


u = User()

u.add("sun")
u.add("hua")

for i in u.data():
    print(i)


for i in u:
    print(i)


# error next
class DataIter:
    def __init__(self, data):
        self._index = 0
        self._data = data._data

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()

        d = self._data[self._index]
        self._index += 1
        return d


class Data:
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        return DataIter(self)


data = Data(1, 2, 3)

#i = iter(data)

for x in data:
    print(i)


# AttributeError: 'generator' object has no attribute 'next'
class Data:
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        for i in self._data:
            yield i


for i in Data(1, 2, 3, 4):
    print(i)

# yield 黑魔法，协程


def coroutine():
    print("start coroutine...")
    result = None
    while True:
        s = yield result
        result = s.split(',')


c = coroutine()
c.send(None)  # 启动
c.send("a, b, c")
c.close()

# 生产消费模型


def consumer():
    while True:
        d = yield
        if not d:
            break
        print("consumer: ", d)


cc = consumer()
c.send(None)  # 启动消费者
c.send(1)  # 生产数据， 并提交给消费者
c.send(2)
c.send(None)  # 生产结束，通知消费者结束

# callback 模式


def framework(logic, callback):
    s = logic()
    print("FX logic:", s)
    print("FX do something ...")
    callback("async: " + s)


def logic():
    return "mylogic"


def callback(s):
    print(s)


framework(logic, callback)


def yieldframework(logic):
    try:
        it = logic()
        s = next(it)
        print("FX logic:", s)
        print("FX do something ...")
        it.send("async: " + s)
    except StopIteration:
        pass


def loginc():
    s = "mylogic"
    r = yield s
    print(r)


yieldframework(loginc)

from itertools import chain
it = chain(range(3), "abc")
list(it)

from itertools import combinations
it = combinations("abcde", 2)
list(it)  # [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e')]

from itertools import combinations_with_replacement
it = combinations_with_replacement("abcde", 2)
list(it)  # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'd'), ('d', 'e'), ('e', 'e')]

from itertools import compress
it = compress("abcde" [1, 0, 1, 0, 0])
list(it)  # ['a', 'c']


# 模块
import sys
import types
m = types.ModuleType("sample", "sample module.")


def test():
    print("test...")


m.test = test
m.test()

# imp
import imp
imp.new_module("sample2")
imp.find_module("os")


# property


class Test:
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


class User:
    def __init__(self, uid):
        self._uid = uid

    uid = property(lambda o: o._uid)
    name = property(
        lambda o: o._name,
        lambda o, value: setattr(o, "_name", value),
        lambda o: delattr(o, "_name")
    )
    # lambda 里面不能使用赋值语句 所以使用setattr
    # 尽可能使用属性，而非暴露内部字段


# __slots__
# 大量对象的时候节约空间


class User:
    __slots__ = ("_name", "_age")

    def __init__(self, name, age):
        self._name = name
        self._age = age

# __setitem__
# __call__ callable
# __dir__


# 异常
import warnings


def test(n):
    try:
        n = n % 2
    except BaseException:
        raise Exception('error num')
    else:
        warnings.warn("this is else no except")
    finally:
        print("this is finally, alway do")

    return n


def test(n):
    # 断言
    assert n > 0, "n must > 0"
    print(n)

# 上下文管理器
# __enter__ 初始化对象。返回上下文信息
# __exit__ 执行清理操作


class MyContext:
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        print("enter: ", self._name)
        return self._name

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(exc_type, ': ', exc_value, '.')
        print('exit')
        return True


with MyContext('a') as a:
    print(a)

with MyContext('b'):
    raise Exception("error message")

with MyContext("aa") as a, MyContext("bb") as b:
    print(a, b)


from contextlib import contextmanager


@contextmanager
def closing(o):
    print("enter...")
    yield o

    print("exit...")
    o.close()


with closing(open('xx', 'r')) as f:
    print(f.readlines())


# 装饰器
class Test:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        args = filter(bool, args)
        self._func(*args)


@Test
def check_args(*args):
    print(args)


def add_action(cls):
    cls.add_action = staticmethod(lambda: "add_action")
    return cls


@add_action
class Test:
    pass


print(Test.add_action())

# 元类
Date = type("Date", (object,), {'x': 1, 'y': lambda x: x + 1})

print(Date.x)
print(Date.y(1))


class InjectMeta(type):
    def __new__(cls, name, bases, attrs):
        t = type.__new__(cls, name, bases, attrs)

        def print_id(self):
            print(hex(id(self)))
        t.print_id = print_id
        t.s = "hello"

        return t


class Test:
    __metaclass__ = InjectMeta
