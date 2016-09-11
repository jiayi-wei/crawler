import pymysql

conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
cur = conn.cursor()
sql="insert into search(Position, Location) VALUES('wanshouxigong','116.35_039.88')"
cur.execute(sql)
onn.commit()
cur.close()
conn.close()
