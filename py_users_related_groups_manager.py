#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db
import Cookie
from datetime import *
import os
from pyDes import *



cgitb.enable()

py_db.checkAccessCookie()
py_db.checkuser(6,py_db.username)



#try:








def getall():
    _str=""
    rows = py_db.executeAndReturnRows("select u_complete_name,u_id,u_org_post from tbl_users order by u_name")
    for row in rows:
        if _str<>"":
            _str=_str+"dressa"+row[0].__str__()+"sxww"+row[1].__str__()+"sxww"+row[2].__str__()
        else:
            _str="dressa"+row[0].__str__()+"sxww"+row[1].__str__()+"sxww"+row[2].__str__()
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print _str
    
    
    
    
def answ(name,items):
    py_db.executesql("insert into tbl_users_related_groups (urg_title) values ('{0}');".format(name))
    row = py_db.executeAndReturnRows("select urg_id from tbl_users_related_groups where urg_title='{0}'".format(name));
    f=[]
    f=items.split("gfhjdg");
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    for item in f:
        py_db.executesql("insert into tbl_users_related_groups_member (urgm_link_to_users,urgm_link_to_groups) values ({0},{1})".format(item,row[0][0]))
       # print("insert into tbl_users_related_groups_member (urgm_link_to_users,urgm_link_to_groups) values ({0},{1})".format(item,row[0][0]))
    

    print "ok"
    
    
    
    
form = cgi.FieldStorage()
param =form.getvalue("getall","-1")
param2 =form.getvalue("name","-1")
param3=form.getvalue("ar","-1")
    
    
    
    

if param  !="-1":getall()    
if param2 !="-1":answ(param2,param3)    
    
