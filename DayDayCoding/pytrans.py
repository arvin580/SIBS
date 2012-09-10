#!/usr/bin/env python
#coding=utf-8
# pytrans.py 
# create :2010-6-2
# last modify: 2010-6-3
# author : ice_cube

import urllib,urllib2  
from sgmllib import SGMLParser  

class URLLister(SGMLParser):  
    """
    页面分析
    """
    def reset(self):  
        SGMLParser.reset(self)  
        self.result = []  
        self.open = False 

    def start_span(self, attrs):  
        id = [v for k, v in attrs if k=='id']  
        if 'result_box' in id:  
            self.open = True 
            
    def handle_data(self, text):  
        if self.open:  
            self.result.append(text)  
            self.open = False 

class GoogleTranslate(object):
    def __init__(self):
        self.url = 'http://translate.google.cn/translate_t' 

    def en2zh(self, text):
        """从英文翻译到中文  text为要翻译的内容"""
        values={'hl':'zh-CN','ie':'utf8','text':text,'langpair':"en|zh-CN"}  
        result = self.get_result(values)
        return result

    def zh2en(self, text):
        """从中文翻译到英文  text为要翻译的内容"""
        values={'hl':'zh-CN','ie':'utf8','text':text,'langpair':"zh-CN|en"}  
        result = self.get_result(values)
        return result

    def get_result(self, values):
        result = ""
        data = urllib.urlencode(values)  
        req = urllib2.Request(self.url, data)  
        req.add_header('User-Agent', "Mozilla/5.0+(compatible;+Googleb\
                /2.1;++http://www.google.com/bot.html)")  
        response = urllib2.urlopen(req)  
        parser = URLLister()  
        parser.feed(response.read())  
        parser.close()  
        for i in parser.result:  
            result += i + " "
        return result

if __name__ == "__main__":
    trans = GoogleTranslate()
    while True:  
        text = raw_input("请输入要翻译的文字(退出输入q)：")  
        if text=='q':  
            break;  
        print "翻译结果:"
        print trans.en2zh(text)
        print trans.zh2en(text)

