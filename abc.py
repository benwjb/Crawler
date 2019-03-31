# -*- coding: utf-8 -*-
from urllib import request
url = "https://images.zhaofulipic.com:8819/allimg/170723/1IK33M4-0.jpg" #网页地址
wp = request.urlopen(url) #打开连接
content = wp.read()#获取页面内容
fp=open('f://abc.txt','wb+') #打开一个文本文件
fp.write(content) #写入数据
fp.close() #关闭文件