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





form = cgi.FieldStorage()








    
def print_current_company_details ():
    row = py_db.executeAndReturnRows("select * from tbl_sell_seller")[0]
    str = "{0}ddr{1}ddr{2}ddr{3}ddr{4}ddr{5}ddr{6}ddr{7}ddr{8}ddr{9}ddr{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
    print str


def print_company_details(company_id):
    rows = py_db.executeAndReturnRows("SELECT * FROM tbl_sell_customers WHERE c_id = {0}".format(company_id))
    if len(rows) == 0:
        print "0"
    else :
        row = rows[0]
        str = "{0}^^{1}^^{2}^^{3}^^{4}^^{5}^^{6}^^{7}^^{8}^^{9}^^{10}^^{11}".format(row[0],row[1],row[2],row[3],row[4],
                                                                                row[5],row[6],row[7],row[8],row[9],
                                                                                row[10],row[11])
        print str
    
    



def get_lookup(title,tablename,display_field_name,return_value,destination_object):
    sql = "select {0},{1} from {2} order by {0}".format(return_value,display_field_name,tablename)
    sql = sql.replace('"','')

    rows = py_db.executeAndReturnRows(sql)
    str = ""
    str = "<table><tbody><tr><td colspan=3>{0}</td></tr><tr><td colspan=3> جستجو </td></tr>".format(title)
    for row in rows:
        str = str+"""<tr><td>{0}</td><td>{1}</td><td><a href='#' onclick='send_to_obj("{0}","{2}");'>انتخاب</a></td></tr>""".format(row[0],row[1],destination_object)
    str = str+"</tbody></table>"
    html = """


    
    """
    
    
    print str


#get_lookup("انتخاب نام نمیدانم","tbl_forms","f_name","f_id","textbox1")

















 
 
print 'Content-Type: text/html; charset=utf-8'
print ''
 


get_current_company_details =  form.getvalue("get_current_company_details","-1")
get_company_details =  form.getvalue("get_company_details","-1")
get_lookupitems = form.getvalue("loookup","-1")


if get_current_company_details!="-1": print_current_company_details()
if get_company_details!="-1": print_company_details(get_company_details)
if get_lookupitems != "-1":
    _title = form.getvalue("title")
    _tablename = form.getvalue("tablename")
    _display_field_name = form.getvalue("display_field_name",)
    _return_value = form.getvalue("return_value")
    _destination_object = form.getvalue("destination_object")
    get_lookup(_title,_tablename,_display_field_name,_return_value,_destination_object)
    
    
    
    

    
    
