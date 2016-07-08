#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from multiprocessing import Pool
from channel_extract import channel_list
import requests
import json
import random
from page_parsing import get_item_info,get_item_link,get_phone_info,get_phone_links,url_list,phNum_list

header = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
}

#定义函数获取商品描述链接
def get_all_links(channel):
    for num in range(1,151):
        ip = random.choice(proxy_lists)
        if channel!="http://bj.ganji.com/shoujihaoma/":
            get_item_link(header,ip,channel,num)
        else:
            get_phone_links(header,ip,num)
    print("所有商品链接已保存成功！")
    for url in url_list:
        ip = random.choice(proxy_lists)
        get_item_info(header,ip,url)
    for url in phNum_list:
        ip = random.choice(proxy_lists)
        get_phone_info(header,ip,url)

def get_proxy():
    resp = requests.get('http://tor1024.com/static/proxy_pool.txt')
    ips_txt = resp.text.strip().split('\n')
    ips = []
    for ip in ips_txt:
        try:
            k = json.loads(ip)
            ips.append(k)
        except Exception as e:
            print(e)
    return ips

#定义主启动函数
if __name__=='__main__':
    proxy_lists = get_proxy()
    pool = Pool()
    pool.map(get_all_links,channel_list.split())
