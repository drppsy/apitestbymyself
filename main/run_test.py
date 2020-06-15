import sys
sys.path.append("D:/FETA/apitestbymyself")
from data_config.get_data import GetData
from base import run_method
import json

class RunTest():

    def __init__(self):
        self.testcases = GetData()
        self.run = run_method.RunMethod()

    def test_method(self):
        cases_num = self.testcases.get_case_lines()
        for i in range(1,cases_num):
            is_run = self.testcases.get_case_is_run(i)
            if is_run:
                url = self.testcases.get_case_url(i)
                method = self.testcases.get_request_method(i)
                request_data = self.testcases.get_request_data(i)
                headers = self.testcases.get_headers(i)
                # print(type(headers))
                res = self.run.run_main(url,method,request_data,headers)

run = RunTest()
res = run.test_method()
