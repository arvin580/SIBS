import re
from PyPlot.PyPlotClass import *


def dp_stat(iFile):
    dp = []
    inFile = open(iFile)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        s = re.search('DP=(\d+);', fields[33])
        if s:
            dp.append(int(s.group(1)))
    inFile.close()
    pp = PyPlot(iFile + '.DP.pdf')
    pp.hist(dp)

    x = [0,5,10,20,30,40,50,60,70,80,90, 100, 200, 300, 400, 500, 600, 700,
         800, 900, 1000,1500,2000,3000,4000]
    y = [0]*len(x)

    for item in dp:
        for i in range(1,len(x)):
            if x[i-1] <= item< x[i]:
                y[i]+=1
    ouFile = open(iFile + '.DP.stat','w')
    ouFile.write('\t'.join([str(m) for m in x[1:]])+'\n')
    ouFile.write('\t'.join([str(m) for m in y[1:]])+'\n')


dp_stat('sum_snv16s.exome_summary')
dp_stat('sum_snv16s.genome_summary')
