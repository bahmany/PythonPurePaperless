#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()
import uuid
import py_db

print 'Content-Type: text/plain'
print ''

form = cgi.FieldStorage()

dt=form.getvalue("id")

py_db.executesql("delete from tbl_letters where l_id="+dt)

