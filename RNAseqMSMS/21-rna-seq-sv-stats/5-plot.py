import math
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

inFile = open('HeLa-deletion-duplication-inversion-translocaton-num')
D1 = {}
D2 = {}
D3 = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D1[fields[0]] = []
    D2[fields[0]] = []
    D3[fields[0]] = []
    for item in fields[1:]:
        its = item.split(':')
        D1[fields[0]].append(int(its[0]))
        D2[fields[0]].append(int(its[1]))
        D3[fields[0]].append(int(math.log(int(its[1]),2)))

inFile.close()
print(D1['Translocation'])
print(D2['Translocation'])
print(D3['Translocation'])

'''
ymin = min(D3['Deletion']+D3['Duplication']+D3['Inversion']+D3['Translocation'])-1
ymax = max(D3['Deletion']+D3['Duplication']+D3['Inversion']+D3['Translocation'])
xmin = min(D1['Deletion']+D1['Duplication']+D1['Inversion']+D1['Translocation'])-1
xmax = max(D1['Deletion']+D1['Duplication']+D1['Inversion']+D1['Translocation'])
'''
ymin = min(D3['Duplication']+D3['Inversion']+D3['Translocation'])-1
ymax = max(D3['Duplication']+D3['Inversion']+D3['Translocation'])+1
xmin = min(D1['Duplication']+D1['Inversion']+D1['Translocation'])-1
xmax = max(D1['Duplication']+D1['Inversion']+D1['Translocation'])+1




fig = plt.figure()
ax=fig.add_subplot(211)
legBar = []

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
'''
xList=D1['Deletion']
yList=D3['Deletion']
ax.plot(xList,yList,linestyle='-', marker='*')
'''

xList=D1['Duplication']
yList=D3['Duplication']
legBar.append(ax.plot(xList,yList,linestyle='-', marker='o',color='blue'))

xList=D1['Inversion']
yList=D3['Inversion']
legBar.append(ax.plot(xList,yList,linestyle='-', marker='s',color='green'))

xList=D1['Translocation']
yList=D3['Translocation']
legBar.append(ax.plot(xList,yList,linestyle='-', marker='^',color='red'))

Bar=[legBar[i][0] for i in range(3)]

#ax.legend(legBar,['Duplication','Inversion','Translocation'],loc='upper right')
ax.legend(Bar,['Duplication','Inversion','Translocation'],loc='upper right')
legBar = []

ymin = min(D3['Deletion']+D3['Duplication']+D3['Inversion']+D3['Translocation'])-1
ymax = max(D3['Deletion']+D3['Duplication']+D3['Inversion']+D3['Translocation'])+1
xmin = min(D1['Deletion']+D1['Duplication']+D1['Inversion']+D1['Translocation'])-1
xmax = max(D1['Deletion']+D1['Duplication']+D1['Inversion']+D1['Translocation'])+1

ax=fig.add_subplot(212)
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
xList=D1['Deletion']
yList=D3['Deletion']
legBar.append(ax.plot(xList,yList,linestyle='-', marker='d',color='magenta'))
Bar=[legBar[i][0] for i in range(1)]
ax.legend(Bar,['Deletion'],loc='upper right')

plt.savefig('haha.pdf')

