#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db
import Cookie
import os
from pyDes import *
#import py_main



cgitb.enable()







def do_insert(param):
    #name:user:comname:possst:false:true:possst
    param = param.replace('false','0')
    param = param.replace('true','1')
    param = param.replace('false','0')
    param = param.replace('true','1')
    user_assistant_u_id=-1
    if param.split(":")[5]=="1":
        sqlstr='''
    select u_id from tbl_users where u_complete_name = '{0}' limit 1
        '''.format(param.split(":")[6]);
        
        db=py_db.GetDB()
        cur=db.cursor();
        cur.execute(sqlstr)
        rows = cur.fetchall()
        for row in rows:
            user_assistant_u_id = row[0]
            
        
    
    sqlstr = '''
    INSERT INTO `tbl_users` 
    (`u_name`,`u_pass`,
    `u_secretariat_group_link`,`u_complete_name`,
    `u_org_post`,`u_active`,
    `u_has_assist`,`u_link_to_user_assistant`,
    u_direct
    
    )
    VALUES
    ('{0}','{1}',{2},'{3}','{4}',{5},{6},{7},{8}
    
    )
    '''.format(
        param.split(":")[0],
        param.split(":")[1],
        param.split(":")[8],
        param.split(":")[2],
        param.split(":")[3],
        param.split(":")[4],
        param.split(":")[5],
        user_assistant_u_id.__str__(),
        param.split(":")[7]
        )
    
    
    
    print 'Content-Type: text/html; charset=utf-8'
    print ''
#    print sqlstr
    py_db.executesql(sqlstr)
    
    print "1"
        

def send_tbl_array():
    sqlstr="""
   
    SELECT
    t1.u_name,
    t1.u_complete_name,
    t1.u_org_post,
    t1.u_active,
    (SELECT t2.u_complete_name FROM tbl_users AS t2 WHERE t2.u_id=t1.`u_link_to_user_assistant`),
    t1.u_direct
    
    FROM tbl_users AS t1 ORDER BY t1.u_name ASC
    
    """
    db=py_db.GetDB()
    cur=db.cursor()
    cur.execute(sqlstr)
    rows = cur.fetchall()
    arr_str=""
    for row in rows:
        arr_str=arr_str+"||"
        for r in row:
            arr_str=arr_str+":::"+r.__str__()
        
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print arr_str
    

def sendonedate(uname):
    sqlstring='''
    select
`u_name`,
`u_pass`,
`u_complete_name`,
`u_org_post`,
`u_active`,
`u_has_assist`,

    (select t2.u_complete_name from tbl_users t2 where t2.u_id=t1.u_link_to_user_assistant) as cmname ,
    `u_direct`,
    u_secretariat_group_link

    from tbl_users t1 where u_name = '{0}' limit 1
    '''.format(uname)
    rows = py_db.executeAndReturnRows(sqlstring)
    str=""
    for row in rows:
        for r in row:
            str=str+"::"+r.__str__()
        
    str=str.replace("::None","::")
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print str

def convert_array_to_string(arr,breaker):
    s=""
    for r in arr:
        s=sr+breaker+r
    return s
    


def checkdupusername(param4):
    rows = py_db.executeAndReturnRows('''
    select count(*) from tbl_users where u_name='{0}' '''.format(param4))
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print rows[0][0]


def checkifu_comp_name_is(param5):
    rows = py_db.executeAndReturnRows('''
    select count(*) from tbl_users where u_complete_name='{0}' '''.format(param5))
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    if rows[0][0]==1:print "0"
    if rows[0][0]==0:print "1"




def do_update(param):
    param = param.replace('false','0')
    param = param.replace('true','1')
    param = param.replace('false','0')
    param = param.replace('true','1')
    user_assistant_u_id=-1
    drf=py_db.ifIntNullThen(param.split(":")[6].__str__()).__str__()
    d=py_db.do_edit("update","tbl_users",
              [["u_name","u_pass","u_secretariat_group_link","u_complete_name",
                "u_org_post","u_active","u_has_assist","u_link_to_user_assistant","u_direct"],
              [
               param.split(":")[0],
               param.split(":")[1],
               param.split(":")[8],
               param.split(":")[2],
               param.split(":")[3],
               param.split(":")[4],
               param.split(":")[5],
               drf,
               param.split(":")[7]
               ],
              [0,0,0,0,0,0,0,1,0]],
              "yes",[
              ["tbl_users ,u_id,u_complete_name,u_id,{0},u_link_to_user_assistant".format(drf)]]
              ,"u_name",param.split(":")[0])
    i=py_db.executesql(d)
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print i
    #print d


def get_sec_list():
    rows = py_db.executeAndReturnRows("""
                                      SELECT DISTINCT(s_group),`s_group_title`
 FROM `tbl_secretariat`
                                      
                                      """
                                      );
    stt = ""
    for row in rows:
        stt = stt+":::"+row[0].__str__()+"ppp"+row[1].__str__()
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print stt    
    
def send_usr_premission_lst(param):
    py_db.checkAccessCookie()
    py_db.checkuser(5,py_db.username)
    sqlstr = """
    SELECT 
t1.m_id,
t1.m_page_title ,


CASE
(SELECT t2.m_type_of_view 
FROM tbl_module_premission t2
WHERE t2.m_user_link = {0} AND t2.m_module_link= t1.`m_id`) 
WHEN 1 THEN "true"
ELSE "false"

END AS sss

FROM tbl_modules t1
        """.format( py_db.get_userID_from_uname(param) )
    rows = py_db.executeAndReturnRows(sqlstr)
    str = ""
    for row in rows:
        str = str+"::"+row[0].__str__()+"pp"+row[1].__str__()+"pp"+row[2].__str__()
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print str    
    

def updateusrprm(param,uid):
    py_db.checkAccessCookie()
    py_db.checkuser(5,py_db.username)
    __form = cgi.FieldStorage()
    sel_uid = py_db.get_userID_from_uname(uid)
    
    sd=param.split("bbb")
    py_db.executesql("delete from tbl_module_premission where m_user_link = "+sel_uid)
    for row in sd:
        s="3"
        if (row.split("=~")[1].__str__())== "true":s="1"
        py_db.executesql("""
                         insert into tbl_module_premission
                         (`m_module_link`,`m_user_link`,`m_type_of_view`)
                         values
                         ({0},{1},{2}) 
                         """.format(row.split("=~")[0].__str__(),
                                    sel_uid,s))
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print "1"      
    

def sendusersum():
    py_db.checkAccessCookie()
    sqlstr = """
    SELECT COUNT(*) FROM  tbl_inbox WHERE `i_position`=1 AND `i_active_user_link`={0}
    
    """.format(py_db.user_id)
    row = py_db.executeAndReturnRows(sqlstr)
    
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print row[0][0]
    
    
def checkif_doc_scanned(_param14):
    row = py_db.executeAndReturnRows("select lp_address from tbl_letters_papers where lp_type=2 and lp_link_to_letters="+_param14)
    str="0"
    if len(row) <> 0: str=row[0][0]
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print str


def get_negahban_list():
    rows = py_db.executeAndReturnRows("SELECT * FROM `tbl_users` WHERE `u_org_post` LIKE '%نگهبان%'")
    s=""
    i=0
    for row in rows:
        if i==0:
            s=row[0].__str__()+"="+row[4].__str__()
        else:
            s=s+"vfdd"+row[0].__str__()+"="+row[4].__str__()
        i+=1
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print s
    



#try:
form = cgi.FieldStorage()
param =form.getvalue("hstr","-1")
param2=form.getvalue("pssws","-1")
param3=form.getvalue("cllon","-1")
param4=form.getvalue("chkdup","-1")
param5=form.getvalue("chkexis","-1")
param6=form.getvalue("edithstr","-1")
param7=form.getvalue("unamsse","-1")
param8=form.getvalue("out","-1")
param9=form.getvalue("seclst","-1")
param10=form.getvalue("usprm","-1")
param11=form.getvalue("urpd","-1")
param12=form.getvalue("uid","-1")
param13=form.getvalue("i","-1")
param14=form.getvalue("checkscanned","-1")
param15=form.getvalue("negahban","-1")


if param  !="-1":do_insert(param)
if param2 !="-1":send_tbl_array()
if param3 !="-1":sendonedate(param3)
if param4 !="-1":checkdupusername(param4)
if param5 !="-1":checkifu_comp_name_is(param5)
if param6 !="-1":do_update(param6)
if param7 !="-1":getFullName(param7)
if param8 !="-1":logout()
if param9 !="-1":get_sec_list()
if param10 != "-1":send_usr_premission_lst(param10)
if param11 != "-1" and param12 != "-1" :updateusrprm(param11,param12)
if param13 !="-1":sendusersum();
if param14!="-1":checkif_doc_scanned(param14)
if param15!="-1":get_negahban_list()

            
#except Exception:
#    print 'Content-Type: text/html; charset=utf-8'
#    print ''
#    print Exception.__str__
    
    



