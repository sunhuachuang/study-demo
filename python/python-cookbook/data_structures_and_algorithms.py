#! /usr/bin/python3
import sys
import heapq
import json
import os
from collections import deque  # 集合
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import namedtuple
from collections import ChainMap
from operator import itemgetter  # 排序
from operator import attrgetter
from itertools import groupby  # 通过字段分组
from itertools import compress

sys.exit(0)

# 20 合并字典 collection ChainMap(引用) dict update(新建)
a = [34, 54, 4]
b = ['sf', 'sd']
print(a + b)  # 列表合并与差集 a+b a-b

a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}
c = ChainMap(a, b)
print(c['a'], c['b'], c['c'])  # 1 2 4
print(len(c))
print(list(c.keys()))
print(list(c.values()))

merge = dict(b)
merge.update(a)
print(merge)  # {'b': 2, 'c': 4, 'a': 1}

# 19 转换计算数据 生成器
num = [1, 4, 5]
num_sum = sum(x * x for x in num)
print(num_sum)

files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There is python')
else:
    print('There is no python!')

s = ['aa', 'aa@example.com', 34]
print(','.join(str(x) for x in s))

# 18 映射名称到序列（命名元组） colletctions namedtuple
Subscriber = namedtuple('Subscriber', ['name', 'email', 'phone'])
sub = Subscriber('admin', 'admin@example.com', 0)
print(sub)
print(sub.email)
sub = sub._replace(phone=123456)
print(sub)

# 17 过滤字典， 生产字典的子集
prices = {
    'a': 34.6,
    'b': 234,
    'c': 450,
    'd': 43.6,
}
prices_derivate = {key: value for key,
                   value in prices.items() if value > 100}  # 字典推导
print(prices_derivate)
filter_name = {'a', 'c', 'f'}
prices_filter = {key: value for key,
                 value in prices.items() if key in filter_name}  # 只有if 没有else
print(prices_filter)

# 16 过滤序列
lists = [1, 4, 67, 3, -6, 4, 0]
lists_derivate = [n for n in lists if n > 0]  # 列表推导 占内存
print(lists_derivate)

pos = (n for n in lists if n > 0)  # 生产器表达式
for i in pos:
    print(i)

values = [23, 6, 3, -4, '-53', '-', 'sfd']


def is_int(val):  # filter
    try:
        x = int(val)
        return True
    except ValueError:
        return False


print(list(filter(is_int, values)))  # [23, 6, 3, -4, '-53']
clip_values = [1, 4, 6, 0, -5, -3]
clip_values_m = [n if n > 0 else 0 for n in clip_values]
print(clip_values_m)

addresses = [
    'aaaaaaa',
    'bbbbbbb',
    'ccccccc',
    'ddddddd'
]

numbers = [2, -3, 4, 0]
numbers_boolean = [n > 0 for n in numbers]
addresses_compress = list(compress(addresses, numbers_boolean))
print(addresses_compress)

# 15 通过某个字段分组 itertools groupby
# 也通过 defaulitdict(list) append遍历添加（快）
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('  ', i)

# 14 排序实例对象 operator attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(22), User(23), User(56), User(4)]
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter('user_id')))

# 13 通过关键字排序字典列表 operator itemgetter sorted or min/max
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))

rows_by_fname_lambda = sorted(rows, key=lambda r: r['fname'])
rows_by_lname_fname_lambda = sorted(
    rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_uid)

# 12 寻找出现次数最多元素 Counter(底层是字典) . most_common
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

counter_words = Counter(words)
top_words = counter_words.most_common(3)
print(top_words)  # [('eyes', 8), ('the', 5), ('look', 4)]
print(counter_words['eyes'])  # 8
add_words = ['eyes', 'the', 'the', 'the']
counter_words.update(add_words)  # add
print(counter_words.most_common(3))

a = Counter(words)
b = Counter(add_words)
# Counter({'eyes': 9, 'the': 8, 'look': 4, 'my': 3, 'into': 3, 'around': 2, "don't": 1, 'not': 1, "you're": 1, 'under': 1})
print(a + b)

# Counter({'eyes': 7, 'look': 4, 'my': 3, 'into': 3, 'around': 2, 'the': 2, "don't": 1, 'not': 1, "you're": 1, 'under': 1})
print(a - b)

# 11 slice
items = [1, 3, 5, 6, 7, 3, 2]

s = slice(2, 8, 2)
print(items[2:4])
print(items[s])

print(s.start, s.stop, s.step)

h = 'helloworld'
print(s.indices(len(h)))
for i in range(*s.indices(len(h))):
    print(h[i])  # o o

# 10 序列set去重
# hashable


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


d = [2, 1, 3, 3, 4, 5, 4, 3]
print(list(dedupe(d)))

# hash enable like {}


def endedupe(items, key=None):
    seen = set()
    for item in items:
        if key is None:
            val = item
        else:
            val = key(item)
            #val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


d = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 3},
]

# [{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 3, 'x': 2}]
print(list(endedupe(d, key=lambda d: (d['x'], d['y']))))
# [{'y': 2, 'x': 1}, {'y': 3, 'x': 2}]
print(list(endedupe(d, key=lambda d: d['x'])))

# 9 same key or value
a = {
    'a': 12,
    'b': 'bb',
    'c': 34
}

b = {
    'a': 'aa',
    'd': 'bb',
    'c': 34
}

print(a.keys() & b.keys())  # {'a', 'c'} a b 交集 array_intersect()
print(a.keys() - b.keys())  # {'b'} a keys 的差集 array_diff_key(php)
# {('c', 34)} keys(), items(), all support, but not values()
print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'c'}}  # 字典推到 array_filter(php)
print(c)  # {'a': 12, 'b': 'bb'}

# 8 字典的运算，求最大最小 zip()只能使用一次 反转 like array_flip(php)
prices = {
    'a': 12,
    'b': 23,
    'c': 1
}
print(min(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

# 7 序列化字典
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['aaa'] = 3
d['foo'] = 5
print(json.dumps(d))

# 6 一个key对应多个值
a = {
    'a': ['a', 'aa', 'aaa'],  # 保证顺序的时候使用列表，去除重复使用集合
    'b': [1, 2, 3]
}
d = defaultdict(list)
d['a'].append('a')
d['a'].append(123)
d['b'].append('b')
print(d)

s = defaultdict(set)
s['a'].add('a')
s['a'].add(123)
s['b'].add('b')
print(s)

d = defaultdict(list)
d['admin'].append('first')

infos = {
    'admin': ['admin', 'admin@example.com', 123],
    'demo': ['demo', 'demo@example.com', 234]
}

for key, values in infos.items():  # add items() for dict.
    for value in values:
        d[key].append(value)

print(d)

# 5 优先级队列


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))  # 最小的放在第一位
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 弹出第一位，讲剩下最小的放到第一位

    def get(self):
        return self._queue


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


p = PriorityQueue()
p.push(Item('foo'), 1)
p.push(Item('bar'), 5)
p.push(Item('aaa'), 4)
p.push(Item('bbb'), 1)
# [(-5, 1, Item('bar')), (-1, 0, Item('foo')), (-4, 2, Item('aaa')), (-1, 3, Item('bbb'))]
print(p.get())
print(p.pop())  # Item('bar')
print(p.pop())  # Item('aaa')
print(p.pop())  # Item('foo')
print(p.pop())  # Item('bbb')
print(p.get())

# 4 biggest or litterest 5 : import heapq
nums = [1, 2, 4, 5, -5, 9, 23, -45, 67, 300, 4, -4, 0]
print(heapq.nlargest(3, nums))  # [300, 67, 23]
print(heapq.nsmallest(3, nums))  # [-45, -5, -4]
print(min(nums))
print(max(nums))
print(sorted(nums)[:5])  # [-45, -5, -4, 0, 1]
print(sorted(nums)[-5:])  # [5, 9, 23, 67, 300]

people = [
    ('admin', 'admin@examle.com', 20.8),
    ('demo1', 'demo1@examle.com', 45.8),
    ('demo2', 'demo2@examle.com', 25.45),
    ('demo3', 'demo3@examle.com', 34),
    ('demo4', 'demo4@examle.com', 4),
    ('demo5', 'demo5@examle.com', 3453),
]
print(heapq.nlargest(3, people, key=lambda p: p[2]))

# 3 队列lastest 5 lines: from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


if __name__ == '__main__':
    with open(r'./test.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# 2 星号解压
email, user, *phone = ('admin@example.com', 'admin', 1234567, 2345678)
print(email)  # admin@example.com
print(phone)  # [1234567, 2345678]

l = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo:', x, y)


def do_bar(s):
    print('bar', s)


for name, *args in l:
    if(name == 'foo'):
        do_foo(*args)
    if(name == 'bar'):
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
name, *fields, homedir, sh = line.split(':')
print(name)  # nobody
print(fields)  # ['*', '-2', '-2', 'Unprivileged User']

# 1 废弃语法
p = ['a', (4, 5), 'b', 'c']
x, y, z, _ = p
print(y)  # (4, 5)

p = (4, 5)
x, y = p
print(x)  # 4
