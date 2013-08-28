import math
inFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    num = int(fields[1])
    D.setdefault(num,0)
    D[num]+=1
inFile.close()
L1 = []
L2 = []
L3 = []
for k in D:
    L1.append(k)
    L2.append(D[k])
    L3.append(math.log(D[k],2))

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

#a=PyPlot('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num.pdf')

#a.plot2([L1,L2])

ymax= 900
ymin = -10
xmax = 70
xmin = 0
fig = plt.figure()
ax=fig.add_subplot(111)
ax.plot(L1,L2,marker='*',color='magenta',markerfacecolor='magenta')

ax.set_ylim(ymin,ymax)
ax.set_xlim(xmin,xmax)
ax.set_xlabel('Number of Structural Variation Events')
ax.set_ylabel('Number of Genes')
ax.set_yticklabels(['']+range(1,ymax,200))
#ax.set_xticklabels(range(1,xmax,20))

ax.set_yticks([-10]+range(1,ymax,200))
#ax.set_xticks(range(0,xmax,20))
plt.savefig('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num.pdf')

