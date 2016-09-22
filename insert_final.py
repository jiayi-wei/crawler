#encoding=utf-8
import pymysql
import sys


conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image',charset='utf-8')
cur = conn.cursor()
a = "万寿西宫"
tmp = a.decode('utf-8')
cur.execute("insert into all_quality(position, location) VALUES('%s','116.35_039.88')"%tmp)
conn.commit()
cur.close()
conn.close()
