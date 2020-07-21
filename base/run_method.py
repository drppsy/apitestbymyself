import requests
import json
from data_config import handle_ini

class RunMethod():

    def post_main(self,url,data=None,headers=None):
        data = json.dumps(data)
        if headers is not None:
            res = requests.post(url=url,data=data,headers=headers)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.get(url=url,params=data,headers=headers)
        else:
            res = requests.get(url=url,params=data)
        return res.json()

    def put_main(self,url,data=None,headers=None):
        data = json.dumps(data)
        if headers is not None:
            res = requests.put(url=url,data=data,headers=headers)
        else:
            res = requests.put(url=url,data=data)
        return res.json()

    def delete_main(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.delete(url=url,data=data,headers=headers)
        else:
            res = requests.delete(url=url,data=data)
        return res.json()

    def run_main(self,method,url,data=None,headers = None):
        res = None
        base_url = handle_ini.HandleIni().getIni('server','host')
        url = base_url + url
        if method == 'post':
            res = self.post_main(url=url,data=data,headers=headers)
        elif method == 'get':
            res = self.get_main(url=url,data=data,headers=headers)
        elif method == 'put':
            res = self.put_main(url=url,data=data,headers=headers)
        else:
            res = self.delete_main(url=url,data=data,headers=headers)
        res = json.dumps(res,ensure_ascii=False,indent=2)
        # print(res)
        return res


# def test_run_method():
#     run = RunMethod()
#     url_1 = "http://apitest.xiniujiao.net/api/v1/user/smscode"
#     request_data = {"phone": "15618300212"}
#     request_data = json.dumps(request_data)
#     url_2 = "http://apitest.xiniujiao.net/api/v1/plate/list/me"
#     res = run.run_main(method='post',url=url_1,data=request_data)
#     res2 = run.run_main(method='get',url=url_2)
#
# test_run_method()