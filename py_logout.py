#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import Cookie
import os
import cgi
import py_db






#print 'Content-Type: text/html; charset=utf-8'
#print ''

cookie = Cookie.SimpleCookie()
cookie['uname'] = "ff"
cookie['pass'] = "cc"
print cookie
print 'Location:frm_login.html'
print 'Content-Type: text/html; charset=utf-8'
print ''


#print ''