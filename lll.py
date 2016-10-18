from lxml import html
from time import sleep
i=0
page="http://bbs.hupu.com/vote-2"
page_ori="http://bbs.hupu.com"
next_button="//a[@class='next']/@href"

x = html.parse(page)
titles = x.xpath("//a[@id='']/font/text()|//a[@id=''][@href]/b/font/text()|//a[@id=''][@href]/b/text()|//a[@id=''][@href]/text()")
authors=x.xpath("//a[@class='u']/text()")
time_=x.xpath("//td[@class='p_author']/text()[preceding-sibling::br]")
replys=x.xpath("//td[@class='p_re']/text()")
last_time_reply=x.xpath("//td[@class='p_retime']/text()[preceding-sibling::br]")
last_time=x.xpath("//a[@title='查看最后回复']/text()")
print(len(titles))
print(len(time_))
print(len(authors))
print(len(replys))
print(len(last_time))
print(len(last_time_reply))
print('------------')

while i<len(titles):
    print("帖子题目："+titles[i])
    print("发帖人："+authors[i+19])
    print("发帖时间："+time_[i])
    print("回复数量/浏览数量："+replys[i])
    print("最新回帖人："+last_time_reply[i])
    print("最新回帖时间："+last_time[i])
    print('------------')
    print('------------')
    i+=1
