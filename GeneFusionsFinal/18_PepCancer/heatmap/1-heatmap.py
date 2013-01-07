from PyPlot.PyPlotClass import *
def gene_heatmap(sampleNameList,ouF,figsize=0,rowList=[]):
    inFile = open('Tandem.Omssa.FDR.pep.genefusions.splicing.final.pos.3.3.spec2.num.tandem')
    LD = []
    geneList = []
    pepList = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        LD.append([int(x) for x in fields[2:5]])
        geneList.append(fields[1])
        pepList.append(fields[0])
    inFile.close()

    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize)


gene_heatmap(['ADC','SCC','Normal'],'Tandem.Omssa.FDR.pep.genefusions.splicing.final.pos.3.3.spec2.num.tandem.heatmap.pdf',figsize=(6,8))

