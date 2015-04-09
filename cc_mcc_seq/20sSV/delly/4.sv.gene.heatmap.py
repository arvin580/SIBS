from PyPlot.PyPlotClass import *
def gene_heatmap(inF,sampleNameList,ouF,figsize=0,rowList=[]):
    D = dict()
    inFile = open(inF)
    row = -1
    for line in inFile:
        row+=1
        line = line.strip()
        fields =line.split('\t')
        for item in fields[1:]:
            D.setdefault(item,[0]*20)
            D[item][row]+=1
    inFile.close()

    D2 = {}
    for k in D:
        fields = k.split('/')
        if len(fields)>1:
            D2[k]=D[k]
    for k in D2: 
        D.pop(k)
        fields = k.split('/')
        k2 = fields[0]+'/'+'...'
        if k2 not in D:
            D[k2] = D2[k]
        else:
            print('warning: ' + k2) 

    LD = []
    geneList = []
    for key in D :
        if sum(D[key])>1:
            LD.append(D[key])
            geneList.append(key)

    ouFile = open(ouF+'.gene', 'w')
    for i in range(len(geneList)):
        ouFile.write(geneList[i]+'\t'+'\t'.join([str(x) for x in LD[i]])+'\n')
    ouFile.close()
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True)

gene_heatmap('1.sv.stat.gene.symbol', ['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'delly.gene.heatmap.pdf')
gene_heatmap('1.sv.stat.exon.symbol', ['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'delly.exon.heatmap.pdf')


