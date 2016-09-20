# encoding: utf-8
import requests
import base64
import pprint
import json

url = "http://www.aqistudy.cn/api/getdata_citydetailinfo_memcache.php"
city = "北京"

city_encode = base64.b64encode(base64.b64encode(base64.b64encode(bytes(city,"UTF-8"))))

data = {'city': city_encode }

r = requests.post(url, data=data)

r_str=base64.b64decode(base64.b64decode(r.text)).decode('ascii')
print(r_str)

pprint.pprint(json.loads(r_str))

