#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import Cookie
import os
import cgi
import py_db





form = cgi.FieldStorage()
uname=form.getvalue("uname","")
passs=form.getvalue("pass","")


#print 'Content-Type: text/html; charset=utf-8'
#print ''


py_db.Setusername(uname,passs)
print 'Location:py_main.py?mid=4'
print 'Content-Type: text/html; charset=utf-8'
print ''


#print ''