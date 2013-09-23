D1 = {}
D2 = {}

inFile = open('unmapped-blated-viruses-100-76.seq.gene-stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D1[fields[0]] = int(fields[1])
inFile.close()

inFile = open('unmapped-blated-viruses-90-60.seq.gene-stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2[fields[0]] = int(fields[1])
inFile.close()


G1 = [D1['E1'],D1['E2'],D1['E4'],D1['E5'],D1['E6'],D1['E7'],D1['L1'],D1['L2']]
G2 = [D2['E1'],D2['E2'],D2['E4'],D2['E5'],D2['E6'],D2['E7'],D2['L1'],D2['L2']]

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import math

def get_color(i,N) :
    #if i <len(self.colors) :
    #    return self.colors[i]
    #else :
    #    return self.colors[-1]
    cm=plt.get_cmap('gist_rainbow')
    return(cm(i/float(N)))


fig = plt.figure()
ax=fig.add_subplot(111)

yList=np.array([[int(math.log(x+1,2)) for x in G1],[int(math.log(x+1,2)) for x in G2]])
n=len(yList[0])
N=len(yList)

xList=np.arange(n)

width=0.9/N

bar=[]
for i in range(N) :
    bar.append(ax.bar(xList+i*width,yList[i],width,color=get_color(i,N)))


ax.set_xlim(-0.1,n)
ax.set_ylim(0,yList.max()*1.1)
ax.set_xticks(xList+0.9/2)

xLabel=['E1','E2','E4','E5','E6','E7','L1','L2']
ax.set_xticklabels(xLabel)
#ax.set_xticklabels(xLabel,rotation='vertical')

legTitle=['Identity=100%, Length=76','Identity=90%, Length=60']
legX=0.97
legY=0.97
ax.set_xlabel('Gene of HPV-18')
ax.set_ylabel('Number of Reads (log2 value)')

legBar=[bar[i][0] for i in range(N)]

ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

fig.savefig('HeLa-Infection-num.pdf')

