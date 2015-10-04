#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db

from datetime import datetime
from pyDes import *
import py_user_manager



cgitb.enable()




#the first step if getting username and password cookies :
# if cookies is not found i redirect page to login
username=""
user_id=0
moduleID=0
 
 
 
 
 
 
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
    
#http://localhost/automation/py_main.py?texts=bahmany|009100|1&id=42   sample url 

def render_page(pageaddress,page_title):
    htmlstr="";
    
    f=open(pageaddress,'r')
    for line in f:
        htmlstr=htmlstr+line
    
    text=""
    text = GetOutOfTag("body",htmlstr)
    return text

 
 
    



def Setusername(uname,passs):
    if checkusername(uname,passs):
        uname=triple_des('mohammad_mrb_009').encrypt(uname, padmode=2)
        passs=triple_des('This@@si*&_&!Sec').encrypt(passs, padmode=2)
        cookie = Cookie.SimpleCookie()
        cookie['uname'] = uname
        cookie['passs'] = passs
        print cookie
    




def logout():
    cookie = Cookie.SimpleCookie()
    cookie['uname'] = ""
    cookie['passs'] = ""
    print cookie
    print "Location: frm_login.html"
    exit



#############################################################
# this line checks security first #
# if unknown user detected then login page appears
#############################################################
if py_db.checkAccessCookie()==0:
    f=open('frm_login.html','r')
    htmlstr=""
    for line in f:
        htmlstr=htmlstr+line
### redirecting to LOGin PaGE  .    
    print 'Content-Type: text/html; charset=utf-8'
    print ''    
    print htmlstr
    exit()
###########################################################
# after true login it is to check module premission
#_________________________________________________________
form = cgi.FieldStorage()
moduleID=form.getvalue("mid","-1")
if moduleID=="--1":logout();
if moduleID=="-1":exit
page=py_db.checkuser(moduleID, py_db.username)
#insert_to_log()
print 'Content-Type: text/html; charset=utf-8'
print ''
#print page
if page[3]==3:
    htmlstr=render_page("frm_block.html","عدم دسترسی")
    htmlstrtemp="";
    f=open("frm_template_page.html",'r')
    for line in f:
        htmlstrtemp=htmlstrtemp+line
    htmlstrtemp=htmlstrtemp.replace("##content",htmlstr)
    htmlstrtemp=htmlstrtemp.replace("##menu","sssssss")
    fullname=py_db.getFullName(py_db.username);
    htmlstrtemp=htmlstrtemp.replace("#user name",fullname )
    
    print htmlstrtemp
    exit
else:
    htmlstr=render_page(page[4],page[5])
    htmlstrtemp="";
    f=open("frm_template_page.html",'r')
    for line in f:
        htmlstrtemp=htmlstrtemp+line
    htmlstrtemp=htmlstrtemp.replace("##content",htmlstr)
    htmlstrtemp=htmlstrtemp.replace("##menu","sssssss")
    htmlstrtemp=htmlstrtemp.replace("#user name ",py_db.getFullName(py_db.username) )
    htmlstrtemp=htmlstrtemp.replace("##timeee",str(datetime.now()) )
    print htmlstrtemp









