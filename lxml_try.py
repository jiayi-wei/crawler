from lxml import html
from time import sleep

i=0
page="http://bbs.hupu.com/vote"
next_button="//a[@class='next']/@href"
while(i<10):
    x = html.parse(page)
    titles = x.xpath("//a[@id][@href]/b/font/text()|//a[@id][@href]/b/text()|//a[@id][@href]/text()")
    for title in titles:
        print(title)
    print('------------')
    pages=x.xpath(next_button)
    page=base_url.format(pages[0])
    print(pages)
    i=i+1
    sleep(3)
    
