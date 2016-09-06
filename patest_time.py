#encoding:UTF-8
import urllib.request
import re
import time
import os

def air_quality(inc=60):
    while True:
        url = 'http://www.pm25.com/city/beijing.html'
        response = urllib.request.urlopen(url)
        content=response.read().decode('utf-8')
        pattern = re.compile('<a class="pjadt_location".*?">(.*?)</a>.*?<span.*?>(.*?)<i class.*?pjadt_pm25">(.*?)<em.*?pjadt_pm10">(.*?)<em.*?div>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            print(item)
        print("------------\n")
        time.sleep(inc)

air_quality(10)


