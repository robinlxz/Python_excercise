#coding:utf-8
import requests
from lxml import html
#import urllib
from bs4 import BeautifulSoup

#Learn from https://zhuanlan.zhihu.com/p/49066394

######
#To improve
#1. Use function
#2. remove the extra written txt
#3. (done)Write for every page, not for all page in one variable
#4. use raw_input for 'url', 'how many pages', 'save file name'
#5. Add a progress bar~~
#####

#p_list = ''

url = 'https://www.52shuku.me/kongbulingyi/23316'
urls=[]
for i in range(1, 2):
	q=i+1
	if q==1:
		urls.append(url + '.html')
	else:
		urls.append(url + '_%r.html' %q)
	print urls[i-1]

for url in urls:
	html = requests.get(url)
	html.encoding = 'utf-8'
	soup = BeautifulSoup(html.txt, features = 'lxml')
	All_txt = soup.find_all('article',{'class': 'article-content'})
	#n = 0

	for p in All_txt:
#		p_list.append(p.text)
		with open('pashu3_output1849.txt','a') as txtfile:
			txtfile.write(p.text.encode('utf-8'))
#		p_list += '\n'+p.text


#print len(p_list)

#with open('pashu_output.txt','wb') as txtfile:
#	txtfile.write(p_list.encode('utf-8'))
