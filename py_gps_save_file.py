#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import cgi
import os,sys
import py_db
import cgitb
import time
import datetime

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
    
        

def capture_gps_to_db(uid,filecontent):
    str_arr = []
    sqlins =""
    bhr=[]
    str_arr = filecontent.split("$")
    total_date = '1998-01-01'
    speed="0"
    _tpe="0"
    x="0"
    y="0"
    z="0"
    sat_count="0"
    ic=0
    
    for i in str_arr:
        ic=ic+1
        ss=[]
        #pp=[]
        ss=i.split(",")
        if ss[0] == "GPGGA":
            _tpe = "1"
            timestamp = ss[1]
            sat_count = ss[7]
            x=conver_decimal_min_to_decimal_degree(float(find_pos(ss,"E")))
            y=conver_decimal_min_to_decimal_degree(float(find_pos(ss,"N")))
            z=float(find_pos(ss,"M"))
    
        if ss[0] == "GPRMC":
            _tpe = "2"
            timestamp = convert_timestamp(ss[1])
            validity = ss[2]
            x=conver_decimal_min_to_decimal_degree(float(find_pos(ss,"E")))
            y=conver_decimal_min_to_decimal_degree(float(find_pos(ss,"N")))
            speed=float(ss[7])
            true_course=ss[8]
            datestamp =convert_datestamp(ss[9])
            eastwest=ss[10]
            total_date = convert_stamped_to_datetime(datestamp,timestamp)
        prmmm = """insert into tbl_gps_positions (g_type,g_x,g_y,g_z,g_sat_count,g_date,g_speed,g_user_id,g_date_post,g_uploaded_user_id)  values  ('{0}','{1}','{2}','{3}','{4}',ADDTIME('{5}','3:30:00'),'{6}','{7}','{8}','{9}');""".format(_tpe,x,y,z,sat_count,total_date,speed,uid,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"-1")
        sqlins = prmmm
        py_db.executesql(sqlins)
        print "|"
    
    
    return  len(str_arr)
        #print sqlins
        #bhr.append(pp)

def beriz_too_dbclass(uid,str):
    cnt = capture_gps_to_db(uid,str)




def myfunction (form):
    uid = form.getvalue("uid")
    negahbanID= form.getvalue("sometext")
    gpstexts = form.getvalue("TextArea1")
    print 'Content-Type: text/html; charset=utf-8'
    print ""
    beriz_too_dbclass(negahbanID,gpstexts)
    print "<a href="">بازگشت</a>   <script type='text/javascript'>  document.location.href = 'py_main.py?mid=15' </script>"






def run():
    cgitb.enable()
    form = cgi.FieldStorage()
    myfunction(form) 





run()





