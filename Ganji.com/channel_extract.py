#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from bs4 import BeautifulSoup
import requests

start_url = "http://bj.ganji.com/wu/"   #定义爬虫起始页面url
host_url = "http://bj.ganji.com"        #定义类目host，用于组合各类目起始url

#定义获取channel的函数
def get_channel_urls(url):
    web_data = requests.get(start_url)
    web_data.encoding = "utf-8"    #经老师指导，编码utf-8，否则页面中文乱码
    soup = BeautifulSoup(web_data.text, "lxml")
    links = soup.select("div.content > div > div > dl > dt > a")
    for link in links:
        channel_url = host_url+link.get("href")
        print(channel_url)

#运行函数，并保存获取到的链接
get_channel_urls(start_url)
channel_list ='''
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/shoujihaoma/
    http://bj.ganji.com/bangong/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/ershoubijibendiannao/
    http://bj.ganji.com/ruanjiantushu/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/diannao/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/shuma/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/qitawupin/
    http://bj.ganji.com/ershoufree/
    http://bj.ganji.com/wupinjiaohuan/
'''