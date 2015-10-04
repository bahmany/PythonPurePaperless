#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import Cookie
import os
import cgi
import py_db





form = cgi.FieldStorage()
uname=form.getvalue("xsa","")






#print 'Content-Type: text/html; charset=utf-8'
#print ''

if uname<>"":
    de=uname.split("szzas");
    if de[2]==de[3]:
        py_db.executesql("""
            update tbl_users set `u_pass`='{0}'
            where u_name='{1}' and u_pass='{2}'""".format(de[2],de[0],de[1])
        )
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    
    
    
    
    


#print ''