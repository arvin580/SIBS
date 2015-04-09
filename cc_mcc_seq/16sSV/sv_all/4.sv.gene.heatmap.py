from PyPlot.PyPlotClass import *
files = ['inversion.exon.symbol','duplication.exon.symbol','translocation.exon.symbol','delition.exon.symbol']
def gene_heatmap(sampleNameList,ouF,figsize=0,rowList=[]):
    D = dict()
    for inF in files:
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

    ouFile = open('16s.sv.exome','w') 
    for k in D : 
        ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]])+'\n')


    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True)

gene_heatmap(['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'sv.exon.heatmap.pdf')


