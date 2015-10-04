#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_db
import py_convert_cgi_form_to_array_with_mapping
cgitb.enable()




py_db.checkAccessCookie()



print 'Content-Type: text/html; charset=utf-8'
print ''


db = py_db.GetDB()


form = cgi.FieldStorage()

dt=form.getvalue("id")
dm=form.getvalue("name")

if py_db.checkuser("10",py_db.username)[3]<>3:
    cur = db.cursor()
    cur.execute("insert into tbl_variables (dsc_name,dsc_type) values ('"+dm+"','"+dt+"')")
    db.commit()
    db.close()
print "1"
