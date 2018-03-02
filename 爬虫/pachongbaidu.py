# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

html=urllib.urlopen("http://www.21ic.com/")

response = BeautifulSoup(html.read(),'html.parser')

text_list = response.find_all("a","target")

for text in text_list:
    print text.get_text()

html.close()


'''
html=urllib.urlopen("http://www.baidu.com")

response = BeautifulSoup(html.read(),'html.parser')

text_list = response.find_all("a","mnav")

for text in text_list:
    print text.get_text()

html.close()
'''
