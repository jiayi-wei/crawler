import pymysql

conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
cur = conn.cursor()
cur.execute("delete from search where position='wanshouxigong'")
conn.commit()
cur.close()
conn.close()
