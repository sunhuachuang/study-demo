# 题目：已知两个1~30之间的数字，甲知道两数之和，乙知道两数之积。
# 甲问乙：“你知道是哪两个数吗？“乙说：“不知道“；
# 乙问甲：“你知道是哪两个数吗？“甲说：“也不知道“；
# 于是，乙说：“那我知道了“；
# 随后甲也说：“那我也知道了“；
# 这两个数是什么？

import math
g_same = True

#已知两个1~30之间的数字，甲知道两数之和，乙知道两数之积。
def cond0(x, y):
    return (x <= y if g_same else x < y) and x >= 1 and x <= 30 and y >= 1 and y <= 30

#甲问乙：“你知道是哪两个数吗？”乙说：“不知道”；
def cond1(x, y):
    s = x * y
    k = 0
    for i in range(1, math.floor(math.sqrt(s))+1):
        if s%i == 0 and cond0(i, s/i):
            k += 1
    return k >= 2

#乙问甲：“你知道是哪两个数吗？”甲说：“也不知道”；
def cond2(x, y):
    s = x + y
    k = 0
    for i in range(1, math.floor(s/2)+1):
        if cond0(i, s-i) and cond1(i, s-i):
            k += 1
    return k >= 2

#于是，乙说：“那我知道了； (=> 乙根据 条件1，条件2 得出唯一解)
def cond3(x, y):
    s = x * y
    k = 0
    for i in range(1, math.floor(math.sqrt(s))+1):
        if s%i == 0 and cond0(i, s/i) and cond1(i, s/i) and cond2(i, s/i):
            k += 1
    return k == 1

#随后甲也说："那我也知道了"； (=>甲根据 条件1，条件2, 条件3 得出唯一解)
def cond4(x, y):
    s = x + y
    k = 0
    for i in range(1, math.floor(s/2)+1):
        if cond0(i, s-i) and cond1(i, s-i) and cond2(i, s-i) and cond3(i, s-i):
            k += 1
    return k == 1

#允许重复
g_same = True
print('允许重复：')
for i in range(1, 31):
    for j in range(1, 31):
        if cond0(i, j) and cond1(i, j) and cond3(i, j) and cond4(i, j):
            print(i, j)

g_same = False
print('不允许重复：')
for i in range(1, 31):
    for j in range(1, 31):
        if cond0(i, j) and cond1(i, j) and cond3(i, j) and cond4(i, j):
            print(i, j)
