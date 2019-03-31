import urllib.request
from lxml import etree
import sys
import os
import re
import random
import time
import requests
def getHTML(url):
	my_header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
	#randdom_header=random.choice(my_headers) 
	#print(randdom_header)  
	#req=urllib.request.Request(url) 
	#req.add_header("User-Agent",my_header)
	#req.add_header("Referer",url)  
	#req.add_header("GET",url)
	#html=urllib.request.urlopen(req).read()#.decode('utf-8')
	cookies={'cookie':"PHPSESSID=ocg6819nr7crjcmrnhlaou7nl6; Ovo6_2132_saltkey=yi5hD65R; Ovo6_2132_lastvisit=1528185553; Ovo6_2132_ulastactivity=1528190154%7C0; Ovo6_2132_auth=a52fZsl60CQ4rGhqKIlgfS%2B33mXJIlhtB5SSjkIMsUnhOpumOvbUwwTKzPjeiaeYVPk3u%2BZ%2FVVpl8laPrPoGWzL%2FaJDR; Ovo6_2132_lastcheckfeed=2757069%7C1528190154; Ovo6_2132_checkfollow=1; Ovo6_2132_lastact=1528190154%09forum.php%09; Ovo6_2132_myrepeat_rr=R0"}
	r=requests.get(url,headers=my_header,cookies=cookies)

	
	
	#r.encoding = 'utf-8'
	#print(r.text) 
	#file=open('douban.txt','wb+')
	#file.write(r.content)
	return r.content
def getLinks(url):
	html=getHTML(url)
	Selector=etree.HTML(html)
	url_list=Selector.xpath('//div[@class="c cl"]/a/@href')
	for i in range(len(url_list)):
		url_list[i]='http://hk-pic2.xyz/'+url_list[i]
		#print(url_list[i])
	return url_list

def getImg(url,i):
	html=getHTML(url)
	Selector=etree.HTML(html)
	img_list=Selector.xpath('//p[@class="mbn"]/a/img/@file')
	t_list=Selector.xpath('//title/text()')
	#print(len(img_list))
	#print(img_list)
	for i in range(len(img_list)):
		img_list[i]='http://hk-pic2.xyz/'+img_list[i]
		#print(img_list[i])
	No=url[40:-16]
	#picN=i
	pic=''.join(t_list).replace("\r",'').replace("\n",'').replace("»",'').replace("，",'').replace(" ",'').replace("=",'').replace("？",'')
	id=1
	try:
		for each  in img_list:
			#fp=open('%s_%d_%d.jpg' % (No,picN,id),'wb+') #打开一个文本文件
			fp=open('%s_%s_%d.png' %(pic,No,id),'wb+') #打开一个文本文件
			fp.write(getHTML(each))
			print('%s_%d.jpg' %(No,id)+" "+"is finished")
			id +=1 #写入数据
			fp.close()
			time.sleep(2) #关闭文件
	except Exception:
		pass


def downloadimg(url_list,num):
	if not os.path.exists('E://downloadbs'):
		os.mkdir('E://downloadbs')
	rootpath=os.getcwd()
	for i in range(num):
		imgdir='E://downloadbs/'#+url_list[i][40:47].replace("&", '')
		if not os.path.exists(imgdir):
			os.mkdir(imgdir)
			print(imgdir)
		os.chdir(imgdir)
		getImg(url_list[i],i)
		os.chdir(rootpath)
	




if __name__ == '__main__':
	print("--------------------piccatchv1.0--------------------")
	#print("--------------------请输入地址：")
	#url= input('')
	url="http://hk-pic2.xyz/forum-18-1.html" 
while True:
	print("--------------------inputpagenum:")
	page=input("")
	if re.findall(r'^[0-9]*$',page):
		page = int(page)
		break



	#urlLinks=getLinks(url)
	#num=len(urlLinks)
	#downloadimg(urlLinks,num)
	
for i in range(page):
	i=i+1
	url1=url[:-6]+'%d' % i+".html"
	print("No."+"%d"% i+"page" )
	#print(url1)
	urlLinks=getLinks(url1)
	num=len(urlLinks)
	downloadimg(urlLinks,num)
		
input('exit')#bs论坛