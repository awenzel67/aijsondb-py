import ctypes
import json
import platform
import os
libaijsondb=None
path = os.path.dirname(os.path.abspath(__file__))
system = platform.system()
if system == "Windows":
    libaijsondb=ctypes.WinDLL(path + '/aijsondbc.dll')
elif system=="Linux":
    libaijsondb=ctypes.CDLL(path + '/libaijsondbc.so')
else:
    raise Exception("Unsupported platform")

def init_db(data_path,schema_path):
    global libaijsondb 
    if libaijsondb == None:
        raise Exception("Dominodb library not loaded")
    
    b_data_path=data_path.encode()
    c_data_path = ctypes.c_char_p(b_data_path)
    b_schema_path=schema_path.encode()
    c_schema_path = ctypes.c_char_p(b_schema_path)
    ret=libaijsondb.ffi_aijsondb_load_data(c_data_path,c_schema_path)
    if ret != 0:
        raise Exception("Failed to load data")

def query_data_javascript(query):
    global libaijsondb 
    if libaijsondb == None:
        return
    buffer = ctypes.create_string_buffer(1024*1000) 

    query_domino_db_o=query

    query_domino_db=query_domino_db_o.encode('utf8')

    cquery=ctypes.c_char_p(query_domino_db)

    retq=libaijsondb.ffi_aijsondb_query(cquery,buffer,1024*1000)
    if retq==0:
        sjson=buffer.value.decode()
        ##print("Query with qjs")
        ##print(sjson)
        if len(sjson)>1024*10*10:
            #print(len(sjson))
            #print(sjson)
            raise ValueError("Data to big!")
        return json.loads(sjson)
    else:
        serror=buffer.value.decode()
        #print(serror)
        raise Exception(serror)