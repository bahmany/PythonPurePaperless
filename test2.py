#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import sys


def GetOutOfTag(tagname,html):
    c=html
    start =  c.index('<'+tagname)+1
    end = c.index('</'+tagname+'>')
    c=c[start:end]
    start=0
    for i in c:
        start=start+1
        if i==">":break
    
    c=c[start:len(c)]
    return c
    
    


print "Content-type: text/plain"                                          
c=GetOutOfTag("body","""
<html><body><sasdasd>sadasd<ASdasd>SAd<sad></body>

""")
print c






