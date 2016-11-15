#埃拉托斯特尼筛法
import math;

n = 100000;

a = [True for i in range(0, n)]

for x in range(2, int(math.sqrt(n))+1):
    for y in range(2, int(n/x)+1):
        if x*y-1 <= n:
            a[y*x-1] = False;

last = 2;
for key, value in enumerate(a):
    if value:
        last = key + 1;

print(last); #0.28s user 0.01s system 98% cpu 0.292 total
