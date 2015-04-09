import os
os.chdir('genome')



dict1=dict()
dict2=dict()
inFile=open('sum_snp.genome_combined.sorted.pass012.new.atcg.exome')
for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1[fields[0]]=[int(i) for i in fields[1:11]]
    dict2[fields[0]]=[int(i) for i in fields[11:21]]

inFile.close()


type=['AT','AC','AG','TA','TC','TG','CA','CT','CG','GA','GT','GC']
type2=['TG','TC','TA','CA','CG','CT']
type3=['T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A']
dict3=dict()
dict4=dict()

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
for item in type :
    dict3.setdefault(item,[])
    dict4.setdefault(item,[])

    dict3[item].append(np.array(dict1[item]).mean())
    dict3[item].append(np.array(dict1[item]).std())
    dict3[item].append(np.array(dict1[item]))

    dict4[item].append(np.array(dict2[item]).mean())
    dict4[item].append(np.array(dict2[item]).std())
    dict4[item].append(np.array(dict2[item]))
    
#    dict3[item].append(np.array([i/300 for i in dict1[item]]).mean())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]).std())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]))

#    dict4[item].append(np.array([i/300 for i in dict2[item]]).mean())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]).std())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]))
 

#N = len(type)
#danMean   = [dict3[item][0] for item in type]
#hunMean   = [dict4[item][0] for item in type]
#danStd   = [dict3[item][1] for item in type]
#hunStd  = [dict4[item][1] for item in type]
N = len(type2)
danMean   = [dict3[item][0] for item in type2]
hunMean   = [dict4[item][0] for item in type2]
danStd   = [dict3[item][1] for item in type2]
hunStd  = [dict4[item][1] for item in type2]



fig = plt.figure()
ax = fig.add_subplot(111)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = ax.bar(ind, danMean,   width, color='r', yerr=danStd)
p2 = ax.bar(ind+width, hunMean, width, color='y', yerr=hunStd)

#plt.title('Scores by group and gender')

ax.set_xlim(-0.3,6)
ax.set_ylim(0,200)
ax.set_ylabel('Number of substitutions')
#plt.yticks(np.arange(0,81,10))

ax.set_xticks(ind+width)
ax.set_xticklabels(type3) 
#ax.legend( (p1[0], p2[0]), ('CC', 'MCC') )
ax.legend( (p1[0], p2[0]), ('CC', 'MCC'),loc = 'upper right',bbox_to_anchor=(0.85,0.95))

plt.savefig('sum_snp.genome_combined.sorted.pass012.new.atcg.exome.pdf')


'''



N = 5
menMeans   = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd     = (2, 3, 4, 1, 2)
womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r', yerr=womenStd)
p2 = plt.bar(ind, womenMeans, width, color='y',
                     bottom=menMeans, yerr=menStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.yticks(np.arange(0,81,10))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

plt.show()

'''
