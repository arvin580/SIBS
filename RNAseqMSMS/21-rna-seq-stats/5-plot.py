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

fig = plt.figure()
ax=fig.add_subplot(111)

xList=[D1['Translocation']]
yList=[D3['Translocation']]
ax.plot(xList,yList,linestyle='-', marker='*')

xList=[D1['Inversion']]
yList=[D3['Inversion']]
ax.plot(xList,yList,linestyle='-', marker='o')

plt.savefig('haha.pdf')

