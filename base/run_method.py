import requests
import json

class RunMethod():

    def run_post(self,url,data,headers):
        res = requests.post(url=url,data = data,headers=headers).json()
        res = json.dumps(res,indent=2)
        return res

    def run_get(self,url,data,headers):
        res = requests.get(url=url,params=data,headers=headers).json()
        res = json.dumps(res,indent=2)
        return res

    def run_main(self,url,method,data=None,headers=None):
        res = None
        if method == 'POST':
            res = self.run_post(url=url,data=data,headers=headers)
        else:
            res = self.run_get(url=url,data=data,headers=headers)
        print(res)
        return res
