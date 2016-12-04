import http.cookiejar
import urllib.request
import pprint


def getOpener(head):
    cj=http.cookiejar.CookieJar()
    pro=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(pro)
    header=[]
    for key,val in head.items():
        elem=(key,val)
        header.append(elem)
    opener.addheaders=header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url_home="http://220.195.3.56:7088/SensorApp_bupt/user/go/homePage"
url="http://220.195.3.56:7088/SensorApp_bupt/user/getLogin"
para={'username':'bupt','password':'bupt'}
opener=getOpener(header)
para=urllib.parse.urlencode(para).encode()
op=opener.open(url,para)
op=opener.open(url_home)
data=op.read()

pprint.pprint(data)
