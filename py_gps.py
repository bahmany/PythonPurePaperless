#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import os
import time
import datetime
import Cookie
import cgi
import py_db


def convert_timestamp(timestamp):
    return timestamp[0:2]+":"+timestamp[2:4]+":"+timestamp[4:6]

def convert_datestamp(datestamp):
    return "20"+datestamp[4:6]+"-"+datestamp[2:4]+"-"+datestamp[0:2]

def convert_stamped_to_datetime(_date,_time):
    tm = time.strptime(_date+" "+_time,"%Y-%m-%d %H:%M:%S")
    tms = tm.tm_year.__str__()+"-"+tm.tm_mon.__str__()+"-"+tm.tm_mday.__str__()+" "+ tm.tm_hour.__str__()+":"+tm.tm_min.__str__()+":"+tm.tm_sec.__str__()
    return tms



def conver_decimal_min_to_decimal_degree(position):
    po = position.__str__()
    decimal_hour = po[0:2]
    decimal_min  = po[2:len(po)]
    return float(decimal_hour)+(float(decimal_min)/60)

def find_pos(position_line_array,E_or_N):
    i=0
    f_i=0
    for b in position_line_array:
        if b==E_or_N:
            f_i=position_line_array[i-1]
            return f_i
        i+=1
    
        
    

        
def get_positions_count(userids):
    dtt = form.getvalue("dt","-1");
    dttt = []
    dttt = dtt.split("mm")
    dtt = "between '"+py_db.sh_to_mil(dttt[0])+" "+dttt[1]+":00' and '"+py_db.sh_to_mil(dttt[2])+" "+dttt[3]+":00' "
    sqlst = "select count(*)  from `tbl_gps_positions` WHERE  g_sat_count  > 5 and  g_user_id in ({1})  and g_date {0} ".format(dtt,userids)
    print 'Content-Type: text/html; charset=utf-8'
    print ""
    print py_db.executeAndReturnRows(sqlst)[0][0].__str__()

    
def get_pos(sel2):
    dtt = form.getvalue("dt2","-1");
    ttl = form.getvalue("totalrows","-1")
    dttt = []
    dttt = dtt.split("mm")
    dtt = "between '"+py_db.sh_to_mil(dttt[0])+" "+dttt[1]+":00' and '"+py_db.sh_to_mil(dttt[2])+" "+dttt[3]+":00' "
  
    sqlst ="""SELECT w.* FROM (SELECT @row := @row + 1 AS _ROW, t.* FROM `tbl_gps_positions` t,(SELECT @row:=0) r WHERE g_sat_count  > 5 and  g_user_id IN ({0})  AND g_date {1} ORDER BY g_date DESC ) w WHERE MOD(_ROW,{2})=0  """.format(sel2,dtt,ttl)
    rows = py_db.executeAndReturnRows(sqlst)
    str = ""
    i=0
    for row in rows :
        if i==0:
            str = "{0}!{1}!{2}!{3}!{4}".format(row[2].__str__(),row[3].__str__(),row[4].__str__(), py_db.mil_to_sh_with_time(row[6].__str__()),row[7].__str__())
        else:
            str = str+"cz{0}!{1}!{2}!{3}!{4}".format(row[2].__str__(),row[3].__str__(),row[4].__str__(),py_db.mil_to_sh_with_time(row[6].__str__()),row[7].__str__())
        i+=1
    print 'Content-Type: text/html; charset=utf-8'
    print ""
    print str
    
    
    
    



form = cgi.FieldStorage()
param = form.getvalue("sel","-1")
param2 = form.getvalue("sel2","-1")


if param != "-1": get_positions_count(param)
if param2 != "-1": get_pos(param2)
        
        

 

