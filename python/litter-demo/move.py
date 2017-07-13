# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个盘子从x移动到y上
        move(1, a, b, c)  # 将最底下的最后一个盘子从x移动到z上
        move(n - 1, b, a, c)  # 将y上的n-1个盘子移动到z上


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
