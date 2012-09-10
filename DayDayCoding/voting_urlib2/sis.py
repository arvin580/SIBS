#coding=utf-8



import urllib2
import urllib
import re
import sys
import time
import cookielib
from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)

sis=dict()
sis['email']=email
sis['password']=password
data=urllib.urlencode(sis)

req=urllib2.Request('http://www.renren.com/PLogin.do', data)
res=openner.open(req)
html=res.read()
