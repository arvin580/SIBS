from PyPlot.PyPlotClass import *

def point_matshow(iFile,geneNum,sampleNameList) :
    geneList=list()
    list1=list()
    row=0
    inFile=open(iFile)
    for line in inFile :
        row+=1
        if row<=geneNum :
            line=line.strip()
            fields=line.split()
            geneList.append(fields[0]+'('+fields[1]+':'+fields[2]+')')
            list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    pp=PyPlot()
    pp.heatmap_matshow(list1,sampleNameList,geneList)

point_matshow('repair_gene_somatic',5,['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])

