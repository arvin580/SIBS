#coding=utf-8
import urllib2
import urllib
import re
import time
import cookielib
from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)
openner.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.5) Gecko/20031107 Debian/1.5-3"),("Accept", "text/html, image/jpeg, image/png, text/*, image/*, */*")]

req=urllib2.Request('http://gzjd.shenyangsheying.com/View.asp?id=26')
res=openner.open(req)
html=res.read()
parser=BeautifulSoup(html)
print(parser)
