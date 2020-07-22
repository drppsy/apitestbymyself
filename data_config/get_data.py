from utils import operate_excel
from utils import opera_json
import json
from jsonpath_rw import parse
from base import run_method
from . import global_data_var
# import global_data_var

class GetData():

    def __init__(self):
        self.excel = operate_excel.OperaExcel()
        self.run = run_method.RunMethod()

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
        if request_data_field == '':
            request_data = None
        else:
            request_data = opera_json.OperaJson().get_data(request_data_field)
            request_data = json.loads(json.dumps(request_data))
        return request_data

    def get_headers(self,rowid):
        colid = global_data_var.get_case_headers_colid()
        headers_val = self.excel.get_cell_value(rowid,colid)
        if headers_val == '':
            headers = None
        elif "_hbdev-" in headers_val:
            headers = {}
            headers['Access-Token'] = headers_val
        else:
            headers = {}
            headers['Access-Token'] = self.get_dependent_data_value_for_headers(rowid)
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

    def get_dependent_data_key(self,rowid):
        colid = global_data_var.get_dependent_data_key_colid()
        dependent_data_key = self.excel.get_cell_value(rowid,colid)
        return dependent_data_key

    def get_headers_dependent_caseid(self,rowid):
        colid = global_data_var.get_case_headers_colid()
        headers_dependent_caseid = self.excel.get_cell_value(rowid,colid)
        return headers_dependent_caseid

    def get_headers_dependent_caseid_rowid_by_casesid(self,headers_dependent_caseid):
        headers_rowid = self.excel.get_rowid_by_cell_value(headers_dependent_caseid)
        return headers_rowid

    def get_headers_dependent_caseid_rowid_by_rowid(self,rowid):
        headers_dependent_caseid = self.get_headers_dependent_caseid(rowid)
        headers_dependent_rowid = self.get_headers_dependent_caseid_rowid_by_casesid(headers_dependent_caseid)
        return headers_dependent_rowid

    def get_headers_dependent_case_rowid(self,rowid):
        headers_dependent_case_rowid = self.get_headers_dependent_caseid_rowid_by_rowid(rowid)
        return headers_dependent_case_rowid

    def get_res_for_headers(self, rowid):
        dependent_case_rowid = self.get_headers_dependent_case_rowid(rowid)
        url = self.get_request_url(dependent_case_rowid)
        request_method = self.get_request_method(dependent_case_rowid)
        request_data = self.get_request_data(dependent_case_rowid)
        headers = self.get_headers(dependent_case_rowid)
        res = self.run.run_main(method=request_method, url=url, data=request_data, headers=headers)
        return json.loads(res)

    def get_dependent_data_value_for_headers(self,rowid):
        res = self.get_res_for_headers(rowid)
        json_path = self.get_dependent_data_key(rowid)
        json_path = parse(json_path)
        madle = json_path.find(res)
        return [item.value for item in madle][0]

# def test_get_data():
#     data = GetData()
    # lines = data.get_lines()
    # print(lines)
    #
    # is_run = data.get_is_run(1)
    # print(is_run)
    #
    # url = data.get_request_url(1)
    # print(url)
    #
    # request_method = data.get_request_method(1)
    # print(request_method)
    #
    # request_data = data.get_request_data(1)
    # print(request_data)
    #
    # expect = data.get_expect(1)
    # print(expect)
    #
    # request_data = data.get_request_data(1)
    # print(request_data)
    #
    # dependent_caseid = data.get_dependent_caseid_rowid_by_rowid(5)
    # print(dependent_caseid)

#     headers = data.get_headers(3)
#     print(headers)
#
# test_get_data()