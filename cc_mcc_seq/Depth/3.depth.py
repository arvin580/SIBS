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
ch_label=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8',
        'chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
        'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']
sample=['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B',
        'CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B']

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
        for i in range(-16,-8):
            tmp.append(float(fields[i]))
            tmp.append(float(fields[i+8]))
        depth.append(tmp)
    else:
        for i in range(-16,-8):
            tmp.append(float(fields[i]))
            tmp.append(float(fields[i+8]))
        site.append(tmp)

inFile.close()

import numpy as np
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

def plot(xList,ouFile):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(1,25),xList)
    ax.set_xticks(range(26))
    ax.set_xticklabels(['']+ch_label+[''], rotation='vertical')
    ax.legend(sample,loc='upper left',bbox_to_anchor=[0.96,0.98],prop={'size':6})

    plt.grid(True)
    plt.savefig(ouFile)

plot(average, '1.depth.cover.pdf')
plot(average_full, '1.depth.full.pdf')

