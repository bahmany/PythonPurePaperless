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

cgitb.enable();

def get_company_names():
    rows = py_db.executeAndReturnRows("SELECT `scn_name` FROM `tbl_sale_company_names` ORDER BY SCN_NAME DESC");
    s=''
    for row in rows:
       s=s+'jotl'+row.__str__()
    print "Content-Type: text/html"
    print
    print s


def chk_n(str):  #check null
    if str=='':
        return null
    else:
        return str


def do_insert(_param):
    print "Content-Type: text/html"
    print
    sqlstr=''
    main_rows = _param.split("[[[a")
    data_field = main_rows[0].split("91A1")
    sqlstr="'{0}','{1}','{2}','{3}'".format(chk_n(data_field[0]),chk_n(data_field[1]),chk_n(data_field[2]),chk_n(data_field[3])) 
    
    fs = """
    INSERT INTO `automation`.`tbl_sale_kharidha`
            (`sk_link_to_company`,
             `sk_namayande_sherkat`,
             `sk_link_faaliat`,
             `sk_tel_no`)
    VALUES (
        {0}); 
        
    """ .format(sqlstr)
    
    
    py_db.executesql(fs)
    new_id = py_db.executeAndReturnRows("select sk_id from tbl_sale_kharidha  order by sk_id desc limit 1")[0][0].__str__()
    
    
    sqlstr_details = ' DELIMITER ; ';
    if main_rows[1]=='':
        print "no_item"
        return
    for row in main_rows[1].split("al12c"):
        row_arr = row.split(",")
        py_db.executesql("""
                         insert into `automation`.`tbl_sale_kharidha_details`
            (
             `skd_link_to_kharid_ha`,
             `skd_zekhamate_varagh`,
             `skd_arz`,
             `skd_tool`,
             `skd_mizan`,
             `skd_zekhamte_ghal`,
             `skd_shekle_varagh`,
             skd_date_kharid)
values (
        '{0}',
        '{1}',
        '{2}',
        '{3}',
        '{4}',
        '{5}',
        '{6}',
        '{7}');
        """.format(new_id,
                   chk_n(row_arr[0]),
                   chk_n(row_arr[1]),
                   chk_n(row_arr[2]),
                   chk_n(row_arr[3]),
                   chk_n(row_arr[4]),
                   chk_n(row_arr[5]),
                   chk_n(row_arr[6])))
        #al12c
    
    print "ok"



def create_excel():
    from tempfile import TemporaryFile
    from xlwt import Workbook
    from xlwt import *
    book = Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    book.add_sheet('Sheet 2')
    sheet1.write(0,0,'نام شرکت')
    sheet1.write(0,1,'تاریخ خرید')
    sheet1.write(0,2,'ضخامت')
    sheet1.write(0,3,'عرض')
    sheet1.write(0,4,'طول')
    sheet1.write(0,5,'میزان کیلوگرم')
    sheet1.write(0,6,'ضخامت قلع')
    sheet1.write(0,7,'شکل ورق')
    
    rows = py_db.executeAndReturnRows("""



SELECT 
(SELECT `sk_link_to_company` FROM `tbl_sale_kharidha` WHERE `sk_id`=`skd_link_to_kharid_ha`) AS kha,
`skd_date_kharid`,
`skd_zekhamate_varagh`,
`skd_arz`,
`skd_tool`,
`skd_mizan`,
`skd_zekhamte_ghal`,
`skd_shekle_varagh`

 FROM `tbl_sale_kharidha_details`
 ORDER BY kha, skd_date_kharid

                                      
                                      """)
    
    i=1
    for row in rows:
        row1 = sheet1.row(i)
        row1.write(0,row[0].__str__())
        row1.write(1,row[1].__str__())
        row1.write(2,Formula("VALUE("+row[2].__str__()+")"))
        row1.write(3,Formula("VALUE("+row[3].__str__()+")"))
        row1.write(4,Formula("VALUE("+row[4].__str__()+")"))
        row1.write(5,Formula("VALUE("+row[5].__str__()+")"))
        row1.write(6,Formula("VALUE("+row[6].__str__()+")"))
        row1.write(7,Formula("VALUE("+row[7].__str__()+")"))
        
        i+=1
        
    sheet1.col(0).width = 10000
    sheet2 = book.get_sheet(1)
    sheet2.row(0).write(0,'Sheet 2 A1')
    sheet2.row(0).write(1,'Sheet 2 B1')
    sheet2.flush_row_data()
    sheet2.write(1,0,'Sheet 2 A3')
    sheet2.col(0).width = 5000
    sheet2.col(0).hidden = True
    book.save('simple.xls')
    book.save(TemporaryFile())
    print "Content-Type: text/html"
    print
    print "ok"
        








form = cgi.FieldStorage()
param = form.getvalue("get_co_names","-1")
param2= form.getvalue("req_str","-1")
param3= form.getvalue("req_getfile","-1")



if param  != "-1" : get_company_names()
if param2 != "-1" : do_insert(param2)
if param3 != "-1" : create_excel()



    

 
