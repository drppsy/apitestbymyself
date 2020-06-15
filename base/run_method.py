import requests
import json

class RunMethod():

    def run_post(self,url,data,headers=None):
        res = None
        if headers is not None:
            res = requests.post(url=url,data = data,headers=headers)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def run_get(self,url,data=None,headers=None):
        res = None
        if headers is not None:
            res = requests.get(url=url,params=data,headers=headers)
        else:
            res = requests.get(url=url,params=data)
        return res.json()

    def run_main(self,url,method,data=None,headers=None):
        res = None
        if method == 'POST':
            res = self.run_post(url,data,headers)
        else:
            res = self.run_get(url,data,headers)
        res = json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        print(res)
        return res

