#!/usr/bin/env Python
# -*- coding:utf-8 -*-
'''
Created on 2016/6/21

@author: tookerski
'''
from bs4 import BeautifulSoup
import requests
import time

#定义获取header的函数，header包含user-agent参数
def get_header():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2767.5 Safari/537.36'}
    return header

#定义获取翻页链接，默认页数100
def get_page_links(seller=0,page_num=100):
    urls=['http://bj.58.com/pbdn/{}/pn{}/'.format(seller,i) for i in range(0,page_num+1)]
    return urls

#定义获取商品的链接
def get_item_links(url,header):
    rp=requests.get(url,headers=header)
    soup=BeautifulSoup(rp.text,'lxml')
    #做一个判断，如果此页有商品，需包含div.infocon标签。有的话继续，没有的pass
    if soup.find('div','infocon'):
        item_all_tags=soup.select('tr > td.t > a.t')#所有商品的链接
        item_zz_tags=soup.select('tr.zzinfo > td.t > a.t')#转转商品的链接
        tags=[i for i in item_all_tags if i not in item_zz_tags]#排除转转商品，添加到列表
        pro_urls = ['http://bj.58.com/pbdn/{}/pn1/'.format(str(i)) for i in range(0, 2)]
        if url==pro_urls[0] or url==pro_urls[1]:
            tags=tags[3:]   #这里，只有第一页的前3个是推广链接，如果是第一页的话，排除前3个链接
        item_links=[]
        for tag in tags:
            item_links.append(tag.get('href'))
        return item_links
    else:
        pass

def get_item_details(url,header,data=0):
    r = requests.get(url,headers=header)
    s = BeautifulSoup(r.text,'lxml')
    view = s.select('span.look_time')[0].text   #获取浏览数
    type = s.select('span.crb_i > a')[0].text   #获取类型
    title = s.select('h1.info_titile')[0].text  #获取主题
    pric = s.select('div.price_li > span > i')[0].text  #获取价格
    area = s.select('div.palce_li > span > i')[0].text  #获取区域
    data = {
        'view':view,
        'type':type,
        'title':title,
        'area':area
    }
    print(data)

#获取header，循环抓取商品信息，一次请求间隔2秒
h = get_header()
for url in get_page_links():
    for link in get_item_links(url,h):
        get_item_details(link,h)
        time.sleep(2)
    time.sleep(2)