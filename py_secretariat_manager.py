#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import MySQLdb
import py_db
import date_utils.calendar_util
import datetime
import cgi
import sys
import cgitb

cgitb.enable()

print 'Content-Type: text/html; charset=utf-8'
print ''

form = cgi.FieldStorage()

letter_id=form.getvalue("id")
_type=form.getvalue("_type")


str = ""
lastid=0;
s_id = "-1"


db1=py_db.GetDB()
cur1=db1.cursor()
cur1.execute("select * from tbl_secretariat where s_group="+py_db.u_secretriat_group_id.__str__()+" and s_type="+_type.__str__())
###cur1.execute("select * from tbl_secretariat where s_group= 1 and s_type=2")
rows = cur1.fetchall()

for row in rows:
    str=row[1]
    lastid=row[2]
    s_id=row[0].__str__()
db1.close()


dd = str.split(".")

stt=""
sttt = datetime.date.today().strftime("%Y-%m-%d")
dddd = sttt.split("-")
m= date_utils.calendar_util.jd_to_persian(
    date_utils.calendar_util.gregorian_to_jd(int(dddd[0]),
                                             int(dddd[1]),
                                             int(dddd[2])))

m0=m[0].__str__()
m1=m[1].__str__()
m2=m[2].__str__()
if len(m1)==1:m1="0"+m1
if len(m2)==1:m2="0"+m2


for d in dd:
    #stt=stt+" "
    if d=="yyyy":stt=stt+m0[0:4]
    elif d=="yyy":stt=stt+m0[1:4]
    elif d=="yy":stt=stt+m0[2:4]
    elif d=="y":stt=stt+m0[3:4]
    elif d=="mm":stt=stt+m1[0:2] 
    elif d=="m":stt=stt+m1[1:2]
    elif d=="dd":stt=stt+m2[0:2] 
    elif d=="d":stt=stt+m2[1:2]
    elif d[0:1]=="x":
        #d=d.replace("x","0")
        #stt=stt+d
        lastid=lastid+1
        db = py_db.GetDB()
        cur = db.cursor()
        cur.execute("update tbl_secretariat set s_autonum_last= "+(lastid).__str__()+
                    " where s_id="+s_id)
        db.commit()
        db.close()
        stt=stt+lastid.__str__()
    else:
        stt=stt+d
        
db3=py_db.GetDB()
cur2 = db3.cursor()
py_db.checkAccessCookie()
sqlstr="insert into tbl_secretrait_letters (sl_secretariat_no,sl_letter_link,sl_secretariat_link,sl_date,sl_user_id) values ('{0}',{1},{2},'{3}','{4}')".format(stt,letter_id,s_id,datetime.date.today().strftime("%Y-%m-%d"),py_db.user_id)

#print sqlstr
cur2.execute(sqlstr)
db3.commit()
db3.close()
    

print stt




