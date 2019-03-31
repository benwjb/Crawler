import urllib.request
from lxml import etree
import sys
import os
import re
import random
import time
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



def getLinks(url):
	html=getHTML(url)
	Selector=etree.HTML(html)
	url_list=Selector.xpath('//a[@class="movie-box"]/@href')
	return url_list

def getImg(url,i):
	html=getHTML(url)
	Selector=etree.HTML(html)
	img_list=Selector.xpath('//a[@class="bigImage"]/img/@src')
	print(len(img_list))
	print(img_list)
	No=url[23:]
	picN=i
	id=0
	for each  in img_list:
		fp=open('%s_%d_%d.jpg' % (No,picN,id),'wb+') #打开一个文本文件
		fp.write(getHTML(each))
		id +=1 #写入数据
		fp.close()
		time.sleep(5) #关闭文件



def downloadimg(url_list,num):
	if not os.path.exists('downloads'):
		os.mkdir('downloads')
	rootpath=os.getcwd()
	for i in range(num):
		imgdir='downloads'
		os.chdir(imgdir)
		getImg(url_list[i],i)
		os.chdir(rootpath)
	




if __name__ == '__main__':
	print("--------------------抓图装置v1.0--------------------")
	print("--------------------请输入地址：")
	url= input('')
while True:
	print("--------------------请输入页数：")
	page=input("")
	if re.findall(r'^[0-9]*$',page):
		page = int(page)
		break

if(page==1):
	while True:
		print("--------------------请输入图片数：")
		num=input("")
		if re.findall(r'^[0-9]*$',num):
			num = int(num)
			break
	urlLinks=getLinks(url)
	downloadimg(urlLinks,num)
else:
	urlLinks=getLinks(url)
	num=len(urlLinks)
	downloadimg(urlLinks,num)
	j=2
	for i in range(page-1):
		url=url+'/page/%d' % j
		urlLinks=getLinks(url)
		num=len(urlLinks)
		downloadimg(urlLinks,num)
		j=+1
input('exit')
