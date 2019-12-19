#coding:utf-8
import requests
from lxml import html
from urllib import urlretrieve
#Python3
#from urllib.request import urlretrieve
from bs4 import BeautifulSoup

#This url failed! Interesting, seem to be something blocking urlretrieve
#!Need to add browser header into the urlretrieve, learn more
#Add header can be learn from 
##https://mp.weixin.qq.com/s?__biz=MzUyOTM5ODgyNw==&mid=2247486021&idx=1&sn=a0ebbd9a6be670318db9d23447f36e14&scene=21#wechat_redirect
url = 'http://www.mm131.com/qingchun/'
html = requests.get(url).text
#Need to use chrome to find the header when doing request
#html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html, features = 'lxml')

All_href = soup.find_all('a',{'target': '_blank'})
n = 0
P = []
for i in All_href:
	P.append(i.img['src'])
	print 'processing No. %r' %n
	image_name = i.img['alt'] + '.jpg'
#	urllib.urlretrieve(P[n], image_name)
	urlretrieve(P[n], image_name)
	n+=1
	if n>3:
		print 'As configured, we stop at %r' %n
		break
print len(P)
