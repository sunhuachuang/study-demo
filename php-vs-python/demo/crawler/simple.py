#! /usr/bin/python3

import requests
import re
from html.parser import HTMLParser

# 100 0000
# 350 0000
url = 'http://www.imooc.com/u/'
regex = re.compile(r'<p class="about-info">([\s\S]*?)</p>')


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(":", data)


parser = MyHTMLParser()

for i in range(1000000, 1000050):
    newUrl = url + str(i)

    response = requests.get(newUrl)
    if response.status_code == 200:
        content = response.text
        text = regex.findall(response.text)[0]
        result = text.replace('\r\n', '')
        result = result.replace(' ', '')
        parser.feed(result)
        print('------------------------------')
