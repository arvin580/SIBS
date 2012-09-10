#coding=utf-8
url='http://www.qvodzy.me'
ouFile=open('qvod.tsv','w')
import urllib2
import urllib
import re
import time
import cookielib
from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)

movieDict=dict()
for offset in range(1,3) :
    time.sleep(1)
    req=urllib2.Request(url+'/index.asp?page='+str(offset))
    res=openner.open(req)
    html=res.read()
    parser=BeautifulSoup(html)
    movies=parser.findAll('a',target="_blank")
    for item in movies :
        s=re.search(r'<a href="(/movie.asp\?ID=.*)" target="_blank">(.*)</a>',str(item))
        if s and s.group(2)!='点击进入' :
            movieDict[s.group(1)]=s.group(2)
    
for key in movieDict :
    time.sleep(1)
    req=urllib2.Request(url+key)
    res=openner.open(req)
    html=res.read()
    parser=BeautifulSoup(html)
    qvodList=list()
    infoList=['']*8
    info=parser.findAll('tr')
    for item in info :
        s=re.search(r'影片名称.*\n<td width=".*">(.*)</td>',str(item))
        if s :
            infoList[0]=s.group(1)
        s=re.search(r'影片状态.*\n<td width=".*">(.*)</td>',str(item))
        if s :
            infoList[1]=s.group(1)

        s=re.search(r'影片年代.*\n<td width=".*">(.*)</td>',str(item))
        if s :
            infoList[2]=s.group(1)
        s=re.search(r'影片演员.*\n<td>(.*)</td>',str(item))
        if s :
            infoList[3]=s.group(1)

        s=re.search(r'影片类型.*\n<td>(.*)</td>',str(item))
        if s :
            infoList[4]=s.group(1)
        s=re.search(r'影片地区.*\n<td>(.*)</td>',str(item))
        if s :
            infoList[5]=s.group(1)
        s=re.search(r'更新时间.*\n<td>(.*)</td>',str(item))
        if s :
            infoList[6]=s.group(1)
        s=re.search(r'影片简介.*\n<td>(.*)</td>',str(item))
        if s :
            infoList[7]=s.group(1)


    qvods=parser.findAll('a',target="_blank")
    for item in qvods :
        s=re.search(r'target="_blank">(qvod:.*)</a>',str(item))
        if s :
            qvodList.append(s.group(1))
    
    for item in qvodList :
        ouFile.write('\t'.join(infoList)+'\t'+item+'\n')

ouFile.close()
 


