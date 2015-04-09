from PyPlot.PyPlotClass import *
import sys
import math
def gene_heatmap(sampleNameList, ouF, figsize=0, rowList=[]):
    D = dict()
    D2 = dict()
    for i,inF in enumerate(sampleNameList):
        inFile = open(inF + '.unmapped.sam.mapped.fa.fa.blasted.top.num')
        for line in inFile:
            line = line.strip()
            fields =line.split('\t')
            D.setdefault(fields[0],[0]*12)
            D2.setdefault(fields[0],[0]*12)
            D[fields[0]][i] = int(math.log(int(fields[1])+1,2))
            D2[fields[0]][i] = int(fields[1])

        inFile.close()
    
    ouFile = open(ouF+'.data','w')
    for k in D2 :
        ouFile.write(k+'\t'+'\t'.join([str(x)for x in D2[k]])+'\n')
        
    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    print(LD)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize,colorTickets=True)

gene_heatmap(['ICC1A','ICC2A','ICC3A','ICC6A','ICC7A','ICC8A','CHC1A','CHC2A','CHC3A','CHC4A','CHC8A','CHC9A'],'viruses.heatmap.pdf',figsize=(8,12))

