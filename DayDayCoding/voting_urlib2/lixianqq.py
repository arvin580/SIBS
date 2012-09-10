#coding=utf-8
import urllib2
import urllib
import re
import time
import cookielib
import random
import hashlib
from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)
openner.addheaders = [('User-Agent', 'Mozilla/5.0')]

req=urllib2.Request('http://check.ptlogin2.qq.com/check?uin=594878246&appid=567008010&r='+str(random.Random().random()))
res=openner.open(req)
html=res.read()
verifycode=html.split("'")[3]

passwd='ecnu322530'
passwd=hashlib.md5(passwd).hexdigest().upper()

req=urllib2.Request(
'http://ptlogin2.qq.com/login?u=594878246&p='+passwd+'&verifycode='+verifycode+'&aid=567008010&u1=http%3A%2F%2Flixian.qq.com%2Fmain.html&h=1&ptredirect=1&ptlang=2052&from_ui=1&dumy=&fp=loginerroralert&action=2-10-&mibao_css=&t=1&g=1'
)
res=openner.open(req)
html=res.read()
parser=BeautifulSoup(html)
print(parser)
