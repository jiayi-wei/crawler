import pymysql
import requests
import base64
import pprint
import json
from pypinyin import pinyin,lazy_pinyin
import pypinyin
import time
import datetime

def crawl_air_quality_beijing():
    url = "http://www.aqistudy.cn/api/getdata_citydetailinfo_memcache.php"
    city = "北京"
    city_encode = base64.b64encode(base64.b64encode(base64.b64encode(bytes(city,"UTF-8"))))
    data = {'city': city_encode }
    r = requests.post(url, data=data)
    print(r.text)
    r_str=base64.b64decode(base64.b64decode(r.text)).decode('ascii')
    air={}
    nor_len=r_str.find("}}",0,len(r_str))+2
    if(nor_len != len(r_str)):
        r_str=r_str[0:nor_len]
    air=json.loads(r_str)
    air_quality_all=air['rows']
    now=datetime.datetime.now()
    for air_quality in air_quality_all:
        s=air_quality['pointname']
        s_name=""
        for s_temp in lazy_pinyin(s):
            s_name+=s_temp
        path="D:\\air_quality\\%s.txt"%s_name
        if air_quality['aqi']=="0":
            air_quality['aqi']="10000"
        if air_quality['pm2_5']=="0":
            air_quality['pm2_5']="10000"
        if air_quality['pm10']=="0":
            air_quality['pm10']="10000"
        with open(path,'a') as f:
            f.write(air_quality['aqi']+"   "+air_quality['pm2_5']+"   "+air_quality['pm10']+"   "+now.strftime('%Y%m%d%H%M%S')+'\n')
    try:
        conn=pymysql.connect(user='root',passwd='123123',host='10.102.0.194',db='image')
        cur = conn.cursor()
        for air_quality in air_quality_all:
            s=air_quality['pointname']
            s_name=""
            for s_temp in lazy_pinyin(s):
                s_name+=s_temp
            cur.execute("insert into all_quality(Position, Location, time, AQI, PM25, PM10) VALUES('%s','%s','%s','%d','%d','%d')"%(s_name,air_quality['longitude'][0:10]+"_0"+air_quality['latitude'][0:9],now.strftime('%Y%m%d%H%M%S'),int(air_quality['aqi']),int(air_quality['pm2_5']),int(air_quality['pm10'])))
            conn.commit()            
        cur.close()
        conn.close()
    except:
        print("未能连接数据库")
        print("all") 
    

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
        crawl_air_quality_beijing()
        crawl_air_quality_bupt()
        time.sleep(inc)


crawl_air_quality(500)
