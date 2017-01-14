import pymysql
import requests
import base64
import pprint
import json
from pypinyin import pinyin,lazy_pinyin
import pypinyin
import time
import datetime

def crawl_air_quality_bupt():
    url="http://220.195.3.56:7088/SensorApp_bupt/user/getLogin"
    para={'username':'bupt', 'password':'bupt'}
    now=datetime.datetime.now()
    timestamp=now.strftime('%Y-%m-%d %H')+':00:00'
    url_home="http://220.195.3.56:7088/SensorApp_bupt/monitoringDiagram/queryPointListByMeasurePointId"
    para_home={'id':'1243', 'timestamp':timestamp, 'page':'1'}
    s=requests.Session()
    s.post(url, data=para)
    r=s.post(url_home, data=para_home)
    print(r)
    da=json.loads(r.text)
    data=da['list'][0]
    path="D:\\air_quality\\bupt.txt"
    try:
        data_pm=round(data['pm25'])
        with open(path, 'a') as f:
            f.write(str(data_pm)+"   "+now.strftime('%Y%m%d%H%M%S')+'\n')
        try:
            conn=pymysql.connect(user='root',passwd='123123',host='10.102.0.194',db='image')
            cur = conn.cursor()
            str_location="116.357996_039.960736"
            cur.execute("insert into all_quality(Position, Location, time,AQI, PM25, PM10) VALUES('%s','%s','%s','%d','%d','%d')"%('bupt',str_location, now.strftime('%Y%m%d%H%M%S'),10000,data_pm,10000))
            conn.commit()       
            cur.close()
            conn.close()
        except:
            print("未能连接数据库")
            print("bupt")      
    except:
        print("no data!")
        print(now.strftime('%Y%m%d%H%M%S')+'\n')
    
    

def crawl_air_quality(inc=500):
    while(True):
        crawl_air_quality_bupt()
        time.sleep(inc)


crawl_air_quality(500)
