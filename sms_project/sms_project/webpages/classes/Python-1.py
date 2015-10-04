#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import py_db
from date_utils import calendar_util
from datetime import datetime
import Cookie
import os
from pyDes import *
import cgi
import sys
import cgitb
cgitb.enable(display=0, logdir="c:\cgilog.txt")






def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


rows = py_db.executeAndReturnRows("select * from sheet2")
b=0

i=0
for row in rows:
    if row[4] is not None:
        if len(row[4].__str__())>3:
            py_db.executesql("update sheet2 set cd3='{0}' , num4='1' where id = '{1}'".format(row[4],row[0]))
            i=i+1
            print "update sheet2 set cd3='{0}' where id = '{1}'".format(row[4],row[0])

#
#for row in rows:
#    dr = []
#    dr = row[1].split('_')
#    
#    for d in dr:
#        dh = d.split('-')
#        i=2
#        for dc in dh:
#            if is_number(dc):
#                i=i+1
#                py_db.executesql("update sheet set num{0}='{1}' where id = '{2}'".format(i,dc,row[11]))
#                print "ok"
#    
#    print b
    
    