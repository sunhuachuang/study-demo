#! /usr/bin/python3
import sys
import os
import math
import cmath
import numpy as np
import random
import ssl
import calendar
from decimal import Decimal
from decimal import localcontext
from fractions import Fraction
from datetime import timedelta, datetime, date
#from pytz import timezone

#16 结合时区的时间操作 pytz

sys.exit(0)

#15 字符串转化为日期 datetime.strptime  strftime
s = '2016-05-15'
d = datetime.strptime(s, '%Y-%m-%d')
z = datetime.now()
diff = z - d
print(d)
print(z)
print(diff) #1 day, 9:41:16.783317
print(datetime.strftime(z, '%A %B %d, %Y')) #Monday May 16, 2016

def parse_ymd(s): #YYYY-MM-DD 大量使用效率高
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

#14 计算当前月份的日期范围
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

#13 计算最后一个周五的日期 dateutil.relativedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_age = (7 + day_num - day_num_target) % 7
    if days_age == 0:
        days_age = 7
    target_date = start_date - timedelta(days=days_age)
    return target_date
print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))
print(get_previous_byday('Monday', datetime(2016, 5, 20)))

#12 基本的时间与日期的转换 datetime
a = timedelta(days=2, hours=20)
b = timedelta(hours=8)
c = a + b
print(c.days) #3
print(c) #3 days, 4:00:00
print(c.seconds) #14400

d = datetime(2016, 5, 12)
print(d) #2016-05-12 00:00:00
print(d + c) #2016-05-15 04:00:00

#11 随机选择 random ssl.RAND_bytes()密码中的随机生产方法
values = [23, 45, '345', 'saf']
print(random.choice(values)) # one
print(random.sample(values, 2)) #[23, 'saf']随机个数
print(values)
random.shuffle(values) #随机打乱 like php shuffle函数
print(values)

print(random.randint(2, 4)) #[2, 4]之间
print(random.random()) # 0~1
print(ssl.RAND_bytes(2))

#10 矩阵与线性代数 np.matrix
m = np.matrix([[1, 2, 3], [-3, -5, -7], [9, 8, 7]])
print(m)

#9 大型数组计算 numpy
x = [1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
print(x * 2) #[1, 2, 3, 4, 1, 2, 3, 4]
print(x + y) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2) #[2 4 6 8]
print(ay + ax) #位数需一致 [ 6  8 10 12]

def f(x):
    return x+1
print(f(ax)) #[2 3 4 5]
print(np.sqrt(ax)) #平方根[ 1 1.41421356  1.73205081  2]
grid = np.zeros(shape=(10, 10), dtype=float)
print(grid)
print(f(grid))

#8 分数运算 fractions
a = Fraction(1, 3)
b = Fraction(3, 7)
print(a, b) #1/3 3/7
print(a * b) #1/7
print(a.numerator) #1
print(a.denominator) #3
print(float(a)) #0.3333333333333333
print(Fraction(35, 84).limit_denominator(8)) #3/7
print(float(35/84))
print(float(3/7))
f = 1.5
print(Fraction(*f.as_integer_ratio())) #3/2

#7 无穷大与NaN(not a number)
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c) #inf -inf nan
print(math.isinf(b)) #True float has isinf isnan
print(math.isnan(c)) #True

d = float('nan')
print(c == d) #False

#6 复数的运算 complex j cmath
a = complex(2, 4)
b = 4j
print(a, ' ', b) #(2+4j)   4j
print(complex(2)) #(2+0j)
print(complex(0, 4)) #4j
print(a.real) #2.0
print(a.imag) #4.0
print(a.conjugate)
print(b.real, b.imag, b.conjugate) #0.0 4.0 <built-in method conjugate of complex object at 0x7f361fd902f0>

print(math.sin(2)) #0.9092974268256817
print(cmath.sin(2j)) #3.626860407847019j

#5 字节到大整数 int.from_bytes int.to_bytes
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data)) #16
print(int.from_bytes(data, 'little')) #69120565665751139577663547927094891008
print(int.from_bytes(data, 'big')) #94522842520747284487117727783387188

num = 354245345345234523452345
print(num.to_bytes(16, 'big')) #b'\x00\x00\x00\x00\x00\x00K\x03\xad\xbc\x0f6H\x98\xf3\xb9' big and little 高低位顺序
print(num.to_bytes(16, 'little')) #b'\xb9\xf3\x98H6\x0f\xbc\xad\x03K\x00\x00\x00\x00\x00\x00'
print(int.from_bytes(b'\x00\x00\x00\x00\x00\x00K\x03\xad\xbc\x0f6H\x98\xf3\xb9', 'big')) #354245345345234523452345

x = 523 ** 23 + 523 ** 23
print(len(str(x))) #63
#print(x.to_bytes(16, 'big')) #int too big to convert
print(x.bit_length()) #208
#print(x.to_bytes(208, 'big')) # b'\x00...\x00\x00\xd0\xb5R\xd9\...'
nbytes, rem = divmod(x.bit_length(), 8)

print(nbytes, '--', rem) #26 -- 1
if rem:
    nbytes += 1

print(x.to_bytes(nbytes, 'big')) #b'\xd0\xb5R\xd9\xc8\xa2\x98\xd1\x91\xec\xee\x18\xcf\xb9\xf3\x16c\xc7\xac\x96Ti\x82\xf1X\x03'
#print(x.to_bytes(26, 'big'))

#4 2,8,16进制
num = 12345
print(bin(num)) #0b11000000111001 二进制
print(oct(num)) #0o30071
print(hex(num)) #0x3039

print(format(num, 'b')) #11000000111001
print(format(num, 'o')) #30071
print(format(num, 'x')) #3039

num2 = -1234
print(format(num2, 'b')) #-10011010010
print(format(2**32+num2, 'b')) #11111111111111111111101100101110
print(int('11111111111111111111101100101110', 2)) #4294966062
print(int('-10011010010', 2)) #-1234
print(int('3039', 16)) #12345 必须是字符串形式
print(int('755', 8)) #493
os.chmod('test.txt', 0o755) #必须是0o八进制

#3 数字的格式化输出

num = 123456.89012345
print(format(num, '<15.3f')) #123456.890     #
print(format(num, ','))      #123,456.89012345
print(format(num, '0,.4f'))  #123,456.8901
print(format(num, 'e'))      #1.234569e+05
print(format(num, '0,.4e'))  #1.2346e+05

#2 精确的浮点数运算
a = 4.2
b = 2.1
c = a+b
print(c) #6.300000000000001

ad = Decimal('4.2')
bd = Decimal('2.1')
cd = ad + bd
print(cd) #6.3

adt = Decimal(4.2)
bdt = Decimal(2.1)
cdt = adt + bdt
print(cdt) #6.300000000000000266453525910

adn = Decimal(a)
bdn = Decimal(b)
cdn = adn + bdn
print(cdn) #6.300000000000000266453525910


al = Decimal('4.2')
bl = Decimal('3.1')
print(al/bl) #1.354838709677419354838709677
with localcontext() as ctx:
    ctx.prec = 5
    print(al/bl) #1.3548
with localcontext() as ctx:
    ctx.prec = 50
    print(al/bl) #1.3548387096774193548387096774193548387096774193548

nums = [1.28e+18, 1, -1.28e+18]
print(sum(nums)) #0.0
print(math.fsum(nums)) #1.0

#1 四舍五入 round() .5是取最近偶数
print(round(1.234, 1)) #1.2
print(round(1.264, 1)) #1.3
print(round(1.254, 1)) #1.3
print(round(1.25, 1))  #1.2
print(round(1.35, 1))  #1.4
print(round(1.35, 3))  #1.35
print(round(1234.1234, 0))  #1234.0
print(round(1234.1234, -1)) #1230.0
print(round(1999.1234, -2)) #2000.0

n = 1.2345
print(format(n, '0.2f')) #1.23
print(format(n, '0.3f')) #1.234
print('number is {:0.3f}'.format(n)) #格式化输出

a = 1.2
b = 2.3
b2 = 2.31
c = a+b
c2 = a+b2
print(c) #3.5
print(c2) #3.51
