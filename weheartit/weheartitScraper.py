#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2016/6/20

@author: tookerski
'''
from bs4 import BeautifulSoup
import requests
import time

#url='http://weheartit.com/inspirations/taylorswift?page=1&before=185755643'
header={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0'}
#proxy={'http':'60.161.14.77:8001'}

def get_img_urls(url,data=None):
    responses = requests.get(url,headers=header)
    if responses.status_code!=200:
        print("response fail")
        return
    soup = BeautifulSoup(responses.text,'lxml')
    imgs = soup.select('img[width="300"]')
    img_urls=[]
    if data == None:
        for img in imgs:
            img_url = img.get('src')
            img_urls.append(img_url)
    return img_urls

urls = ['http://weheartit.com/inspirations/taylorswift?page={}&before=185755643'.format(str(i)) for i in range(1,11)]

def download_imgs(urls):
    for url in urls:
        links = get_img_urls(url)
        for link in links:
            #print(link)
            r = requests.get(link,headers=header)
            if r.status_code!=200:
                continue
            file_name = link.split('/')[0]
            target = 'F:\\a3\\{}'.format(file_name)
            with open(target,'wb') as fs:
                fs.write(r.content())
            print('%s=>%s' % (link,target))
            time.sleep(2)

if __name__ =='__main__':
    download_imgs(urls)