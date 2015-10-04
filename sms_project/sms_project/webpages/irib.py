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
import py_login
cgitb.enable()


mehv = [['1','نهادینه سازی فرهنگ تمسک به قرآن و عترت (امام عصر (عج)) و تبیین، ترویج، تقویت و ساماندهی شعائر الهی، نمادها و آیین های اسلامی ایرانی؛','1010000'],
        ['2',' بازآفرینی نظام فکری، ساختارهای رسمی و غیررسمی و میراث تمدنی جامعه مبتنی بر جهان بینی و تعالیم اسلام ناب محمدی (ص)(آسیب شناسی مسائل " ساختار  سازمان، منابع انسانی ،آموزشی ، سیاستگذاری ، جهت گیری ها " و بازشناسی موارد مذکور با نگاه به سند چشم انداز 1404  و نقشه مهندسی کشور با هدف تحول)  ','1020000'],
        ['3','تبیین، تشکیل، تحکیم، تعالی و ایمن سازی خانواده','1030000'],
        ['4','اصلاح سیاست جمعیتی کشور و بازشناسی آن براساس آموزه های اسلامی ','1040000'],
        ['5','نهادینه سازی آداب و سبک زندگی اسلامی ایرانی در زمینه های فردی، خانوادگی و اجتماعی ','1050000'],
        ['6','انسجام بخشی و تقویت مشارکت فراگیر و نظام مند نهاد خانواده ، نظام تعلیم و تربیت ، نهادهای فرهنگی به منظورگسترش نظم و انضباط، قانون گرایی و احساس امنیت عمومی ','1060000'],
        ['7','تبیین، نهادینه سازی و ارتقاء اخلاق و رفتار بر اساس نظام حقوقی اسلام در حوزه های اجتماعی و سیاسی','1070000'],
        ['8','ترویج الگوی اسلامی اخلاق و فرهنگ کار و رفتار اقتصادی دولت و مردم در عرصه تولید، توزیع و مصرف','1080000'],
        ['9','تبیین، ترویج و نهادینه سازی هنر متعهد، تعالی بخش، شوق آفرین و استکبارستیز و تعمیق درک زیباشناسانه عمومی و بهره گیری از ظرفیت هنر در تعمیق فرهنگ اسلامی ایرانی و گفتمان انقلاب اسلامی مبتنی بر فرمایشات امام خمینی (ره) و مقام معظم رهبری (مدظله العالی)','1090000'],
        ['10','فرهنگ سازی نظام جامع و کارآمد اطلاعات، ارتباطات و رسانه ای مبتنی بر آموزه های دینی، انقلابی و ارزش های اخلاقی','1100000'],
        ['11','گسترش تاثیر گذاری و ارزش آفرینی فرهنگی جمهوری اسلامی ایران با تاکید بر معرفی دستاوردها و الگوهای موفق در سطح جهانی برای جهانی شدن گفتمان اسلام ناب محمدی (ص) در موضوعات و مسائل بشری و جهانی','1110000'],
        ['12','بازشناسی اهداف، کارکردها و ساختارهای نظام های فرهنگی، اجتماعی، سیاسی و اقتصادی مبتنی بر نقشه مهندسی فرهنگی برای انسجام و ارتقاء کارکرد فرهنگی آنها','1120000'],
        ['13','آگاهی بخشی و مشارکت مردمی در جبهه فرهنگی انقلاب اسلامی نسبت به جنگ نرم و ارتقاء مؤلفه های قدرت نرم نظام اسلامی.','1130000'],
        ['14','ارتقاء سطح بصیرت عمومی با افزایش سطح آگاهی های دینی و تاریخی در جامعه','1140000']]

channels = [
    ['ch1','شبکه اول'],
    ['ch2','شبکه دوم'],
    ['ch3','شبکه سوم'],
    ['ch4','شبکه چهار'],
    ['ch5','شبکه تهران'],
    ['ch7','شبکه آموزش'],
    ['ch8','شبکه قرآن'],
    ['ch_salama','شبکه سلامت'],
    ['ch_jam','شبکه جام جم'],
    ['ch_mostanad','شبکه مستند'],
    ['ch_pooya','شبکه پویا'],
    ['ch_namayesh','شبکه نمایش'],
    ['ch_tamasha','شبکه تماشا'],
    ['ch_varzesh','شبکه ورزش'],
    ['ch_shoma','شبکه شما'],
    ['ch_nasim','شبکه نسیم']]

asliii = "الویت  های اول"
FARII = "الویت  های دوم"

tbl = ""
RadeefeShabake = 0;
for ch in channels:
    RadeefeShabake=0
    #retrieving *
    tbl = tbl+"<table  class='tbl_irib'  cellpadding='0' cellspacing='0' ><tbody><tr class='tr_ch'><td colspan='3'>{0}</td><tr>".format(ch[1])
    for i in mehv:
        sql='select main_code,Onvan from sheet_anavin where {0}="*" and LinkToAhdaf ="{1}" order by main_code'.format(ch[0],i[0])
        
        
        rows = py_db.executeAndReturnRows(sql)
        c=0
        
        assli_zero = 0
        if len(rows) != 0:
            tbl=tbl+"<tr class='tr_onvan'><td colspan='2'>{1}</td><td>{0}</td><tr>".format(i[2],i[1])
        else: assli_zero = 1

        for row in rows:
            RadeefeShabake=RadeefeShabake+1
            if c==0:
                tbl=tbl+"<tr class='tr_onvan_asli'><td colspan='3'>{0}</td><tr>".format(asliii)
                tbl=tbl+"<tr class='tr_onvan'><td>ردیف</td><td>محور ها</td><td>کد</td><tr>".format(i[2],i[1])
            c=c+1
            tbl = tbl+"<tr><td>{2}</td><td>{1}</td><td>{0}</td></tr>".format(row[0],row[1],RadeefeShabake)
            

        
        rows = py_db.executeAndReturnRows('select main_code,Onvan from sheet_anavin where {0}="**" and LinkToAhdaf ="{1}" order by main_code'.format(ch[0],i[0]))
        if assli_zero == 1 and len(rows)!=0:
            tbl=tbl+"<tr class='tr_onvan'><td colspan='2'>{1}</td><td>{0}</td><tr>".format(i[2],i[1])
        c=0
        for row in rows:
            RadeefeShabake=RadeefeShabake+1
            if c==0:
                tbl=tbl+"<tr class='tr_onvan_fari'><td colspan='3'>{0}</td><tr>".format(FARII)
            c=c+1
            tbl = tbl+"<tr><td>{2}</td><td>{1}</td><td>{0}</td></tr>".format(row[0],row[1],RadeefeShabake)
            

    tbl = tbl+"</tbody><table>"
    tbl = tbl+"<br>"+"<br>"+"<br>"+"<br>"


html = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd"
    >
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html lang="en">
<head>
    <title>
        <!-- Insert your title here -->
    </title>
    <link rel="stylesheet" href="html pages/css/main_style.css" type="text/css" />
        <script src="js/jquery.min.js" type="text/javascript"></script><script src="js/main_script.js" type="text/javascript"></script>
    <script src="js/jquery.maskedinput-1.2.2.js" type="text/javascript"></script>

</head>
    


<body dir="rtl">


{0}


</body>
</html>

""".format(tbl)

print html



