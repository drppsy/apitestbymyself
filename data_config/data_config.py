# 该文件用于定义excel中常量的列号/col

class global_var:
    Id = 0
    url = 2
    is_run  =3
    request_method = 4
    headers = 5
    dependent_case_id = 6
    dependent_case_data = 7
    request_data = 8
    expect = 9
    results = 10

def id_colid():
    return global_var.Id

def url_colid():
    return global_var.url

def is_run_colid():
    return global_var.is_run

def request_method_colid():
    return global_var.request_method

def headers_colid():
    return global_var.headers

def request_data_colid():
    return global_var.request_data

def expect_colid():
    return global_var.expect