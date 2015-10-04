#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import MySQLdb
from classes import py_db
import Cookie
import os
import cgi
import sys
import cgitb
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
    
    <ul class="ul_channel">
    
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

    





get_channels_list =  form.getvalue("get_channel_list","-1")
get_main_grid =  form.getvalue("get_main_grid","-1")
get_edit_content =  form.getvalue("get_edit_content","-1")
get_edited_data = form.getvalue("send_edit_data","-1")

if get_channels_list != "-1":
    send_channel_lists()
if get_main_grid != "-1":
    create_main_ul_master()
if get_edit_content != "-1":
    create_edit_content(get_edit_content)
if get_edited_data != "-1":
    set_edit_post(get_edited_data)