#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
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



cgitb.enable(display=0, logdir="c:\cgilog.txt")



# [0] = input value retrieved from tag and cgi posts
# [1] = html input id code from tbl_forms_items
#[ retrieved record 
def do_insert(request):
    insert_str = ""
    before_value = ""
    after_value = ""
    sql="select f_table_name from tbl_forms where f_id=(select fi_link_to_form_name from tbl_form_items where fi_id='{0}' limit 1)".format(request[0][0])
    table_name = py_db.executeAndReturnRows(sql)[0][0]
    #print request
    for item in request:
        #print item.__str__()+"<br>"
        #['1', '1', (1L, u'\u0646\u0627\u0645', 1, None, None, None, 1, 0, None, None, 1L, 1L, None, None, None, u'soccc_name')]
        if before_value == "":before_value ="{0}".format(item[2][15])
        else: before_value +=",{0}".format(item[2][15])
        if after_value == "":after_value ="'{0}'".format(item[1])
        else: after_value +=",'{0}'".format(item[1])
        
    sql="insert into {0} ({1}) values ({2})".format(table_name,before_value,after_value)
    py_db.executesql(sql)
    return sql


def do_update(request,keyfieldID):
    update_str = ""
    sql="select f_table_name,f_key_field from tbl_forms where f_id=(select fi_link_to_form_name from tbl_form_items where fi_id='{0}' limit 1)".format(request[0][0])
    
    tt = py_db.executeAndReturnRows(sql)
    table_name = tt[0][0]
    ketfield_name = tt[0][1]
    
    for item in request:
        if update_str == "":update_str ="{0}='{1}'".format(item[2][15],item[1])
        else: update_str +=",{0}='{1}'".format(item[2][15],item[1])
        
    sql="update {0} set {1} where {2}".format(table_name,update_str,ketfield_name+"='{0}'".format(keyfieldID[0]))
    #print sql
    
    sql=sql.replace("'empty'",'(NULL)')
    py_db.executesql(sql)


































form = cgi.FieldStorage()

 
 
 
 
print 'Content-Type: text/html; charset=utf-8'
print ''




# start getting hashed validation mapping .
hashed_ordinaries = form.getvalue("hv")
fff_key =  form.getvalue("fff_key","-1")

hashed=""
_hashed=""

OOO = hashed_ordinaries.split("::")
for _ord in OOO:
    if _ord <> "" and _ord.isdigit():
        hashed+= chr(int(_ord))
unhashed = py_db.decode(hashed)
objs_array = unhashed.split("::")
keyfieldID=""
if fff_key!="-1":
    _OOO = fff_key.split("::")
    for __ord in _OOO:
        if __ord <> "" and __ord.isdigit():
            _hashed+= chr(int(__ord))
    _unhashed = py_db.decode(_hashed)
    keyfieldID = _unhashed.split("::")




#getting form data from db
#print objs_array
hs=py_db.executeAndReturnRows("select * from tbl_form_items where fi_link_to_form_name = (select fi_link_to_form_name from tbl_form_items where fi_id={0}) order by fi_order".format(objs_array[1].split("##")[1]))
# converting hashed mapping to array
http_inputs = []
for ob in objs_array:
    if ob!="":
        ps=[]
        ps.append(ob.split("##")[0])
        ps.append(ob.split("##")[1])
        http_inputs.append(ps)

items=[]
# here we are going to make final array which contains mapped field and webform 

for row in hs:
    item=[]
    for i in http_inputs :
        if i[1].__str__() == row[0].__str__():
            item.append(i[1])
            item.append(form.getvalue(i[0],"empty"))
        else:
            if row[2]==8:
                    item.append(i[1])
                    item.append(py_login.get_socc_id())
            else:
                if row[2]==7:
                        item.append(i[1])
                        item.append(py_login.get_user_id())
                    
    item.append(row)
    
    items.append(item)
# print items
# all mapping with fields stored in array
# now it is time to serverside validation
# [0] = input value retrieved from tag and cgi posts
# [1] = html input id code from tbl_forms_items
#items = [['1', '1', (1L, u'\u0646\u0627\u0645', 1, None, None, None, 1, 0, None, None, 1L, 1L, None, None, None, u'soccc_name')], ['2', '1', (2L, u'\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc', 1, None, None, None, 1, 1, u' ', None, 1L, 2L, None, 9L, None, u'soccc_family')], ['3', '1311/11/11', (3L, u'\u062a\u0627\u0631\u06cc\u062e \u062a\u0648\u0644\u062f', 6, u'hhhhh', None, None, 1, 1, u' ', None, 1L, 3L, None, None, None, u'soccc_birthdate')], ['4', '1321464654', (4L, u'\u06a9\u062f \u0645\u0644\u06cc', 1, None, u'9999999999', None, 1, 1, u' ', None, 1L, 4L, None, 10L, None, u'soccc_id_code')], ['5', '6546549656', (5L, u'\u06a9\u062f \u067e\u0633\u062a\u06cc', 1, None, u'9999999999', None, 1, 1, u'', u'', 1L, 5L, u'checked', 10L, None, u'soccc_post_code')], ['6', '1', (6L, u'\u0646\u0648\u0639 \u0634\u062e\u0635', 1, None, u'9', None, 1, 1, u'1:::50', u'', 1L, 6L, u'checked', None, u'1= \u0645\u062f\u06cc\u0631    2=\u067e\u0631\u0633\u0646\u0644 \u0648 \u0622\u0645\u0648\u0632\u06af\u0627\u0631\u0627\u0646     3= \u062f\u0627\u0646\u0634 \u0622\u0645\u0648\u0632\u0627\u0646', u'soccc_position')]]
is_validation_ok = True
validation_message = ""


for field in items:
    # NULL checking
    # Valid Number Checking
    # Valid Length Checking
    # Valid DateTime Checking
    
    #----------Null Checking---------------------
    if field[2][6]==1:
        if field[1]=="empty" or field[1]=="" or field[1] == None:
            is_validation_ok=False;
            validation_message="لطفا اطلاعات خواسته شده را خالی رها نکنید"+"\n"
            validation_message+=field[1]+field[2][1]
            print "1"
    #--------Valid Number Checking------------
    
    if field[2][2]==2:
        if field[1]=="empty" or field[1]=="" or field[1] == None:
            pass
        else:
            if field[1].isdigit() == False:
                is_validation_ok=False;
                validation_message="لطفا اطلاعات خواسته شده بصورت عدد را صحیح وارد نمایید"+"\n"
                validation_message+=field[1]+field[2][1]
            
    #---------Validating Length-----------------
    if field[2][13]<>None:
        if len(field[1])!=field[2][13] :
            is_validation_ok=False;
            validation_message="طول اطلاعات وارد شده بیش از طول مد نظر است لطفا اصلاح نمایید"+"\n"
            validation_message+=field[1]+field[2][1]
            #print "1"
    #--------Datetime Validating---------------
    if field[2][2]==6:
        if py_db.is_valid_shamsi_date(field[1])==False:
            is_validation_ok=False
            validation_message="تاریخ وارد شده را اصلاح نمایید"+"\n"
            validation_message+=field[1]+field[2][1]
            #print "1"
        else:
            field[1] = py_db.sh_to_mil(field[1])
            #print "1"

#----------------------------------------------------------------------------------
    
    
#---------------------- Generating SQL Script -----------------------------------------------


print is_validation_ok
print validation_message
if is_validation_ok:
    if fff_key=="-1":
        do_insert(items)
    else:
        do_update(items,keyfieldID)
            

    
    






