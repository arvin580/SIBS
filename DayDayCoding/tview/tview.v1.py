#!/usr/bin/env python
import os
import fcntl
import termios
import time
import threading
import subprocess

offset = 50
def screenshot(cp,sample):
    ch = cp.split(':')[0]
    pos = int(cp.split(':')[1])+offset
    cmd = 'ssh hanice@10.10.155.143 "export DISPLAY=:0;import -window root tview/%s_%s_%s.png"'%(ch,pos,sample)
    os.system(cmd)

def readSNV():
    inFile = open('sum_snv16s.exome_summary.nonsynonymous')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[21]
        pos = str(int(fields[22])-offset)
        SNV.append(ch+':'+pos)
    inFile.close()

SNV=[]
readSNV()
ouFile = open('tview.log','a')

class Tview(threading.Thread):
    def __init__(self,sample):
        threading.Thread.__init__(self)
        self.sample = sample
    def run(self):
        time.sleep(2)
        ty = subprocess.check_output('tty').strip()
        tty = open(ty)
        for item in SNV:
            try:
                fcntl.ioctl(tty, termios.TIOCSTI,'g')
                for c in item:
                    fcntl.ioctl(tty, termios.TIOCSTI,c)
                fcntl.ioctl(tty, termios.TIOCSTI,'\n')
                screenshot(item,self.sample)
            except:
                ouFile.write(item+':'+self.sample+'\n')
        fcntl.ioctl(tty, termios.TIOCSTI,'q')


samples1 = ['4A','5A','9A','10A']
samples2 = ['4B','5B','9B','10B',]
samples3 = ['5A','6A','7A','10A']
samples4 = ['5B','6B','7B','10B']

for s in samples1:
    tv = Tview('ICC'+s)
    tv.start()
    os.system('samtools tview /netshare1/home1/szzhongxin/proj1/hansun/mapping/%s/%s.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta'%(s,s))

for s in samples2:
    tv = Tview('ICC'+s)
    tv.start()
    os.system('samtools tview /netshare1/home1/szzhongxin/proj1/hansun/mapping3/%s/%s.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta'%(s,s))

for s in samples3:
    tv = Tview('CHC'+s)
    tv.start()
    os.system('samtools tview /netshare1/home1/szzhongxin/proj1/hansun/mapping2/%s/%s.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta'%(s,s))

for s in samples4:
    tv = Tview('CHC'+s)
    tv.start()
    os.system('samtools tview /netshare1/home1/szzhongxin/proj1/hansun/mapping4/%s/%s.bam /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta'%(s,s))

ouFile.close()
