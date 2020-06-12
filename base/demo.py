from requests import request
import json

class RunMethod():

    def run_post(self,url,method,data=None):
        res = request(url=url,method=method,data = data).json()
        res = json.dumps(res,indent=2)
        return res

    def run_get(self,url,method,data=None):
        res = request(url=url,method=method,data=data).json()
        res = json.dumps(res,indent=2)
        return res

    def run_main(self,url,method,data):
        res = None
        if method == 'POST':
            res = self.run_post(url,method,data)
        else:
            res = self.run_get(url,method,data)
        return  res

if __name__ == "__main__":
    url_one = "http://apitest.xiniujiao.net/api/v1/user/smscode"
    url_two = "http://apitest.xiniujiao.net/api/v1/plate/bbs"
    data_r = {"phone": "15618300212"}
    data = json.dumps(data_r)

    res = RunMethod()
    res = res.run_main(url_one,'POST',data)
    print(res)