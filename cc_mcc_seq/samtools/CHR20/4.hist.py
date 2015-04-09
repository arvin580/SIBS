import os
import sys 
import re
#chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
#        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
#        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']

chrs = ['chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']


def get_dp(s):
    r=re.search(r'DP=(\d+);',s)
    if r :
        dp.append(int(r.group(1)))

def get_gq(s):
    gq.append(float(s.split(':')[-1]))


head = 27
num = [0] * 16
somatic = [0] * 8 
dp = []
gq = []
for ch in chrs:
    f = 'var.flt.%s.vcf'%ch
    inFile=open(f)
    for n in range(head):
        line = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        get_dp(fields[7])
        for item in fields[-16:]:
            get_gq(item)
    inFile.close()


from PyPlot.PyPlotClass import *
pp = PyPlot()
pp.hist(dp)
#pp = PyPlot()
#pp.hist(gq)






