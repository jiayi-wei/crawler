from lxml import html
from time import sleep
import requests

i=0
page="http://bbs.hupu.com/vote"
page_ori="http://bbs.hupu.com"
next_button="//a[@class='next']/@href"

x = html.parse(page)
titles = x.xpath("//a[@id='']/font/text()|//a[@id=''][@href]/b/font/text()|//a[@id=''][@href]/b/text()|//a[@id=''][@href]/text()")
authors=x.xpath("//a[@class='u']/text()")
replys=x.xpath("//td[@class='p_re']/text()")
last_time=x.xpath("//a[@title='查看最后回复']/text()")
while i<len(titles):
    print(titles[i]+"  "+authors[i+19]+"  "+replys[i]+"  "+last_time[i])
    i+=1
print('------')
print(len(titles))
print(len(authors))
print(len(replys))
print(len(last_time))
print('------------')

