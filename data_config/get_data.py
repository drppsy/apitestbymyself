from . import data_config
# import data_config
from util import operate_excel

class GetData():

    def __init__(self):
        self.excel = operate_excel.OperaExcel()

    def get_case_id(self,rowid):
        colid = data_config.id_colid()
        case_id = self.excel.get_cell_value(rowid,colid)
        return case_id


    def get_case_lines(self):
        case_lines = self.excel.get_table_lines()
        return case_lines

    def get_case_url(self,rowid):
        colid = data_config.url_colid()
        url = self.excel.get_cell_value(rowid,colid)
        return url

    def get_case_is_run(self,rowid):
        colid = data_config.is_run_colid()
        is_run = self.excel.get_cell_value(rowid,colid)
        flag = None
        if is_run == "yes":
            flag = True
        else:
            flag = False
        return flag

    def get_request_method(self,rowid):
        colid = data_config.request_method_colid()
        request_method = self.excel.get_cell_value(rowid,colid)
        return request_method

    def get_headers(self,rowid):
        colid = data_config.headers_colid()
        token = self.excel.get_cell_value(rowid,colid)
        if token == "no":
            return None
        else:
            headers = {}
            headers['Access-Token'] = token
            return headers

    def get_request_data(self,rowid):
        colid = data_config.request_data_colid()
        request_data = self.excel.get_cell_value(rowid,colid)
        return request_data

    def get_expect(self,rowid):
        colid = data_config.expect_colid()
        expect = self.excel.get_cell_value(rowid,colid)
        return expect

# def test_get_data():
#     testcases = GetData()
#
#     caseid = testcases.get_case_id(1)
#     print(caseid)
#
#     case_lines = testcases.get_case_lines()
#     print(case_lines)
#
#     case_url = testcases.get_case_url(1)
#     print(case_url)
#
#     is_run = testcases.get_case_is_run(1)
#     print(is_run)
#
#     request_method = testcases.get_request_method(1)
#     print(request_method)
#
#     headers = testcases.get_headers(2)
#     print(headers)
#
#     request_data = testcases.get_request_data(1)
#     print(request_data)
#
#     expect = testcases.get_expect(1)
#     print(expect)
#
# test_get_data()