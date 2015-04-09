from PyPlot.PyPlotClass import *
import re
files = ['delly.1.sv.stat.gene.symbol','duppy.1.sv.stat.gene.symbol','invy.1.sv.stat.gene.symbol','jumpy.1.sv.stat.gene.symbol']
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
    ''' 
    ######
    D['MEA1']=D['MEA1/PTK7/CUL7/PPP2R5D/MRPL2/KLC4/KLHDC3/RRP36/PEX6']
    D['SLC25A21']=D['SLC25A21/LOC100129794/MIPOL1']
    D['PARVB']=D['PARVB/PARVG/KIAA1644']
    D['ALG3']=D['ALG3/MIR1224/EIF4G1/FAM131A/CLCN2/ECE2/PSMD2/SNORD66/CAMK2N2/VWA5B2']
    D['ANXA1']=D['ANXA1/ALDH1A1']
    ######
    D.pop('MEA1/PTK7/CUL7/PPP2R5D/MRPL2/KLC4/KLHDC3/RRP36/PEX6')
    D.pop('SLC25A21/LOC100129794/MIPOL1')
    D.pop('PARVB/PARVG/KIAA1644')
    D.pop('ALG3/MIR1224/EIF4G1/FAM131A/CLCN2/ECE2/PSMD2/SNORD66/CAMK2N2/VWA5B2')
    D.pop('ANXA1/ALDH1A1')
    '''
    Add = []
    Del = []
    for k in D:
        fields = re.split(r'[/:]',k)
        if len(fields)>1:
            for item in fields:
                if item!='*':
                    Add.append([item,D[k]])
            Del.append(k)

    for x in Del:
        D.pop(x)
    for x in Add:
        D[x[0]]=x[1]

    ouFile = open('16s.sv.exome.gene','w') 
    for k in D : 
        ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]])+'\n')


    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize)


    for key in D :
        print(key)

gene_heatmap(['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'sv.gene.heatmap.genename.pdf',figsize=(8,10))


