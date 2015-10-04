#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db
cgitb.enable()

form = cgi.FieldStorage()
dt=form.getvalue("id","42")

print 'Content-Type: text/html; charset=utf-8'
print ''
db=py_db.GetDB()
cur = db.cursor()
cur.execute("select * from tbl_letters_papers where lp_link_to_letters="+dt)
rows = cur.fetchall()
strr = ""
for row in rows:
    strr=strr+"?"+str(row[0])+":"+str(row[4]).split("_")[1]

print strr




