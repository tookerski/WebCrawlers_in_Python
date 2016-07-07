#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on Jun 29

from multiprocessing.dummy import Pool as ThreadPool
import requests
import time

def getResource(url):
    html = requests.get(url)

urls = ['http://esf.dg.fang.com/house/i3{}/'.format(str(i)) for i in range(1,5)]
pool = ThreadPool(2)
time1 = time.time()
result = pool.map(getResource, urls)
pool.close()
pool.join()
time2 = time.time()
print('耗时',str(time2-time1))