import os, sys


path = 'D:/xampp/htdocs/ams'
if path not in sys.path:
    sys.path.append(path)

#sys.path.append('C:/xampp/htdocs/ams')


#print "____________________________________________________"
#print path
os.environ['DJANGO_SETTINGS_MODULE'] = 'ams.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()