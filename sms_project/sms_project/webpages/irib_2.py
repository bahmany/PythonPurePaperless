#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
from BeautifulSoup import BeautifulSoup
import re
import codecs
import sys
f = open('fff.htm')
html = f.read()
soup = BeautifulSoup(html)
body = soup.body.contents
para = soup.findAll('p')
print str(para).encode('utf-8')
