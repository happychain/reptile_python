#!use/bin/ Python3
#coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import ssl

url="https://www.taobao.com"
ssl._create_default_https_context = ssl._create_unverified_context
page=urllib.request.urlopen(url).read()
soup=BeautifulSoup(page,"html.parser")
# print (soup)

label_a=soup.find_all("a");
for i in label_a:
    # print(i)
    print (i.getText()+"----"+i.get("href")+"---->")




