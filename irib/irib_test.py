#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-


import sys
import MySQLdb
from classes import py_db


def prepare_farsi_alf(text):
    b=text
    b=b.replace('ي','ی')
    b=b.replace('آ','آ')
    b=b.replace('ش','ش')
    b=b.replace('ن','ن')
    b=b.replace('ا','ا')
    b=b.replace('ب','ب')
    b=b.replace(' ',' ')
    b=b.replace('ح','ح')
    b=b.replace('ك','ک')
    b=b.replace('م','م')
    b=b.replace('ه','ه')
    b=b.replace('ع','ع')
    b=b.replace('و','و')
    b=b.replace('ظ','ظ')
    b=b.replace('ق','ق')
    b=b.replace('ط','ط')
    b=b.replace('پ','پ')
    b=b.replace('د','د')
    

    
        

    print b    
    return b

#print ord("د")
#print ord("د")


rows = py_db.executeAndReturnRows("select * from mehvarz")
cco = 0
for row in rows:
    r1 = prepare_farsi_alf(row[1])
    py_db.executesql("""
                     update mehvarz set
                     _text = '{0}' where id='{1}'
                     """.format(r1,row[2]))
    cco += cco
    print cco
    
    
print "succ"
