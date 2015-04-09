from PyPlot.PyPlotClass import *

score=1

def gene_heatmap(iFile,sampleNameList,oFile,figsize=0,rowList=[]) :
    geneList=list()
    list1=list()
    row=0
    inFile=open(iFile)
    if rowList:
        for line in inFile :
            row+=1
            if row in rowList :
                line=line.strip()
                fields=line.split('\t')
                geneList.append(fields[1])
                list1.append([int(x) for x in fields[-8:]])
    else:
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            N=[int(x) for x in fields[-8:]]
            if sum(N[0:8])>score :
                geneList.append(fields[1])
                print(fields[1])
                list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp=PyPlot(oFile)
    if figsize:
        pp.heatmap(list1,figsize=figsize,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)
    else:
        pp.heatmap(list1,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)

#gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'heatmap.somatic.nonsynonymous_1_6.pdf',rowList=range(1,7))
gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'heatmap.somatic.nonsynonymous_recurrent.pdf',figsize=(12,18))


#gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(1,500),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_1_1451.pdf',figsize=(8,40))
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(61,91),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_61_90.pdf')
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(91,121),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_91_120.pdf')
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(121,151),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_121_150.pdf')
