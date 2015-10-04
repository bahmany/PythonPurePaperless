#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_db
import Cookie
from datetime import *
import os
from pyDes import *
cgitb.enable()




def handlethis(param1,param2):
    rows = py_db.executeAndReturnRows("select count(*) from tbl_inbox  where i_active_user_link =  (select u_id from tbl_users where u_name='{0}' and u_pass = '{1}')  and i_position=1".format(param1,param2))
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print rows[0][0].__str__()
                                      




form = cgi.FieldStorage()
param1 =form.getvalue("uname",-1)
param2 =form.getvalue("pass",-1)




if  param1 <> "-1" : handlethis(param1,param2)
    