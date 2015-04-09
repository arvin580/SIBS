from PyPlot.PyPlotClass import *
def gene_heatmap(inF,sampleNameList,ouF,figsize=0,rowList=[]):
    D = dict()
    inFile = open(inF)
    row = -1
    for line in inFile:
        row+=1
        line = line.strip()
        fields =line.split('\t')
        for item in fields[1:]:
            D.setdefault(item,[0]*16)
            D[item][row]+=1
    inFile.close()

    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True)

gene_heatmap('1.sv.stat.gene.symbol', ['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'invy.gene.heatmap.pdf')
gene_heatmap('1.sv.stat.exon.symbol', ['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'invy.exon.heatmap.pdf')


