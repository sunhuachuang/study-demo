def sqrt(x):
    return sqrt_iter(1.0, x)


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        print('1')
        return sqrt_iter(improve(guess, x), x)


def good_enough(guess, x):
    return self_abs(guess * guess - x) < 0.001


def improve(guess, x):
    return (guess + (x / guess)) / 2


def self_abs(x):
    if x < 0:
        return -x
    else:
        return x


# print(sqrt(2)) #1.4142156862745097
# print(sqrt(23452345234523452345))
print(sqrt(0.0000000000000000000000032))
