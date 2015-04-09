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
            geneList.append(fields[1])
            list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp=PyPlot(oFile)
    pp.heatmap_matshow(list1,sampleNameList,geneList)

gene_matshow('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'exome.UTR.INDEL.nondbsnp_1_30.pdf')
gene_matshow('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test',range(31,61),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'exome.UTR.INDEL.nondbsnp_31_60.pdf')
gene_matshow('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test',range(61,91),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'exome.UTR.INDEL.nondbsnp_61_90.pdf')
gene_matshow('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test',range(91,121),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'exome.UTR.INDEL.nondbsnp_91_120.pdf')
gene_matshow('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test',range(121,151),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'exome.UTR.INDEL.nondbsnp_121_150.pdf')
