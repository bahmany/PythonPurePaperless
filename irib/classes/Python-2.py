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






def ord_validation_mapping(hashed_text):
    txt="";
    for i in list(hashed_text):
        txt+=" "+ord(i).__str__()
    return txt
    
rows = py_db.executeAndReturnRows("select * from sheet2")
for row in rows:
    if row[2] is not None:
        if len(row[2].__str__())>0:
            ss= row[2]
            ss=ss.replace("ي","ی")
            ss=ss.replace("ك","ک")
            py_db.executesql("update sheet2 set cd3='{0}' where id = '{1}'".format(ss,row[0]))
            print row[0]
            
            






#print ord_validation_mapping("ك")
#print ord_validation_mapping("ک")+"  <<< "

