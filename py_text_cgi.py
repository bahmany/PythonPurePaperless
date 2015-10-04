#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-


reqdata="""-----------------------------4242\r
Content-Disposition: form-data; name="param1"\r
\r
Value of param1\r
-----------------------------4242\r
Content-Disposition: form-data; name="param2"\r
\r
Value of param2\r
-----------------------------4242\r
Content-Disposition: form-data; name="file"; filename=""\r
Content-Type: application/octet-stream\r
\r
\r
-----------------------------4242\r
"""

print len(reqdata)
headers={'QUERY_STRING': 'extraarg=extra',
	'CONTENT_LENGTH': str(len(reqdata)),
	'REQUEST_METHOD': 'POST',
	'CONTENT_TYPE': 'multipart/form-data; boundary=---------------------------4242' 
	}

import cgi, cStringIO

fs = cgi.FieldStorage(environ=headers, fp=cStringIO.StringIO(reqdata))
print fs


 	  	 