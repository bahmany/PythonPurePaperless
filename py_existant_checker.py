#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
cgitb.enable()


print 'Content-Type: text/html; charset=utf-8'
print ''


db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                     user="root", # your username
                     passwd="009100", # your password
                     db="automation",
                     charset="utf8",
                     use_unicode=True) # name of the data base

form = cgi.FieldStorage()
_type = form["id"].value
_name = form["name"].value
sqlstr = "select count(*) as ssss from tbl_variables where dsc_name='"+str(_name)+"' and dsc_type='"+str(_type)+"'"

cur = db.cursor()
cur.execute(sqlstr)
rows = cur.fetchall()
for row in rows:
    if row[0]<>0:
        print "1"
    else:
        print "0"
