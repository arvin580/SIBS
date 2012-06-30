from PaperProxyClass import *
import threading  
import Queue

p=PaperProxy()
p.getMail()
p.dlPaper()
p.sendMail()
