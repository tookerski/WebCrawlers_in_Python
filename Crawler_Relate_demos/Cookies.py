#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

params = {'username':'tookerski','password':'password'}
url = 'http://pythonscraping.com/pages/cookies/welcome.php'
r = requests.post(url,params)

print('cookies is set to: ', r.cookies.get_dict())
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)