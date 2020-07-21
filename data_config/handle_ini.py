import configparser

class HandleIni:

    def loadIni(self):
        file_path = "../data_config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8-sig')
        return cf

    def getIni(self,section,key):
        cf = self.loadIni()
        data = cf.get(section,key)
        return data

# def test_handle_ini():
#     hi = HandleIni()
#     base_url = hi.getIni('server','username')
#     print(base_url)
#
# test_handle_ini()