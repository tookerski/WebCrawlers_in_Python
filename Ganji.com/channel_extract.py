#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from bs4 import BeautifulSoup
import requests

start_url = "http://bj.ganji.com/wu/"
host_url = "http://bj.ganji.com"

def get_channel_urls(url):
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text, "lxml")
    links = soup.select("div.content > div > div > dl > dt > a")
    for link in links:
        import pdb; pdb.set_trace()
        print(link.encode("utf8"))
        channel_url = host_url+link.get("href")
        #print(channel_url)

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