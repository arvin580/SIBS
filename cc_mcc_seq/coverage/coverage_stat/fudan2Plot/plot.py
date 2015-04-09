import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import math

chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

files=os.listdir('../fudan2')

for ch in chr :
    for sample in range(10) :
        for f in files :
            if f.find(ch+'.'+str(sample))!=-1 :
                x_list=[]
                inFile=open('../fudan2/'+f)
                for line in inFile :
                    line=line.strip()
                    x_list.append(math.log(int(line)+1,2))
                inFile.close()
                fig = plt.figure()
                plt.plot(range(1,len(x_list)+1),x_list)
                plt.savefig(f+'.pdf')



