#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os 
import sys
import requests
from bs4 import BeautifulSoup

class Proxy360:
	def __init__(self, path):
		self.urls = [
			"http://www.proxy360.cn/QQ-Proxy",
			"http://www.proxy360.cn/Proxy",
			"http://www.proxy360.cn/Region/Brazil",
			"http://www.proxy360.cn/Region/China",
			"http://www.proxy360.cn/Region/America",
			"http://www.proxy360.cn/Region/Taiwan",
			"http://www.proxy360.cn/Region/Japan",
			"http://www.proxy360.cn/Region/Thailand",
			"http://www.proxy360.cn/Region/Vietnam",
			"http://www.proxy360.cn/Region/bahrein"
		]
		self.path = path


	def start(self):
		with open(self.path, "a") as fs:
			for url in self.urls:
				r = requests.get(url)
				r.encoding = "gbk"
				if r.status_code != 200:
					continue
				soup = BeautifulSoup(r.text, "html.parser")
				tags = soup.select("#ctl00_ContentPlaceHolder1_upProjectList > div > div")
				for tag in tags:
					spans = [ t.text for t in tag.select("span")]
					if len(spans) < 2:
						continue


					ip = spans[0].strip()
					port = spans[1].strip()

					if not ip:
						continue

					if not port:
						port = 80


					if not port.isdigit():
						continue

					_proxy = "http://%s:%s" % (ip, port)
					try:
						_r = requests.head("http://www.bbc.com", proxies={"http": _proxy})
						if _r.status_code == 200:
							fs.write("%s\n\r" % _proxy)
							print("%s ok" % _proxy)
					except:
						print("%s failed" % _proxy)

class IP66:
	def __init__(self, path):
		self.urls = [
			"http://www.66ip.cn/%s.html" % i for i in range(1, 575)
		]
		self.path = path


	def start(self):
		with open(self.path, "a") as fs:
			for url in self.urls:
				r = requests.get(url)
				r.encoding = "gbk"
				if r.status_code != 200:
					continue
				soup = BeautifulSoup(r.text, "html5lib")
				tags = soup.select("#main > div > div > table > tbody > tr")
				for tag in tags:
					spans = [ t.text for t in tag.select("td")]
					if len(spans) < 2:
						continue


					ip = spans[0].strip()
					port = spans[1].strip()

					if not ip:
						continue

					if not port:
						port = 80

					if not port.isdigit():
						continue

					_proxy = "http://%s:%s" % (ip, port)
					try:
						_r = requests.head("http://www.bbc.com", proxies={"http": _proxy})
						if _r.status_code == 200:
							fs.write("%s\n\r" % _proxy)
							print("%s ok" % _proxy)
					except:
						print("%s failed" % _proxy)

if __name__ == '__main__':
	startfolder = os.path.dirname(os.path.realpath(sys.argv[0]))

	client = IP66(os.path.join(startfolder, "proxies.txt"))
	client.start()


	client = Proxy360(os.path.join(startfolder, "proxies.txt"))
	client.start()

