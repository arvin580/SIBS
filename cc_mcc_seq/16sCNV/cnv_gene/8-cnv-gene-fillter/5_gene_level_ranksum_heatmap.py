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
            #if sum(N[0:8])>score :
            geneList.append(fields[1])
            print(fields[1])
            print(N)
            list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp=PyPlot(oFile)
    if figsize:
        pp.heatmap(list1,figsize=figsize,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)
    else:
        pp.heatmap(list1,col=False,xLabel=sampleNameList,yLabel=geneList,grid=True)

#gene_heatmap('6.varScan.copynumber.called.depth_1.5_upper_down_gene.ranksum_test.recurrent.mc',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'6.varScan.copynumber.called.depth_1.5_upper_down_gene.ranksum_test.recurrent.mc_1.86.heatmap.pdf',rowList=range(1,87),figsize=(12,18))
gene_heatmap('6.varScan.copynumber.called.depth_2_upper_down_gene.ranksum_test.recurrent.mc',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'6.varScan.copynumber.called.depth_2_upper_down_gene.ranksum_test.recurrent.mc.heatmap.pdf',figsize=(6,8))

