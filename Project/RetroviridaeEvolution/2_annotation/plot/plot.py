import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

inFile=open('human_ABL1')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    name=fields[1]
    chrom=fields[2]
    strand=fields[3]
    txStart=int(fields[4])
    txEnd=int(fields[5])
    cdsStart=int(fields[6])
    cdsEnd=int(fields[7])
    exonCount=int(fields[8])
    exonStarts=fields[9].split(',')[0:-1]
    exonEnds=fields[10].split(',')[0:-1]
    name2=fields[12]
    exonFrames=fields[15].split(',')[0:-1]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(exonCount) :
        ax.plot([exonStarts[i],exonEnds[i]],[1,1])
    ax.plot([cdsStart,cdsEnd],[2,2])
    ax.set_xlim(txStart,txEnd)
    ax.set_ylim(0,2)
    plt.savefig('haha.pdf')


inFile.close()
