import pymysql
conn = pymysql.connect(host="122.51.4.96",user="root",password="​212233",port=3306,db="mysite",charset='utf8')
cursor = conn.cursor()

sql = "select * from blog_blog"
test = cursor.execute(sql)
print(test)
