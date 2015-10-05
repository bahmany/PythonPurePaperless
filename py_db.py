#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-


import MySQLdb
import date_utils.calendar_util
from datetime import datetime
import Cookie
import os
from pyDes import *





def GetDB():
    db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                         user="", # your username
                         passwd="", # your password
                         db="automation",
                         charset="utf8",
                         use_unicode=True) # name of the data base
    return db


global u_id
global u_secretriat_group_id

moduleID=0


user_id=0
username=""

u_id=1
u_secretriat_group_id = 1



def executesql(sqlstring):
    db=GetDB()
    cur = db.cursor()
    cur.execute(sqlstring)
    db.commit()
    db.close()
    return "1"

def checkuser(module_id,username):
    db=GetDB()
    cur = db.cursor()
    
    # in address bar localhost/automation/py_main.py?texts=bahmany|009100|1%id*42
    #   %   is devider
    __module_id=module_id.__str__()
    if len(module_id.__str__().split("%"))<>0:
        __module_id=module_id.__str__().split("%")[0]
    
    
    
    sqlstr = """
    SELECT *,
    (SELECT m_page_file_name FROM tbl_modules WHERE tbl_modules.m_id=m_module_link) AS module_name,
(SELECT m_page_title FROM tbl_modules WHERE tbl_modules.m_id=m_module_link) AS page_name


    
    FROM tbl_module_premission
WHERE m_user_link = {0}
AND
      m_module_link = {1}
      """.format(
        get_userID_from_uname(username)
        ,__module_id)    
    #print sqlstr
    cur.execute(sqlstr)
    rows = cur.fetchall()
    #print rows
    type_of_acess=[]  #means block
    type_of_acess.append("-1")
    type_of_acess.append("-1")
    type_of_acess.append("-1")
    type_of_acess.append("3")
    type_of_acess.append("")
    type_of_acess.append("")
    
    
    for row in rows:
        
        type_of_acess[3] = row[3]
        type_of_acess[0] = row[0]
        type_of_acess[1] = row[1]
        type_of_acess[2] = row[2]
        type_of_acess[4] = row[4]
        type_of_acess[5] = row[5]
        
        
    
    db.close()
    insert_to_log(module_id,get_userID_from_uname(username))
    #print type_of_acess
    return type_of_acess
        
    
    
def mil_to_sh_with_time(mildate):
    
    #dd = datetime.strptime(mildate)
    
   
    try:
    
        m = date_utils.calendar_util.jd_to_persian(
            date_utils.calendar_util.gregorian_to_jd(
               int(mildate.split(" ")[0].split("-")[0]),
               int(mildate.split(" ")[0].split("-")[1]),
               int(mildate.split(" ")[0].split("-")[2])
                ))
        dt=m[0].__str__()+"/"+m[1].__str__()+"/"+m[2].__str__()+" "+mildate.split(" ")[1]
        return dt
    except:
        return ""

def sh_to_mil(mildate):
    try:

        m = date_utils.calendar_util.jd_to_gregorian(
            date_utils.calendar_util.persian_to_jd(
               int(mildate.split("/")[0]),
               int(mildate.split("/")[1]),
               int(mildate.split("/")[2])
                ))
        dt=m[0].__str__()+"/"+m[1].__str__()+"/"+m[2].__str__()
        return dt
    except:
        return ""





def checkusername(uname,passs):
    #print 'Content-Type: text/html; charset=utf-8'
    #print '' 
    #print uname+"                        "+passs
    db = GetDB();
    cur = db.cursor();
    sql = "select count(*) from tbl_users where u_name='{0}' and u_pass='{1}'".format(uname,passs)
    cur.execute(sql)
    rows = cur.fetchall()
    if rows[0][0]==0:
        return False
    if rows[0][0]==1:
        username = uname
        user_id = get_userID_from_uname(uname)
        return True
        

    db.close()

def get_userID_from_uname(__uname):
    db = GetDB();
    cur = db.cursor();
    sqlss="select u_id from tbl_users where u_name='{0}'".format(__uname)
    cur.execute(sqlss)
    rows = cur.fetchall()
    #for row in rows:
        #user_id = get_userID_from_uname(row[0])
    db.close()
    return rows[0][0].__str__()
       


def executeAndReturnRows(sqlstring):
    db = GetDB();
    cur = db.cursor();
    cur.execute(sqlstring)
    rows = cur.fetchall()
    db.close();
    return rows



def ifIntNullThen(sr):
    if len(sr)==0:return -1
    else : return sr



def do_edit(edit_type,tablename,itemArray,isThereAnySubSelect="no",subselect=[],ifupdateKeyField="",ifupdateKeyValue=""):
    #subselect array format [tablename:fieldname:keyfield:value:ToParentItem]
    #ItemArrayFormat [fieldname,fieldname],[value(n)],[isKeyField(n)]]
    
    value_from_subselect = []   # item_name , value 
    if isThereAnySubSelect=="yes":
        for s in subselect:
            for ss in s:
                f=ss.split(",")
                
                str = "select {0} from {1} where {2} = '{3}' LIMIT 1".format(
                    f[1],f[0],f[2],f[4]
                    )
                row = executeAndReturnRows(str)
                if len(row)!=0:
                    value_from_subselect.append(f[5]+":"+row[0][0].__str__())
                #print value_from_subselect
    
    if edit_type=="update":
        setarray=itemArray[0]
        setstring=""
        i=0
        for s in setarray:
            if itemArray[2][i]==0:
                setstring = setstring+" , "+s+" ='"+itemArray[1][i]+"' "
            if itemArray[2][i]==1:
                __value = ""
                for v in value_from_subselect:
                    if v.split(":")[0]==s:
                       __value= v.split(":")[1]
                setstring = setstring+" , "+s+" ='"+__value+"' "
            
            
            i=i+1
        #print setstring
        sqlstr="update {0} set {1} where {2}='{3}'".format(
            tablename,setstring,ifupdateKeyField,ifupdateKeyValue);
        
        sqlstr=sqlstr.replace("set  ,","set  ")
        return sqlstr    
            
            
        
#do_edit("update","tbl_users",
#        [["u_name","u_pass","u_secretariat_group_link","u_complete_name","u_org_post","u_active","u_has_assist","u_link_to_user_assistant"],
#        ["bahmany99","009100","1","محمد رضا بهمنی","office manager","1","1","محمد رضا بهمنی"],
#        [0,0,0,0,0,0,0,1]],
#        "yes",[
#        ["tbl_users ,u_id,u_complete_name,u_id,1,u_link_to_user_assistant"],
#        ["tbl_users ,u_id,u_complete_name,2,u_link_to_user_assistant"],
#        ["tbl_users ,u_id,u_complete_name,3,u_complete_name"]],"u_name","bahmany")
            
        
        

def checkAccessCookie():
    cookie=Cookie.SimpleCookie()
    bd=0
    if os.environ.has_key('HTTP_COOKIE'):
        cookie.load(os.environ['HTTP_COOKIE'])
        
        try:
            uname = cookie["uname"].value
            passs = cookie["pass"].value
            uname = triple_des('mohammad_mrb_009').decrypt(uname, padmode=2)
            passs = triple_des('This@@si*&_&!Sec').decrypt(passs, padmode=2)
            if checkusername(uname,passs):
                bd=1
                global username
                global user_id
                username=uname
                user_id=get_userID_from_uname(uname)
            else: bd=0
            return bd
            
        except Exception:
            bd=0
            return bd
    return bd


def Setusername(uname,passs):
    if checkusername(uname,passs):
        uname=triple_des('mohammad_mrb_009').encrypt(uname, padmode=2)
        passs=triple_des('This@@si*&_&!Sec').encrypt(passs, padmode=2)
        cookie = Cookie.SimpleCookie()
        cookie['uname'] = uname
        cookie['pass'] = passs
        print cookie
        
        
        


def getFullName(unme):
    rows = executeAndReturnRows("select u_complete_name from tbl_users where u_name='"+unme+"'")
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    return rows[0][0].__str__()




def getUserNameAndPassAndSetItToGlobals():
    checkAccessCookie()




def insert_to_log(mod_id,userID):
    ssqlstr ='''
    INSERT INTO `automation`.`tbl_users_clicked_module`
                (`ua_user_link`,
                 `ua_date`,
                 `us_module_link`)
    VALUES ('{0}',
            '{1}',
            '{2}');
            
            '''.format(
                userID,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                mod_id
            )
    executesql(ssqlstr)
    


def get_datetime_of_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
