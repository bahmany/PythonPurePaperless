#!D:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_db
cgitb.enable()
#--------------------------------------------------
# Point : in site.py ascii must change to utf-8
#--------------------------------------------------
print 'Content-Type: text/html; charset=utf-8'
print ''
db = py_db.GetDB()
cur = db.cursor() 
is_it_ok = 0
form = cgi.FieldStorage()
httpreqs = form.getvalue("tp").split(",")   #getting item types to transfer
ss=""
for httpreq in httpreqs:
    ss+="!"+httpreq+":"
    cur.execute("select dsc_name FROM tbl_variables where dsc_type="+httpreq+" order by dsc_name ")
    for row in cur.fetchall() :
            ss+=","+str(row[0])
print   ss
