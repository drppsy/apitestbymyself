import json
import os

root_path = os.path.abspath("..")


class OperaJson():

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open(root_path+'/data/request_data.json') as fp:
            data = json.load(fp)
            return data

    def get_data(self,key):
        return self.data[key]

# def test_opera_json():
#     data = OperaJson()
#     print(data.data)
#
#     print(data.data['phoneNumber'])
# test_opera_json()