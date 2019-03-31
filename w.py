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
	#print(randdom_header)  
	req=urllib.request.Request(url) 
	req.add_header("User-Agent",randdom_header)
	#req.add_header("Referer",url)  
	req.add_header("GET",url)
	html=urllib.request.urlopen(req).read()#.decode('utf-8')
	return html



def getLinks(url):
	html=getHTML(url)
	Selector=etree.HTML(html)
	url_list=Selector.xpath('//th[@class="subject new"]/span/a/@href')
	for i in range(len(url_list)):
		url_list[i]='http://h.91p11.space/'+url_list[i]
		#print(url_list[i])
	return url_list

def getImg(url,i):
	html=getHTML(url)
	Selector=etree.HTML(html)
	img_list=Selector.xpath('//img[@src="images/common/none.gif"]/@file')
	t_list=Selector.xpath('//div[@id="nav"]/text()')
	#print(len(img_list))
	#print(img_list)
	for i in range(len(img_list)):
		img_list[i]='http://h.91p11.space/'+img_list[i]
		#print(img_list[i])
	No=url[40:-16]
	#picN=i
	pic=''.join(t_list).replace("\r",'').replace("\n",'').replace("»",'').replace("，",'').replace(" ",'')
	id=1
	for each  in img_list:
		#fp=open('%s_%d_%d.jpg' % (No,picN,id),'wb+') #打开一个文本文件
		fp=open('%s_%s_%d.png' %(pic,No,id),'wb+') #打开一个文本文件
		fp.write(getHTML(each))
		print('%s_%s_%d.png' %(pic,No,id)+" "+"is finished")
		id +=1 #写入数据
		fp.close()
		time.sleep(2) #关闭文件



def downloadimg(url_list,num):
	if not os.path.exists('E://download'):
		os.mkdir('E://download')
	rootpath=os.getcwd()
	for i in range(num):
		imgdir='E://download/'+url_list[i][40:47].replace("&", '')
		if not os.path.exists(imgdir):
			os.mkdir(imgdir)
		os.chdir(imgdir)
		getImg(url_list[i],i)
		os.chdir(rootpath)
	




if __name__ == '__main__':
	print("--------------------抓图装置v1.0--------------------")
	#print("--------------------请输入地址：")
	#url= input('')
	url="http://h.91p11.space/forumdisplay.php?fid=19&filter=digest&page=" 
while True:
	print("--------------------请输入页数：")
	page=input("")
	if re.findall(r'^[0-9]*$',page):
		page = int(page)
		break



	#urlLinks=getLinks(url)
	#num=len(urlLinks)
	#downloadimg(urlLinks,num)
	
for i in range(page):
	i=i+1
	url1=url+'%d' % i
	print("第"+"%d"% i+"页" )
	#print(url1)
	urlLinks=getLinks(url1)
	num=len(urlLinks)
	downloadimg(urlLinks,num)
		
input('exit')#91论坛

