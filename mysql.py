import pymysql

con = pymysql.connect(host = '10.102.7.193',port = 3306,user = "root",passwd = "123123",db = "image",charset = 'UTF8')
cursor = con.cursor()
cursor.excute("select version()")
for i in cursor:
    print(i)
cursor.close()
con.close()
