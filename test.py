import aijsondb

def test_dominodb():
    path_data="data/500 KB_V2.json"
    path_schema="data/employeeSchemaDescription_V2.json"
    #path_data="C:/del/output_utf8.json"
    #path_schema="C:/del/output_utf8_schema.json"
    aijsondb.init_db(path_data,path_schema)
    query="var result=data.employees.length"
    res=aijsondb.query_data_javascript(query)
    print(res)

test_dominodb()