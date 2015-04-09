import re
from PyPlot.PyPlotClass import *


def qual_stat(iFile):
    qual = []
    inFile = open(iFile)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[-16:]:
            qual.append(int(item.split(':')[-1]))
    inFile.close()
    pp = PyPlot(iFile + '.qual.pdf')
    pp.hist(qual)

    x = [0,5,10,15,20,25,30,40,50,100,200,300,400,500,800,1000]
    y = [0]*len(x)

    for item in qual:
        for i in range(1,len(x)):
            if x[i-1] <= item< x[i]:
                y[i]+=1
    ouFile = open(iFile + '.qual.stat','w')
    ouFile.write('\t'.join([str(m) for m in x[1:]])+'\n')
    ouFile.write('\t'.join([str(m) for m in y[1:]])+'\n')


qual_stat('sum_snv16s.exome_summary')
qual_stat('sum_snv16s.genome_summary')
