# 该文件用于存放常量
class global_var:
    Id ='0'
    url = '2'
    is_run = '3'
    request_method = '4'
    headers = '5'
    request_data = '9'
    expect = '10'
    result = '11'

def get_caseid_colid():
    return int(global_var.Id)

def get_case_is_run_colid():
    return int(global_var.is_run)

def get_case_url_colid():
    return int(global_var.url)

def get_case_request_method():
    return int(global_var.request_method)

def get_case_headers_colid():
    return int(global_var.headers)

def get_case_request_data_colid():
    return int(global_var.request_data)

def get_case_expect_colid():
    return int(global_var.expect)

def get_case_result_colid():
    return int(global_var.result)
