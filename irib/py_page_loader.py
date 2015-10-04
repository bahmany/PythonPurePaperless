#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
#روز 21 شهریور بروی بنده شروع نمودم و فقط جداول رو طراحی کردم و روند مربوط به ساختن فرم معمولی
#23 شهریور امروز میبایست برای استیل دهی و نحوه اسکریپت نویسی و ولیدیشن کار کنم
#5mehr Login m check module to takmil kardam :))) hala moondeh takmile form generator 
#
#
import MySQLdb
from classes import py_db
from classes.date_utils import calendar_util
from datetime import datetime
import Cookie
import os
from classes.pyDes import *
import cgi
import sys
import cgitb
import py_login
from py_page import *
cgitb.enable()




#print 'Content-Type: text/html; charset=utf-8'
#print ''
frm = ""
tmpl = ""
ck = py_login.get_sec_cookie()

# this line transfer cookie settings into other class
set_cookie_settings(ck)
#print ck
if len(ck) == 0:
    print 'Location: login.html'
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    
else:
   # print 'Content-Type: text/html; charset=utf-8'
   # print ''
    user_id = ck[2]
    
    #checking group and then user premission 
    #1=full access 2=readonly 3=denied
    
    user_level=0
    group_level=0
    final_permission=0
    
    #print user_id


    form = cgi.FieldStorage()
    formID = form.getvalue("id","-1")
    edit_from_id = form.getvalue("idsf","-1")
    
    
    if formID <> "-1":
        user_level = py_login.check_user_permission(user_id,formID)
        group_level = py_login.check_user_permission_from_group(user_id,formID)
        final_permission = py_login.check_total_premission(user_level,group_level)
        if final_permission == 4:
            frm = "عدم دسترسی"
        else:
            frm = render_form(formID, 1, user_id)
        tmpl = get_template_page()
        tmpl = tmpl.replace("##content", frm)
        tmpl = tmpl.replace("##loginInfo", py_db.get_company_name_from_user_id(user_id)+" خوش آمدید")
        tmpl = tmpl.replace("##UserInfo", py_login.get_username_from_user_id(user_id))
        tmpl = tmpl.replace("##Menu", create_right_menu())
        
        print tmpl
    if formID == "-1":
        print "عدم دسترسی"
    
    
    if edit_from_id <> "-1": print send_form(edit_from_id)
        



    