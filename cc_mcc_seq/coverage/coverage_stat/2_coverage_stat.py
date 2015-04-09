import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

for sample in range(3,13) :
    for ch in chr :
        inFile=open('../fudan2.coverage')
        list1=list()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if fields[0].find(ch)!=-1 :
                list1.append(int(fields[sample]))

        fig = plt.figure()
        plt.plot(range(1,len(list1)+1),list1)
        plt.savefig('fudan2.coverage.'+ch+'.'+str(sample-3)+'.pdf')

        inFile.close()
