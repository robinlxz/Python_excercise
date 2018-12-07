#coding:utf-8
import requests
#from lxml import html
#from urllib import urlretrieve
#import urllib
#from bs4 import BeautifulSoup


jpg_url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2541019743.webp'

r = requests.get(jpg_url, stream=True)
#image_name = '3rd'
with open('./img/abcd3rd.webp', 'wb') as f:
	for chunk in r.iter_content(chunk_size=128):
		f.write(chunk)
print 'Done'