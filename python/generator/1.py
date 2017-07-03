def test(n):
    for i in range(10):
        yield i


for i in test(1):
    print(i)
