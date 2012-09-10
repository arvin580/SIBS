import urllib2
import urllib
#import re
import time
import cookielib
#from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)

for i in range(10000) :
	req=urllib2.Request('http://events.mcss.ca/fcwr2/vote_handler.php?id=59')
	res=openner.open(req)
	html=res.read()
	#parser=BeautifulSoup(html)
	#print(parser)
	print(html)
	time.sleep(1)
