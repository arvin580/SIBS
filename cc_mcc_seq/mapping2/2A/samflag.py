##python samflag.py 2A.sam  2A.sam.stat
import sys
import os

inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[2],'w')

dict1={}
row=0

while(row<96):
    row+=1
    inFile1.readline()

for line in inFile1 :
    fields=line.split('\t')
    dict1.setdefault(fields[1],0)
    dict1[fields[1]]+=1

inFile1.close()

for key in dict1 :
    ouFile1.write(key+'\t'+str(dict1[key])+'\n')

ouFile1.close()
