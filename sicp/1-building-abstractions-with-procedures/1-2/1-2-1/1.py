def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) #120

def factorial2(n):
    return fact_iter(1, 1, n)

def fact_iter(product, counter, maxn):
    if counter > maxn:
        return product
    else:
        return fact_iter(product*counter, counter+1, maxn)

print(factorial2(6)) #720
