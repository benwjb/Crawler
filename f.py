import urllib.request
from lxml import etree
import sys
import os
import re
import random
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#url = "http://www.cnblogs.com/sangern/p/7766247.html"
def getHTML(url):
	my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", 
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36", 
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14", 
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"] 

	randdom_header=random.choice(my_headers) 
	print(randdom_header)  
	req=urllib.request.Request(url) 
	req.add_header("User-Agent",randdom_header)
	#req.add_header("Referer",url)  
	req.add_header("GET",url)
	html=urllib.request.urlopen(req).read()#.decode('utf-8')
	return html

url = "https://www.javbus2.pw/DINM-443/"	


Selector=etree.HTML(getHTML(url))
img_list=Selector.xpath('//a[@class="bigImage"]/img/@src')
print(len(img_list))
print(img_list)
picN=1
for i  in img_list:
	fp=open('f_%d.jpg' % picN,'wb+') #打开一个文本文件
	fp.write(getHTML(i))
	picN +=1 #写入数据
	fp.close() #关闭文件
#for each in img_list:
	#urllib.request.urlretrieve(each,'pic_1.jpg')
    
