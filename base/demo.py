import requests


'''
请求体是表单形式，接口测试
'''

data = {"csrfmiddlewaretoken":"57eQhS9FzWFApVP3MLZ7bQPRpS2dolMroEtEkGMTucAzCSyN56YXDCNVe5CZmJJy","content_type":"blog",
        "object_id":25,"text":"1testttfortes212t","reply_comment_id":0}

headers = {'Cookie':'blog_25_read=true;csrftoken=ovza9hE2NqTVJKr4InIaxtid7CEaYgqZH2OYc5hgIGOUWHaO1IH0ZfghWPeWWEn6;sessionid=nh6p0sxlwki42mdsripygi40qy52du3j'}
res = requests.post('http://122.51.4.96/comment/update_comment',data=data,headers=headers).json()
print(res)




'''请求体是form-data 和 二进制文件的形式'''
request_data = {'remark':'ttest'}
headers = {'Access-Token':'_hbdev-admin'}
files = {'file':open('F:/apitestbymyself/data/wangzherongyao.xlsx','rb')}
res = requests.post('http://apitest.xiniujiao.net/api/v2/kit/admin/import/games/000008',data=request_data,headers=headers,files=files).json()
print(res)