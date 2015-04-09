from PyPlot.PyPlotClass import *
#files = ['invy.1.sv.stat.exon.symbol','jumpy.1.sv.stat.exon.symbol','duppy.1.sv.stat.exon.symbol','delly.1.sv.stat.exon.symbol']
files = ['delly.1.sv.stat.exon.symbol']
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
                D.setdefault(item,[0]*20)
                D[item][row]+=1
        inFile.close()

    ouFile = open('delly.1.sv.stat.exon.symbol.heatmap','w') 
    ouFile2 = open('delly.1.sv.stat.exon.symbol.heatmap2','w') 
    for k in D : 
        ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]])+'\n')

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
    for i in range(len(geneList)):
        ouFile2.write(geneList[i]+'\t'+'\t'.join([str(x) for x in LD[i]])+'\n')
    ouFile2.close()
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=[6,8])

gene_heatmap(['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'delly.exon.heatmap.pdf')


