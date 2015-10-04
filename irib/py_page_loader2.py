#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
#روز 21 شهریور بروی بنده شروع نمودم و فقط جداول رو طراحی کردم و روند مربوط به ساختن فرم معمولی
#23 شهریور امروز میبایست برای استیل دهی و نحوه اسکریپت نویسی و ولیدیشن کار کنم
#5mehr Login m check module to takmil kardam :))) hala moondeh takmile form generator 
#
#
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



 
def GetOutOfTag(tagname,html):
    c=html
    start =  c.index('<'+tagname)+1
    end = c.index('</'+tagname+'>')
    c=c[start:end]
    start=0
    for i in c:
        start=start+1
        if i==">":break
    
    c=c[start:len(c)]
    return c
    



def render_page(pageaddress,page_title):
    htmlstr="";
    f=open("html pages/"+pageaddress,'r')
    for line in f:
        htmlstr=htmlstr+line
    text=""
    text = GetOutOfTag("body",htmlstr)
    return text

 
 
    


print 'Content-Type: text/html; charset=utf-8'
print ''
frm = ""
tmpl = ""


form = cgi.FieldStorage()
formID = form.getvalue("id","-1")


form_name = py_db.executeAndReturnRows("select f_english_form_name from tbl_forms where f_id = "+formID.__str__())[0][0]

frm = render_page(form_name, "testtttt")
tmpl = get_template_page()
tmpl = tmpl.replace("##content", frm)
#tmpl = tmpl.replace("##loginInfo", py_db.get_company_name_from_user_id(user_id)+" خوش آمدید")
#tmpl = tmpl.replace("##UserInfo", py_login.get_username_from_user_id(user_id))
tmpl = tmpl.replace("##Menu", create_right_menu())

print tmpl




    