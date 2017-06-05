#!/usr/bin/python3
# -*- coding: utf-8- -*-
"""
.az domainlərin üçün Whois
 autor: SQS
"""
import sys
import requests
import re
from bs4 import BeautifulSoup
header= {"Accept-Encoding": "gzip, deflate","Accept-Language": "en-US,en;q=0.5" ,"Content-Length": "7", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,"Referer": "http://whois.az/cgi-bin/whois.cgi","Content-Type": "application/x-www-form-urlencoded", "Host": "whois.az", "User-Agent": "MMozilla/5.0 "}


try:
	line = sys.argv[1]
except:
	print("Usage: ./whoisaz.py [ hostname ]\n " )
	sys.exit()


try:

	hostname=(re.split(r'[.]',line))
	domain=hostname[0]
	payload={'dom':'.az','domain':domain,'lang':'en'}
	s=requests.post("http://www.whois.az/cgi-bin/whois.cgi", data=payload, headers=header)
	soup = BeautifulSoup(s.text, 'html.parser')
	c=soup.find_all('pre')[0].get_text()

except KeyboardInterrupt:
	print("\nPressed Ctrl+C")
	sys.exit()

except:
	pass
print("Domain:\t"+line.lower(),c.lower())
