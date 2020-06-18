import sys
sys.path.append('D:/FETA/apitestbymyself')
from base import run_method
from data_config import get_data
from utils import common_util
from data_config import dependent_data
import json

class RunTest():

    def __init__(self):
        self.run = run_method.RunMethod()
        self.testcases = get_data.GetData()
        self.is_contain = common_util.CommonUtil()
        self.depend_data = dependent_data.DependData()

    def run_main(self):
        lines = self.testcases.get_lines()
        for i in range(1,lines):
            is_run = self.testcases.get_is_run(i)
            if is_run:
                url = self.testcases.get_request_url(i)
                request_data = self.testcases.get_request_data(i)
                request_data = json.loads(request_data)
                request_method = self.testcases.get_request_method(i)
                headers = self.testcases.get_headers(i)
                expect = self.testcases.get_expect(i)
                dependent_data = self.testcases.get_dependent_caseid(i)
                if dependent_data != "":
                    dependent_data_value = self.depend_data.get_dependent_data_value(i)
                    dependent_data_field = self.testcases.get_dependent_data_field(i)
                    request_data[dependent_data_field] = dependent_data_value

                res = self.run.run_main(method=request_method,url=url,data=request_data,headers=headers)

                if self.is_contain.is_contain(expect,str(res)):
                    self.testcases.write_result(i,'pass')
                else:
                    self.testcases.write_result(i,res)
            i += 1


if __name__ == '__main__':
    run = RunTest()
    run.run_main()
