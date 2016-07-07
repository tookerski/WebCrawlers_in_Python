#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_item_link

def get_all_links(channel):
    for num in range(1,151):
        get_item_link(channel,num)

if __name__=='__main__':
    pool = Pool()
    pool.map(get_all_links,channel_list.split())
