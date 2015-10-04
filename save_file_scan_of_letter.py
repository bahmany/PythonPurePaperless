#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()
import uuid
import py_db

    



py_db.checkAccessCookie()
py_db.checkuser(3,py_db.username)



try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()
id=form.getvalue("id")
# A nested FieldStorage instance holds the file
fileitemArr=[]
fileitemArr.append(form['file1'])


# Test if the file was uploaded
message = ''
i=0
uploadedFileName = []

for fileitem in fileitemArr:
    if fileitem.filename:
        i+=i+1
       #uuid.uuid1()
       # strip leading path from file name to avoid directory traversal attacks
        s = "abs"+str(uuid.uuid1())

        fn = os.path.basename(s+"_"+fileitem.filename)
        open('files/' + fn, 'wb').write(fileitem.file.read())
        uf=[]
        uf.append("file"+str(i))
        uf.append(fileitem.filename)
        uf.append(s+"_"+fileitem.filename)
        uploadedFileName.append(uf)
        message += 'The file "' + fileitem.filename + '" was uploaded successfully' +'<br/>'
        #1=richtext 2=scan 3=attachment 4=related letter id
        py_db.executesql("insert into tbl_letters_papers (lp_type,lp_address,lp_link_to_letters) values (2,'{0}',{1}) ".format(
           s+"_"+fileitem.filename
           ,id)
        )

print "Location: py_main.py?mid=2&id="+id
print ""
#print message
#print uploadedFileName
