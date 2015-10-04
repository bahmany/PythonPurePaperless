#!c:/Python27/python.exe -u
# -*- coding: UTF-8 -*-
import MySQLdb
import cgi
import sys
import cgitb
import py_convert_cgi_form_to_array_with_mapping
import py_db
cgitb.enable()


print 'Content-Type: text/html; charset=utf-8'
print ''



py_db.checkAccessCookie()
username = py_db.username
py_db.checkuser("1",username)



db = py_db.GetDB()

form = cgi.FieldStorage()

dt=form.getvalue("frmd")

ObjectsArray = str(dt).split(",")
i=0
newObjectsArray=[]
 
for objar in ObjectsArray:
    newObjectsArray.append(objar.split(":"))
    
# here we have to start mapping data
#creating object from class
mp = py_convert_cgi_form_to_array_with_mapping

type_of_letter = 0

if newObjectsArray[0][1]=="true":
    mp._map(newObjectsArray, "obj_Text1", "l_creator_company_link")
    mp._map(newObjectsArray, "obj_Text2", "l_creator_person_link");
    mp._map(newObjectsArray, "obj_Radio1", "l_type_link");
    mp._map(newObjectsArray, "obj_Text3", "l_date_of_create");
    mp._map(newObjectsArray, "obj_Text4", "l_type_of_recieve_link");
    mp._map(newObjectsArray, "obj_Text13", "l_letter_number");
    type_of_letter = 1
    #py_db.checkAccessCookie()
    #py_db.checkuser("7",py_db.username)
    
if newObjectsArray[1][1]=="true":
    mp._map(newObjectsArray, "obj_Text5", "l_creator_company_link")
    mp._map(newObjectsArray, "obj_Text6", "l_creator_person_link");
    mp._map(newObjectsArray, "obj_Radio2", "l_type_link");
    mp._map(newObjectsArray, "obj_Text7", "l_date_of_create");
    mp._map(newObjectsArray, "obj_Text8", "l_type_of_recieve_link");
    #mp._map(newObjectsArray, "uname", username);
    type_of_letter = 2
    #py_db.checkAccessCookie()
    #py_db.checkuser("8",py_db.username)


if newObjectsArray[2][1]=="true":
    mp._map(newObjectsArray, "obj_Text9", "l_creator_person_link");
    mp._map(newObjectsArray, "obj_Text1", "l_creator_company_link");
    mp._change_array_value(newObjectsArray,"obj_Text1",mp._find_from_field_name(newObjectsArray,"obj_Text9"));
    mp._map(newObjectsArray, "obj_Text11", "l_date_of_create");
    mp._map(newObjectsArray, "obj_Text12", "l_type_of_recieve_link");
    #mp._map(newObjectsArray, "uname", username);
    type_of_letter = 3
    #py_db.checkAccessCookie()
    #py_db.checkuser("9",py_db.username)

    

mp._map(newObjectsArray, "obj_Text18", "l_letter_to_link");
mp._map(newObjectsArray, "obj_Text17", "l_attachment_count");
mp._map(newObjectsArray, "obj_Text14", "l_date_of_letter");
mp._map(newObjectsArray, "editable", "editable");
mp._map(newObjectsArray, "obj_Text19", "l_subject");
mp._map(newObjectsArray, "uname", username);




#print newObjectsArray 

#l_creator_company_link,
#l_creator_person_link,
#l_type_link,
#l_letter_to_link,
#l_type_of_recieve_link,
#l_date_of_create,
#l_attachment_count,
#l_letter_number,
#l_date_of_letter
if type_of_letter <> 3:
    sqlstring = " '{0}','{1}',{2},'{3}','{4}','{5}',{6},'{7}','{8}','{9}','{11}','{10}'".format(
        mp._find_from_field_name(newObjectsArray,"l_creator_company_link"),
        mp._find_from_field_name(newObjectsArray,"l_creator_person_link"),
        type_of_letter,
        mp._find_from_field_name(newObjectsArray,"l_letter_to_link"),
        mp._find_from_field_name(newObjectsArray,"l_type_of_recieve_link"),
        mp._find_from_field_name(newObjectsArray,"l_date_of_create"),
        mp._find_from_field_name(newObjectsArray,"l_attachment_count"),
        mp._find_from_field_name(newObjectsArray,"l_letter_number"),
        mp._find_from_field_name(newObjectsArray,"l_date_of_letter"),
        mp._find_from_field_name(newObjectsArray,"editable"),
        mp._find_from_field_name(newObjectsArray,"l_subject"),
        py_db.username
        

        )
else:
    sqlstring = " '{1}','{1}',{2},'{3}','{4}','{5}',{6},'{7}','{8}','{9}','{11}','{10}'".format(
        mp._find_from_field_name(newObjectsArray,"l_creator_company_link"),
        mp._find_from_field_name(newObjectsArray,"l_creator_person_link"),
        type_of_letter,
        mp._find_from_field_name(newObjectsArray,"l_letter_to_link"),
        mp._find_from_field_name(newObjectsArray,"l_type_of_recieve_link"),
        mp._find_from_field_name(newObjectsArray,"l_date_of_create"),
        mp._find_from_field_name(newObjectsArray,"l_attachment_count"),
        mp._find_from_field_name(newObjectsArray,"l_letter_number"),
        mp._find_from_field_name(newObjectsArray,"l_date_of_letter"),
        mp._find_from_field_name(newObjectsArray,"editable"),
        mp._find_from_field_name(newObjectsArray,"l_subject"),
        py_db.username
        )
#print newObjectsArray    
    
                       




idof=form.getvalue("id","-1")
if idof=="-1":
    sqlstring=" call proc_insert_into_tbl_letters ("+sqlstring+")"
else:
    sqlstring=" call proc_update_into_tbl_letters ("+idof+","+sqlstring+")"

#print sqlstring


okk = 0
# restricting user
if (type_of_letter == 1 and idof=="-1"):
    if (py_db.checkuser(7,py_db.username)[3]<>3):
        okk = 1
if (type_of_letter == 2 and idof=="-1"):
    if (py_db.checkuser(8,py_db.username)[3]<>3):
        okk = 1
if (type_of_letter == 3 and idof=="-1"):
    if (py_db.checkuser(9,py_db.username)[3]<>3):
        okk = 1

if (type_of_letter == 1 and idof!="-1"):
    if (py_db.checkuser(11,py_db.username)[3]<>3):
        okk = 1
if (type_of_letter == 2 and idof!="-1"):
    if (py_db.checkuser(12,py_db.username)[3]<>3):
        okk = 1
if (type_of_letter == 3 and idof!="-1"):
    if (py_db.checkuser(13,py_db.username)[3]<>3):
        okk = 1


if okk==1:
    cur = db.cursor()
    cur.execute(sqlstring)
    db.commit()
    db.close()
    print "1"
else:
    print "2:شما به مجوز های لازم دسترسی ندارید"

#print py_db.checkuser(7,py_db.username)


