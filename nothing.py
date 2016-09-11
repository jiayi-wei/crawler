import pymysql

conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
cur = conn.cursor()
cur.execute("CREATE VIEW [Current Product List] AS SELECT*FROM search WHERE Discontinued=No")
cur.execute("SELECT * FROM [Current Product List]")
conn.commit()
cur.close()
conn.close()
