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
            self.msg.append([msg['From'],msg['Subject']])
        
    
    def dlPaper(self) :
        for msg in self.msg :
            filename=''
            From=msg[0]
            url=msg[1]
            uf=self.urlFrom(url)

            if uf==1 or uf==2 :
                nature='http://www.nature.com'
                req=urllib2.Request(url)
                res=self.openner.open(req).read()
                parser=BeautifulSoup(res)
                pdf=parser.findAll(attrs={'class':re.compile(r'download')})
                for item in pdf :
                    s=re.search(r'href="(.*.pdf)"',str(item))
                    if s :
                        pdf=nature+s.group(1)
                        filename=pdf.rstrip('pdf').split('/')[-1]+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
                        urllib.urlretrieve(pdf,filename)
                        msg.append(filename)
                        msg.append(1)
                        break
            else :
                msg.append(filename)
                msg.append(0)
        
    def urlFrom(self,url):
        if url.find('nature')!=-1 :
            #if url.find('/nbt/') !=-1 :
            #    return 1
            #if url.find('/ng/')!=-1 :
            #    return 2
            return 1
        

    def sendMail(self) :
        for item in self.msg :
            if item[-1]==1 :
                to=item[0]
                subject=item[1]
                filename=item[2]

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

            if item[-1]==0 :
                to=item[0]
                subject=item[1]
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
    
