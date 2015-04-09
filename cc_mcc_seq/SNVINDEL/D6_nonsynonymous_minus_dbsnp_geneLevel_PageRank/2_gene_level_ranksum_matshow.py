from PyPlot.PyPlotClass import *

def gene_matshow(iFile,rowList,sampleNameList,oFile) :
    geneList=list()
    list1=list()
    row=0
    inFile=open(iFile)
    for line in inFile :
        row+=1
        if row in rowList :
            line=line.strip()
            fields=line.split('\t')
            geneList.append(fields[0])
            list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp=PyPlot(oFile)
    pp.heatmap_matshow(list1,sampleNameList,geneList)

gene_matshow('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel_pageranked',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'nonsynonymous_nondbsnp.geneLevel_pageranked_1_30.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel_pageranked',range(31,61),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'nonsynonymous_nondbsnp.geneLevel_pageranked_31_60.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel_pageranked',range(61,91),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'nonsynonymous_nondbsnp.geneLevel_pageranked_61_90.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel_pageranked',range(91,121),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'nonsynonymous_nondbsnp.geneLevel_pageranked_91_120.pdf')
gene_matshow('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel_pageranked',range(121,151),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'nonsynonymous_nondbsnp.geneLevel_pageranked_121_150.pdf')
