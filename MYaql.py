import pymysql

conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
cur = conn.cursor()
cur.execute("SELECT * FROM search")
for r in cur:      
      print("row_number:" , (cur.rownumber) )        
      print("time:"+str(r[0])+"   location:"+str(r[1])+"   AQI:"+str(r[2])) 
cur.close()    
conn.close()
