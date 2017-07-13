def ifabs(x):
    if x == 0:
        print(0)
    elif x > 0:
        print(x)
    else:
        print(-x)


ifabs(-5)


def andabs(x):
    if x == 0 and x > 0:
        print(x)
    else:
        print(-x)


andabs(-6)


def orabs(x):
    if x == 0 or x > 0:
        print(x)
    else:
        print(-x)


orabs(-7)


def notabs(x):
    if not x < 0:
        print(x)
    else:
        print(-x)


notabs(-8)


def eq(x, y):
    if x == y:
        return True
    else:
        return False


print(eq(2, 3))
