import requests
import base64
import json
import pprint
import datetime
import hashlib



url = "https://www.zq12369.com/api/zhenqiapi.php"
city = "北京"
method = "GETCITYPOINTPERIOD"
ty = "HOUR"
pointname = "通州新城"
timeend = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
timestart = (datetime.datetime.now()-datetime.timedelta(hours=27)).strftime("%Y-%m-%d %H:00:%S")

ID='a01901d3caba1f362d69474674ce477f'
secret_str = ID + method + str(base64.b64encode(bytes(city,"UTF-8"))) + str(base64.b64encode(bytes(pointname,"UTF-8"))) + ty + timestart + timeend
secret_string_long = secret_str.replace("\s","")
secret_md5 = hashlib.md5(secret_string_long.encode('utf-8'))
secret_md5.hexdigest()

data = {'appId': ID,
        'method': base64.b64encode(bytes(method,"UTF-8")),
        'city':base64.b64encode(bytes(city,"UTF-8")),
        'pointname': base64.b64encode(bytes(pointname,"UTF-8")),
        'type':base64.b64encode(bytes(ty,"UTF-8")),
        'startTime':base64.b64encode(bytes(timestart,"UTF-8")),
        'endTime':base64.b64encode(bytes(timeend,"UTF-8")),
        'secret':secret_md5.hexdigest()}
pprint.pprint(data)
r = requests.post(url, data = data)
print(r.text)
context=base64.b64decode(base64.b64decode(base64.b64decode(r.text))).decode('ascii')

point_info=json.loads(str(context))
pprint.pprint(point_info)
