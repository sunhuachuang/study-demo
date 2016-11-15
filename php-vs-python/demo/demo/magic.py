#! /usr/bin/python3

# 迭代器 生成器 描述器 装饰器

l = [1, 2, 3, 4]

for i in l:
    print(i)

def create_iter():
    a = 0
    while a < 10:
        yield a
        a += 1

for i in create_iter():
    print(i)


from functools import wraps

def check(func):
    @wraps(func)
    def wrapper(x):
        if isinstance(x, int):
            return func(x)
        raise TypeError('Not int type')
    return wrapper

@check
def add_one(x):
    return x + 1

# add_one = check(add_one())

# add_one(1)
# add_one('a')


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A is {}, {}'.format(self.x, self.y)

    def __len__(self):
        return len(self.__dict__)

a = A(1, 2)

print(str(a))
print(len(a))
