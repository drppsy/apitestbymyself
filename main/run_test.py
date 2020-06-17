import sys
sys.path.append('D:/FETA/apitestbymyself')
from base import run_method
from data_config import get_data

class RunMethod():

    def __init__(self):
        self.run = run_method.RunMethod()
        self.testcases = get_data.GetData()

    def run_main(self):
        lines = self.testcases.get_lines()
        for i in range(1,lines):
            is_run = self.testcases.get_is_run(i)
            if is_run:
                url = self.testcases.get_request_url(i)
                request_data = self.testcases.get_request_data(i)
                request_method = self.testcases.get_request_method(i)
                headers = self.testcases.get_headers(i)
                self.run.run_main(method=request_method,url=url,data=request_data,headers=headers)
            i += 1

res = RunMethod()
res.run_main()
