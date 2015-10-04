#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import py_db
from date_utils import calendar_util
from datetime import datetime
import Cookie
import os
from pyDes import *
import cgi
import sys
import cgitb
import re
import codecs
from urllib import unquote
import datetime
import HTMLParser
#from docx import Document
#from docx.shared import Inches

cgitb.enable(display=0, logdir="c:\cgilog.txt")


print 'Content-Type: text/html; charset=utf-8'
print ''



def create_docx():
    rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats order by io_id")
    str = ""
    for row in rows:
        str = str+"<tr class='tr__1'><td colspan=3>{1}</td></tr>".format(row[0],row[1])
        _rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo where iom_link = '{0}' order by iom_id".format(row[0]))
        for _row in _rows:
            str = str+"<tr class='tr__2'><td>{0}</td><td colspan=2>{1}</td></tr>".format(_row[0],_row[1])
            __rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo_mehvarz where iomm_link = '{0}' order by iomm_id".format(_row[0]))
            for __row in __rows:
                str = str+"<tr class='tr__3'><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(_row[0],__row[0],__row[1])
    str = "<table class='tbl_report'><tbody>{0}</tbody></table>".format(str)
    print str

            
        
print create_docx()
