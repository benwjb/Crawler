import requests
from lxml import etree


html=requests.get('https://www.javbus2.pw')
Selector=etree.HTML(html.text)
url_list=Selector.xpath('//div[@class="iterm masonry-brick"]/a/@href')
for i in url_list:
	file=open("urllist.txt","w+")
	file.write(i)
	
