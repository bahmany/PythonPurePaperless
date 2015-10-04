#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import MySQLdb
from classes import py_db
import Cookie
import os
import cgi
import sys
import cgitb
import codecs
import datetime


cgitb.enable()


form = cgi.FieldStorage()

print 'Content-Type: text/html; charset=utf-8'
print ''
 




def generate_ul():
    def is_key_ext_in_ar(array,key):
	for ar in array:
	    if ar == key : return True
	return False
    
    def get_child(parent_id,level=1):
	rows = py_db.executeAndReturnRows("select * from tbl_irib_book where ib_parent = {0}".format(parent_id))
	if len(rows)>0:
	    print "<ul>"
	    for row in rows:
		print "<li id='li_{1}'>{0}</li>".format(row[1],row[0])
		get_child(row[0],level+1)
	    print "</ul>" 

    rows = py_db.executeAndReturnRows("select * from tbl_irib_book ORDER BY ib_parent")
    if len(rows)>0:
	print "<ul>"
	for row in rows:
	    print "<li id='li_{1}'>{0}</li>".format(row[1],row[0])
	    get_child(row[0])
	    print "</ul>"
	    return
	
	

def get_content_from_id(id):
    print py_db.executeAndReturnRows("select ib_name from tbl_irib_book where ib_id = {0}".format(id))[0][0]

	    


def insertdt(inds,isd):
    py_db.executesql("insert into tbl_irib_book (ib_name,ib_parent) values ('{0}','{1}')".format(inds,isd));
    print py_db.executeAndReturnRows("select ib_id from tbl_irib_book order by ib_id desc limit 1")[0][0]



def del_dt(_del_ins_dt_sel):
    py_db.executesql("delete from tbl_irib_book where ib_id = '{0}'".format(_del_ins_dt_sel))
    print 'thisok';

def edit_content(_id,txt):
    py_db.executesql("update tbl_irib_book set ib_name = '{0}' where ib_id = {1}".format(txt,_id))
    print 'ok';
    
def add_meh_to_book(sel_meh,sel_book):
    if sel_book=="-1": return
    py_db.executesql("insert into tbl_irib_book (ib_name,ib_parent) value ((select _text from mehvarz where id={0} limit 1),{1})".format(str(sel_meh),str(sel_book)))
    print py_db.executeAndReturnRows("select ib_id from tbl_irib_book where ib_parent="+str(sel_book)+" order by ib_id desc limit 1")[0][0].__str__()+"__"+py_db.executeAndReturnRows("select _text from mehvarz where id = "+str(sel_meh))[0][0]



ins_dt = form.getvalue("ins_dt","-1")
ins_dt_sel = form.getvalue("ins_dt_sel","-1")
del_ins_dt_sel = form.getvalue("del_ins_dt_sel","-1")
get_ulli = form.getvalue("get_ulli","-1")
edit_ins_dt = form.getvalue("edit_ins_dt","-1")
edit_ins_dt_sel = form.getvalue("edit_ins_dt_sel","-1")
content_from_id = form.getvalue("g_c_id","-1")
id_of_edi = form.getvalue("id_of_edit","-1")
txt_of_edited = form.getvalue("new_txt","-1")
sel_meh = form.getvalue("sel_meh","-1")
sel_book = form.getvalue("sel_book","-1") 


if ins_dt!="-1": insertdt(ins_dt,ins_dt_sel)
if get_ulli!="-1": generate_ul()
if del_ins_dt_sel != "-1":  del_dt(del_ins_dt_sel)
if content_from_id != "-1": get_content_from_id ( content_from_id  )
if id_of_edi != "-1": edit_content( id_of_edi , txt_of_edited )
if sel_meh != "-1": add_meh_to_book(sel_meh,sel_book)


