import pymysql
import requests
import base64
import pprint
import json
from pypinyin import pinyin,lazy_pinyin
import pypinyin
import time
import datetime

def crawl_air_quality(inc=1800):
    while True:
        url = "http://www.aqistudy.cn/api/getdata_citydetailinfo_memcache.php"
        city = "北京"
        city_encode = base64.b64encode(base64.b64encode(base64.b64encode(bytes(city,"UTF-8"))))
        data = {'city': city_encode }
        r = requests.post(url, data=data)
        r_str=base64.b64decode(base64.b64decode(r.text)).decode('ascii')
        air={}
        try:
            air=json.loads(r_str)
        except:
            time.sleep(300)
            continue
        air_quality_all=air['rows']
        try:
            conn=pymysql.connect(user='root',passwd='123123',host='10.102.0.194',db='image')
            cur = conn.cursor()
        except:
            time.sleep(300)
            continue;
        now=datetime.datetime.now() 
        for air_quality in air_quality_all:
            s=air_quality['pointname']
            s_name=""
            for s_temp in lazy_pinyin(s):
                s_name+=s_temp
            cur.execute("insert into all_quality(Position, Location, time, AQI, PM25, PM10) VALUES('%s','%s','%s','%d','%d','%d')"%(s_name,air_quality['longitude'][0:6]+"_0"+air_quality['latitude'][0:5],now.strftime('%Y%m%d%H%M%S'),int(air_quality['aqi']),int(air_quality['pm2_5']),int(air_quality['pm10'])))
            conn.commit()
            path="D:\\air_quality\\%s.txt"%s_name
            with open(path,'a') as f:
                f.write(air_quality['aqi']+"   "+air_quality['pm2_5']+"   "+air_quality['pm10']+"   "+now.strftime('%Y%m%d%H%M%S')+'\n')
        cur.close()
        conn.close()
        time.sleep(inc)

crawl_air_quality(1800)
