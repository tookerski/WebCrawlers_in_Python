#!/usr/bin/env Python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import random
import json

def get_proxy():
    resp = requests.get('http://tor1024.com/static/proxy_pool.txt')
    ips_txt = resp.text.strip().split('\n')
    ips = []
    for ip in ips_txt:
        try:
            k = json.loads(ip)
            # print(k)
            ips.append(k)
        except Exception as e:
            print(e)
    return ips
# 爬取一页职位的跳转链接，返回一个list
# url = 'https://www.liepin.com/zhaopin/?key=%数据挖掘&dqs=050&curPage=0'
# url = 'https://job.liepin.com/554_5543233/?imscid=R000000075'

def get_job_info(url, headers,ip):
    u = url
    h = headers
    i = ip
    # print(u)
    try:
        r = requests.get(u, headers=h,proxies=i)
        soup = BeautifulSoup(r.text, 'lxml')
        link_tags = soup.select('div.sojob-result > ul > li > div > div.job-info > h3 > a')
        for link_tag in link_tags:
            # print(link_tag.get('href'))
            get_details(link_tag.get('href'), h, i)
            time.sleep(random.randint(2, 3))
    except Exception as e:
        print(e)

def get_details(url, headers, ip, data=None):
    try:
        r = requests.get(url, headers=headers,proxies=ip)
        soup = BeautifulSoup(r.text, 'lxml')
        if data == None:
            data = {
                'title': soup.select('div.title-info > h1')[0].get('title'),
                'company': soup.select('div.title-info > h3 > a')[0].get('title'),
                'salary': soup.select('p.job-main-title')[0].get_text().split('\r')[0],
                'place': soup.select('p.basic-infor > span')[0].get_text().strip(),
                'description': soup.select(
                    '#job-view-enterprise > div.wrap.clearfix > div.main > div.title > div:nth-of-type(3) > div')[
                    0].get_text().strip()
            }
            print(data)
    except Exception as e:
        print(e)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
urls = ['https://www.liepin.com/zhaopin/?pubTime=&salary=&clean_condition=&jobKind=&isAnalysis=&init=1&sortFlag=15&key=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&industries=&dqs=050&curPage={}'.format(str(i)) for i in range(0, 29)]
ips = get_proxy()
for url in urls:
    ip = random.choice(ips)
    get_job_info(url, headers,ip)