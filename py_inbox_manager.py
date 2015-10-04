#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db

from datetime import datetime
cgitb.enable()

py_db.checkAccessCookie()

print 'Content-Type: text/html; charset=utf-8'
print ''




form = cgi.FieldStorage()
dta=form.getvalue("ddf","-1")
sds=""
baygani = 0
if dta!="-1":
    rows = dta.split("sazw")
    for row in rows:
        r = row.split("zzz")
        
        if r[0]=="_obj_chk_unread":
            if r[1]=="true": sds =sds+ " i_position = 1 "
        if r[0]=="_obj_chk_read":
            if r[1]=="true": sds =sds+ " or i_position = 2 "
        if r[0]=="_obj_chk_sent":
            if r[1]=="true": sds =sds+ " or i_position = 3 "
        if r[0]=="_obj_chk_baygani":
            if r[1]=="true":
                sds =sds+ " or i_active_user_link = 43160 "
                baygani=1
        
        if r[0]=="_obj_from": sds =sds+ "and i_date_of_create between '"+py_db.sh_to_mil(r[1])+"' and "
        if r[0]=="_obj_to": sds =sds+ " '"+py_db.sh_to_mil(r[1])+"' "
        if r[0]=="_obj_search": sds=sds+ """
        ) AND (    
        ((i_order LIKE '%{0}%') OR 
        (l_subject LIKE '%{0}%') OR
        (l_letter_number LIKE '%{0}%') OR
        (((SELECT tbl_secretrait_letters.sl_secretariat_no FROM tbl_secretrait_letters WHERE sl_letter_link=i_letter_link LIMIT 1)) LIKE '%{0}%') OR 
        ((SELECT u_complete_name FROM tbl_users WHERE u_name='{1}' ) LIKE '%{0}%') OR 
        ((SELECT u_complete_name FROM tbl_users WHERE u_id=i_prev_active_user_link ) LIKE '%{0}%'))  
            )""".format(r[1],py_db.username)
    if sds[0:3]==" or": sds=sds[4:len(sds)]
    if sds[0:4]==" and": sds=sds[5:len(sds)]
#    print sds
        
       
        
        
        
        
        
    


sqlstr = """
SELECT r.* FROM
(
select 
tbl_inbox.`i_id`,
tbl_inbox.`i_letter_link`,
CASE WHEN (SELECT tbl_secretrait_letters.sl_secretariat_no FROM tbl_secretrait_letters WHERE sl_letter_link=i_letter_link LIMIT 1) IS NULL THEN 'امضا نشده'
ELSE (SELECT tbl_secretrait_letters.sl_secretariat_no FROM tbl_secretrait_letters WHERE sl_letter_link=i_letter_link LIMIT 1)
END AS sec,
`tbl_letters`.`l_date_of_create`,
`tbl_letters`.`l_date_of_letter`,
`tbl_inbox`.`i_date_of_create`,
CASE WHEN `tbl_inbox`.`i_date_of_seen` IS NULL THEN '' ELSE `tbl_inbox`.`i_date_of_seen` END AS i_date_of_seen, 
(SELECT u_complete_name FROM tbl_users WHERE u_id=l_created_user ) AS creator_user,
(SELECT u_complete_name FROM tbl_users WHERE u_id=i_prev_active_user_link ) AS latest_user,
(SELECT u_complete_name FROM tbl_users WHERE u_id=i_active_user_link ) AS _current_user,
`tbl_inbox`.`i_order`,
`tbl_inbox`.`i_position`,
tbl_letters.l_subject


FROM
    `automation`.`tbl_inbox`
    INNER JOIN `automation`.`tbl_letters` 
        ON (`tbl_inbox`.`i_letter_link` = `tbl_letters`.`l_id`)
WHERE (i_active_user_link='{0}')  and
(i_letter_link NOT IN (SELECT i_letter_link FROM tbl_inbox WHERE i_active_user_link IN( 43156 )))

        and ( {1}
        order by i_id desc
        LIMIT 51) r
        GROUP BY r.i_letter_link ORDER BY  i_position ASC,i_id DESC limit 50
""".format(py_db.user_id,sds)
partstr=""
partstr="""(i_active_user_link='{0}')  and""".format(py_db.user_id)
if baygani==1:
    sqlstr=sqlstr.replace(partstr,"(i_prev_active_user_link='{0}')  and".format(py_db.user_id))
#print sqlstr
db = py_db.GetDB();
cur=db.cursor()
cur.execute(sqlstr)
rows=cur.fetchall()
str=""
for row in rows:
    str=str+"|"
    daa=""
    if row[6].__str__()=="":daa="مشاهده نشده"
    else: daa=py_db.mil_to_sh_with_time(row[6].__str__())
    str=str+row[11].__str__()+"$"+row[1].__str__()+"$"+row[2].__str__()+"$"+py_db.mil_to_sh_with_time(row[3].__str__())+"$"+py_db.mil_to_sh_with_time(row[5].__str__())+"$"+daa+"$"+row[7].__str__()+"$"+row[8].__str__()+"$"+row[9].__str__()+"$"+row[11].__str__()+"$"+row[10].__str__()+"$"+row[12].__str__()
    
    
db.close()
    
str=str.replace("00:00:00","");

print str


