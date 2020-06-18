from utils import operate_excel
from utils import opera_json
import json
from . import global_data_var
# import global_data_var


class GetData():

    def __init__(self):
        self.excel = operate_excel.OperaExcel()

    def get_lines(self):
        lines = self.excel.get_lines()
        return lines

    def get_is_run(self,rowid):
        colid = global_data_var.get_case_is_run_colid()
        flag = None
        is_run = self.excel.get_cell_value(rowid,colid)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_request_url(self,rowid):
        colid = global_data_var.get_case_url_colid()
        url = self.excel.get_cell_value(rowid,colid)
        return url

    def get_request_method(self,rowid):
        colid = global_data_var.get_case_request_method()
        request_method = self.excel.get_cell_value(rowid,colid)
        return request_method

    def get_request_data_field(self,rowid):
        colid = global_data_var.get_case_request_data_colid()
        request_data_field = self.excel.get_cell_value(rowid,colid)
        return request_data_field

    def get_expect(self,rowid):
        colid = global_data_var.get_case_expect_colid()
        expect = self.excel.get_cell_value(rowid,colid)
        return expect

    def get_request_data(self,rowid):
        request_data_field = self.get_request_data_field(rowid)
        request_data = opera_json.OperaJson().get_data(request_data_field)
        request_data = json.dumps(request_data)
        return request_data

    def get_headers(self,rowid):
        colid = global_data_var.get_case_headers_colid()
        token = self.excel.get_cell_value(rowid,colid)
        headers = {}
        headers['Access-Token'] = token
        return headers

    def write_result(self,rowid,value):
        colid = global_data_var.get_case_result_colid()
        self.excel.write_data(rowid,colid,value)

    def get_dependent_caseid(self,rowid):
        colid = global_data_var.get_dependent_caseid_colid()
        dependent_caseid = self.excel.get_cell_value(rowid,colid)
        return dependent_caseid

    def get_dependent_caseid_rowid_by_casesid(self,dependent_caseid):
        rowid = self.excel.get_rowid_by_cell_value(dependent_caseid)
        return rowid

    def get_dependent_caseid_rowid_by_rowid(self,rowid):
        dependent_caseid = self.get_dependent_caseid(rowid)
        dependent_rowid = self.get_dependent_caseid_rowid_by_casesid(dependent_caseid)
        return dependent_rowid

    def get_dependent_data_json_exep(self,rowid):
        colid = global_data_var.get_dependent_data_json_exep_colid()
        dependent_data_json_exep = self.excel.get_cell_value(rowid,colid)
        return dependent_data_json_exep

    def get_dependent_data_field(self,rowid):
        colid = global_data_var.get_dependent_data_filed_colid()
        dependent_data_field = self.excel.get_cell_value(rowid,colid)
        return dependent_data_field
#
# def test_get_data():
#     data = GetData()
#     lines = data.get_lines()
#     print(lines)
#
#     is_run = data.get_is_run(1)
#     print(is_run)
#
#     url = data.get_request_url(1)
#     print(url)
#
#     request_method = data.get_request_method(1)
#     print(request_method)
#
#     request_data = data.get_request_data(1)
#     print(request_data)
#
#     expect = data.get_expect(1)
#     print(expect)

#     request_data = data.get_request_data(1)
#     print(request_data)

    # dependent_caseid = data.get_dependent_caseid_rowid_by_rowid(5)
    # print(dependent_caseid)

# test_get_data()