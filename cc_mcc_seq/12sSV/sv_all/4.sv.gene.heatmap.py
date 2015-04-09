from PyPlot.PyPlotClass import *
files = ['invy.1.sv.stat.exon.symbol','duppy.1.sv.stat.exon.symbol','jumpy.1.sv.stat.exon.symbol','delly.1.sv.stat.exon.symbol']
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
                D.setdefault(item,[0]*12)
                D[item][row]+=1
        inFile.close()

    ouFile = open('12s.sv.exome','w') 
    for k in D :
        ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]])+'\n')

    ######
    D['DISC1']=D['DISC1/TSNAX-DISC1']
    D['FN1']=D['FN1/ABCA12/BARD1/ATIC']
    D['CYP2B6']=D['CYP2B6/CYP2B7P1/CYP2A7/CYP2G1P/CYP2A13/CYP2A6/CYP2F1']
    D['TIGIT']=D['TIGIT/QTRTD1/ZBTB20/DRD3/MIR568/ZNF80/KIAA1407/ZBTB20-AS1']
    D['IFNA10']=D['IFNA10/IFNA7/IFNA21/IFNA17/IFNW1/IFNA16/IFNA14/IFNA4']
    D['RPL31']=D['RPL31/NPAS2/TBC1D8']
    D['PLEK2']=D['PLEK2/EIF2S1/TMEM229B']
    D['PRR7']=D['PRR7/PDLIM7/GRK6/DBN1/F12/LOC340037']
    ######
    D.pop('DISC1/TSNAX-DISC1')
    D.pop('FN1/ABCA12/BARD1/ATIC')
    D.pop('CYP2B6/CYP2B7P1/CYP2A7/CYP2G1P/CYP2A13/CYP2A6/CYP2F1')
    D.pop('TIGIT/QTRTD1/ZBTB20/DRD3/MIR568/ZNF80/KIAA1407/ZBTB20-AS1')
    D.pop('IFNA10/IFNA7/IFNA21/IFNA17/IFNW1/IFNA16/IFNA14/IFNA4')
    D.pop('RPL31/NPAS2/TBC1D8')
    D.pop('PLEK2/EIF2S1/TMEM229B')
    D.pop('PRR7/PDLIM7/GRK6/DBN1/F12/LOC340037')

    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize)

gene_heatmap(['ICC1A','ICC2A','ICC3A','ICC6A','ICC7A','ICC8A','CHC1A','CHC2A','CHC3A','CHC4A','CHC8A','CHC9A'],'sv.exon.heatmap.pdf',figsize=(8,12))


