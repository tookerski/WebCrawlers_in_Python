#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_item_info,get_item_link,get_phone_info,get_phone_links

#定义主抓取商品链接的函数
def get_all_links(channel):
    for num in range(1,151):
        if channel!="http://bj.ganji.com/shoujihaoma/":
            get_item_link(channel,num)
        else:
            get_phone_links(num)

#定义主启动函数
if __name__=='__main__':
    pool = Pool()
    pool.map(get_all_links,channel_list.split())
