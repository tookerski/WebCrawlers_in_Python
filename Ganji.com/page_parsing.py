#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient("localhost",27017)
ganji = client["ganji"]
url_list = ganji["url_list"]
item_info = ganji["item_info"]

#spider1爬取非手机号的商品链接
def get_item_link(channel,pages,who_seller=1):
    #http://bj.ganji.com/jiaju/a1o119/
    url = "{}a{}o{}".format(channel,str(who_seller),str(pages))
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text,"lxml")
    next = soup.select("div.pageBox > ul > li > a > span")
    if next!=[]:
        links = soup.select("dd.feature > div > ul > li > a")
        for link in links:
            item_link = link.get("href")
            url_list.insert_one({'item_link':item_link})
    else:pass

#get_item_link('http://bj.ganji.com/jiaju/',1)

#spider2爬取手机号商品链接
def get_phone_info(url):
    w = requests.get(url)
    soup = BeautifulSoup(w.text, "lxml")
    title = soup.select("h1.title-name")[0].get_text()
    price = soup.select(" b.f22.fc-orange.f-type")[0].get_text()
    place = list(soup.select("ul.det-infor > li:nth-of-type(2)")[0].stripped_strings)
    data = {
        "title": title,
        "price": price,
        "place": place
    }
    item_info.insert_one(data)
    print(data)

#spider3爬取详情页数据
def get_item_info(url):
    w = requests.get(url)
    soup = BeautifulSoup(w.text,"lxml")
    title = soup.select("h1.title-name")[0].get_text()
    type = soup.select("ul.det-infor > li > span > a")[0].get_text()
    price = soup.select(" i.f22.fc-orange.f-type")[0].get_text()
    place = list(soup.select("ul.det-infor > li:nth-of-type(3)")[0].stripped_strings)
    new = soup.select("ul.second-det-infor.clearfix > li")[0].get_text().split()
    data = {
        "title":title,
        "type":type,
        "price":price,
        "place":place,
        "new":new
    }
    #item_info.insert_one(data)
    print(data)

get_item_info("http://bj.ganji.com/shoujihao/1799327353_1667867301x.htm")