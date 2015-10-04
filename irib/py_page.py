
#!d:/Python27/python.exe -u
# -*- coding: utf-8 -*-

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




header_script = """
    <link rel="stylesheet" href="html pages/css/main_style.css" type="text/css" />
     <script src="js/jquery.min.js" type="text/javascript"></script><script src="js/main_script.js" type="text/javascript"></script>
    <script src="js/jquery.maskedinput-1.2.2.js" type="text/javascript"></script>
"""


f_english_form_name=""
script=""
HV = ''


def set_cookie_settings(_ck):
    global ck
    ck = _ck

def create_validation_js_sctipt(set_tag):
    s='''
    var is_it_true=true;
    var err_msg="";
    jQuery.fn.ForceNumericOnly = function(){
        return this.each(function()    {
            $(this).keydown(function(e){
                var key = e.charCode || e.keyCode || 0;
                return (key == 8 || key == 9 || key == 46 || key == 110 || key == 190 || (key >= 35 && key <= 40) || (key >= 48 && key <= 57) || (key >= 96 && key <= 105));
                });
            });
            };
        '''
    ss='<script type="text/javascript"> {0}  </script> '.format(s)
    if set_tag==True: return ss
    else: return s
    
def create_post_js_script(formname,posturl,set_tag):
    s= '''function  submit_frm_'''+formname+'''()
    {
    
    
        _data= $("#'''+formname+'''").serialize();
    
    if (typeof(fff_key) != "undefined")
    
    {_data = _data + "&fff_key="+fff_key;}
        $.post("'''+posturl+'''",_data, function(data) {
        //$('.result').html(data);
        alert(data);
        
        });}'''  
    ss='<script type="text/javascript">{0} </script> '.format(s)
    if set_tag==True: return ss
    else: return s
    
    

def create_form_html(objs_mapping,f_english_form_name,objshtml):
   # print objshtml
    formhtml='''
    <form action="py_do.py" method="post" id="{1}" name="{1}">
    <table dir=rtl style="font-family:tahoma; font-size:12px;">
    <tbody>
       <input id="hv_{1}" name="hv" type="hidden" value="{0}" />{2}</tbody></table></form>'''.format(objs_mapping,f_english_form_name,objshtml)
    return formhtml
   


# this was verrrry hard !!
def create_right_menu():
    weight0=""
    weight1=""
    weight2=""
    weight3=""
    weight=""
    rows=[]
    _rows=[]
    __rows=[]
    ___rows=[]
    rows = py_db.executeAndReturnRows("select * from tbl_template_right_menu where trm_weight=0 and trm_parent_id=0")
    for row in rows:
        weight0=weight0+"<ul>"+row[1]
        _rows = py_db.executeAndReturnRows("select * from tbl_template_right_menu where trm_weight=1 and trm_parent_id={0}".format(row[0]))
        weight1=""
        if len(_rows) > 1 : weight1="<ul>"
        for _row in _rows:
            weight1=weight1+"<li><a href='{0}'>".format(_row[5].__str__())+_row[1]+"</a>"
            __rows = py_db.executeAndReturnRows("select * from tbl_template_right_menu where trm_weight=2 and trm_parent_id={0}".format(_row[0]))
            weight2=""
            if len(__rows) > 1 : weight2="<ul>"
            for __row in __rows:
                weight2=weight2+"<li><a href='{0}'>".format(__row[5].__str__())+__row[1]+"</a>"
                ___rows = py_db.executeAndReturnRows("select * from tbl_template_right_menu where trm_weight=3 and trm_parent_id={0}".format(__row[0]))
                weight3=""
                if len(___rows) > 1 : weight3="<ul>"
                for ___row in ___rows:
                    weight3=weight3+"<li><a href='{0}'>".format(___row[5].__str__())+___row[1]+"</a></li>"
                if len(___rows)  >1: weight2=weight2+weight3+"</ul></li>"
                else : weight2=weight2+weight3+"</li>"
            if len(__rows) > 1 : weight1=weight1+weight2+"</ul></li>"
            else : weight1=weight1+weight2+"</li>"
        if len(_rows) > 1 : weight0=weight0+weight1+"</li></ul>"
        else : weight0=weight0+weight1+"</ul>"
    return weight0      
        

    



def get_template_page():
    htmlstrtemp=""
    hh=""
    with open("template.html") as f:
        f.__enter__()
        htmlstrtemp=f.read()
        for l in htmlstrtemp:
            hh+=l
        
        f.__exit__()

    return hh


def ord_validation_mapping(hashed_text):
    txt="";
    for i in list(hashed_text):
        txt+="::"+ord(i).__str__()
    return txt
    
def conv_array_to_str(arr):
    b=""
    for a in arr:
        b=b+"::"+a[1]+"##"+a[0].__str__()
    return b


def create_grid(form_id,view_type):
    f_table_name = py_db.executeAndReturnRows("select f_table_name from tbl_forms where f_id={0}".format(form_id))[0][0].__str__()
    sqls = "select f_key_field from tbl_forms where f_id={0}".format(form_id)
    #print sqls
    f_key_field =  py_db.executeAndReturnRows(sqls)[0][0].__str__()
    rows = py_db.executeAndReturnRows("select `fgd_link_to_form`,`fgd_field_name`,`fgd_title` from  tbl_form_grid_dictionary where fgd_link_to_form={0} order by fgd_id ".format(form_id))
    if len(rows)==0: return ""
    th = ""
    field_names = ""
    field_title = ""
    i=0
    for row in rows:
        i=i+1
        th = th+"<th>{0}</th>".format(row[2])
        if i==1: field_names = row[1].__str__()
        else : field_names = field_names+","+row[1].__str__()
       # if i==1: field_title = row[2].__str__()
       # else : field_title = field_title+","+row[2].__str__()
    sqls = "select {2} as key_fieeld,{0} from {1} limit 20".format(field_names,f_table_name,f_key_field)
   
    rows = py_db.executeAndReturnRows(sqls)
    tr = ""
    _tr=""
    __tr=""

    for row in rows:
        __tr=""
        i=0
        for ro in row:
            if i!=0:   #this line is for making delete and update button becuase it need primary fields
                __tr = __tr+"<td>{0}</td>".format(ro)
            i=i+1 
        hashid = form_id.__str__()+"?(xs)@"+row[0].__str__()+"?(xs)@"+ck[2].__str__()
        hashid = ord_validation_mapping(py_db.encode(hashid))
        __tr=__tr+"""<td>
        <a href="#" onclick="showModal('py_page_loader.py?idsf={0}')">Edit</a>
        </td><td><a href="#" onclick="__del('{0}')">Delete</a></td>
        
        """.format(hashid)
        _tr = "<tr>"+__tr+"</tr>"
        tr = tr+_tr
        # del and edit encode link is   table_id + key_field + user_id

    
    
    tbl = """
    <table class="bordered">
    <thead><tr>{0}</tr><thead>
    <tbody>{1}</tbody>
    </table>
    
    
    <script type="text/javascript">
 
 
    
    </script>
    
    
    
    """.format(th,tr)
    
    return tbl

def get_items_field_name(objects_array):
    items = []
    for obj in objects_array:
        # getting items properties
        field_name = py_db.executeAndReturnRows("select fi_field_name,fi_object_type from tbl_form_items where fi_id={0} ".format(obj[0]))
        items.append([field_name[0][0],obj[1],field_name[0][1]])
    return items    #it returns 0=field_name  , 2=object_name , 1=field_type

def get_items_value_from_tbl(key_id,key_field_name,tbl_name,objects_array):
    items = []
    objs = get_items_field_name(objects_array);
    for obj in objs:
        #getting stored value 
        sql = "select {0} from {1} where {2} = {3}".format(obj[0],tbl_name,key_field_name,key_id)
        objsValue = py_db.executeAndReturnRows(sql)[0][0]
        items.append([objsValue,obj[0],obj[1],obj[2]])
    return items


def get_table_and_keyfield_from_obj_id(objects_array):
    rows = py_db.executeAndReturnRows("select f_key_field,f_table_name from tbl_forms where f_id = (select fi_link_to_form_name from tbl_form_items where fi_id={0} limit 1)".format(objects_array[0][0]))
    return [rows[0][0],rows[0][1]]
#final def
#[[1L, 'obj_1'], [2L, 'obj_2'], [3L, 'obj_3'], [4L, 'obj_4'], [5L, 'obj_5'], [6L, 'obj_6']]

def create_value_by_element_type(item):
#    1=text box string   2=textbox int   3=checkbox  4=radio   5=select 6=datetime 7=user id 8=socc_id
    object_type = item[3]
    object_fieldname = item[1]
    object_value = item[0]
    object_element_name = item[2]
    if object_type == 1: js='document.getElementById("{0}").value="{1}";'.format(object_element_name,object_value)
    if object_type == 2: js='document.getElementById("{0}").value="{1}";'.format(object_element_name,object_value)
    if object_type == 3: js='document.getElementById("{0}").checked="{1}";'.format(object_element_name,object_value)
    if object_type == 4: js='document.getElementById("{0}").checked="{1}";'.format(object_element_name,object_value)
    if object_type == 5: js='document.getElementById("{0}").value="{1}";'.format(object_element_name,object_value)
#    if object_type == 6: js='document.getElementById("{0}").value="{1}";'.format(object_element_name,py_db.mil_to_sh(object_value,","))
    if object_type == 6: js='document.getElementById("{0}").value="{1}";'.format(object_element_name,py_db.mil_to_sh(object_value.__str__()))
    
    return js;
    
    
    
    
    
def create_edit_script(unhashed_objs,fieldID):
    #unhashed_objs = py_db.unhash_decode_ord_conv_to_arr(unhashed_objs)
    
    #print HV
    #print unhashed_objs
    gtkkk = get_table_and_keyfield_from_obj_id(unhashed_objs)

    items = get_items_value_from_tbl(fieldID,gtkkk[0],gtkkk[1],unhashed_objs)
    #print items
    i=""
    fff =  ord_validation_mapping(py_db.encode(fieldID))
    #[u'\u0645\u062d\u0645\u062f \u0631\u0636\u0627', u'soccc_name', 'obj_1', 1]
    for it in items:
       i=i+create_value_by_element_type(it)
    i="<script type='text/javascript'>var fff_key='{1}';{0}</script>".format(i,fff)
    return i

#print create_edit_script([[1, 'obj_1'], [2, 'obj_2'], [3, 'obj_3'], [4, 'obj_4'], [5, 'obj_5'], [6, 'obj_6']])
        
        
    





def read_form_from_database_and_generate_html_with_objects_map(form_id):
# in this line i get form name for making form tag
    f_english_form_name = py_db.executeAndReturnRows("select f_english_form_name from tbl_forms where f_id={0}".format(form_id))[0][0].__str__()
# we get form items right now
    sql = """
    select
    fi_id,
    fi_name,
    fi_object_type,
    fi_if_radio_group_name,
    fi_if_mask_maskstring,
    fi_if_3_4_5_link_value,
    fi_not_null,
    fi_check_value_between,
    fi_check_value_from_to,
    fi_if_4_link_tbl_name,
    fi_link_to_form_name,
    fi_order,
    fi_default_value,
    fi_length,
    fi_exp
    from tbl_form_items where fi_link_to_form_name = (select f_id from tbl_forms where f_id={0}) order by fi_order
    """.format(form_id)
    rows = py_db.executeAndReturnRows(sql)
#this is link for sending data to server
# i set function name for js post then i will write other nec code
    formhtml=''
# generating vars
    script=""
    index=0
    objs_mapping=[]
# here we go making form items
#==============================================================
#==============================================================
#==============================================================
    for row in rows:
        if row[2] <> 7 and row[2] <> 8 :
            index=index+1
#__________________________________________________________________________________

        obj_map=[]
        obj_map.append(row[0])
        obj_map.append("obj_"+index.__str__())
        objs_mapping.append(obj_map)       
# Generating Simple Tags ---------------------------------------------------------------------------------------
        formhtml=formhtml+"<tr>"
        exp = ""
# getting if default value has or not
        def_val = " "
        if row[12]!="-1":
            def_val = " value='{0}'".format(row[12])
#________________________________
        if row[14] !=None:exp=row[14] 
# handling if simple textbox 
        if row[2] == 1:
            if row[4]!=None:
                script+='$("#obj_{0}").mask("{1}");'.format(index,row[4])
            formhtml += """<td class='td_lbls'>{1}</td><td><input type="text" name="obj_{0}" id="obj_{0}"  {3}/></td><td>{2}</td>""".format(index,row[1],exp,def_val)
# handling if simple textbox 
        if row[2] == 6:
            script += '$("#obj_{0}").mask("{1}");'.format(index,"1399/99/99")
            formhtml += """<td class='td_lbls'>{1}</td><td><input type="text" name="obj_{0}" id="obj_{0}"   {3}/> </td><td>{2}</td>""".format(index,row[1],exp,def_val)
    
 # handling if simple textbox 
        if row[2] == 2:
            formhtml += """<td class='td_lbls'>{1}</td><td><input type="text" name="obj_{0}" id="obj_{0}"   {3}/> </td><td>{2}</td>""".format(index,row[1],exp,def_val)
            
#______________________________
        if row[2]==3:
            def_val = ""
            if row[12]=="checked":
                def_val = ' checked="checked"'
            formhtml += """<td class='td_lbls'>{2}</td><td><input id="obj_{0}" name="obj_{0}"  type="checkbox" {1}  /> </td><td>{3}</td>""".format(index,def_val,row[1],exp)   

#______________________________
        if row[2]==4:
            def_val = ""
            if row[12]=="checked":
                def_val = ' checked="checked"'
                
            if row[3]!=None:
                def_val += ' group="'+row[3]+'"'

            formhtml += """<td class='td_lbls'>{2}</td><td><input name="obj_{0}"  id="obj_{0}" type="radio"  {1}   /> </td><td>{3}</td>""".format(index,def_val,row[1],exp)   
 #______________________________       
        if row[2]==5:
            ssql = "select {0},{1} from {2} {3}".format(
                row[9].split(":::")[1],
                row[9].split(":::")[2],
                row[9].split(":::")[0],
                row[9].split(":::")[3])
            ssql = ssql.replace("//1//",py_login.get_user_id())
            ssql = ssql.replace("//2//",py_login.get_socc_id())
            
            rowss = py_db.executeAndReturnRows(ssql)
            dd=""
            for r in rowss:
                dd+=' <option value="{0}">{1}</option>'.format(r[1],r[0])
                formhtml +="""  <td>{2}</td><td>  <select name="obj_{0}"  id="obj_{0}"> {1}  </select></td><td>{3}</td>  """.format(index,dd,row[1],exp)   
        
        formhtml=formhtml+"</tr>"
    
#--------------------Scripts ---------------------
        if row[2]==2:
            #// checking if text is integer
            script+= ' $("#obj_{0}").ForceNumericOnly();'.format(index)
        if row[6]==1:
            #checking if it is empty or not
            pass
#==============================================================
#==============================================================
#==============================================================
#here i make form
# i put hv as validation for hacking purposes
    formhtml = ' <a href="#" onclick="submit_frm_'+f_english_form_name+'()">Post</a>  '+formhtml

    HV = ord_validation_mapping( py_db.encode(conv_array_to_str(objs_mapping)))
    #print HV
    script = '   <script type="text/javascript">  {0}  </script>'.format(script)
    formhtml= create_form_html( HV,f_english_form_name,formhtml+script)
    htm = []
    htm.append(formhtml)

    htm.append(objs_mapping)
    return htm
    # [0]=form HTML     [1]=form elements array   


def get_form_name_from_form_id(formID):
    return py_db.executeAndReturnRows("select f_english_form_name from tbl_forms where f_id = {0} limit 1".format(formID))[0][0]

def get_key_field_name_from_form_id(formID):
    return py_db.executeAndReturnRows("select f_key_field from tbl_forms where f_id = {0} limit 1".format(formID))[0][0]





# _type :   1= with grid new    2=no grid new  3=no grid edit
# 
# print read_form_from_database_and_generate_html_with_objects_map(1)[1]
# field id is filled when it is for editting 
def create_form(form_id,_type,user_id,fieldID=0):
    #print user_id
    formhtml = ""
#    print user_id
    #print fieldID
    # user_id user id is equals to field ID 
    f_english_form_name = get_form_name_from_form_id(form_id)
    #print f_english_form_name
    ff=read_form_from_database_and_generate_html_with_objects_map(form_id)

   #handling if grid is needed or this for edit or insert ??
   #in here i decide to put headers i mean how to put them  :)))  ???
   
    if _type==1:
        formhtml = create_validation_js_sctipt(True)+"""
        <table class="dynamic_form">
        <tbody><tr><td id="d1">{0}</td><td id="d2">{1}</td></tr></tbody></table>
        """.format(ff[0],create_grid(form_id,1))
    if _type == 2:
        formhtml = formhtml+"""
        {1}
        {2}
        {0}
        """.format(ff[0],header_script,create_validation_js_sctipt(True))
    if _type == 3:
        formhtml = formhtml+"""
        {1}
        {2}
        {0}
        """.format(ff[0],header_script,create_validation_js_sctipt(True))


    form_submit_script = create_post_js_script(f_english_form_name,'py_do.py',False)
    form_submit_script = form_submit_script 
    form_submit_script = '<script type="text/javascript"> {0} </script>'.format(form_submit_script)
   
    #retriving items js  data
    # here i have to put it end because by the following lines some global variables fills .
    edit_js = ""
    if fieldID != 0:
        #print edit_from_id
        edit_js = create_edit_script(ff[1],fieldID)   

   # print 
    return formhtml+form_submit_script+edit_js


edit_from_id=""
#print create_form('1', 1, '1')

def send_form(form_id):
    #form_id.__str__()+"?(xs)@"+row[0].__str__()+"?(xs)@"+ck[2].__str__()
    #[0] = formID   [1] = fieldID   [2] uID
    ff = py_db.unhash_decode_ord_conv_to_arr(edit_from_id).split("?(xs)@")
    #print ff
    formID = ff[0]
    fieldID = ff[1]
    #print ff
    #print ff
    return render_form(formID,3,ff[2],fieldID)



#_type = 1 = insert     2=update 3= edit
#form_name is   form_id !!!!
# field id is done when it is for editing
def render_form(form_id,_type,user_id,fieldID=0):
    return create_form(form_id,_type,user_id,fieldID )

