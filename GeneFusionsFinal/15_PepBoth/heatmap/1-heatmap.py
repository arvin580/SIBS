from PyPlot.PyPlotClass import *
def gene_heatmap(sampleNameList,ouF,figsize=0,rowList=[]):
    inFile = open('Tandem.Omssa.Fusion.Splicing.gene.curate')
    LD = []
    geneList = []
    pepList = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        LD.append([int(x) for x in fields[2:4]])
        geneList.append(fields[0])
        pepList.append(fields[1])
    inFile.close()

    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize)


gene_heatmap(['X!Tandem','Omssa'],'Tandem.Omssa.Fusion.Splicing.gene.curate.heatmap.pdf',figsize=(8,12))

