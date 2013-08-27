#!/usr/bin/env python
import os
import fcntl
import termios
import time
import threading
import subprocess
import sys

offset = 70 
#def screenshot(cp,sample):
#    ch = cp.split(':')[0]
#    pos = int(cp.split(':')[1])+offset
#    cmd = 'ssh hanice@10.10.155.143 "export DISPLAY=:0;import -window root tview/%s_%s_%s.png"'%(ch,pos,sample)
#    os.system(cmd)

def readSNV():
    if len(sys.argv)== 2:
        inFile = open(sys.argv[1])
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            ch = fields[21]
            pos = str(int(fields[22])-offset)
            SNV.append(ch+':'+pos)
        inFile.close()
    else:
        print('Input Error')
        return
    
    #if len(sys.argv) == 3:
    #    ch = sys.argv[1]
    #    pos = str(int(sys.argv[2])-offset)
    #    SNV.append(ch+':'+pos)

SNV=[]
readSNV()
#ouFile = open('tview.v2.log','a')

class Tview(threading.Thread):
    def __init__(self,snv,sample):
        threading.Thread.__init__(self)
        self.sample = sample
        self.snv = snv
    def run(self):
        time.sleep(1)
        ty = subprocess.check_output('tty').strip()
        tty = open(ty)
        try:
            fcntl.ioctl(tty, termios.TIOCSTI,'g')
            for c in self.snv:
                fcntl.ioctl(tty, termios.TIOCSTI,c)
            fcntl.ioctl(tty, termios.TIOCSTI,'\n')
            #screenshot(item,self.sample)
        except:
            #ouFile.write(item+':'+self.sample+'\n')
            pass
        #fcntl.ioctl(tty, termios.TIOCSTI,'q')

row = 0
for item in SNV:
        row +=1
        tv = Tview(item,'HeLa')
        tv.start()
        os.system('samtools tview /netshare1/home1/people/hansun/Data/HeLa/Illumina/ERR0498-04-05.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta')
        print(str(row)+'\t'+item)
#ouFile.close()
