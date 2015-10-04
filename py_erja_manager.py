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


def send_users_list():
    sql='''
      SELECT
      u_id,
u_complete_name,
u_org_post,
u_has_assist,
(SELECT `u_complete_name` FROM `tbl_users` t2 WHERE t2.u_id= t1.u_link_to_user_assistant) AS sssdsd

 FROM tbl_users t1
 
 where u_id not in ( select uh_user_id from tbl_users_hidden )
 and u_id in (SELECT DISTINCT t1.`urgm_link_to_users` FROM tbl_users_related_groups_member t1 WHERE t1.urgm_link_to_groups IN (SELECT DISTINCT t2.urgm_link_to_groups FROM tbl_users_related_groups_member t2 WHERE t2.`urgm_link_to_users`={0}))
 and u_id not in ({0})
 order by u_complete_name
        '''.format(py_db.user_id)
    print sql
    rows = py_db.executeAndReturnRows(sql)
    txt = ""
    
    for row in rows:
        txt=txt+"|"
        for r in row:
            txt = txt+"::"+r.__str__()
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print txt
        
    
def insert_into_erja(param1,l_id):
    st=param1
    #print st
    st=st[3:len(st)]
    #print st
    st=param1.split("zzz")
    for s in st:
        sr=s.split(")))")
        if len(s)<>0:
            hidd=1
            if sr[1][0:2]=="**":
                hidd=2
            py_db.executesql("""
                             
            UPDATE tbl_inbox
            set i_position= 3
            WHERE i_active_user_link={1} and 
            i_letter_link = {0}
            
            
            
            
                             """.format(l_id,py_db.user_id)
                             )
            sqlstr = """
            
        INSERT INTO `automation`.`tbl_inbox`
            (
             `i_letter_link`,
             `i_position`,
             `i_date_of_create`,
             
             `i_active_user_link`,
             `i_order`,
        
             `i_prev_active_user_link`,
             `i_erja_type`)
VALUES (
        '{0}',
        '1',
        '{1}',

 (
 
 
SELECT 
CASE t1.u_direct
WHEN 0 THEN {2}
WHEN 1 THEN 
	CASE  (SELECT t3.`u_has_assist` FROM tbl_users t3 WHERE t3.u_id={2})
	WHEN 0 THEN {2}
	WHEN 1 THEN 
		CASE  (SELECT t5.u_link_to_user_assistant FROM tbl_users t5 WHERE t5.u_id={2})
		WHEN {5} THEN {2}
		ELSE (SELECT t2.u_id FROM tbl_users t2 WHERE t2.u_id = (SELECT t3.`u_link_to_user_assistant` FROM tbl_users t3 WHERE t3.u_id={2}) LIMIT 1)
		END
	END 
END AS ssss
 FROM tbl_users t1 WHERE t1.u_id={5}
 
        )
        
        ,
        '{3}',
        
        {5},
        '{4}'
        );
            
            
            """.format(
                l_id,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                sr[0],
                sr[1],
                hidd,
                py_db.user_id
                )
            
    
            py_db.executesql(sqlstr);
    
    




    print 'Content-Type: text/html; charset=utf-8'
    print ''
    #print sqlstr
    print "1"
    


def getErjaList(param2):
    rows = py_db.executeAndReturnRows(
        '''
SELECT 

t1.i_date_of_create,
t1.i_date_of_seen,
(SELECT t2.u_complete_name FROM tbl_users t2 WHERE t2.u_id=t1.i_active_user_link LIMIT 1) AS current,
(SELECT t2.u_complete_name FROM tbl_users t2 WHERE t2.u_id=t1.`i_prev_active_user_link` LIMIT 1) AS lastuser,
t1.i_order,


CASE TRUE
WHEN t1.`i_erja_type` = 1 THEN "معمولی"
WHEN t1.i_erja_type = 2 THEN "فوری"
WHEN t1.i_erja_type = 3 THEN "خیلی فوری"
END AS hello 

,
CASE TRUE
WHEN t1.i_position = 1 THEN "خوانده نشده"
WHEN t1.i_position = 2 THEN "خوانده شده"
WHEN t1.i_position = 3 THEN "ارجاع شده"
WHEN t1.i_position = 4 THEN "بایگانی شده"
END AS hello 




 FROM tbl_inbox t1


WHERE 
t1.i_letter_link = {0}  AND
t1.i_erja_type=1
ORDER BY t1.i_id asc        
        '''.format(param2)
    );
    i=0
    str = "<div>"
    for row in rows:
        s=""
        if i==0:
            s="<div>"+"ثبت در سیستم مورخه "+":"+py_db.mil_to_sh_with_time(row[0].strftime("%Y-%m-%d %H:%M:%S"))+"<br>"+" توسط "+ row[2]+":"+  "</div>"+"<hr>"
            s=s
        else:
            s="<div> با هامش "+":"+row[4]+"<br>"+" ارسال شده به "+":"+row[2]+"<br>"+" در تاریخ "+":"+ py_db.mil_to_sh_with_time(row[0].strftime("%Y-%m-%d %H:%M:%S"))+"<br>"+" وضعیت "+":"+row[6]+"</div>ارجاع کننده : "+row[3]+"<hr>"
            s=s       
        #dd = 
        str=str+s
        i=i+1
               
               
            
    str=str+"</div>"
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print str
    


def isItOkToErja(param3):
    py_db.checkAccessCookie()
    userID = py_db.user_id;
    sqlstr = """
    select i_position from tbl_inbox where i_letter_link = {0} and i_active_user_link={1} order by i_id desc limit 1
    """.format(param3,userID)
    rows = py_db.executeAndReturnRows(sqlstr)
    str = ""
    str = rows[0][0].__str__()
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print str


def GetVar():
    strlist=""
    rows = py_db.executeAndReturnRows("select dsc_name from tbl_variables where dsc_type=7 order by dsc_name")
    for row in rows :
	if strlist == "" :
	    strlist = row[0]
	else:
	    strlist = strlist+"zzhtc"+row[0]
    rows = py_db.executeAndReturnRows('SELECT DISTINCT `i_order` FROM `tbl_inbox` WHERE i_prev_active_user_link='+py_db.user_id+' AND i_order <>"" ORDER BY i_id desc limit 5')
    for row in rows :
	if strlist == "" :
	    strlist = row[0]
	else:
	    strlist = strlist+"zzhtc"+row[0]
    print 'Content-Type: text/html; charset=utf-8'
    print ''
    print strlist
    
    


#try:
form = cgi.FieldStorage()
param =form.getvalue("gulst","-1")
param1 =form.getvalue("dddta","-1")
param2 =form.getvalue("erj_l_id","-1")
param3 =form.getvalue("erj_is_ok","-1")
param4 = form.getvalue("listID","-1")

if param  !="-1":send_users_list()
if param1  !="-1":insert_into_erja(param1,form.getvalue("l_id"))
if param2 !="-1":getErjaList(param2)
if param3 !="-1":isItOkToErja(param3)
if param4 !="-1":GetVar()


            
#except Exception:
#    print 'Content-Type: text/html; charset=utf-8'
#    print ''
#    print Exception.__str__
    
    



