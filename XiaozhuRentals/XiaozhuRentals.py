#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 16-6-30

from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost',27017)
rentals = client['rentals']
sheet_tap = rentals['sheet_tap']

header = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
urls = ['http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,4)]

for url in urls:
    html = requests.get(url,headers=header)
    soup = BeautifulSoup(html.text,'lxml')
    addresses = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > em')
    prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
    descriptions = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
    for address,price,description in zip(addresses,prices,descriptions):
        data = {
            'address':address.get_text().split()[-1],
            'price':int(price.get_text()),
            'description':description.get_text()
        }
        sheet_tap.insert_one(data)
        #print(data)
for item in sheet_tap.find({'price':{'$gt':300}}):
    print(item)