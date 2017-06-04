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
c.send(None) # 启动
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
c.send(None) # 启动消费者
c.send(1) # 生产数据， 并提交给消费者
c.send(2)
c.send(None) # 生产结束，通知消费者结束

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
list(it) #[('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e')]

from itertools import combinations_with_replacement
it = combinations_with_replacement("abcde", 2)
list(it) #[('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'd'), ('d', 'e'), ('e', 'e')]

from itertools import compress
it = compress("abcde" [1, 0, 1, 0, 0])
list(it) # ['a', 'c']


# 模块
import sys, types
m = types.ModuleType("sample", "sample module.")

def test():
    print("test...")

m.test = test
m.test()

# imp
import imp
imp.new_module("sample2")
imp.find_module("os")
