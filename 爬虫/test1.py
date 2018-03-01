# -*- coding: cp936 -*-
#coding = utf-8
'''
Xpath：/html/body/div[x]/ul/li[y]/img
css selector:谁，在哪，第几个，长什么样
body > div.main-content > ul > li:nth-child(x) > img
'''
from bs4 import BeautifulSoup
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1
    return imglist

html = getHtml("http://pic.yxdown.com/list/0_0_1.html")

print getImg(html)
