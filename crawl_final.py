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
        conn=pymysql.connect(user='root',passwd='123123',host='10.102.7.193',db='image')
        cur = conn.cursor()
        now=datetime.datetime.now() 
        for air_quality in air_quality_all:
            s=air_quality['pointname']
            s_name=""
            for s_temp in lazy_pinyin(s):
                s_name+=s_temp
            cur.execute("update all_quality set time='%s' where position='%s'"%(now.strftime('%Y%m%d%H%M%S'),s_name))
            cur.execute("update all_quality set AQI='%d' where position='%s'"%(int(air_quality['aqi']),s_name))
            cur.execute("update all_quality set PM25='%d' where position='%s'"%(int(air_quality['pm2_5']),s_name))
            cur.execute("update all_quality set PM10='%d' where position='%s'"%(int(air_quality['pm10']),s_name))
            conn.commit()
            path="D:\\air_quality\\%s.txt"%s_name
            with open(path,'a') as f:
                f.write(air_quality['aqi']+"   "+air_quality['pm2_5']+"   "+air_quality['pm10']+"   "+now.strftime('%Y%m%d%H%M%S')+'\n')
        cur.close()
        conn.close()
        time.sleep(inc)

crawl_air_quality(1800)
