
import urllib.request
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#url = "http://www.cnblogs.com/sangern/p/7766247.html"
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
target_url = "https://www.javbus2.pw"
req=urllib.request.Request(url=target_url,headers=headers) 
html=urllib.request.urlopen(req).read().decode('utf-8') 
print(html)

fp=open('b.txt','w+',encoding='utf-8') #打开一个文本文件
fp.write(html) #写入数据
fp.close() #关闭文件