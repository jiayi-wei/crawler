#encoding:UTF-8
import urllib.request
import re 

url = 'http://www.pm25.com/city/beijing.html'
response = urllib.request.urlopen(url)
content=response.read().decode('utf-8')
pattern = re.compile('<a class="pjadt_location".*?">(.*?)</a>.*?<span.*?>(.*?)<i class.*?pjadt_pm25">(.*?)<em.*?pjadt_pm10">(.*?)<em.*?div>',re.S)
items = re.findall(pattern,content)
print(items[0][0])
