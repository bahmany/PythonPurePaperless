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
newfile = form.getvalue("NewFile")
# Test if the file was uploaded
message = ''
i=0
uploadedFileName = []


i+=i+1
#uuid.uuid1()
# strip leading path from file name to avoid directory traversal attacks
s = str(uuid.uuid1())
fn = os.path.basename(s+"_1_.jpg")
filename=s+"_1_.jpg"
open('files/' + fn, 'wb').write(newfile)
sstrl="<script type=\"text/javascript\">(function(){var d=document.domain;while (true){try{var A=window.top.opener.document.domain;break;}catch(e) {};d=d.replace(/.*?(?:\.|$)/,'');if (d.length==0) break;try{document.domain=d;}catch (e){break;}}})();window.parent.OnUploadCompleted(0,'/files/"+filename+"','"+filename+"','') ;</script>"
print 'Content-Type: text/html; charset=utf-8'
print ''
print sstrl
#print message
#print uploadedFileName
