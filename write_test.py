#encoding:UTF-8
import urllib.request
import re
import time
import os

path_wanshou_china="D:\\weather\\wanshou_china.txt"
path_wanshou_USA="D:\\weather\\wanshou_USA.txt"

path_dingling_china="D:\\weather\\dingling_china.txt"
path_dingling_USA="D:\\weather\\dingling_USA.txt"

path_dongsi_china="D:\\weather\\dongsi_china.txt"
path_dongsi_USA="D:\\weather\\dongsi_USA.txt"

path_tiantan_china="D:\\weather\\tiantan_china.txt"
path_tiantan_USA="D:\\weather\\tiantan_USA.txt"

path_nongzhanguan_china="D:\\weather\\nongzhanguan_china.txt"
path_nongzhanguan_USA="D:\\weather\\nongzhanguan_USA.txt"

path_guanyuan_china="D:\\weather\\guanyuan_china.txt"
path_guanyuan_USA="D:\\weather\\guanyuan_USA.txt"

path_wanliu_china="D:\\weather\\wanliu_china.txt"
path_wanliu_USA="D:\\weather\\wanliu_USA.txt"

path_shunyi_china="D:\\weather\\shunyi_china.txt"
path_shunyi_USA="D:\\weather\\shunyi_USA.txt"

path_huairou_china="D:\\weather\\huairou_china.txt"
path_huairou_USA="D:\\weather\\huairou_USA.txt"

path_changping_china="D:\\weather\\changping_china.txt"
path_changping_USA="D:\\weather\\changping_USA.txt"

path_olympic_china="D:\\weather\\olympic_china.txt"
path_olympic_USA="D:\\weather\\olympic_USA.txt"

path_gucheng_china="D:\\weather\\gucheng_china.txt"
path_gucheng_USA="D:\\weather\\gucheng_USA.txt"

path_embassy_china="D:\\weather\\embassy_china.txt"
path_embassy_USA="D:\\weather\\embassy_USA.txt"

def air_quality(inc=3600):
    while True:
        url = 'http://www.pm25.com/city/beijing.html'
        response = urllib.request.urlopen(url)
        content=response.read().decode('utf-8')
        pattern = re.compile('<a class="pjadt_location".*?">(.*?)</a>.*?<span.*?>(.*?)<i class.*?pjadt_pm25">(.*?)<em.*?pjadt_pm10">(.*?)<em.*?div>',re.S)
        items = re.findall(pattern,content)
        for i in range(len(items)):
            if items[i][0]=="万寿西宫":
                if i<12 :
                    with open(path_wanshou_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_wanshou_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="定陵":
                if i<12 :
                    with open(path_dingling_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_dingling_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="东四":
                if i<12 :
                    with open(path_dongsi_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_dongsi_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')        
            elif items[i][0]=="天坛":
                if i<12 :
                    with open(path_tiantan_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_tiantan_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="农展馆":
                if i<12 :
                    with open(path_nongzhanguan_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_nongzhanguan_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="官园":
                if i<12 :
                    with open(path_guanyuan_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_guanyuan_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="海淀区万柳":
                if i<12 :
                    with open(path_wanliu_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_wanliu_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="顺义新城":
                if i<12 :
                    with open(path_shunyi_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_shunyi_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')   
            elif items[i][0]=="怀柔镇":
                if i<12 :
                    with open(path_huairou_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_huairou_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="昌平镇":
                if i<12 :
                    with open(path_changping_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_changping_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="奥体中心":
                if i<12 :
                    with open(path_olympic_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_olympic_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="古城":
                if i<14 :
                    with open(path_gucheng_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=14:
                     with open(path_gucheng_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
            elif items[i][0]=="美国大使馆":
                if i<12 :
                    with open(path_embassy_china,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
                elif i>=12:
                     with open(path_embassy_USA,'a') as f:
                        f.write(items[i][1]+"   "+items[i][2]+"   "+items[i][3]+'\n')
        time.sleep(inc)

air_quality(3600)        
