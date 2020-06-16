import json

class OperaJson():

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open('../data/request_data.json') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        return self.data[id]


# def test_opera_json():
#     json_data = OperaJson()
#     data = json_data.read_data()
#     print(data)
#     print(data['phoneNumber'])
#
# test_opera_json()
