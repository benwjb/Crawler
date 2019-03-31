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
    url_list=Selector.xpath('//a[@class="thumbnail"]/@href')
    for i in range(len(url_list)):
        url_list[i]='http://trb01.com/'+url_list[i]
        #print(url_list[i])
    return url_list

def getImg(url,i):
    html=getHTML(url)
    Selector=etree.HTML(html)
    img_list=Selector.xpath('//p/img/@src')
    t_list=Selector.xpath('//h1[@class="article-title"]/text()')
    url_list2=Selector.xpath('//div[@class="pagination pagination-multi"]/ul/li/a/@href')
    #print(len(img_list))
    #print(img_list)
 	
    #No=url[25:-6]
    picN=i
    pic=''.join(t_list).replace("/",'').replace("\n",'').replace("»",'').replace("，",'').replace(" ",'')
    #id=1
    #for each  in img_list:
        #fp=open('%s_%d_%d.jpg' % (No,picN,id),'wb+') #打开一个文本文件
        #fp=open('%s_%s_%d.jpg' %(pic,No,id),'wb+') #打开一个文本文件
        #fp.write(getHTML(each))
        #print('%s_%s_%d.jpg' %(pic,No,id)+" "+"is finished")
        #id +=1 #写入数据
        #fp.close()
    pic_name = 0
    for each in img_list:
        urllib.request.urlretrieve(each, 'pic_%d_%s_%d.jpg' % (pic_name,pic,picN))
        print('%d_%d.jpg' %(pic_name,picN)+" "+"is finished")
        pic_name += 1
        time.sleep(2) #关闭文件
    for i in range(len(url_list2)):
    	url_list2[i]=url[:-9]+url_list2[i]
    	#print(url_list2[i])
    downloadimg1(url_list2,len(url_list2))

def getImg1(url,i):
    html=getHTML(url)
    Selector=etree.HTML(html)
    img_list=Selector.xpath('//p/img/@src')
    t_list=Selector.xpath('//h1[@class="article-title"]/text()')    	
	
    picN=i
    pic=''.join(t_list).replace("/",'').replace("\n",'').replace("»",'').replace("，",'').replace(" ",'')
    #id=1
    #for each  in img_list:
        #fp=open('%s_%d_%d.jpg' % (No,picN,id),'wb+') #打开一个文本文件
        #fp=open('%s_%s_%d.jpg' %(pic,No,id),'wb+') #打开一个文本文件
        #fp.write(getHTML(each))
        #print('%s_%s_%d.jpg' %(pic,No,id)+" "+"is finished")
        #id +=1 #写入数据
        #fp.close()
    pic_name = 0
    for each in img_list:
        urllib.request.urlretrieve(each, 'pic_%d_%s_%d.jpg' % (pic_name,pic,picN))
        print('%d_%d.jpg' %(pic_name,picN)+" "+"is finished")
        pic_name += 1
        time.sleep(2) #关闭文件

def downloadimg1(url_list,num):
	if not os.path.exists('downloa'):
		os.mkdir('downloa')
	rootpath=os.getcwd()
	for i in range(num):
		imgdir='downloa/'+url_list[i][25:-9].replace("/", '')
		if not os.path.exists(imgdir):
			os.mkdir(imgdir)
		os.chdir(imgdir)
		getImg1(url_list[i],i)
		os.chdir(rootpath)

def downloadimg(url_list,num):
	if not os.path.exists('downloa'):
		os.mkdir('downloa')
	rootpath=os.getcwd()
	for i in range(num):
		imgdir='downloa/'+url_list[i][25:-9].replace("/", '')
		if not os.path.exists(imgdir):
			os.mkdir(imgdir)
		os.chdir(imgdir)
		getImg(url_list[i],i)
		os.chdir(rootpath)




if __name__ == '__main__':
    print("--------------------抓图装置v1.0--------------------")
    #print("--------------------请输入地址：")
    #url= input('')
    url="http://trb01.com/" 
while True:
    print("--------------------请输入页数：")
    page=input("")
    if re.findall(r'^[0-9]*$',page):
        page = int(page)
        break



#urlLinks=getLinks(url)
#num=len(urlLinks)
#downloadimg(urlLinks,num)
    
for i in range(page-1):
    i=i+1
    url1=url+"page/"+'%d' % i+".html"
    print("第"+"%d"% i+"页" )
    #print(url1)
    urlLinks=getLinks(url1)
    num=len(urlLinks)
    #print(num)
    downloadimg(urlLinks,num)
        
input('exit')#trb01网站