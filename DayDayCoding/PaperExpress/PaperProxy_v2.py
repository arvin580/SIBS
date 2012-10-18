from PaperProxyClass import *
import threading  
import Queue

#p=PaperProxy()
#p.getMail()
#p.dlPaper()
#p.sendMail()


queue=Queue.Queue()

class PaperProxyThread(threading.Thread) :
    def __init__(self,queue) :
        threading.Thread.__init__(self)
        self.queue=queue

    def __del__(self) :
        pass

    def run(self) :
        while True :
            data=self.queue.get()
            p=PaperProxy()
            p.getMail()
            p.dlPaper()
            p.sendMail()


for i in range(5) :
    t=PaperProxyThread(queue)
    t.start()

while True :
    queue.put('')
    time.sleep(120)
