def plus_know(value):
    c = 0
    if value < 30:
        cyc = int(value)
    else:
        cyc = 30
    for i in range(1, cyc):
        if value%i == 0 and i <= value/i:
            c += 1
    return c == 1

def add_know(value):
    c = 0
    cyc = int(value/2)
    for i in range(1, cyc):
        j = value - i
        if not plus_know(i*j):
            c += 1
    return c == 1

def plus_know2(value):
    c = 0
    if value < 30:
        cyc = int(value)
    else:
        cyc = 30
    for i in range(1, cyc):
        if value%i == 0 and i<= value/i and (not add_know(i+value/i)):
            c += 1
    return c == 1

for a in range(1, 30):
    for b in range(a, 30):
        x = a + b
        y = a * b
        if (not plus_know(y)) and (not add_know(x)) and plus_know2(y):
            print(a, b)
