D = {}
inFile = open('ERR0498-04-05.mpileup.depth2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = float(fields[1])
inFile.close()

CH = ['chr'+str(x) for x in range(1,23)] + ['chrX']
YCH = [D[x] for x in CH]
print(CH)
print(YCH)


import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def plot(yTitle,ouFile):
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.2,0.8,0.7])
    ax.plot(range(1,24),YCH)
    ax.set_xlim(0,24)
    ax.set_xticks(range(25))
    ax.set_yticks(range(0,30,2))
    ax.set_xticklabels(['']+CH+[''], rotation='vertical')
    #ax.legend('HeLa',loc='upper left',bbox_to_anchor=[0.98,0.98],prop={'size':6})
    ax.set_ylabel(yTitle)
    plt.grid(True)
    plt.savefig(ouFile)

plot('Average Depth (covered sites)','depth.cover.genome2.pdf')

