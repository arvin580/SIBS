from PyPlot.PyPlotClass import *

def gene_matshow(iFile,rowList,sampleNameList,oFile,figsize=0) :
    geneList=list()
    list1=list()
    row=0
    inFile=open(iFile)
    for line in inFile :
        row+=1
        if row in rowList :
            line=line.strip()
            fields=line.split('\t')
            geneList.append(fields[1])
            list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp = PyPlot(oFile)
    if figsize:
        pp.heatmap(list1,figsize=figsize,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)
    else:
        pp.heatmap(list1,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)

gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ICC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'ICC.somatic.nonsynonymous_1_30.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.CHC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'CHC.somatic.nonsynonymous_1_30.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ICC_CHC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'ICC_CHC.somatic.nonsynonymous_1_30.pdf')
