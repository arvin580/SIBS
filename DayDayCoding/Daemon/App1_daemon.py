from daemonClass import *
class AppDaemon(Daemon) :

    def run(self) :
        while True :
            time.sleep(2)


a=AppDaemon('test.py')
a.start()
