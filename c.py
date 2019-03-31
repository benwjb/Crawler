import urllib.request
import random
import requests
#url = "http://www.cnblogs.com/sangern/p/7766247.html"
my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", 
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36", 
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14", 
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    
] 
randdom_header=random.choice(my_headers) 
url="https://pics.javcdn.pw/cover/6lm9_b.jpg"  
req=urllib.request.Request(url) 
req.add_header("User-Agent",randdom_header) 
req.add_header("GET",url) 
#response=requests.get(url,header=randdom_header)
html=urllib.request.urlopen(req).read()
#print(html)
#urllib.request.urlretrieve(url,'pic_1.jpg')
fp=open('c.jpg','wb+') #打开一个文本文件
fp.write(html) #写入数据
fp.close() #关闭文件
