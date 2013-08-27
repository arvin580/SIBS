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

ymax= 1300
ymin = -10
xmax = 110
xmin = 0
fig = plt.figure()
ax=fig.add_subplot(111)
ax.plot(L1,L2)

ax.set_ylim(ymin,ymax)
ax.set_xlim(xmin,xmax)

'''
ax.set_yticks(range(-10,ymax,100))
ax.set_xticks(range(-10,xmax,10))
ax.set_yticklabels(range(0,ymax,100))
ax.set_xticklabels(range(0,xmax,10))
'''
plt.savefig('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num.pdf')

