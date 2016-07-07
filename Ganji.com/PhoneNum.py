#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/4

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient("localhost",27017)
ganji_phone = client["ganji_phone"]
phone_urls = ganji_phone["phone_urls"]
phone_info = ganji_phone["phone_info"]

start_url = "http://bj.ganji.com/shoujihaoma/"
def get_phone_links(channel,pages,who_seller=1):
    #http://bj.ganji.com/shoujihaoma/a1o2/
    url = "{}a{}o{}".format(channel,str(who_seller), str(pages))
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, "lxml")
    next = soup.select("div.pageBox > ul > li > a > span")
    if next != []:
        links = soup.select("a.pn-lbox")
        for link in links:
            phone_link = link.get("href")
            phone_urls.insert_one({"phone":phone_link})
            print(phone_link)


#get_phone_links(1)

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
    phone_info.insert_one(data)
    print(data)

#get_phone_info("http://bj.ganji.com/shoujihao/1799327353_1667867301x.htm")

for page in range(1,200):
    get_phone_links(page)

for info in phone_urls.find():
    url = info["phone"]
    get_phone_info(url)