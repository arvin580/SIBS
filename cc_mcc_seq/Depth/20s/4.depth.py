chr1=249250621
chr2=243199373
chr3=198022430
chr4=191154276
chr5=180915260
chr6=171115067
chr7=159138663
chr8=146364022
chr9=141213431
chr10=135534747
chr11=135006516
chr12=133851895
chr13=115169878
chr14=107349540
chr15=102531392
chr16=90354753
chr17=81195210
chr18=78077248
chr19=59128983
chr20=63025520
chr21=48129895
chr22=51304566
chrX=155270560
chrY=59373566
chrM=16571

ch=[chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,
        chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,
        chr17,chr18,chr19,chr20,chr21,chr22,chrX,chrY]
ch.append(sum(ch))
ch_label=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8',
        'chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
        'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','genome']

sample=['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A',
                'CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A']

inFile = open('1.depth')
row = 0
depth = []
site = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    row += 1
    tmp = []
    if row % 2 == 1:
        for i in range(20):
            tmp.append(float(fields[i]))
        depth.append(tmp)
    else:
        for i in range(20):
            tmp.append(float(fields[i]))
        site.append(tmp)

inFile.close()

import numpy as np

depth.append(sum(np.array(depth)[:,:]))
site.append(sum(np.array(site)[:,:]))

depth = np.array(depth)
site = np.array(site)

average=depth/site
print(average)
average_full = [depth[i]/ch[i] for i in range(len(depth))]
print(average_full)

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def plot(xList,yTitle,ouFile):
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.2,0.8,0.7])
    ax.plot(range(1,26),xList)
    ax.set_xticks(range(27))
    ax.set_xticklabels(['']+ch_label+[''], rotation='vertical')
    ax.legend(sample,loc='upper left',bbox_to_anchor=[0.98,0.98],prop={'size':6})
    ax.set_ylabel(yTitle)

    plt.grid(True)
    plt.savefig(ouFile)

plot(average,'Average Depth (covered sites)','1.depth.cover.genome.pdf')
plot(average_full,'Average Depth (total sites)','1.depth.full.genome.pdf')

