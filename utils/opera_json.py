import json


class OperaJson():

    def __init__(self,filename=None):
        if filename is None:
            self.filename = '../data/request_data.json'
        else:
            self.filename = filename
        self.data = self.read_data()

    def read_data(self):
        with open(self.filename) as fp:
            data = json.load(fp)
            return data

    def get_data(self,key):
        return self.data[key]

    def write_data(self,jsobj):
        with open(self.filename,'w') as  fw:
            fw.write(jsobj)
            fw.close()


# def test_opera_json():
#     data = OperaJson()
#     print(data.data)
#
#     print(data.data['phoneNumber'])
#
#     filename = '../data/headers.json'
#     data = OperaJson(filename=filename)
#     res = {"aa":"11","bb":"22"}
#     jsobj = json.dumps(res)
#     data.write_data(jsobj)
#
#
# test_opera_json()