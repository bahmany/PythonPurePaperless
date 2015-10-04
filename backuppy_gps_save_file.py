#!d:/Python27/python.exe -u 
# -*- coding: UTF-8 -*-

import cgi
import os
import cgitb
import uuid
import py_db
import py_gps
import thread
import time
import tempfile
    

cgitb.enable()

#py_db.checkAccessCookie()
#py_db.checkuser(3,py_db.username)



def beriz_too_dbclass(uid,str):
    cnt = py_gps.capture_gps_to_db(uid,str)




try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    print "import error"
    pass


#tmp_file = tempfile.TemporaryFile()
#temp_file.write(environ['wsgi.input'].read()) # or use buffered read()
#temp_file.seek(0)
#form = cgi.FieldStorage(fp=temp_file, environ=environ, keep_blank_values=True)
form = cgi.FieldStorage()

#uid=form.getvalue("uid","-1")
# A nested FieldStorage instance holds the file
fileitemArr=[]


print 'Content-Type: text/html; charset=utf-8'
print ""




fileitemArr.append(form['filecontent1'])
fileitemArr.append(form['filecontent2'])
fileitemArr.append(form['filecontent3'])
fileitemArr.append(form['filecontent4'])
fileitemArr.append(form['filecontent5'])
fileitemArr.append(form['filecontent6'])
fileitemArr.append(form['filecontent7'])
fileitemArr.append(form['filecontent8'])

# Test if the file was uploaded

message = ''
uploadedFileName = []
file_content=""
fr=""
for fileitem in fileitemArr:
    if fileitem.filename:
       #uuid.uuid1()
       # strip leading path from file name to avoid directory traversal attacks
        s = str(uuid.uuid1())
        fn = os.path.basename(s+"_"+fileitem.filename)
        file_content+=fileitem.file.read()
        #open('files/' + fn, 'wb').write(fileitem.file.read())
        #uf=[]
        #uf.append("file"+str(i))
        #uf.append(fileitem.filename)
        #uf.append(s+"_"+fileitem.filename)
        #uploadedFileName.append(uf)
        #message += 'The file "' + fileitem.filename + '" was uploaded successfully' +'<br/>'
        #1=richtext 2=scan 3=attachment 4=related letter id
        #py_db.executesql("insert into tbl_letters_papers (lp_type,lp_address,lp_link_to_letters) values (3,'{0}',{1}) ".format(
         #  s+"_"+fileitem.filename
         #  ,id)
        #)

html = """
<html>
<body>

</body>
<html>

"""
print 'Content-Type: text/html; charset=utf-8'
print ""
beriz_too_dbclass(uid,file_content)
#thread.start_new_thread(beriz_too_dbclass,(file_content,))
print "<a href="">بازگشت</a>   <script type='text/javascript'>  document.location.href = 'py_main.py?mid=15' </script>"
#print file_content
#print message
#print uploadedFileName
