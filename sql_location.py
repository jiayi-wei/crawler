import pymysql

conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
cur = conn.cursor()
cur.execute("insert into air_quality(Position, Location) VALUES('wanshouxigong','116.35_039.88')")
cur.execute("insert into air_quality(Position, Location) VALUES('dongsi','116.42_039.93')")
cur.execute("insert into air_quality(Position, Location) VALUES('nongzhanguan','116.47_039.94')")
cur.execute("insert into air_quality(Position, Location) VALUES('guanyuan','116.34_039.93')")
cur.execute("insert into air_quality(Position, Location) VALUES('shunyi','116.66_040.13')")
cur.execute("insert into air_quality(Position, Location) VALUES('huairou','116.63_040.33')")
cur.execute("insert into air_quality(Position, Location) VALUES('aoti','116.40_039.90')")
cur.execute("insert into air_quality(Position, Location) VALUES('embassy','116.47_039.96')")
cur.execute("insert into air_quality(Position, Location) VALUES('wanliu','116.29_039.99')")
cur.execute("insert into air_quality(Position, Location) VALUES('changping','116.23_040.22')")
cur.execute("insert into air_quality(Position, Location) VALUES('dingling','116.22_039.29')")
cur.execute("insert into air_quality(Position, Location) VALUES('tiantan','116.41_039.89')")
cur.execute("insert into air_quality(Position, Location) VALUES('gucheng','116.19_039.92')")
conn.commit()
cur.close()
conn.close()
