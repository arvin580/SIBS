import numpy as np
def dist(xList,yList):
    s = 0
    for i in range(len(xList)):
        s += abs(xList[i] - yList[i])
    return s
        
def dp_dist(inF):
    ds = []
    for D in [0,3,5,10]:
        inFile = open(inF)
        dp = [[] for i in range(16)]
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            for i,item in enumerate(fields[-16:]):
                d = int(item.split(':')[2])
                if d <=D:
                    dp[i].append(0)
                else:
                    dp[i].append(1)
                        
        inFile.close()
        tmp = []
        for i in range(8):
            tmp.append(dist(dp[i],dp[i+8]))
        ds.append(tmp)
    return ds
    
    

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

sample = ['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10']

#line1=r'D=$\sum_{i=0}^N|T_i-N_i|\quadT_i=1(d_i\geq1),T_i=0(d_i<1);N_i=1(d_i\geq1),N_i=0(d_i<1)$'
line1=r'$T_i=1(d_i\geq1),\ \ T_i=0(d_i<1);\quadN_i=1(d_i\geq1),\ \ N_i=0(d_i<1)$'
line2=r'$T_i=1(d_i\geq3),\ \ T_i=0(d_i<3);\quadN_i=1(d_i\geq3),\ \ N_i=0(d_i<3)$'
line3=r'$T_i=1(d_i\geq5),\ \ T_i=0(d_i<5);\quadN_i=1(d_i\geq5),\ \ N_i=0(d_i<5)$'
line4=r'$T_i=1(d_i\geq10),\ \ T_i=0(d_i<10);\quadN_i=1(d_i\geq10),\ \ N_i=0(d_i<10)$'
line = [line1,line2,line3,line4]

def plot(xList,ouFile):
    fig = plt.figure()
    ax = fig.add_axes([0.2,0.1,0.7,0.7])
    ax.plot(range(1,9),xList[0],range(1,9),xList[1],range(1,9),xList[2],range(1,9),xList[3])
    ax.set_xticks(range(10))
    ax.set_xticklabels(['']+sample+[''])
    ax.set_ylabel(r'Distance = $\sum_{i=0}^N|T_i-N_i|$')
    ax.legend(line,loc='lower center',bbox_to_anchor=[0.5,1],prop={'size':8})

    plt.grid(True)
    plt.savefig(ouFile)

plot(dp_dist('sum_snv16s.exome_summary'), '1.depth.exome.dist.pdf')
plot(dp_dist('sum_snv16s.genome_summary'), '1.depth.genome.dist.pdf')

