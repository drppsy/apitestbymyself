import pymysql
import json

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(host='122.51.4.96',user='root',password='212233',port=3306,db='mysite',use_unicode=True,charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def search_one(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        res = json.dumps(res)
        return res

if __name__ == "__main__":
    op_mysql = OperationMysql()
    sql = "select * from blog_blogtype"
    res = op_mysql.search_one(sql)
    print(res)