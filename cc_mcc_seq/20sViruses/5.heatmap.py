from PyPlot.PyPlotClass import *
import sys
import math
import numpy

V = {}
V['NC_001669.1']='Simian virus'
V['NC_006273.2']='Human herpesvirus 5'
V['NC_003287.2']='Enterobacteria phage M13'
V['NC_000898.1']='Human herpesvirus 6B'
V['NC_007605.1']='Human herpesvirus 4 type 1'
V['NC_009334.1']='Human herpesvirus 4'
V['NC_003977.1']='Hepatitis B virus'

def gene_heatmap(sampleNameList, ouF, figsize=0, rowList=[]):
    D = dict()
    D2 = dict()
    for i,inF in enumerate(sampleNameList):
        inFile = open(inF + '.unmapped.sam.mapped.fa.fa.blasted.top.num')
        for line in inFile:
            line = line.strip()
            fields =line.split('\t')
            D.setdefault(fields[0],[0]*20)
            D2.setdefault(fields[0],[0]*20)
            #D[fields[0]][i] = int(math.log(int(fields[1])+1,2))
            D[fields[0]][i] = int(fields[1])
            D2[fields[0]][i] = int(fields[1])
        inFile.close()
    D3 = {}
    D4 = {}
    D3['Human herpesvirus']=[int(math.log(x+1,2)) for x in (numpy.array(D['NC_006273.2'])+numpy.array(D['NC_000898.1'])+numpy.array(D['NC_007605.1'])+numpy.array(D['NC_009334.1']))]
    D3['Hepatitis B virus']=[int(math.log(x+1,2)) for x in D['NC_003977.1']]
    D3['Enterobacteria phage M13']=[int(math.log(x+1,2)) for x in D['NC_003287.2']]

    D4['Human herpesvirus']=numpy.array(D['NC_006273.2'])+numpy.array(D['NC_000898.1'])+numpy.array(D['NC_007605.1'])+numpy.array(D['NC_009334.1'])
    D4['Hepatitis B virus']=D['NC_003977.1']
    D4['Enterobacteria phage M13']=D['NC_003287.2']


    ouFile = open(ouF+'.data','w')
    for k in D4 :
        ouFile.write(k+'\t'+'\t'.join([str(x)for x in D4[k]])+'\n')
        
    LD = []
    geneList = []
    for key in D3 :
        if max(D3[key])>3:
            LD.append(D3[key])
            geneList.append(key)
    print(LD)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize,colorTickets=True)

gene_heatmap(['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'viruses.heatmap2.pdf',figsize=(6,8))

