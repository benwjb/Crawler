import urllib.request
from lxml import etree
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#url = "http://www.cnblogs.com/sangern/p/7766247.html"
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
target_url = "https://www.javbus2.pw"
req=urllib.request.Request(url=target_url,headers=headers) 
html=urllib.request.urlopen(req).read().decode('utf-8')
Selector=etree.HTML(html)
page_list=Selector.xpath('//li[@class="active"]/a/@href')
print(len(page_list))
for i in page_list:
	print(page_list)
	f=open('e.txt','a')
	f.write(i+'\n')
	f.close
