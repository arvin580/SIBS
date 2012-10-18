import threading
import Queue
import time
import mechanize
import poplib
import smtplib
import imaplib
import re
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders

popServer='pop.126.com'
smtpServer='smtp.126.com'
imapServer='imap.126.com'
user='paperexpress@126.com'
passwd='expresspaper'
time_sleep=60


class PaperExpress():
    def __init__(self,user=user,passwd=passwd,pop=popServer,smtpServer=smtpServer,imapServer=imapServer):
        self.user=user
        self.passwd=passwd

        self.smtpServer=smtpServer
        #self.smtp=smtplib.SMTP(self.smtpServer)
        #self.smtp.login(self.user,self.passwd)
        self.imapServer=imapServer
        self.imap=imaplib.IMAP4(self.imapServer)
        self.imap.login(self.user,self.passwd)


        self.br = mechanize.Browser()
        self.br.addheaders = [('User-agent', 'Mozilla/5.0')]
        self.br.set_handle_robots(False)
        self.log=open('PaperExpress.log','a')


    def checkMail(self,queue):
        while True:
            self.imap.select()
            typ, data = self.imap.search(None, 'UnSeen')
            for num in data[0].split():
                typ, data = self.imap.fetch(num, '(RFC822)')
                msg = email.message_from_string(data[0][1])
                queue.put([msg['From'],msg['Subject']])
            time.sleep(time_sleep)


    def sendMail(self,msg):
        try:
            self.smtp=smtplib.SMTP(self.smtpServer)
            self.smtp.login(self.user,self.passwd)
            if msg[-1]!=0 :
                to=msg[0]
                subject=msg[1]
                filename=msg[2]
    
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
                self.log.write('success'+'\t'+to+'\t'+subject+'\t'+filename+'\n')
                self.log.flush()
                os.remove(filename)
            else:
                to=msg[0]
                subject=msg[1]
                msg = MIMEText('Sorry, I can fetch this paper for you.')
                msg['Subject']='reply:'+subject
                msg['From'] =  self.user
                msg['To'] = to
    
                self.smtp.sendmail(self.user,to,msg.as_string())
                self.log.write('failure'+'\t'+to+'\t'+subject+'\t'+''+'\n')
                self.log.flush()
            self.smtp.quit()
        except:
            print('cant send mail')

    def downLoadPaper(self,msg):
        From=msg[0]
        url=msg[1]
        if url.find('nature')!=-1:
            self.nature(msg)
        elif url.find('science')!=-1:
            self.science(msg)
        elif url.find('cell')!=-1:
            self.cell(msg)
        else:
            self.default(msg)
        self.sendMail(msg)
    
    def nature(self, msg):
        try:
            url= msg[1]
            self.br.open(url)
            rsp = self.br.follow_link(text_regex=r'.*PDF.*')
            pdf = rsp.geturl()
            filename = rsp.geturl().split('/')[-1]
            done = self.br.retrieve(pdf, filename)
            if done:
                msg.append(filename)
            else:
                msg.append(0)
        except:
            msg.append(0)



    def science(self, msg):
        try:
            url= msg[1]
            self.br.open(url)
            rsp = self.br.follow_link(text_regex=r'.*PDF.*')
            pdf = rsp.geturl()
            filename = rsp.geturl().split('/')[-1]
            done = self.br.retrieve(pdf, filename)
            if done:
                msg.append(filename)
            else:
                msg.append(0)
        except:
            msg.append(0)


    def cell(self, msg):
        try:
            url= msg[1]
            self.br.open(url)
            rsp = self.br.follow_link(text_regex=r'Switch to Standard View')
            self.br.open(rsp.geturl())
            rsp = self.br.follow_link(text_regex=r'.*PDF.*')
            pdf = rsp.geturl() + '?intermediate=true'
            filename = rsp.geturl().split('/')[-1]
            done = self.br.retrieve(pdf, filename)
            if done:
                msg.append(filename)
            else:
                msg.append(0)
        except:
            msg.append(0)

    def default(self, msg):
        try:
            url= msg[1]
            self.br.open(url)
            rsp = self.br.follow_link(text_regex=r'.*PDF.*')
            pdf = rsp.geturl()
            filename = rsp.geturl().split('/')[-1]
            done = self.br.retrieve(pdf, filename)
            if done:
                msg.append(filename)
            else:
                msg.append(0)
        except:
            msg.append(0)


class PaperExpressThread(threading.Thread):
    
    def __init__(self, queue,pe):
        threading.Thread.__init__(self)
        self.queue = queue
        self.pe = pe

    def run(self):
        while True:
            msg = self.queue.get()
            self.pe.downLoadPaper(msg)
            self.queue.task_done()
   

def main():

    queue = Queue.Queue()
    pe = PaperExpress()

    for i in range(5):
        t = PaperExpressThread(queue,pe)
        t.setDaemon(True)
        t.start()
    
    pe.checkMail(queue)
 
main()
