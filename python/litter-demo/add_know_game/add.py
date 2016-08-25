def plus_know(value): #函数 plus_konw(参数)
    c = 0 #变量
    if value < 30: #条件判断, 条件表达式不需要括号
        cyc = int(value) #ｉｎｔ类型强转化
    else:
        cyc = 30
    for i in range(1, cyc): # i 从１取到ｃｙｃ　相当于ｆｏｒ(i=1; i=<cyc; i++)循环
        if value%i == 0 and value/i != i: #ｖａlue取模，　and not or都是逻辑判断语句 相当于 && ! ||
            c += 1 # c = c + 1缩写
    return c > 1 # 排除1和本身

def add_know(value):
    c = 0
    cyc = int(value/2)
    for i in range(1, cyc):
        j = value - i
        if i != j and plus_know(i*j):
            c += 1
    return c > 1

def plus_know2(value):
    c = 0
    if value < 30:
        cyc = int(value)
    else:
        cyc = 30
    for i in range(1, cyc):
        if value%i == 0 and add_know(i+value/i):
            c += 1
    return c == 1

for a in range(1, 30):
    for b in range(a+1, 30):
        x = a + b
        y = a * b
        if plus_know(y) and add_know(x) and plus_know2(y):
            print(a, b)
