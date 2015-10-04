def _map(array,Objname,dbname):
    ar=[]
    for objar in array:
        
        if objar[0]==Objname:
            objar.append(dbname)
        ar.append(objar)
    array=ar
            
def _find_from_field_name(array,fieldname):
    a=""
    for obj in array:
        if len(obj)==3:
            if obj[2]==fieldname:
                a=obj[1]
    return a
        
def _change_array_value(array,ObjectName,newValue):
    ar=[]
    for objar in array:
        if objar[0]==ObjectName:
            objar[1]==newValue
        ar.append(objar)
    array=ar
