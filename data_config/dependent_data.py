from base import run_method
from . import get_data
from jsonpath_rw import jsonpath,parse
import json
# import get_data

class DependData():

    def __init__(self):
        # self.excel = operate_excel.OperaExcel()
        self.data = get_data.GetData()

    def get_dependent_case_rowid(self,rowid):
        dependent_case_rowid = self.data.get_dependent_caseid_rowid_by_rowid(rowid)
        return dependent_case_rowid


    def get_res(self,rowid):
        dependent_case_rowid = self.get_dependent_case_rowid(rowid)
        url = self.data.get_request_url(dependent_case_rowid)
        request_method = self.data.get_request_method(dependent_case_rowid)
        request_data = self.data.get_request_data(dependent_case_rowid)
        headers = self.data.get_headers(dependent_case_rowid)
        run = run_method.RunMethod()
        res = run.run_main(method=request_method,url=url,data=request_data,headers=headers)
        return json.loads(res)

    def get_dependent_data_value(self,rowid):
        res = self.get_res(rowid)
        json_exep = self.data.get_dependent_data_json_exep(rowid)
        json_exe = parse(json_exep)
        madle = json_exe.find(res)
        return [math.value for math in madle][0]


# def test_depend_data():
#     dependdata = DependData()
#     res = dependdata.get_res(5)
#     print(res)
#
#     value = dependdata.get_dependent_data_value(5)
#     print(value)
#
# test_depend_data()
