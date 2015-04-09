#!/usr/bin/python
import sys
import os
file=sys.argv[1]
ff='samtools tview /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/'+file+'/'+file+'.realigned.bam $hg19'
os.system(ff)



