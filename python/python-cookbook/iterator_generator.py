#! /usr/bin/python3
import sys
import itertools
import heapq
from collections import deque
from collections import Iterable

sys.exit(0)

# 16 迭代器替代while无线循环
with open('./test.txt') as f:
    for chunk in iter(lambda: f.read(10), ''):
        print(chunk)

# 15 序列合并后迭代 heapq.merge
a = [1, 2, 7, 3]
b = [45, 46, 2, 99]
for x in heapq.merge(sorted(a), sorted(b)):
    print(x)  # 1 2 7 3 45 46 2 99 必须是已经排序好的序列

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# 14 展开嵌套的序列 yield from 类似递归写法


def flatten(items, ignore_type=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
            yield from flatten(x)
        else:
            yield x


l = [1, 2, [3, [4, 5]]]
for x in flatten(l):
    print(x)  # 1 2 3 4 5
ls = ['abc', 'bcd', ['ert', 'hello']]
for x in flatten(ls):
    print(x)

# 13 创建数据处理管道

# 12 不同集合上元素的迭代 itertools.chain() 比序列合并再迭代效率高
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd', 'e']
for x in itertools.chain(l1, l2):
    print(x)  # 1 2 3 4 a b c d e

# 11 同时迭代多个序列 zip() 返回一个迭代器
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd', 'e']
for x in zip(l1, l2):
    print(x)  # (1, 'a') (2, 'b') (3, 'c') (4, 'd')
for x in itertools.zip_longest(l1, l2):
    print(x)  # (1, 'a') (2, 'b') (3, 'c') (4, 'd') (None, 'e')
for x in itertools.zip_longest(l1, l2, fillvalue=0):
    print(x)  # (1, 'a') (2, 'b') (3, 'c') (4, 'd') (0, 'e')

# 10 序列上的索引值迭代 enumerate
l = ['a', 'b', 'c', 'd']
for num, x in enumerate(l):
    print(num, ': ', x)  # 0 :  a  1 :  b  2 :  c  3 :  d
for num, x in enumerate(l, 1):  # 从1开始
    print(num, ':', x)  # 1 : a 2 : b 3 : c 4 : d

# 9 排列组合的迭代 itertools.permutations(有序所有组合) itertools.combinations(无序所有组合) combinations_with_replacement(可重复元素)
l = ['a', 'b', 'c', 'd']
for x in itertools.permutations(l, 2):
    print(x)
print('----combinations----')
for x in itertools.combinations(l, 4):
    print(x)  # ('a', 'b', 'c', 'd')
for x in itertools.combinations(l, 2):
    print(x)
print('----combinations_with_replacement----')
for x in itertools.combinations_with_replacement(l, 4):
    print(x)

# 8 跳过可迭代对象的开始部分 dropwhile
with open('./test.txt') as f:
    for line in itertools.dropwhile(lambda line: line.startswith('p'), f):
        print(line, end='')

with open('./test.txt') as f:
    lines = (line for line in f if not line.startswith('p'))
    for line in lines:
        print(line, end='')

# 7 迭代器切片 itertools.isLice


def count(n):
    while True:
        yield n
        n += 1


c = count(1)

for x in itertools.islice(c, 10, 20):  # [10:20]
    print(x)  # 11~20

for x in itertools.islice(c, 10, 20):  # [10:20]
    print(x)  # 31~40不可逆

# 6 带有外部状态的生成器函数


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('./test.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}行:{}'.format(lineno, hline), end='')

# 5 反向迭代 reversed() 不是列表的话预先转化为list
xs = [1, 2, 3, 4]
for x in reversed(xs):
    print(x)  # 4 3 2 1


class Countdone:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for x in Countdone(4):
    print(x)  # 4 3 2 1
for xr in reversed(Countdone(4)):
    print(xr)  # 1 2 3 4

# 4 实现迭代器协议 迭代内部子元素


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, child):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)  # Node(0) Node(1) Node(4) Node(2) Node(5)

# 3 使用生成器创建新的迭代模式


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for x in frange(1, 20, 2):
    print(x)
# [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
print(list(frange(0, 1, 0.125)))
print(sum(frange(1, 10, 2)))  # 25


def countdone(n):
    while n > 0:
        yield n
        n -= 1
    print('done')


c = countdone(3)
print(next(c))  # 3
print(next(c))  # 2
print(next(c))  # 1
print(next(c))  # done StopIteration

# 2 代理迭代


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, child):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)  # Node(1) Node(2)

# 1 手动遍历迭代器


def manual_iter():
    with open('./test.txt') as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            pass
# manual_iter()


def manual_iter_none():
    with open('./test.txt') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line)


manual_iter_none()
