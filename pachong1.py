#coding:utf-8
import requests
from lxml import html
#from urllib import urlretrieve
import urllib
from bs4 import BeautifulSoup


url = 'https://movie.douban.com/chart'
html = requests.get(url).content
soup = BeautifulSoup(html, features = 'lxml')

All_nbg = soup.find_all('a',{'class': 'nbg'})
n = 0
P = []
for i in All_nbg:
	P.append(i.img['src'])
	print n
	image_name = i.img['alt'] + '.jpg'
	urllib.urlretrieve(P[n], image_name)
	n+=1
print P

#urllib.urlretrieve(Result[0],'1.jpg')