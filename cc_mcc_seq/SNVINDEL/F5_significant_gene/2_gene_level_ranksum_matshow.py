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

gene_matshow('SNV.genome.somatic.exome.UTR.nondbsnp.geneLevel.ICC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'ICC_somatic.nonsynonymous_nondbsnp_1_30.pdf')
gene_matshow('SNV.genome.somatic.exome.UTR.nondbsnp.geneLevel.CHC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'CHC_somatic.nonsynonymous_nondbsnp_1_30.pdf')
gene_matshow('SNV.genome.somatic.exome.UTR.nondbsnp.geneLevel.ICC_CHC.fisher_test.sorted',range(1,31),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'ICC_CHC_somatic.nonsynonymous_nondbsnp_1_30.pdf')
