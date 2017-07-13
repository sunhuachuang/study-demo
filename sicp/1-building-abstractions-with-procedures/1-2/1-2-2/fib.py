def fib_recursive(n):
    if n == 1 or n == 0:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


print(fib_recursive(6))


def fib_iteration(n):
    def fib_iter(a, b, count):
        if count == 0:
            return b
        return fib_iter(a + b, a, count - 1)
    return fib_iter(1, 0, n)


print(fib_iteration(6))
