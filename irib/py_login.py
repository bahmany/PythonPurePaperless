#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-


from classes.py_db import *
from classes.date_utils import calendar_util
from datetime import datetime
import Cookie
import os
from classes.pyDes import *
import cgi
import sys
import cgitb
cgitb.enable()




def check_user_and_pass(_uname,_pass):
    sql = "select count(*) from tbl_users where u_name='{0}' and u_pass='{1}' ".format(_uname,_pass)
    user_count = executeAndReturnRows(sql)[0][0]
    if user_count==1: return True
    else: return False



def check_total_premission(userlevel,grouplevel):
    if userlevel==4 and grouplevel==4: return 3
    if userlevel==1 : return 1
    if userlevel==2 : return 2
    if userlevel==3 : return 3
    if userlevel==4 and grouplevel==1: return 1
    if userlevel==4 and grouplevel==2: return 2
    if userlevel==4 and grouplevel==3: return 3

    


#1=full access 2=readonly 3=denied 4=No Field
def check_user_permission(user_id,module_id):
    sql="select up_permission from tbl_users_permission where up_user_link={0} and up_module_link={1} limit 1".format(user_id,module_id)
    permission = executeAndReturnRows(sql)
    if permission==():
        return 4
    return permission[0][0]


#1=full access 2=readonly 3=denied 4=No Field 
def check_user_permission_from_group(user_id,module_id):
    sql = "select ugp_permission from tbl_users_groups_permission where ugp_module_link = {0} and ugp_group_link = (select ugn_group_link from tbl_users_groups_members where ugm_user_link={1} limit 1) limit 1".format(module_id,user_id)
    permission = executeAndReturnRows(sql)
    if permission==():
        return 4
    return permission[0][0]

    
def check_sec_cookie(_uname,_pass):
    _uname = decode(_uname)
    _pass = decode(_pass)
    return check_user_and_pass(_uname,_pass)

def set_sec_cookie(_uname,_pass):
    c = Cookie.SimpleCookie()
    c["_uname"]=_uname
    c["_pass"]=_pass
    
    dec_uname = decode(_uname)
    dec_uid = get_user_id_from_db(dec_uname)
    
    c["_uid"]=encode(dec_uid)
    print c.output()
    #print "Set-Cookie: _uname="+_uname
    #print "Set-Cookie: _pass="+_pass
    #print "Set-Cookie: _uid="+encode(get_user_id(decode(_uname)).__str__())
        
        
def get_sec_cookie():
    s=[]
    try:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        _uname = cookie["_uname"].value
        _pass = cookie["_pass"].value
        _uid = cookie["_uid"].value
        
        #print cookie
        

        
        if (check_user_and_pass(decode(_uname),decode(_pass)  )):
            s.append(decode(_uname))
            s.append(decode(_pass ))
            s.append(decode(_uid))
            return s
        else :
            return s       
    except (Cookie.CookieError, KeyError):
        return s

        
def get_user_id(_uname):
    row = executeAndReturnRows("select u_id from tbl_users where u_name='{0}' limit 1".format(_uname))
    if row<>():
        return row[0][0]
    else:
        return -1



def check_login_and_unEncrypt(_uname,_pass):
    
    if check_user_and_pass(_uname,_pass):
        set_sec_cookie(encode(_uname),encode(_pass))
        print "Location: py_page_loader.py?id=1"
        print ''
        
    else:
        print "Location: login.html"
        print ''
        
        
def get_username_from_user_id(uid):
    return executeAndReturnRows("select u_name from tbl_users where u_id={0}".format(uid))[0][0]



def get_socc_id():
    ss = get_sec_cookie()
    return executeAndReturnRows("select u_soccc_id from tbl_users where u_name = '{0}'".format(ss[0]))[0][0]

def get_user_id():
    return get_sec_cookie()[2]

def get_user_id_from_db(uname):
    return executeAndReturnRows("select u_id from tbl_users where u_name = '{0}'".format(uname))[0][0].__str__();



def log_out():
    c = Cookie.SimpleCookie()
    c["_uname"]="z"
    c["_pass"]="z"
    c["_uid"]="-1"
    print "Location: login.html"
    print ''


form = cgi.FieldStorage()


#param1=form.getvalue("chklgn","-1")
param2=form.getvalue("___uname","-1")
param3=form.getvalue("___pass","-1")
param4=form.getvalue("logout","-1")





#if param1 <> "-1": check_login(param1.split("xxxx")[0],param1.split("xxxx")[1])



#print form

if param2 <> "-1" and param3 <> "-1":check_login_and_unEncrypt(param2,param3)
if param4 <> "-1" :log_out()




        
    



#print check_user_permission_from_group("1","1")


    
