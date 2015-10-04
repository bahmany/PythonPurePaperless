#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import MySQLdb
from classes import py_db
import Cookie
import os
import cgi
import sys
import cgitb
from bs4 import BeautifulSoup
import re
import codecs
from urllib import unquote
import datetime
import HTMLParser

cgitb.enable()


form = cgi.FieldStorage()

print 'Content-Type: text/html; charset=utf-8'
print ''
 

def convert_items_to_checkboxes(start_pos,data):
    checkboxes = data.split(")))")
    str = "<table><tbody>"
    counter = 0
    for chk in checkboxes:
        counter = counter+1
        check_box_name = chk.split("^^")[1]
        check_box_value = chk.split("^^")[0]
        str = str+"""<tr><td> {2} </td><td> <input type="checkbox" id="chk_{0}_{1}" >     </td></tr>""".format(start_pos,counter,check_box_name)
    str = str+"</tbody></table>"
    return str        
    


def send_channel_lists():
    rows = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id ")
    i=0
    str = ""
    for row in rows:
        if i == 0:
            str = row[0].__str__()+"^^"+row[1].__str__()
        else :
            str = str+")))"+row[0].__str__()+"^^"+row[1].__str__()
        i=i+1
    str = convert_items_to_checkboxes("channels",str)
    print str
        
        
#send_channel_lists()


def create_channel_with_checked (hadaf_id):
    rows_channels = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id")
    channels_col = []
    for row in rows_channels:
        channels_col.append([row[0],row[1]])
    sqlstr=""
    fr=""
    i=0

    sqlstr = """
    
    SELECT 
x1.*,

      CONCAT(
        CAST( (SELECT COUNT(*) FROM tbl_irib_mehvarha_content AS x2 WHERE x2.`imc_mehvar_link` = {2} AND 
        x2.`imc_channels_link`= x1.`ic_id` AND x2.imc_type=1) AS CHAR(2) )
        ,
	CAST( (SELECT COUNT(*) FROM tbl_irib_mehvarha_content AS x2 WHERE x2.`imc_mehvar_link` = {2} AND 
        x2.`imc_channels_link`= x1.`ic_id`  AND x2.imc_type=2) AS CHAR(2) )) AS ch1
 FROM `tbl_irib_channels` AS x1
    
    """.format(row[0],fr,hadaf_id)
    rows = py_db.executeAndReturnRows(sqlstr)
    li = ""
    for row in rows:
	cc=""
	if row[2] == "01": cc="الویت اول"
	if row[2] == "10": cc="الویت دوم"
	if row[2] == "00": cc="---"
	
	li=li+"""
	<div class="div_ch"><span class="div_ch_name">{0}</span><span class="div_ch_value">{1}</span></div>
	
	
	""".format(row[1],cc)

    return ""+li+""

def create_content_div(mehvar_id):
    row = py_db.executeAndReturnRows("""select x1.`cim_id`,x1.`cim_name`,x1.`cim_codes`,
				     (select c_name from tbl_irib_ahdaf where c_id = x1.cim_codes) as ahadaf_text
				     from tbl_irib_mehvarha as x1 where x1.cim_id = """+mehvar_id.__str__()+" order by cim_id")[0]
    div = """
    
    <ul class="ul_channel" id="ul_{4}">
    
    <li class="li_right">
<table>
<tbody>
    <tr><td class="td_onv">ردیف</td><td class="td_val1">{0}</td></tr>
    <tr><td class="td_onv">هدف</td><td class="td_val2">{1}</td></tr>
    <tr><td class="td_onv">محور</td><td class="td_val3">{2}</td></tr>
    <tr><td class="td_vir" colspan=2> <a href='#' onclick='get_edit_content({4})'> ویرایش </a>  <a href='#' onclick=''> نظر </a>
    <span>آخرین ویرایش در تاریخ : 93/01/01  - تعداد نظرات  : .... - تعداد ویرایش ها : .....</span>
    
    </td></tr>
    </tbody></table>




    </li>



    <li class="li_left">
    <ul>
    {3}</ul>
    </li>
    </ul>
    
    """.format(row[0].__str__(),
	       row[1].__str__(),
	       row[2].__str__()+"- "+row[3].__str__(),
	       create_channel_with_checked(mehvar_id),
	       mehvar_id)
    return div


#print create_content_div(1)

def create_main_ul_master():
    rows_mehvarha = py_db.executeAndReturnRows("select cim_id from tbl_irib_mehvarha order by cim_id")
    
    content = ""
    for row in rows_mehvarha:
	content=content+create_content_div(row[0])
    print "<ul><li>"+content+"</li></ul>"
#create_main_ul_master()
	
	

def create_main_table_master_editing():
    rows_channels = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id")
    channel_rows_count = len(rows_channels)
    channel_rows_count = channel_rows_count + 3
    top_colspan = ['ردیف','کد هدف','عنوان محور','شبکه ها']
    channels_col = []
    for row in rows_channels:
        channels_col.append([row[0],row[1]])
    #creating title columns
    header_cols = "<td rowspan=2>ردیف</td>"
    header_cols = header_cols+"<td rowspan=2>کد هدف</td>"
    header_cols = header_cols+"<td rowspan=2>عنوان محور</td>"
    header_cols = header_cols+"<td colspan = {0}>شبکه ها</td>".format(channel_rows_count - 3)
    header_cols = "<table id='tbl_main_grid'><tbody><tr class = 'col_header'>{0}</tr><tr class = 'col_header1'>".format(header_cols)
    #creating channels list title columns
    for i in channels_col:
        header_cols = header_cols+"<td>{0}</td>".format(i[1])
    header_cols = header_cols+"</tr>"
    rows_mehvarha = py_db.executeAndReturnRows("select * from tbl_irib_mehvarha order by cim_id")
    sqlstr = ""
    for row in rows_channels:
        sqlstr = sqlstr+"""
        , CONCAT(
        CAST( (SELECT COUNT(*) FROM tbl_irib_mehvarha_content AS x2 WHERE x2.`imc_mehvar_link` = x1.cim_id AND 
        x2.`imc_channels_link`= {0} AND x2.imc_type=1) AS CHAR(2) )
        ,
	CAST( (SELECT COUNT(*) FROM tbl_irib_mehvarha_content AS x2 WHERE x2.`imc_mehvar_link` = x1.cim_id AND 
        x2.`imc_channels_link`= {0} AND x2.imc_type=2) AS CHAR(2) )) AS ch{0}
        """.format(row[0])
    sql = " SELECT x1.* {0} FROM  tbl_irib_mehvarha  AS x1 order by cim_id".format(sqlstr)
    rows = py_db.executeAndReturnRows(sql)
    ii = 0
    ct = ""
    for row in rows:
        ct = ct+"<tr>"
        ii = 0;
        for r in row:
            if ii==1:
                ct = ct+"<td class='tdXs'>{0}-- <a href='#' onclick='get_edit_content({1})'> ویرایش </a> -- <a href='#' onclick=''> نظر </a></td>".format(r,row[0])
            else:
                p=r;
                if r=="00":p="--"
                if r=="01":p="اول"
                if r=="10":p="دوم"
                ct = ct+"<td>{0}</td>".format(p)
            ii = ii+1
        ct = ct+"</tr>"
    header_cols = header_cols+ct+"</tbody></table>"
    print header_cols

#create_main_table_master_editing()



def create_edit_content(get_edit_content):
    rows = py_db.executeAndReturnRows("select * from tbl_irib_mehvarha where cim_id = {0}".format(get_edit_content))
    rows_channels = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id ")
    rows_mehvarz = py_db.executeAndReturnRows("select * from tbl_irib_ahdaf order by c_id")
    #creating mehvarz dropdown
    select = "<select id='sel_ahdaf'>"
    cim_codes = rows[0][2]
    i=1
    for r in rows_mehvarz:
	if r[0]==cim_codes:
	    select = select + "<option value={0} selected>{2} - {1}</option>".format(r[0],r[1],i)
	else:
	    select = select + "<option value={0}>{2} - {1}</option>".format(r[0],r[1],i)
	    
	i+=1
    select = select+"</select>"
    
    def create_select(value,_id):
	_select = """
	<select id='sel_olv_{0}'>
	<option value=2>الویت اول</option>
	<option value=1>الویت دوم</option>
	<option value=0>بدوم الویت</option>
	</select>
	""".format(_id)
	_select = _select.replace("value="+value,"value="+value+" selected")
	return _select
    # begining check position with channels
    items= []
    for rp in rows_channels:
        rows_position_fari = """
        select count(*) from tbl_irib_mehvarha_content where imc_channels_link = {0} and imc_mehvar_link={1} and imc_type={2}
        """.format(rp[0],rows[0][0],1)
        rows_position_asli = """
        select count(*) from tbl_irib_mehvarha_content where imc_channels_link = {0} and imc_mehvar_link={1} and imc_type={2}
        """.format(rp[0],rows[0][0],2)
        result_fari = py_db.executeAndReturnRows(rows_position_fari)[0][0].__str__()
        result_asli = py_db.executeAndReturnRows(rows_position_asli)[0][0].__str__()
	
	main_result = "0"
	if result_fari == "1" and result_asli=="0" : main_result = "1"
	if result_fari == "0" and result_asli=="1" : main_result = "2"

        items.append([rp[0],rp[1],rows[0][1],main_result])
    div = "<div><textarea id='txt_mehvar'>{0}</textarea><input type='hidden' id='mehvar_code' value='{2}'><br>{1}<table><tbody>".format(rows[0][1],select,get_edit_content)
    for it in items:
        div = div+"<tr><td>{0}</td><td>{1}</td></tr>".format(it[1],create_select(it[3],it[0]))
    div = div+"</tbody></table></div><a href='#' onclick='post_edited_data()'>ثبت اطلاعات</a>-----<a href='#' onclick=''>لغو</a>"
    print div
    
        
        
        
        
#create_edit_content(1)
    
def set_edit_post(edited_data):
    edited_array = []
    set_channels = "  ";
    ed = edited_data.split("yupp")
    get_txt = ed[0]
    get_mehvar = ed[1]
    get_hadaf_id = ed[3]

    for sd in ed[2].split("^"):
	if sd!="":
	    
	    set_channels =  """
	    delete from tbl_irib_mehvarha_content where imc_channels_link={0} and imc_mehvar_link={1};
	
		""".format(sd.split(">")[0],get_hadaf_id)
	    py_db.executesql(set_channels)
	    if sd.split(">")[1] != "0":
		set_channels = """
	    insert into tbl_irib_mehvarha_content (imc_channels_link,imc_mehvar_link,imc_type) values({0},{1},{2});
	
		    """.format(sd.split(">")[0],get_hadaf_id,sd.split(">")[1])
	    py_db.executesql(set_channels)
    
    py_db.executesql("update tbl_irib_mehvarha set cim_name='{0}', cim_codes='{1}' where cim_id = {2}".format(get_txt,get_mehvar,get_hadaf_id))
	    
	

#set_edit_post('احیاء، بازتولید و ارتقاء کارکردهای شعائر، نمادها و آیین های اسلامی، ایرانی و انقلابی و زمینه سازی برای ظهور و بروز آنها در کلیه شئون زندگی فردی، خانوادگی، نهادی و اجتماعی؛yupp1yupp^1>2^2>2^3>1^4>1^5>0^6>0^7>0^8>0^9>0^10>0^11>0^12>0^13>0^14>0^15>0^16>0')

    

def get_updated_div(ul_id):
    print create_content_div(ul_id)



   

def send_search_result(_search_text):
    
    rtxt = "select * from mehvarz where  match (_text) against('{0}')".format(_search_text)
    rows =py_db.executeAndReturnRows(rtxt)
    str84 = ""
    for row in rows:
	str84 = str84+"{2} - {0}<a class='a_add_meh' onclick='add_meh({1})' >+</a><br>".format(row[1],row[2],row[0])

    ss = str84
    
    
    r_txt = "SELECT COUNT(_year) ,_year FROM  `mehvarz`  WHERE match (_text) against('{0}') GROUP BY _year".format(_search_text)
    rows =py_db.executeAndReturnRows(r_txt)
    str_srch = ""
    for row in rows:
	str_srch = str_srch + "<span id='scscscd'> سال {0} نتیجه {1} </span> - ".format(row[1],row[0])
    str_srch = "<div id='div_srch'>{0}</div>".format(str_srch)
    
    
    
    #ss = ss.replace(_search_text,"<span class = 'sp_found'>{0}</span>".format(_search_text))
    print ss+"____"+str_srch

    
    
				      
def send_olaviats_list():
    rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats order by io_id")
    i=0
    res = ""
    for row in rows:
	i=i+1
	if i==1:
	   res=row[0].__str__()+"====="+row[1].__str__()
	else:
	    res = res+"____"+row[0].__str__()+"====="+row[1].__str__()
    print res
    
def send_olaviats_mozoo_list(id):
    rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo where iom_link={0} order by iom_id".format(id))
    i=0
    res = ""
    for row in rows:
	i=i+1
	if i==1:
	   res=row[0].__str__()+"====="+row[1].__str__()
	else:
	    res = res+"____"+row[0].__str__()+"====="+row[1].__str__()
    print res
    
def send_olaviats_mozoo_mehvar_list(id):
    rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo_mehvarz where iomm_link={0} order by iomm_id".format(id))
    i=0
    res = ""
    for row in rows:
	i=i+1
	if i==1:
	   res=row[0].__str__()+"====="+row[1].__str__()
	else:
	    res = res+"____"+row[0].__str__()+"====="+row[1].__str__()
    print res
    

def send_chlist():
    rows = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id")
    i=0
    res = ""
    for row in rows:
	i=i+1
	if i==1:
	   res=row[0].__str__()+"====="+row[1].__str__()
	else:
	    res = res+"____"+row[0].__str__()+"====="+row[1].__str__()
    print res
    


def send_channel_groups_with_mehvarz(channelID,mehvar):
    rows = py_db.executeAndReturnRows("select * from tbl_irib_channels_group where icg_link_to_channels={0} order by icg_id desc".format(channelID))
    str = ''
    for row in rows:
	_rows = py_db.executeAndReturnRows("select * from tbl_irib_ch_gr_meh where icgm_channel_link={0} and icgm_mehvar_link={1}  and icgm_out='0'".format(row[0],mehvar))
	if len(_rows)==0:
	    str = str+"_{0}po{1}po{2}po{3}po{4}po{5}".format(row[0],row[2],'no','','','')
	else:
	    #Code Group Shabake, Name Group Shabake , Code Mehvar Name Mehvar , Matne Mehvare Special , Percent
	    str = str+"_{0}po{1}po{2}po{3}po{4}po{5}".format(row[0],
							    row[2],
							    _rows[0][2],
							    py_db.executeAndReturnRows("select iomm_name from tbl_irib_olaviats_mozoo_mehvarz where iomm_id={0}".format(_rows[0][2]))[0][0] ,
							    _rows[0][3],
							    _rows[0][4].__str__())
    print str
	    
#send_channel_groups_with_mehvarz(1,1)

def decodeHTML(_str):
        str1 = _str
	str1 = str1.replace("ule12",">");
        str1 = str1.replace("ule13","<");
        str1 = str1.replace("ule14","'");
        str1 = str1.replace("ule15","\"");
        str1 = str1.replace("ule16","?");
        str1 = str1.replace("ule17","&");
        str1 = str1.replace("ule18","-");
        str1 = str1.replace("ule19","$");
        str1 = str1.replace("ule20","/");
        str1 = str1.replace("ule21","\\");
        str1 = str1.replace("ule22","=");
        str1 = str1.replace("ule10"," ");
	return str1

def unquote_u(source):
    result = unquote(source)
    if '%u' in result:
        result = result.replace('%','\\').decode('unicode_escape')
    return result
#print unquote_u("%u0647%u0648%u06CC%u062A")
def update_edited_data(_data):
    dt=unquote_u(_data)

    #print dt
    #print dt
    soup = BeautifulSoup(dt)
    dd = ""
    inputs = soup.findAll('input')
    final_array = []
    for sp in inputs:
	obj_attr = sp.attrs
	if 'value' in sp.attrs:
	    obj_value = sp.attrs['value']
	else:
	    obj_value = ""
	obj_id = obj_attr['id']
	obj_type = obj_attr['type']
	obj_id_type = obj_id.split("_")[0]
	
	obj_value_olaviats_mozoo_mehvar = ""
	obj_value_Code_Group_Shabake = ""
	if obj_id.split("_")[0]!="txt":
	    obj_value_olaviats_mozoo_mehvar = obj_id.split("_")[1].split("cvf")[0]
	    obj_value_Code_Group_Shabake = obj_id.split("_")[1].split("cvf")[1]

	    
	dynamic_key = ''
	if obj_id_type == "txtspm":
	    dynamic_key = obj_id.split("_")[2]
	if obj_id_type == "txtpercm":
	    dynamic_key = obj_id.split("_")[2]
	final_array.append(
	    [obj_id_type,
	     obj_value,
             obj_value_olaviats_mozoo_mehvar,
 	     obj_value_Code_Group_Shabake,
	     dynamic_key])
    get_objects_txtsp = filter(lambda x:x[0] == "txtsp",final_array)
    get_objects_txtperc = filter(lambda x:x[0] == "txtperc",final_array)
    get_objects_txtspm = filter(lambda x:x[0] == "txtspm",final_array)
    get_objects_txtpercm = filter(lambda x:x[0] == "txtpercm",final_array)
    
    # get_objects_txtsp[0][0]  = txtsp object suffix
    # get_objects_txtsp[0][1]  = object value
    # get_objects_txtsp[0][2]  = Channel Group ID
    # get_objects_txtsp[0][3]  = Mehvar ID
    # get_objects_txtsp[0][4]  = code dynamic ezafeh shodeha dar soorate added
    
    objects_combined_txtsp_with_txtperc = []
    for o in get_objects_txtsp:
	for o1 in get_objects_txtperc:
	    if o[2]==o1[2] and o[3]==o1[3] :
		objects_combined_txtsp_with_txtperc.append([o,o1])
   
   
    objects_combined_dynamic_txtsp_with_txtperc = []
    for o in get_objects_txtspm:
	for o1 in get_objects_txtpercm:
	    if o[2]==o1[2] and o[3]==o1[3] and o[4]==o1[4]:
		objects_combined_dynamic_txtsp_with_txtperc.append([o,o1])

#objects_combined_dynamic_txtsp_with_txtprec
    # get_objects_txtsp[0][0]  = txtsp object suffix
    # get_objects_txtsp[0][1]  = object value
    # get_objects_txtsp[0][2]  = Channel Group ID
    # get_objects_txtsp[0][3]  = Mehvar ID
    # get_objects_txtsp[0][4]  = code dynamic ezafeh shodeha dar soorate added
    today = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S" );    
    for o in objects_combined_txtsp_with_txtperc:
	if o[1][1]!="":
	    prc = o[1][1]
	sqlstr = """
   UPDATE `irib`.`tbl_irib_ch_gr_meh`
SET 
  
  `icgm_out` = '{4}',
  `icgm_dateout` = '{5}'
  where
    `icgm_mehvar_link` = '{1}' and 
  `icgm_channel_link` = '{0}' and
  icgm_out = '0'

	""".format(o[0][2],
		   o[0][3],
		   o[0][1],
		   prc,
		   '1',
		   today)
	py_db.executesql(sqlstr)
    for o in objects_combined_dynamic_txtsp_with_txtperc:
	prc = 0
	if o[1][1]!="":
	    prc = o[1][1]
	sqlstr = """
   UPDATE `irib`.`tbl_irib_ch_gr_meh`
SET 
  `icgm_channel_link` = '{0}',
  `icgm_out` = '{4}',
  `icgm_dateout` = '{5}'
  where
    `icgm_mehvar_link` = '{1}' and 
  `icgm_channel_link` = '{0}' and
  icgm_out = '0'
	""".format(o[0][2],
		   o[0][3],
		   o[0][1],
		   prc,
		   '1',
		   today)
	py_db.executesql(sqlstr)
    
    for o in objects_combined_txtsp_with_txtperc:
	prc = 0
	if o[1][1]!="":
	    prc = o[1][1]
	sqlstr = """
	INSERT INTO `irib`.`tbl_irib_ch_gr_meh`
            (
             `icgm_channel_link`,
             `icgm_mehvar_link`,
             `icgm_special_text`,
             `icgm_percent`,
             `icgm_out`,
             `icgm_datecreate`,
             `icgm_dateout`)
VALUES (
        '{0}',
        '{1}',
        '{2}',
        '{3}',
        '0',
        '{4}',
        (NULL)	);
	
	""".format(o[0][3],
		   o[0][2],
		   o[0][1],
		   prc,
		   today)
	
	py_db.executesql(sqlstr)
    
    for o in objects_combined_dynamic_txtsp_with_txtperc:
	prc = 0
	if o[1][1]!="":
	    prc = o[1][1]
	sqlstr = """
	INSERT INTO `irib`.`tbl_irib_ch_gr_meh`
            (
             `icgm_channel_link`,
             `icgm_mehvar_link`,
             `icgm_special_text`,
             `icgm_percent`,
             `icgm_out`,
             `icgm_datecreate`,
             `icgm_dateout`)
VALUES (
        '{0}',
        '{1}',
        '{2}',
        '{3}',
        '0',
        '{4}',
        (NULL)	);
	
	""".format(o[0][3],
		   o[0][2],
		   o[0][1],
		   prc,
		   today)
	
	py_db.executesql(sqlstr)
	print "inserted"
    print "ok"


#	print sqlstr
    
   # print objects_combined_dynamic_txtsp_with_txtperc;
	
    
    
#	print obj_attr['id']
   # print final_array
    
def add_old_mehvarz_to_new(_added_mehvar_id,_selected_code_id):
    py_db.executesql("""
insert into tbl_irib_olaviats_mozoo_mehvarz
(`iomm_name`,`iomm_link`) values
('{0}','{1}')""".format(
    py_db.executeAndReturnRows("select _text from mehvarz where id="+_selected_code_id)[0][0],
    _added_mehvar_id
    ))
    print "ok"


def update_headers(_text_of_value,_type_of_updateing,_id_of_selected_header):
    sqlstr=""
    if int(_type_of_updateing)==1:
	sqlstr="update tbl_irib_olaviats set io_Onvan = '{0}' where io_id='{1}'".format(_text_of_value,_id_of_selected_header)
    if int(_type_of_updateing)==2:
	sqlstr="update tbl_irib_olaviats_mozoo set iom_name = '{0}' where iom_id='{1}'".format(_text_of_value,_id_of_selected_header)
    if int(_type_of_updateing)==3:
	sqlstr="update tbl_irib_olaviats_mozoo_mehvarz set iomm_name = '{0}' where iomm_id='{1}'".format(_text_of_value,_id_of_selected_header)
    if int(_type_of_updateing)==4:
	sqlstr="update tbl_irib_channels set ic_name = '{0}' where ic_id='{1}'".format(_text_of_value,_id_of_selected_header)
    #print sqlstr
    py_db.executesql(sqlstr)
    print "ok"
    
def del_headers(_type_of_updateing,_id_of_selected_header):
    sqlstr=""
    if int(_type_of_updateing)==1:
	sqlstr="delete from tbl_irib_olaviats  where io_id='{1}'".format('',_id_of_selected_header)
    if int(_type_of_updateing)==2:
	sqlstr="delete from tbl_irib_olaviats_mozoo where iom_id='{1}'".format('',_id_of_selected_header)
    if int(_type_of_updateing)==3:
	sqlstr="delete from tbl_irib_olaviats_mozoo_mehvarz  where iomm_id='{1}'".format('',_id_of_selected_header)
    if int(_type_of_updateing)==4:
	sqlstr="delete from tbl_irib_channels  where ic_id='{1}'".format('',_id_of_selected_header)
    #print sqlstr
    py_db.executesql(sqlstr)
    print "ok"
    

def add_to_headers(_added_texxxxxxt,_added_typeeeeee,_parent_______id):
    sqlstr = ""
    if _added_typeeeeee == "1":
	sqlstr = "insert into tbl_irib_olaviats (io_Onvan) values ('{0}')".format(_added_texxxxxxt)
    if _added_typeeeeee == "2":
	sqlstr = "insert into tbl_irib_olaviats_mozoo (iom_name, iom_link) values ('{0}','{1}')".format(_added_texxxxxxt,_parent_______id)
    if _added_typeeeeee == "3":
	sqlstr = "insert into tbl_irib_olaviats_mozoo_mehvarz (iomm_name,iomm_link) values ('{0}','{1}')".format(_added_texxxxxxt,_parent_______id)
    if _added_typeeeeee == "4":
	sqlstr = "insert into tbl_irib_channels (ic_name) values ('{0}')".format(_added_texxxxxxt,_parent_______id)
    py_db.executesql(sqlstr)
    print "ok refresh"
    
    
    
    
    
def create_prn_ahdaf_tree():
    ul = ""
    rows = py_db.executeAndReturnRows("select * from tbl_irib_olaviats order by io_id")
    #<ul class='ul_ahdaf_14' id='ul_14'>
    ul = "<ul class='tree'>"
    i1 = 0
    i2 = 0
    i3 = 0
    for row in rows:
	i1=i1+1
	i2 = 0
	i3 = 0 
	ul = ul+"<li id='olaviat_{1}'><a href='#'> {2} -  {0}</a>".format(row[1],row[0],i1)
	rows_rahbord =  py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo where iom_link = '{0}' order by iom_id".format(row[0]))
	if len(rows_rahbord)>0: ul = ul+"<ul>"
	i2 = 0
	i3 = 0
	for row_r in rows_rahbord:
	    i2=i2+1
	    ul = ul+"<li id='rahbord_{1}'><a href='#'> {2} -  {3} -  {0} </a>".format(row_r[1],row[0],i1,i2)
	    rows_mehvar =  py_db.executeAndReturnRows("select * from tbl_irib_olaviats_mozoo_mehvarz where iomm_link = '{0}' order by iomm_id".format(row_r[0]))
	    if len(rows_mehvar)>0: ul = ul+"<ul>"
	    i3=0
	    for row_m in rows_mehvar:
		i3=i3+1
		ul = ul+"<li id='mehvar_{1}'> <a href='#'>  {2} -  {3} - {4} - {0}</a></li>".format(row_m[1],row[0],i1,i2,i3)
	    if len(rows_mehvar)>0: ul = ul+"</ul></li>"
	if len(rows_rahbord)>0: ul = ul+"</ul></li>"
	else :  ul = ul+"</ul></li>"
    ul = '<div class="span9 well mhrz cccf" id="div_mohvarz_tree">'+ul + "</ul></div>"
    print ul
	
def create_prn_chnl_tree():
    ul = ""
    rows = py_db.executeAndReturnRows("select * from tbl_irib_channels order by ic_id")
    
    for row in rows:
	ul = ul + "<li id='chanel_{1}' ><a href='#'> {0}</a>".format(row[1],row[0])
	_rows = py_db.executeAndReturnRows("select * from tbl_irib_channels_group where icg_link_to_channels = {0}".format(row[0]))
	if len(_rows)> 0 : ul = ul+"<ul>"
	for _row in _rows:
	    ul = ul+"<li id='chgroups_{1}' ><a href='#'> {0}</a></li>".format(_row[2],_row[0])
	if len(_rows)> 0 : ul = ul+"</ul></li>"
    ul = '<div class="span3 well chnls cccf" id="div_channels_tree"><ul>{0}</ul></div>'.format(ul)
    print ul
	
    

	
    



#
#bbpppp =""" 
# <table> <tbody> <tr> <td> <img src="html pages/images/img_olaviatha.jpg"><br> <table class="a_head_btn"><tbody><tr><td><input value="" id="txt_1" type="text"></td><td><a onclick=""> </a><a onclick="">-</a></td></tr></tbody></table> <select id="sel_olaviats" size="10"> <option value="1">هویت اسلامی ، ایرانی و انقلابی</option><option value="2">نهاد خانواده و جمعیت</option><option value="3">سبک زندگی اسلامی - ایرانی</option><option value="4">اخلاق و فرهنگ عمومی جامعه</option><option value="5">هنر</option><option value="6">مقابله هوشمندانه با تهاجم فرهنگی</option><option value="7">اطلاعات ، ارتباطات و رسانه</option><option value="8">تمدن نوین اسلامی- ایرانی</option><option value="9">نظام سازی فرهنگی</option><option value="10">بهره گیری از ظرفیت های جدید رسانه های نوین </option></select> </td> <td><img src="html pages/images/img_mozooat.jpg"><br> <table class="a_head_btn"><tbody><tr><td><input value="" id="txt_2" type="text"></td><td><a onclick=""> </a><a onclick="">-</a></td></tr></tbody></table> <select id="sel_olaviats_mozoo" size="10"><option value="1">انتظار منجی</option><option value="2">قرآن و عترت </option><option value="3">نماز و مسجد</option><option value="4">ولایت فقیه</option><option value="5">فرهنگ بسیجی</option><option value="6">فرهنگ ایثار و گذشت</option><option value="7">جهاد و شهادت</option><option value="8">صیانت از زبان ، ادبیات و خط فارسی</option><option value="9">تاریخ </option></select> </td> <td><img src="html pages/images/img_mehvarha.jpg"><br> <table class="a_head_btn"><tbody><tr><td><input value="" id="txt_3" type="text"></td><td><a onclick=""> </a><a onclick="">-</a></td></tr></tbody></table> <select id="sel_olaviats_mozoo_mehvar" size="10"><option value="5"> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </option><option value="6"> پاسخ به شبهات مهدویتکد اولویت یک دو سه چهار تهران قرآن آموزش جام جم مستند نمایش تماشا ورزش سیما صبا</option><option value="7">پاسخ به شبهات مربوط به مهدویت )ولادت،امامت، توقیعات..( </option><option value="8">تاثیر انقلاب اسلامی در توجه نسل جوان کشورهایمنطقه به اسلام ناب و عناصر عزتمندی و امید در آنمانند عاشورا و مهدویت ؛</option><option value="9">تعمیق باور به مهدی عجل الله تعالی فرجه و اهدافمهدویت </option><option value="11"> رویارویی تاریخی حق و باطل )تبیین گفتمان انتظار(؛ </option><option value="12"> ضرورت قیام عمومی برای قسط )مبانی نهضتانتظار( </option><option value="13"> عدالت جهانی و گفتمان انتظار ؛ </option></select> </td> <td><img src="html pages/images/img_chann.jpg"><br> <table class="a_head_btn"><tbody><tr><td><input value="" id="txt_4" type="text"></td><td><a onclick=""> </a><a onclick="">-</a></td></tr></tbody></table> <select id="sel_channels" size="10"><option value="1">شبکه اول</option><option value="2">شبکه دوم</option><option value="3">شبکه سوم</option><option value="4">شبکه چهارم</option><option value="5">شبکه پنجم</option><option value="6">شبکه آموزش</option><option value="7">شبکه قرآن</option><option value="8">شبکه سلامت</option><option value="9">جام جم</option><option value="10">شبکه مستند</option><option value="11">شبکه پویا</option><option value="12">شبکه نمایش</option><option value="13">شبکه تماشا</option><option value="14">شبکه ورزش</option><option value="15">شبکه شما</option><option value="16">شبکه نسیم </option></select> </td> </tr> <tr> <td colspan="4" id="td_ch_groups"><table class="tbl_details"><thead><tr><td>گروه شبکه</td><td>محور مد نظر </td><td>محور نهایی</td><td>درصد پرداخت</td></tr></thead><tbody><tr><td>کودک و نوجوان</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf1" value="اخلاق اسلامی ( اخلاق عملی )" type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf1&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf1" value="0.0" type="text"> </td></tr><tr><td>فرهنگ و معارف اسلامی ، تاریخ و هنر</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf2" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf2&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf2" value="2.0" type="text"> </td></tr><tr><td>فیلم و سریال</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf3" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf3&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf3" value="0.0" type="text"> </td></tr><tr><td>اجتماعی</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf4" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf4&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf4" value="0.0" type="text"> </td></tr><tr><td>دانش و اقتصاد</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf5" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf5&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf5" value="0.0" type="text"> </td></tr><tr><td>سیاسی</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf6" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf6&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf6" value="0.0" type="text"> </td></tr><tr><td>حماسه و دفاع مقدس</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf7" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf7&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf7" value="0.0" type="text"> </td></tr><tr><td>خود شبکه</td><td> مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام </td><td><input id="txtsp_5cvf69" value=" مدعیان دروغین مهدویت و ارتباط با مهدیعلیه السلام " type="text"> <a id="a_add" onclick="addnew(this,&quot;5cvf69&quot;);">اضافه</a> </td><td><input id="txtperc_5cvf69" value="0" type="text"> </td></tr><tr><td colspan="4"><a onclick="postdt();">ثبت داده ها</a></td></tr></tbody></table></td> </tr> </tbody> </table> 
#  """
 
#update_edited_data(bbpppp)

get_channels_list =  form.getvalue("get_channel_list","-1")
get_main_grid =  form.getvalue("get_main_grid","-1")
get_edit_content =  form.getvalue("get_edit_content","-1")
get_edited_data = form.getvalue("send_edit_data","-1")
get_search_text = form.getvalue("search_text","-1")
send_olaviats = form.getvalue("get_olaviats_list","-1")
send_olaviats_mozoo = form.getvalue("get_olaviats_mozoo_list","-1")
send_olaviats_mozoo_mehvar = form.getvalue("get_olaviats_mozoo_mehvar_list","-1")
get_chlist = form.getvalue("get_chlist","-1")
get_detail_list_cgi = form.getvalue("cgi","-1")
get_detail_list_oi = form.getvalue("oi","-1")
get_edited_items = form.getvalue("dta","-1")
edited_items = form.getvalue("btp","-1")
added_mehvar_id = form.getvalue("meh_id","-1")
selected_code_id = form.getvalue("codeID","-1")

text_of_value = form.getvalue("txtval","-1")
type_of_updateing = form.getvalue("__type","-1")
id_of_selected_header = form.getvalue("__id","-1")

del_type_of_header = form.getvalue("______type","-1")
del_id_of_selected = form.getvalue("______id","-1")

added_texxxxxxt = form.getvalue("________txtval","-1")
added_typeeeeee = form.getvalue("________type","-1")
parent_______id = form.getvalue("________id","-1")


create_ahdaf_tree = form.getvalue("cattt","-1")







if get_channels_list != "-1":
    send_channel_lists()
if get_main_grid != "-1":
    create_main_ul_master()
if get_edit_content != "-1":
    create_edit_content(get_edit_content)
if get_edited_data != "-1":
    set_edit_post(get_edited_data)
if get_search_text != "-1":
    send_search_result(get_search_text)
if send_olaviats != "-1":
    send_olaviats_list()
if send_olaviats_mozoo != "-1":
    send_olaviats_mozoo_list(send_olaviats_mozoo)
if send_olaviats_mozoo_mehvar != "-1":
    send_olaviats_mozoo_mehvar_list(send_olaviats_mozoo_mehvar)
if get_chlist != "-1":
    send_chlist()
if get_detail_list_cgi != "-1":
    send_channel_groups_with_mehvarz(get_detail_list_cgi,get_detail_list_oi)
if get_edited_items != "-1":
    update_edited_data(edited_items)
if added_mehvar_id != "-1":
    add_old_mehvarz_to_new(added_mehvar_id,selected_code_id)
if text_of_value!="-1":
    update_headers(text_of_value,type_of_updateing,id_of_selected_header)
if del_type_of_header!="-1":
    del_headers(del_type_of_header,del_id_of_selected)
    
if added_texxxxxxt!="-1":
    add_to_headers(added_texxxxxxt,added_typeeeeee,parent_______id)
    
if create_ahdaf_tree!="-1":
    create_prn_ahdaf_tree()
    create_prn_chnl_tree()
    
    