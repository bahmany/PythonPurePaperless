#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import os
import time
import datetime
import Cookie
import cgi
import py_db



print 'Content-Type: text/html; charset=utf-8'
print ""

    
    







def insert(str):
    _str = str.split("__")
    uid = -1
    if _str[12].split("ffdd")[1] == "private":
        uid = py_db.user_id
        
    
    sqlstr = """
    INSERT INTO `automation`.`tbl_tels`
            (
             `t_sazman`,
             `t_name`,
             `t_semat`,
             `t_mozoo`,
             `t_tel`,
             `t_fax`,
             `t_mob`,
             `t_email`,
             `t_site`,
             `t_address`,
             `t_exp`,
             t_private_user_id)
             
VALUES (
        '{0}',
        '{1}',
        '{2}',
        '{3}',
        '{4}',
        '{5}',
        '{6}',
        '{7}',
        '{8}',
        '{9}',
        '{10}',
        '{11}'
        
        );
    
    """.format(_str[1].split("ffdd")[1],
               _str[2].split("ffdd")[1],
               _str[3].split("ffdd")[1],
               _str[4].split("ffdd")[1],
               _str[5].split("ffdd")[1],
               _str[6].split("ffdd")[1],
               _str[7].split("ffdd")[1],
               _str[8].split("ffdd")[1],
               _str[9].split("ffdd")[1],
               _str[10].split("ffdd")[1],
               _str[11].split("ffdd")[1],
               uid,
               
               
               )
   # print sqlstr
    
    py_db.executesql(sqlstr)
    ss = "select t_id from tbl_tels where t_sazman = '{0}' order by t_id desc limit 1".format(_str[1].split("ffdd")[1])
    print "ok__"+py_db.executeAndReturnRows(ss)[0][0].__str__()


#insert("	__tnnnn1ffddنام سازمان__tnnnn2ffddنام شخص__tnnnn3ffddسمت__tnnnn4ffddموضوع فعالیت__tnnnn5ffddتلفن ثابت__tnnnn6ffddفاکس__tnnnn7ffddهمراه__tnnnn8ffddایمیل__tnnnn9ffddسایت__tnnnn10ffddآدرس__tnnnn11ffddتوضیحات")
#insert("__tnnnn1ffdd1__tnnnn2ffdd2__tnnnn3ffdd3__tnnnn4ffdd4__tnnnn5ffdd5__tnnnn6ffdd6__tnnnn7ffdd7__tnnnn8ffdd8__tnnnn9ffdd9__tnnnn10ffdd10__tnnnn11ffdd11")


def send_table_data():
    rows = py_db.executeAndReturnRows("select * from tbl_tels where (t_private_user_id = '{0}' or t_private_user_id = '-1')  order by t_sazman,t_name".format(py_db.user_id))
    tbl_str = ''
    for row in rows:
        if tbl_str == '':
            tbl_str = '{0},,,{1},,,{2},,,{3},,,{4},,,{5},,,{6},,,{7},,,{8},,,{9},,,{10},,,{11},,,{12}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],)
        else: tbl_str = tbl_str+"li_"+'{0},,,{1},,,{2},,,{3},,,{4},,,{5},,,{6},,,{7},,,{8},,,{9},,,{10},,,{11},,,{12}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],)
    tbl_str = tbl_str.replace("None","")
    print tbl_str    



def send_tr(_id):
    rows = py_db.executeAndReturnRows("select * from tbl_tels where t_id='{0}' and (t_private_user_id = '{1}' or t_private_user_id = '-1') ".format(_id,py_db.user_id))
    tbl_str = ''
    for row in rows:
        if tbl_str == '':
            tbl_str = '{0},,,{1},,,{2},,,{3},,,{4},,,{5},,,{6},,,{7},,,{8},,,{9},,,{10},,,{11},,,{12}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],)
        else: tbl_str = tbl_str+"li_"+'{0},,,{1},,,{2},,,{3},,,{4},,,{5},,,{6},,,{7},,,{8},,,{9},,,{10},,,{11},,,{12}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],)
    tbl_str = tbl_str.replace("None","")
    print tbl_str    




    

def edit_data(_id,line):
    _str = line.split("__")
    uid = -1
    if _str[12].split("ffdd")[1] == "private":
        uid = py_db.user_id
        
    
    sqlstr = """
    update `automation`.`tbl_tels`
            set
             `t_sazman`='{0}',
             `t_name`='{1}',
             `t_semat`='{2}',
             `t_mozoo`='{3}',
             `t_tel`='{4}',
             `t_fax`='{5}',
             `t_mob`='{6}',
             `t_email`='{7}',
             `t_site`='{8}',
             `t_address`='{9}',
             `t_exp`='{10}',
             `t_private_user_id`='{12}'

             where t_id = '{11}'
             

    
    """.format(_str[1].split("ffdd")[1],
               _str[2].split("ffdd")[1],
               _str[3].split("ffdd")[1],
               _str[4].split("ffdd")[1],
               _str[5].split("ffdd")[1],
               _str[6].split("ffdd")[1],
               _str[7].split("ffdd")[1],
               _str[8].split("ffdd")[1],
               _str[9].split("ffdd")[1],
               _str[10].split("ffdd")[1],
               _str[11].split("ffdd")[1],
               _id,
               uid,
               )
    py_db.executesql(sqlstr)
    _str = send_tr(_id)
    print _str

    
#send_table_data()
#edit_data("29","	__tnnnn1ffddنام سازمان__tnnnn2ffddنام شخص__tnnnn3ffddسمت__tnnnn4ffddموضوع فعالیت__tnnnn5ffddتلفن ثابت__tnnnn6ffddفاکس__tnnnn7ffddهمراه__tnnnn8ffddایمیل__tnnnn9ffddسایت__tnnnn10ffddآدرس__tnnnn11ffddتوضیحات")


def delrow(_id):
    py_db.executesql("delete from tbl_tels where t_id='{0}'".format(_id))
    print _id


def update_prv_pub(vv):
    ss = vv.split("ftr")
    uu="-1"
    if ss[1]=='true':
        uu = py_db.user_id
    py_db.executesql("update tbl_tels set t_private_user_id = '{0}' where t_id={1}".format(uu,ss[0]))
    print "ok"

 


py_db.checkAccessCookie()



form = cgi.FieldStorage()
param = form.getvalue("insert","-1")
param2=form.getvalue("ins_vals","-1")
param3=form.getvalue("getmetbl","-1")
param4=form.getvalue("rowID","-1")
param5=form.getvalue("edit","-1")
param6=form.getvalue("delids","-1")
param7=form.getvalue("prv_pub","-1")




if param != "-1": insert(param2)
if param3 != "-1": send_table_data()
if param4 != "-1": send_tr(param4)
if param5 != "-1": edit_data(param5,param2)
if param6 != "-1": delrow(param6)
if param7 != "-1": update_prv_pub(param7)

        
        

 

