from PyPlot.PyPlotClass import *

'''
pyHeatmap.py 156-165 changed to clolor viruses.
'''



def gene_heatmap(sampleNameList,ouF,figsize=0,rowList=[]):
    LD = []
    geneList = []
    inFile = open('viruse.pos.distribution')
    for line in inFile :
        line = line.strip()
        fields = line.split('\t')
        LD.append([int(x) for x in fields[1:]])
        geneList.append(fields[0])
    inFile.close()
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=[10,16])

gene_heatmap(['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'viruse.pos.distribution.heatmap.pdf')


