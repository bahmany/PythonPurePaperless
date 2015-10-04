#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db
cgitb.enable()


print 'Content-Type: text/html; charset=utf-8'
print ''


py_db.checkAccessCookie()
py_db.checkuser("2",py_db.username)


db = py_db.GetDB()
form = cgi.FieldStorage()
dt=form.getvalue("id")
dta=form.getvalue("tpy","xcc")
cur = db.cursor()
sqlstr = """
SELECT l_id,
(SELECT dsc_name FROM tbl_variables WHERE dsc_id = l_creator_company_link),
(SELECT dsc_name FROM tbl_variables WHERE dsc_id = l_creator_person_link),
l_type_link,
l_letter_to_link,
(SELECT dsc_name FROM tbl_variables WHERE dsc_id = l_type_of_recieve_link),
l_date_of_create,
l_attachment_count,
l_letter_number,
l_date_of_letter,
l_letter_text,
(select u_name from tbl_users where u_id = l_created_user),
l_subject,
(select i_position from tbl_inbox where (i_letter_link = l_id) and (i_active_user_link = {0}) order by l_id desc limit 1) as i_pos
FROM tbl_letters
 where l_id={1}""".format(py_db.user_id,dt)
#print sqlstr
cur.execute( sqlstr)
rows = cur.fetchall()
r=""
for row in rows:
    #print row
    r=str(row[0])+"|"+str(row[1])+"|"+str(row[2])+"|"+str(row[3])+"|"+str(row[4])+"|"+str(row[5])+"|"+str(row[6])+"|"+str(row[7])+"|"+str(row[8])+"|"+str(row[9])+"|"+str(row[10])+"|"+str(row[11])+"|"+str(row[12])+"|"+str(row[13])
db.close()

db2=py_db.GetDB()
cur2=db2.cursor()
cur2.execute("select * from tbl_secretrait_letters where sl_letter_link="+dt)
f="no"
rows = cur2.fetchall()
if len(rows)!=0:
    for row in rows:
        f=row[1]
       


db3=py_db.GetDB()
cur3=db3.cursor()
cur3.execute("select * from tbl_letters_papers where lp_link_to_letters="+dt)
rows = cur3.fetchall()
db3.close();
strr = ""
for row in rows:
    strr=strr+"?"+str(row[0])+":"+str(row[4]).split("_")[1]+":"+row[4]


print r+"|"+f+"|"+strr




## when user enters to letter the letter must change to read
#
sqls ='''
UPDATE `automation`.`tbl_inbox`
SET 
  `i_position` = '2',
  `i_date_of_seen` = '{2}'
WHERE
i_letter_link = {0} and
i_position='1' and
i_active_user_link={1}

'''.format(
           dt,
           py_db.user_id,
           py_db.get_datetime_of_now()
           
           );
#print sqls
py_db.executesql(sqls)



if dta<>"xcc":
    print "hey"




