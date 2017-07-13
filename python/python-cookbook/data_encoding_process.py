#! /usr/bin/python3
import sys
import csv
import json
from collections import namedtuple
from collections import Counter
from urllib.request import urlopen
from pprint import pprint
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
import sqlite3
import binascii
import base64
from struct import Struct
import itertools

# 13 数据的累加与统计 pandas
sys.exit(0)

# 12 读取嵌套可变长二进制数据
polys = [
    [(1, 2), (2, 3), (3, 4)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]

a = 'abc'
b = 'wer'
print(list(itertools.chain(a, b)))  # ['a', 'b', 'c', 'w', 'e', 'r']

print(list(itertools.chain(*polys)))
#[(1, 2), (2, 3), (3, 4), (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0), (3.4, 6.3), (1.2, 0.5), (4.6, 9.2)]


def write_polys(filename, polys):
    flattened = list(itertools.chain(*polys))
    x_min = min(x for x, y in flattened)
    x_max = max(x for x, y in flattened)
    y_min = min(y for x, y in flattened)
    y_max = max(y for x, y in flattened)


# 11 读写二进制数组数据 struct
def write_records(records, formats, f):
    records_struct = Struct(formats)
    for r in records:
        f.write(records_struct.pack(*r))


records = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
with open('tmp/data.d', 'wb') as f:
    write_records(records, '<idd', f)


def read_records(f, formats):
    records_struct = Struct(formats)
    chunks = iter(lambda: f.read(records_struct.size), b'')
    return (records_struct.unpack(chunk) for chunk in chunks)


with open('tmp/data.d', 'rb') as f:
    for r in read_records(f, '<idd'):
        print(r)  # (1, 2.0, 3.0) (2, 3.0, 4.0) (3, 4.0, 5.0)


def unpack_records(formats, data):
    records_struct = Struct(formats)
    return (records_struct.unpack_from(data, offest) for offest in range(0, len(data), records_struct.size))


with open('tmp/data.d', 'rb') as f:
    data = f.read()
    for r in unpack_records('<idd', data):
        print(r)  # (1, 2.0, 3.0) (2, 3.0, 4.0) (3, 4.0, 5.0)

# 10 编码解码ｂａｓｅ６４数据
s = b'hello'
h = base64.b64encode(s)
print(h)  # b'aGVsbG8='
ss = base64.b64decode(h)
print(ss)
print(h.decode('ascii'))  # aGVsbG8=

# 9 编码和解码十六进制数 binascii
s = b'hello'
h = binascii.b2a_hex(s)
print(h)  # b'68656c6c6f'
ss = binascii.a2b_hex(h)  # 可识别大小写
print(ss)  # b'hello'
print(base64.b16encode(s))  # b'68656C6C6F'
print(base64.b16decode(base64.b16encode(s)))  # b'hello'
# print(base64.b16decode(h)) Error 只识别大写

# 8 与关系型数据库的交互 orm SQLAlchemy
db = sqlite3.connect('database.db')
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()
c.executemany('insert into portfolio values (?, ?, ?)', stocks)
db.commit()
for row in db.execute('select * from portfolio'):
    print(row)

# 7 利用命名空间解析ｘｍｌ　lxml
for event, element in iterparse('tmp/test2.xml', ('end', 'start-ns', 'end-ns')):
    print(event, element)  # start-ns ('', 'http://www.w3.org/1999/xhtml')...

# 6 解析与修改ｘｍｌ
doc = parse('tmp/pred.xml')
root = doc.getroot()
print(root)  # <Element 'stop' at 0x7f37d336b728>
root.remove(root.find('sri'))
print(root.getchildren().index(root.find('nm')))  # 1
root.find('nm').text = '100'

name = Element('name')
name.text = 'sun'
root.append(name)

age = Element('age')
age.text = '24'

root.insert(2, age)

doc.write('tmp/newPred.xml', xml_declaration=True)

# 5 将字典转化为ｘｍｌ xml.etree.Elementtree.Element


def dict_to_xml(tag, data):
    elem = Element(tag)
    for key, value in data.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem


data = {'name': 'sun', 'age': 24}
person = dict_to_xml('person', data)
print(person)  # <Element 'person' at 0x7f3c85034728>

person.set('id', '1')
person_string = tostring(person)
print(person_string)  # b'<person id="1"><name>sun</name><age>24</age></person>'

# 4 增量式解析大型xml iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


c = Counter()
data = parse_and_remove('tmp/test.xml', 'channel/item')

for d in data:
    c[d.findtext('title')] += 1

for title, num in c.most_common():
    print(title, num)

# 3 解析xml数据 xml模块 or from lxml.etree import parse
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    print(item.findtext('title'))

# 2 读写json数据 json.dumps()编码 json.loads()解码
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)  # json.dump() 文件
print(json_str)  # {"price": 542.23, "shares": 100, "name": "ACME"}

data = json.loads(json_str)  # json.load() 文件
print(data)  # {'shares': 100, 'price': 542.23, 'name': 'ACME'} dict

data = {'a': True, 'b': False, 'c': 123, 'd': None}
print(json.dumps(data))  # {"d": null, "c": 123, "b": false, "a": true}

# u = urlopen('https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi')
# resp = json.load(u.read().encode('utf-8'))
# pprint(resp)


class Person:
    def __init__(self, d):
        self.__dict__ = d


data = '{"price": 542.23, "shares": 100, "name": "ACME"}'
# object_hook object_pairs_hook
dataObject = json.loads(data, object_hook=Person)
print(dataObject)  # <__main__.Person object at 0x7f4b7ce99630>
print(dataObject.price)  # 542.23

data = {"price": 542.23, "shares": 100, "name": "ACME"}
print(json.dumps(data, indent=4))  # 格式化输出


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


d = json.dumps(p, default=serialize_instance)
print(d)  # {"x": 1, "__classname__": "Point", "y": 2}

classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


# <__main__.Point object at 0x7fdfa3faea20>
print(json.loads(d, object_hook=unserialize_object))

# 1 读写csv csv csv.reader(f, delimiter='\t') csv.writer(f) Pandas包处理数据统计pandas.read_csv()
with open('tmp/test.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)  # ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    for row in f_csv:
        print(row)

with open('tmp/test.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        # Row(Symbol='AA', Price='39.48', Date='6/11/2007', Time='9:36am', Change='-0.18', Volume='181800') ...
        print(Row(*r))

with open('tmp/test.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # {'Symbol': 'AA', 'Date': '6/11/2007', 'Change': '-0.18', 'Volume': '181800', 'Time': '9:36am', 'Price': '39.48'} ..
        print(row)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 1818000000),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 1955000000000),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 93500000000000000),
        ]

with open('tmp/test.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
