#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tookerski on 2016/7/5

import time
from page_parsing import url_list

while True:
    print(url_list.find().count())
    time.sleep(5)