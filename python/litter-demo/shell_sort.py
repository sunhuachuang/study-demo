def shellSort(seq):
    length = len(seq)
    inc = 0
    while inc <= length / 3:
        inc = inc * 3 + 1
    print(inc)  # 13
    while inc >= 1:
        for i in range(inc, length):
            tmp = seq[i]
            for j in range(i, 0, -inc):
                if tmp < seq[j - inc]:
                    seq[j] = seq[j - inc]
                else:
                    j += inc
                    break
            seq[j - inc] = tmp

        inc //= 3


seq = [5, 6, 3, 7, 23, 545, 6, 32, 6, 10, 43,
       42, 4323,    4, 3, 423, 43, 6, 65, 97, 76]
shellSort(seq)
print(seq)
