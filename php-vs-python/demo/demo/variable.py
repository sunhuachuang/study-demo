a = 'aaa'

a = b = c = 1

aa, bb, cc = 'a', 'b', 'c'

# aa, bb, cc = 'a', 'b', 'c', 'd' #ValueError: too many values to unpack (expected 3)

# aa, bb, cc, dd = 'a', 'b', 'c'  #ValueError: not enough values to unpack (expected 4, got 3)

aa, bb, cc, _ = 'a', 'b', 'c', 'd'

aa, bb, cc, *dd = 'a', 'b', 'c', 'd', 1, 2

aa, bb, cc, *_ = 'a', 'b', 'c', 'd', 1, 2


print(dd)  # ['d', 1, 2]
