import urllib2
import urllib
import time
import cookielib
import threading  

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)


class Voting(threading.Thread):  

    def __init__(self,interval):  
        threading.Thread.__init__(self)  
        self.thread_stop = False  
	self.interval=interval
   
    def run(self): 
        while not self.thread_stop:  
	    req=urllib2.Request('http://events.mcss.ca/fcwr2/vote_handler.php?id=24')
	    res=openner.open(req)
	    html=res.read()
            print(html)
	    time.sleep(self.interval)
    def stop(self):  
        self.thread_stop = True  

while True :
    newThread =Voting(1)
    newThread.start()
    time.sleep(30)
    newThread.stop()
