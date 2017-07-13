#! /usr/bin/python3
import sys
import html
from functools import partial
import math
from urllib.request import urlopen
from queue import Queue
from functools import wraps

sys.exit(0)

# 12 访问闭包中定义的变量


def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func


f = sample()
f()
f.set_n(1)
print(f.get_n())
f.set_n(2)
print(f.get_n())
f.set_n(3)
print(f.get_n())
f.set_n(4)
print(f.get_n())


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))
    # Redirect special methods

    def __len__(self):
        return self.__dict__['__len__']()

# Example use


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
s.push(10)
s.push(20)
s.push('hello')
print(len(s))  # 3
print(s.pop())  # hello
print(s.pop())  # 20
print(s.pop())  # 10

# 11 内联回调函数


def apply_async(func, args, callback):
    result = func(*args)
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', ' world'))
    print(r)
    for n in range(1, 10):
        r = yield Async(add, (n, n))
        print(r)
    print('ok')


test()

# 10 带额外状态信息的回调函数


def apply_async(func, args, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got: ', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', ', world!'), callback=print_result)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}]: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', ', world!'), callback=r.handler)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}]: {}'.format(sequence, result))
    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)  # [1]: 5
apply_async(add, ('hello', ', world!'), callback=handler)  # [2]: hello, world!


def make_handler2():  # 协程
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}]: {}'.format(sequence, result))


handler2 = make_handler2()
next(handler2)
apply_async(add, (2, 3), callback=handler2.send)  # [1]: 5
apply_async(add, ('hello', ', world!'),
            callback=handler2.send)  # [2]: hello, world!

# 9 将单方法的类转换为函数


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener


# Example use
yahoo = urltemplate(
    'http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# 8 减少可调用对象的参数个数 functools.partial


def param(a, b, c, d):
    print(a, b, c, d)


s1 = partial(param, 1)  # 固定传值
s1(2, 3, 4)  # 1 2 3 4
s2 = partial(param, 1, 2)
s2(3, 4)  # 1 2 3 4
s3 = partial(param, d='last')
s3(1, 2, 3)  # 1 2 3 last

points = [(10, 0), (1, 2), (4, 6), (-3, 6), (0, -9)]


def distance(p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    return math.hypot(x1 - x2, y1 - y2)


pt = (0, 0)
points.sort(key=partial(distance, pt))
print(points)  # [(1, 2), (4, 6), (-3, 6), (0, -9), (10, 0)]

# 7 匿名函数捕获变量值
x = 10


def a(y): return x + y


aa = lambda y, x=x: x + y
print(a(10))  # 20
x = 20


def b(y): return x + y


print(a(10))  # 30
print(b(10))  # 30
print(aa(10))  # 20

nums = [lambda x: x + n for n in range(5)]
for n in nums:
    print(n(1))  # 5 5 5 5 5

numss = [lambda x, n=n: x + n for n in range(5)]
for n in numss:
    print(n(1))  # 1 2 3 4 5

# 6 定义匿名或内联函数


def add(x, y): return x + y


print(add(2, 3))


def sum_self(*xs):
    ss = 0
    for x in xs:
        ss += int(x)
    return ss


print(sum_self(1, 2, 3, '4'))

# 5 定义有默认参数的函数
_no_value = object()


def spam(name, o=_no_value):
    if o is _no_value:
        print('o is nothing')
    else:
        print('o is {}'.format(o))


spam('sun', None)  # o is None
spam('sun', 'aaa')  # o is aaa
spam('sun',)  # o is nothing

# 4 返回多个值的名称


def myfun():
    return 1, 'aa'


print(myfun())  # (1, 'aa') 元组是由,号产生的

# 3 给函数参数添加元信息 注解


def avg(a: int, b: int) -> float:
    return (a + b) / 2


print(avg(1, 2))  # 1.5
# {'a': <class 'int'>, 'return': <class 'float'>, 'b': <class 'int'>}
print(avg.__annotations__)

# 2 强制关键字参数


def force_param(name, *, home):
    print('ok')


force_param('sun', home='ok')
# force_param('sun') TypeError


def force_param2(name, *homes, age):
    print(homes, age)


force_param2('sun', 'ok', 'okk', age='where')  # ('ok', 'okk') where
# force_param2('sun', 'where') #TypeError: force_param2() missing 1 required keyword-only argument: 'age'
force_param2('sun', age=24)  # () 24


def param(name, age):
    print(name, age)


param(name='sun', age=24)  # sun 24
param(age=24, name='sun')  # sun 24

# 1 接受任意参数的函数


def avg(first, *param):
    print(param)  # (2, 3) (2, 3, 4) (2, 3, 4, 5)
    return (first + sum(param)) / (1 + len(param))


print(avg(1, 2, 3))  # 2.0
print(avg(1, 2, 3, 4))  # 2.5
print(avg(1, 2, 3, 4, 5))  # 3.0


def make_element(name, value, **attrs):
    attrs_value = ['%s="%s"' % item for item in attrs.items()]
    attrs_values = ' '.join(attrs_value)
    element = '<{name} {attr}>{value}</{name}>'.format(
        name=name,
        value=html.escape(value),
        attr=attrs_values
    )
    return element


# <div classes="eclass" ides="eid">this is div</div>
print(make_element('div', 'this is div', ides='eid', classes='eclass'))
# <p names="ep">&lt;span&gt;p&lt;/span&gt;</p>
print(make_element('p', '<span>p</span>', names='ep'))
