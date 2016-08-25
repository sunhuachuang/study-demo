#! /usr/bin/python3
import sys
import re #正则
import os
import html
#from html.parser import HTMLParser.unescape
#from xml.sax.saxutils import unescape
import textwrap #格式化字符串宽
from fnmatch import fnmatch, fnmatchcase #shell 中的通配符
import unicodedata #unicode编码
from collections import namedtuple

sys.exit(0)

#20 字节字符串上的字符串操作
s = b'hello:'
print(s[:2]) #b'he'
print(s.startswith(b'he')) #True

sarray = bytearray(b'hello world')
print(sarray)
print(sarray.endswith(b'world')) #True

data = b'aa:bb:cc'
print(re.split(b'[:]', data)) #[b'aa', b'bb', b'cc']

s = 'hello'
bs = b'hello'
print(s[0])  #h
print(bs[0]) #104
print(s[1])  #e
print(bs[1]) #101

print(bs.decode('ascii')) #hello

#19 递归下降分析器

#18 字符串令牌解析
text  = 'foo = 10 + 20 * 30'
NAME  = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM   = r'(?P<NUM>\d+)'
PLUS  = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

tokens = (tok for tok in generate_tokens(master_pat, text)
            if tok.type != 'WS')
for tok in tokens:
    print(tok)

#17 在字符串中处理 html 与 xml html/xml模块
s = 'p in html is "<p>text</p>"'
print(s)
print(html.escape(s)) #p in html is &quot;&lt;p&gt;text&lt;/p&gt;&quot;
print(html.escape(s, quote=False)) #p in html is "&lt;p&gt;text&lt;/p&gt;"

#16 以指定列宽格式化字符串 textwrap
s = 'asdfasdfadsfadsfadsfaa \
adsfasdfasdfasdfadsfqqqqqqqqqqqqqqqqq \
qqqqqqqqqq'
print(s)

print(textwrap.fill(s, 10))
print(textwrap.fill(s, 20, initial_indent='  ')) #首行缩进2
print(textwrap.fill(s, 20, subsequent_indent='  ')) #除了首行外缩进2
print(os.get_terminal_size().columns) #终端宽

#15 字符串中加入变量 format; fomat_map(vars()) 变量域 变量在前
name = 'sun'
age  = 24
print('my name is {name}, age is {age}') #my name is {name}, age is {age}
print('my name is {name}, age is {age}'.format(name=name, age=age)) #my name is sun, age is 24
print('my name is {name}, age is {age}'.format_map(vars())) #my name is sun, age is 24

class Info:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

a = Info('huachuang', 24)
print('my name is {name}, age is {age}'.format_map(vars(a))) #my name is huachuang, age is 24

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

print('my home is {place}'.format_map(safesub(vars()))) #my home is {place}
place = 'earth'
print('my home is {place}'.format_map(safesub(vars()))) #my home is earth

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(sub('my name is {name}, age is {age}')) #my name is sun, age is 24

#14 合并拼接字符串 string.join(); +
lists = ['we', 'are', 'friends']
print(' '.join(lists)) #we are friends
print(','.join(lists)) #we,are,friends

s1 = 'hello'
s2 = 'world'
print(s1 + ' ' + s2) #hello world
print('{} {}'.format(s1, s2)) #hello world
a = 'hello ' 'world ' '!'
print(a) #hello world !

s = '';
for l in lists:
    s+=l
print(s) #低效率
print(' '.join(str(d) for d in lists)) #生成器高效

print('a' + ':' + 'b' + ':' + 'c') #低效
print(':'.join(['a', 'b', 'c'])) #低效
#print('a', 'b', 'c', sep=':') #高效

f = open(r'./test.txt')

#f.write('s1' + 's2') 短字符串效率高
#f.write(s1) f.write(s2) 超长字符串效率高
#大量片段用yield
def simple():
    yield 'aaa'
    yield 'bbb'
    yield 'ccc'
print(' '.join(simple()))

def append(source, maxlen):
    parts = []
    length = 0
    for part in source:
        parts.append(part)
        length += len(part)
        if length > maxlen:
            yield ' '.join(parts)
            parts = []
            length = 0
        yield ' '.join(parts)
with open('./test.txt', 'a') as f:
    for part in append(simple(), 10000):
        f.write(part + '\n')
#aaa
#aaa bbb
#aaa bbb ccc

#13 对齐字符串 string.ljust(), rjust(), center();  format()
s = 'hello'
print(s.ljust(10))  #hello     #
print(s.rjust(10))  #     hello#
print(s.center(10)) #  hello   #

print(s.ljust(10, '-'))  #hello-----
print(s.rjust(10, '='))  #=====hello
print(s.center(10, '*')) #**hello***

print(format(s, '<10')) #hello     #
print(format(s, '>10')) #     hello#
print(format(s, '^10')) #  hello   #
print(format(s, '>4'))  #不变
print(format(s, '-<10')) #hello-----
print(format(s, '=>10')) #=====hello
print(format(s, '*^10')) #**hello***

print('{:>10s} {:>10s}'.format('hello', 'world')) #     hello      world# s 代表是格式化字符串

print(format(1.2345678, '>15')) #      1.2345678#
print(format(1.2375678, '^8.2f')) #  1.24  #

#12 清理字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None, #delete
}
st = s.translate(remap) #过滤表
print(s) #pýtĥöñis	awesome
print(st) #pýtĥöñ is awesome

s_b = unicodedata.normalize('NFD', st)
s_b_e = s_b.encode('ascii', 'ignore').decode('ascii')
print(s_b_e) #python is awesome

#11 删除字符串的首尾字符
s = ' hello world hello people! '
ss = s.strip()
s_left = s.lstrip()
s_right = s.rstrip()
print(s)
print(ss) #默认删除两端空白
print(s_left)
print(s_right)

s = '--hello----world===, hello-=-=people!=='
s_all = s.strip('-=')
s_left = s.lstrip('-=')
s_right = s.rstrip('-=')
s_replace = s.replace('-', '').replace('=', '')
print(s_all) #hello----world===, hello-=-=people!
print(s_left) #hello----world===, hello-=-=people!==
print(s_right) #--hello----world===, hello-=-=people!
print(s_replace) #helloworld, hellopeople!

with open('./test.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

#10 在正则中使用unicode

#9 unicode 标准化 unicodedata.normalize
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2) #False
u1 = unicodedata.normalize('NFC', s1) #单一编码 NFC NFKC
u2 = unicodedata.normalize('NFC', s2)
print(ascii(u1)) #'Spicy Jalape\xf1o'
print(ascii(u2)) #'Spicy Jalape\xf1o'
print(u1 == u2) #true

u3 = unicodedata.normalize('NFD', s1) #多种编码 NFD NFKD
u4 = unicodedata.normalize('NFD', s2)
print(ascii(u3)) #'Spicy Jalapen\u0303o'
print(ascii(u4)) #'Spicy Jalapen\u0303o'
print(u3 == u4) #true

#8 多行匹配 (?:.|\n)指定了一个非捕获组 re.DOTALL 可以让 . 匹配任意字符
s1 = '/* this is one comment */'
s2 = '''
/*
 this is comment
*/
'''
comment = re.compile(r'/\*(.*?)\*/')

print(comment.findall(s1))
print(comment.findall(s2)) #[]

comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment2.findall(s1))
print(comment2.findall(s2)) #['\n this is comment\n']

#7 最短匹配， 克服“ 的贪婪模式
s = 'say "hello." say "bye."'
ss = re.findall(r'\"(.*)\"', s)
print(ss) #['hello." say "bye.']

ss = re.findall(r'\"(.*?)\"', s)
print(ss) #['hello.', 'bye.']

#6 忽略大小写的匹配 flags=re.IGNORECASE
s = 'aaa, bbb, ccc, BBB, DDD'
s = re.sub('bbb', 'eee', s, flags=re.IGNORECASE)
print(s) #aaa, eee, ccc, eee, DDD

s = 'aaa, bbb, ccc, ddd'
s = s.replace('aaa', 'AAA')
print(s)

time = 'from 24/5/2016 to 1/10/2017'
#5 time = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', time) #3, 2, 1代表匹配的捕获序号
datecop = re.compile(r'(\d+)/(\d+)/(\d+)'); #编译再执行
time = datecop.sub(r'\3-\2-\1', time)
print(time)

#4 字符串的匹配 str.find re.match
s = 'aaa bbb cc dd'
print(s.find('cc')) #8
s = '98/34/65'
if re.match(r'\d+/\d+/\d+', s):
    print('yes')
else:
    print('no')

datecop = re.compile(r'\d+/\d+/\d+')
if datecop.match(s):
    print('yes')
else:
    print('no')
s = 'today is 34/34/65, tomermer is 7667/454/45'
print(datecop.findall(s)) #['34/34/65', '7667/454/45']

datecops = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datecops.match('34/3424/234')
print(m.group()) #34/3424/234
print(m.group(1)) #34
print(m.groups()) #('34', '3424', '234')

ms = datecops.findall(s)
print(ms)#[('34', '34', '65'), ('7667', '454', '45')]

for year, month, day in ms:
    print(year, ' ' , month, ' ', day)
for m in datecops.finditer(s):
    print(m.groups())

#3 shell 中的通配符 * ? fnmatch fnmatchcase
s = ['text.txt', 'text1.txt', 'text2.txt', '1.csv', '2.csv']

print(fnmatch('text.txt', '*.txt'))
print(fnmatchcase('text.txt', '?ext.TXT'))

#2 字符串开头或者结尾 startswith endswith
s = 'test.txt'
if s.startswith('a'):
    print('start with a')
if s.endswith('.txt'):
    print('end with .txt')
if s.endswith(('.txt', '.py')):
    print('end in txt or py')


#1 正则表达式分割字符串 re split
s = 'sdf; sdg;fs,sf. s fs, s'
s_re = re.split(r'[;,.\s]\s*', s)
print(s_re)

s_str = s.split(',')
print(s_str)
