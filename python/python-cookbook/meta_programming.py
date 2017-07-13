#! /usr/bin/python3
import sys
import time
import logging
import types
import weakref
import operator
from functools import wraps, partial
from inspect import signature
from collections import OrderedDict
from inspect import Signature, Parameter
from contextlib import contextmanager
import ast
import dis

# 25 拆解python字节码


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print('down!')


dis.dis(countdown)

exit(0)
# 24 解析与分解python源码 ast源码树
x = 20
s = 'x+10'
print(eval(s))
exec('for i in range(10): print(i)')

ex = ast.parse('x+20', mode='eval')
print(ex)  # <_ast.Expression object at 0x7fc22b4c3748>
print(ast.dump(ex))
'''
Expression(
           body=BinOp(
                      left=Name(
                                id='x',
                                ctx=Load()),
                      op=Add(),
                      right=Num(n=20)))
'''
top = ast.parse('for i in range(10): print(i)', mode='exec')
print(ast.dump(top))
'''
Module(body=[
             For(
                 target=Name(
                             id='i',
                             ctx=Store()),
                 iter=Call(
                           func=Name(
                                     id='range',
                                     ctx=Load()),
                           args=[
                                 Num(n=10)],
                           keywords=[]),
                 body=[
                       Expr(
                            value=Call(
                                       func=Name(
                                                 id='print',
                                                 ctx=Load()),
                                       args=[
                                             Name(
                                                  id='i',
                                                  ctx=Load())],
                                       keywords=[]))],
                 orelse=[])])
'''
exit(0)
# 23 在局部变量域中执行代码 exec() locals()
exec('b =  1 + 2')
print(b)  # 3


def get():
    exec('a = 1 + 2')
    print(a)  # NameError: name 'a' is not defined
# get()


def geta():
    print(locals())
    loc = locals()
    exec('a = 2 + 2')
    a = loc['a']
    print(locals())
    print(type(locals()))
    print(a)


geta()  # 4

exit(0)
# 22 定义上下文管理器的简单方法 contextlib.contextmanager


@contextmanager
def timethis(label):
    start = time.time()

    try:
        yield  # 之前代码作为__enter__()执行, 之后代码作为 __exit__()执行
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


with timethis('continuing'):
    n = 1000000
    while n > 0:
        n -= 1

exit(0)

# 21 避免重复的属性方法


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(
                'Expected type. {} must a type {}'.format(name, expected_type))
        else:
            setattr(self, storage_name, value)
    return prop


class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('sun', 24)
#p1 = Person('s', 'u')
print(p.name)

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


class Person1:
    name = String('name')
    age = Integer('age')


p1 = Person1()
p1.name = 'sun'
p1.age = 24

print(p1.name)
print(p1.age)


exit(0)
# 20 利用函数注解实现函数重载


class Test:
    def foo(self, x):
        print('this is foo one:', x)

    def foo(self, x, y):
        print('this is foo two:', x, y)

#t = Test()
# t.foo('a')
#t.foo('a', 'b')


class MultiMethod:
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        sig = signature(meth)

        types = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is Parameter.empty:
                raise TypeError(
                    'Argument {} must be annotated with a type'.format(name))
            if not isinstance(param.annotation, type):
                raise TypeError(
                    'Argument {} annotation must be a type'.format(name))
            if param.default is not Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(param.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No Match method for types{}'.format(types))

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class MultiDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultiMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


class Spam(metaclass=MultiMeta):
    def foo(self, x: int, y: int):
        print('foo1 int: {}, int: {}'.format(x, y))

    def foo(self, x: str, y: str):
        print('foo2 str: {}, str: {}'.format(x, y))

    def foo(self, x: str, y: int = 0):
        print('foo3 str： {}, int: {}'.format(x, y))


s = Spam()
s.foo('sun', 'say')
s.foo(12, 33)
s.foo('sun', 24)


class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults + 1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class Spam:
    @multimethod
    def bar(self, *args):
        # Default method called if no match
        raise TypeError('No matching method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('Bar 1:', x, y)

    @bar.match(str, int)
    def bar(self, s, n=0):
        print('Bar 2:', s, n)


exit(0)

# 19 在定义的时候初始化类的成员


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'age']


class Point(StructTuple):
    _fields = ['x', 'y']


s = Stock('sun', 24)
print(s)  # ('sun', 24)

exit(0)
# 18 以编程方式定义类


def __init__(self, name, age):
    self.name = name
    self.age = age


def say(self):
    print('say hello')


cls_dict = {
    '__init__': __init__,
    'say': say
}

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__  # change types to main

print(Stock)
s = Stock('sun', 3)
print(s)
exit(0)

# 17 在类上强制使用编程规约


class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['hello'] = 'world'
        print('class:', cls)  # class: <class '__main__.MyMeta'>
        print('clsname:', clsname)  # clsname: B
        print('bases:', bases)  # bases: (<class '__main__.A'>,)
        # clsdict: {'__module__': '__main__', '__qualname__': 'B',
        print('clsdict:', clsdict)
        #          'hello': 'world', 'say': <function B.say at 0x7f2ca96b3bf8>}
        return super().__new__(cls, clsname, bases, clsdict)

    def __init__(self, clsname, bases, clsdict):
        print(self)  # <class '__main__.B'>
        print('clsname:', clsname)
        print('bases:', bases)
        print('clsdict:', clsdict)
        super().__init__(clsname, bases, clsdict)


class A(metaclass=MyMeta):
    def __init__(self, name):
        self.name = name
    pass


class B(A):
    def say(self):
        pass


a = A('sun')

# 16 *args, **kwargs 强制参数签名 inspect
params = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None)
]

sig = Signature(params)
print(sig)  # (x, y=42, *, z=None)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


func(1, 2, z=4)
func('a', 'b')


def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
              for name in names]
    return Signature(params)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'age')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


print(signature(Stock))
print(signature(Point))

s = Stock('sun', 24)
print(s.name)
# ss = Stock('sun') TypeError: missing a required argument: 'age'


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class MyStructure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(MyStructure):
    _fields = ['name', 'shares', 'price']


class Point(MyStructure):
    _fields = ['x', 'y']


print(signature(Stock))
print(signature(Point))

# 15 定义有可选参数的元类


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        super().__init__(name, bases, ns)

# 14 捕获类的属性定义顺序


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Excepted type {} ' + str(self._expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)

# Example use


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# 13 使用元类控制实例的创建


class NoInstance(type):  # 注意type
    def __call__(self, *args, **kwargs):
        raise TypeError('Cannot instance this class')


class A(metaclass=NoInstance):
    @staticmethod
    def show(name):
        print('this is static show ' + name)


# a = A() # TypeError: Cannot instance this class
A.show('sun')

# 单例模式


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class B(metaclass=Singleton):
    def __init__(self):
        print('Create a B')


b = B()
bb = B()
print(b == bb)  # True

# 缓存模式


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()  # 创建value为弱引用对象的字典

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class C(metaclass=Cached):
    def __init__(self, name, age):
        print('createing name ' + name)


c = C('sun', 24)
cc = C('hua', 24)
ccc = C('sun', 24)
print(c == ccc)

# 12 使用装饰器扩充类的功能


def log_getattribute(cls):
    orig_attr = cls.__getattribute__

    def new_attr(self, name):
        print('getting ' + name)
        return orig_attr(self, name)

    cls.__getattribute__ = new_attr
    return cls


@log_getattribute
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        pass


a = A('sun', 24)
a.name
a.age
a.foo()

# 11 在装饰器中给包装函数增加参数


def add_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling debug...')
        return func(*args, **kwargs)
    return wrapper


@add_debug
def add(x, y):
    return x + y


add(1, 2)
add(1, 2, debug=True)

# 10 为类和静态方法提供装饰器　@staticmethod, @classmethod之前
# staticmethod 与 classmethod 区别：　前者不需要传递self, 后者只需要传递cls; 前者只能通过类名调用类变量， 后者能通过cls调用


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper


class Test:
    @timethis
    def instance_method(self, n):
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        while n > 0:
            n -= 1


t = Test()
t.instance_method(10000000)
t.class_method(10000000)
t.static_method(10000000)
Test.class_method(10000000)
Test.static_method(10000000)

# 9 将装饰器定义为类


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


print(add(10, 2))
print(add.ncalls)
print(add(2, 4))
print(add.ncalls)


class Test:
    @Profiled
    def add(self, x, y):
        return x + y


print('------')
t = Test()
t.add(2, 3)
t.add(3, 5)
print(t.add.ncalls)  # 2
print(Test.add.ncalls)  # 2

t2 = Test()
t2.add(3, 4)
print(t2.add.ncalls)  # 3
print(Test.add.ncalls)  # 3

# 8 将装饰器定义为类的一部分


class A:
    def decorate(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decoreate1...')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorate2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decoreate2...')
            return func(*args, **kwargs)
        return wrapper


a = A()

# 实例调用


@a.decorate
def add(x, y):
    pass

# 类调用


@A.decorate2
def add2(x, y):
    pass


add(1, 2)
add2(1, 2)


class B(A):
    @A.decorate2
    def foo(self):
        pass


b = B()
b.foo()

# 7 利用装饰器强制函数上的类型检查


def typeassert(*type_args, **type_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargrs):
            bound_values = sig.bind(*args, **kwargrs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(
                            name, bound_types[name]))
            return func(*args, **kwargrs)
        return wrapper
    return decorate


@typeassert(int, int)
def add(x, y):
    return x + y


@typeassert(int, z=int)
def add2(x, y, z=20):
    return x + y + z


print(add(2, 3))
# add(2., 'hello') TypeError: Argument x must be <class 'int'>
# add2(2, 'hello', 'world') #TypeError: Argument z must be <class 'int'>

# 6 带可选参数的装饰器


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use


@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

# 5 可自定义属性的装饰器 nonlocal


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kws):
            log.log(level, logmsg)
            return func(*args, **kws)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmessage):
            nonlocal logmsg
            logmsg = newmessage

        return wrapper
    return decorate

# Example use


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

# 4 定义一个带参数的装饰器


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


add(2, 3)
spam()

# 3 解除一个装饰器 func.__wrapped__()


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


def decorator3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 3')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
@decorator3
def add(x, y):
    return x + y


add(2, 3)  # decorator1 decorator2 decorator3
add.__wrapped__(2, 3)  # decorator2 decorator3 不一样之处

# 2 创建装饰器时保留函数元信息 functools.wraps


def timethis(func):
    @wraps(func)
    def wrapped(*args, **kws):
        starttime = time.time()
        result = func(*args, **kws)
        endtime = time.time()
        print(func.__name__, endtime - starttime)
        return result
    return wrapped


@timethis
def test(n):
    while n > 0:
        n -= 1


print(test.__name__)
test.__wrapped__(100)  # 直接访问原函数
test(100)

# 1 在函数上添加装饰器

test(1000000)
test(10000000)
test(100000000)
