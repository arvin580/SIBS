import subprocess
import poplib
import smtplib
import imaplib
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import os
import cookielib
import email
from email import parser
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders

popServer='pop.126.com'
smtpServer='smtp.126.com'
imapServer='imap.126.com'
user='paperproxy@126.com'
passwd='proxypaper'


class PaperProxy :
    def __init__(self,user=user,passwd=passwd,pop=popServer,smtpServer=smtpServer,imapServer=imapServer) :
        self.user=user
        self.passwd=passwd

        #self.pop=pop
        #self.pop=poplib.POP3_SSL(self.pop)
        #self.pop.user(self.user)
        #self.pop.pass_(self.passwd)

        self.smtpServer=smtpServer
        self.smtp=smtplib.SMTP(self.smtpServer)
        self.smtp.login(self.user,self.passwd)

        self.imapServer=imapServer
        self.imap=imaplib.IMAP4(self.imapServer)
        self.imap.login(self.user,self.passwd)


        self.msg=[]
        
        myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self.openner=urllib2.build_opener(myCookie)
        self.openner.addheaders = [('User-agent', 'Mozilla/5.0')]

        self.log=open('PaperProxy.log','a')
    
    #def getMail2(self) :
    #    msg=[]
    #    for i in range(len(self.pop.list()[1])) :
    #        msg.append(self.pop.retr(i+1))
        
    #    for i in range(len(msg)) :
    #        msg[i]=parser.Parser().parsestr('\n'.join(msg[i][1]))

    #    for item in msg:
    #        self.msg.append([item['From'],item['subject']])
                
    def getMail(self) :
        self.imap.select()
        typ, data = self.imap.search(None, 'UnSeen')
        for num in data[0].split():
            typ, data = self.imap.fetch(num, '(RFC822)')
            msg = email.message_from_string(data[0][1])
            self.msg.append({'From':msg['From'],'Subject':msg['Subject'],'Date':msg['Date'],'Flag':0,'FileName':''})

    def dlPaper(self) :
        for msg in self.msg :
            
            url=msg['Subject']
            uf=self.urlFrom(url)

            if uf==1 :
                self.FromNature(msg)
            elif uf==2 :
                self.FromScience(msg)
            elif uf==3 :
                self.FromCell(msg)
            else :
                msg['FileName']=''
                msg['Flag']=0
        
    def urlFrom(self,url):
        if url.find('nature')!=-1 :
            return 1
        if url.find('sciencemag')!=-1 :
            return 2
        if url.find('cell.com')!=-1 :
            return 3
        
    def FromCell(self,msg) :
        url=msg['Subject']
        pub=''
        req=urllib2.Request(url)
        res=self.openner.open(req).read()
        parser=BeautifulSoup(res)
        pr=parser.findAll(attrs={'name':re.compile(r'citation_pdf_url')})
        for item in pr :
            s=re.search(r'content="(.*?.pdf)"',str(item))
            if s :
                pdf=pub+s.group(1)
                print(pdf)
                req=urllib2.Request(pdf)
                res=self.openner.open(req).read()
                parser=BeautifulSoup(res)
                pa=parser.findAll('p')
                for it in pa :
                    s=re.search(r'href="(.*?)"',str(it))
                    if s :
                        s=s.group(1).split('amp;')
                        pdf=''.join(s)
                        print(pdf)
                        #filename=pdf.rstrip('pdf').split('/')[-1]+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
                        #urllib.urlretrieve(pdf,filename)
                        #msg['FileName']=filename
                        #msg['Flag']=1


    def FromNature(self,msg) :
        url=msg['Subject']
        pub='http://www.nature.com'
        req=urllib2.Request(url)
        res=self.openner.open(req).read()
        parser=BeautifulSoup(res)
        pr=parser.findAll(attrs={'class':re.compile(r'download')})
        for item in pr :
            s=re.search(r'href="(.*?.pdf)"',str(item))
            if s :
                pdf=pub+s.group(1)
                filename=pdf.rstrip('pdf').split('/')[-1]+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
                urllib.urlretrieve(pdf,filename)
                msg['FileName']=filename
                msg['Flag']=1

    def FromScience(self,msg) :
        url=msg['Subject']
        pub='http://www.sciencemag.org'
        req=urllib2.Request(url)
        res=self.openner.open(req).read()
        parser=BeautifulSoup(res)
        pr=parser.findAll('a')
        for item in pr :
            s=re.search(r'href="(.*?.pdf)"',str(item))
            if s :
                pdf=pub+s.group(1)
                filename=pdf.rstrip('pdf').split('/')[-1]+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
                urllib.urlretrieve(pdf,filename)
                msg['FileName']=filename
                msg['Flag']=1

    def sendMail(self) :
        for item in self.msg :
            if item['Flag']==1 :
                to=item['From']
                subject=item['Subject']
                filename=item['FileName']

                msg = MIMEMultipart()
                msg['Subject']='reply:'+subject
                msg['From'] =  self.user
                msg['To'] = to

                inFile=open(filename,'rb')
                part=MIMEBase('application', "octet-stream")
                part.set_payload(inFile.read())
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename='+filename)
                msg.attach(part)
                inFile.close()
                
                self.smtp.sendmail(self.user,to,msg.as_string())
                self.log.write('success'+'\t'+subject+'\t'+filename+'\n')
                os.remove(filename)

            if item['Flag']==0 :
                to=item['From']
                subject=item['Subject']
                msg = MIMEText('Sorry, I can fetch this paper for you.')
                msg['Subject']='reply:'+subject
                msg['From'] =  self.user
                msg['To'] = to

                self.smtp.sendmail(self.user,to,msg.as_string())
                self.log.write('failure'+'\t'+subject+'\t'+''+'\n')


    def __del__(self) :
        #self.pop.quit()
        self.smtp.close()
        self.imap.close()
        self.log.close()
    
