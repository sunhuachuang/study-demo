#! /usr/bin/python3
import sys
import os
import io
import gzip
import bz2
import time
import glob
import urllib.request
from functools import partial
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
import pickle

sys.exit(0)

#21 序列化python对象 pickle
class Person:
    def __init__(self, name):
        self.name = name

data = Person('Tom');
#f = open('test.txt', 'ab')
#pickle.dump(data, f)
#f.close()

s = pickle.dumps(data)
print(s) #b'\x80\x03c__main__\nPerson\nq\x00)\x81q\x01}q\x02X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Tomq\x04sb.'
print(pickle.loads(s)) #<__main__.Person object at 0x7f59cace0a58>

#20 与串行端口的数据通信 pySerial

#19 创建临时文件与文件夹 tempfile
with TemporaryFile('w+t') as f:
    f.write('hello world\n')
    f.write('test\n')
    f.seek(0)
    print(f.read())

with NamedTemporaryFile('w+t', delete=False) as f:
    print(f.name) # /tmp/tmpjl16pgc8

with TemporaryDirectory() as dirname:
    print(dirname) #/tmp/tmphsfkxnck

#18 将文件描述符包装成文件对象 os.open()
fd = os.open('test.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'at', closefd=False)
f.write('hello world\n')
f.close()

#17 讲字节写入文本文件 sys.stdout.buffer.write
print(sys.stdout.write('hello')) #hello5
#print(sys.stdout.write(b'hello')) TypeError: write() argument must be str, not bytes
print(sys.stdout.buffer.write(b'hello')) #hello5

#16 增加或者改变已打开文件的编码 io.TextIOWrapper()
f = open('test.txt', 'at')
print(f) #<_io.TextIOWrapper name='test.txt' mode='at' encoding='UTF-8'>

print(sys.stdout.encoding)
u = urllib.request.urlopen('http://www.baidu.com');
f = io.TextIOWrapper(u, encoding='utf-8')
#print(f.read())
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding) #latin-1


#15 打印不合法的文件名
def bad_filename(filename):
    return repr(filename)[1:-1]

def bad_good_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

filename = os.path.listdir('.')

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_good_filename(filename))

#14 忽略文件名编码 os.listdir(b'.')
print(sys.getfilesystemencoding()) #utf-8
print(os.listdir(b'.'))

#13 获取文件夹的文件列表 os.listdir glob.glob() os.stat()
print(os.listdir('../../../php')) #['test.php', 'phpMyAdmin-4.6.0-all-languages', 'symfony3', 'symfony2', 'laravel', 'learn']
phps = [name for name in os.listdir('../../../php') if name.endswith('.php')]
print(phps) #['test.php']

files = [name for name in os.listdir('../../../php') if os.path.isfile(os.path.join('../../../php', name))]
print(files) #['test.php']

print(glob.glob('*.txt')) #['test2.txt', 'test.txt']

print(os.stat('test.txt')) #os.stat_result(st_mode=33261, st_ino=1973591, st_dev=2057, st_nlink=1, st_uid=1000, st_gid=1000, st_size=270, st_atime=1463545076, st_mtime=1462503183, st_ctime=1463032395) 对象
print(os.stat('test.txt').st_ctime) #1463032395.0300977

#12 测试文件是否存在 os.path.exists()
print(os.path.exists('test.py')) # False
print(os.path.exists('test.txt')) # True
print(os.path.isfile('test.txt')) # True
print(os.path.isdir('../../../php')) # True
print(os.path.islink('/usr/bin/python3')) # True
print(os.path.realpath('/usr/bin/python3')) # /usr/bin/python3.5
print(os.path.getsize('test.txt')) #270
print(time.ctime(os.path.getmtime('test.txt'))) #1462503183.2089999->Fri May  6 10:53:03 2016

#11 文件路径名的操作 os.path
path = '/home/sun/test.py'
print(os.path.basename(path)) #test.py
print(os.path.dirname(path)) #/home/sun
#print(dir(str))
print(os.path.join('tmp', 'python', os.path.basename(path))) #tmp/python/test.py

path2 = '~/workspace'
print(os.path.expanduser(path2)) #/home/sun/workspace
print(os.path.splitext('/home/sun/tmp/test.py.txt')) #('/home/sun/tmp/test.py', '.txt')
print(os.path.abspath('test.py')) #/home/sun/workspace/python/study/python-study/test.py

#10 内存映射的二进制文件 mmap

#9 读取二进制文件到可变缓冲区域 readinto
def ask_ok(prompt, retries=4, complaint='\n-> Say Yes, please!\n'):
    while True:
        ok = input(prompt)
        if ok.lower() in ('y', 'ye', 'yes'):
            print('\n-> Good Boy!\n')
            return True
        if ok.lower() in ('n', 'no'):
            print('\n-> No ?? you are really a dog!\n')
        else:
            print(complaint)
ask_ok('you are a dog ? ')

#8 固定大小记录的文件迭代 iter functools.partial() 主要针对二进制文件
RECORD_SIZE = 32
with open('./test.txt') as f:
    records = iter(partial(f.read, RECORD_SIZE), '')
    for r in records:
        print(r)

#7 读写压缩文件 compresslevel(9-1)(high-low)
with gzip.open('./somefile.gz' 'wt') as f:
    f.write('hello')

with gzip.open('./somefile.gz' 'rt') as f:
    text = f.read()

#6 字符串的io操作 io.StringIO() io.BytesIO()
s = io.StringIO();
s.write('Hello, world!\n')
#print('this is next line.', file=s)
#print(s.getvalue())
s = io.StringIO('abcdefg');
print(s.read(2)) #ab
print(s.read(2)) #cd
print(s.getvalue()) #abcdefg

#5 文件不存在才可以创建写入 xt xb
if not os.path.exists('test.txt'):
    with open('./test.txt', 'wt') as f:
        f.write('aaa') #File exists: './test.txt'
else:
    print('file has exists')

with open('./test.txt', 'xt') as f:
    f.write('aaa') #File exists: './test.txt'


#4 读写字节数据 open() rb wb ab
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

#3 使用其他分隔符和行终止符 print() sep, end
print('hello', 2016, sep='-', end='!!!\n') #hello-2016!!!

#2 打印输出到文件 print(string, file=f)
with open('./test2.txt', 'wt') as f:
    print('hello, world', file=f)

#1 读写文本数据 open() rt读, wt写, at追加 with会自动关闭文件
with open('./test.txt', 'rt', encoding='utf-8', newline='', errors='ignore') as f:
    #f.read() f.write print(line, file=f)
    for line in f:
        print(line)

#personal test
class Test:
    def __init__(self, name):
        self.name = name

test1 = Test('sun')
print(test1.name)

def check(test):
    test.name = 'sss'

check(test1)
print(test1.name)
