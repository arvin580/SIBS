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
    if len(sys.argv)== 1:
        inFile = open('/netshare1/home1/people/hansun/DayDayCoding/tview/sum_snv16s.exome_summary.nonsynonymous')
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            ch = fields[21]
            pos = str(int(fields[22])-offset)
            SNV.append(ch+':'+pos)
        inFile.close()

    if len(sys.argv)== 2:
        inFile = open(sys.argv[1])
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            ch = fields[1]
            pos = str(int(fields[2])-offset)
            SNV.append(ch+':'+pos)
        inFile.close()
    
    if len(sys.argv) == 3:
        ch = sys.argv[1]
        pos = str(int(sys.argv[2])-offset)
        SNV.append(ch+':'+pos)

SNV=[]
readSNV()
ouFile = open('tview.v2.log','a')

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
            ouFile.write(item+':'+self.sample+'\n')
        #fcntl.ioctl(tty, termios.TIOCSTI,'q')


samples = [['4A','mapping'],['4B','mapping3'],['5A','mapping'],['5B','mapping3'],
        ['9A','mapping'],['9B','mapping3'],['10A','mapping'],['10B','mapping3'],
        ['5A','mapping2'],['5B','mapping4'],['6A','mapping2'],['6B','mapping4'],
        ['7A','mapping2'],['7B','mapping4'],['10A','mapping2'],['10B','mapping4']]

for item in SNV:
    for s in samples:
        tv = Tview(item,s[0])
        tv.start()
        os.system('samtools tview /netshare1/home1/szzhongxin/proj1/hansun/%s/%s/%s.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta'%(s[1],s[0],s[0]))
    
ouFile.close()
