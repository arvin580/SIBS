from PyPlot.PyPlotClass import *

def dist(xList,yList):
    s = 0
    for i in range(len(xList)):
        s += abs(xList[i] - yList[i])
    return s
        
def dp_heatmap(inF,D):
    inFile = open(inF)
    dp = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        x = []
        y = []
        z = []
        for item in fields[-16:]:
            d = int(item.split(':')[2])
            #if d<=D:
            #    x.append(d)
            #else:
            #    x.append(d)
            if D == 0:
                x.append(d)
            else:
                if d <=D:
                    x.append(0)
                else:
                    x.append(d)
                    
        for i in range(8):
            y.append(x[i])
            y.append(x[i+8])
        dp.append(y)
            
    inFile.close()
    
    pp=PyPlot(inF+'.'+str(D)+'.dp.heatmap.pdf')
    xLabel=['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B',
            'CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B']
    pp.heatmap(dp,row=False,col=False,xLabel=xLabel)


dp_heatmap('sum_snv16s.exome_summary',0)
dp_heatmap('sum_snv16s.exome_summary',3)
dp_heatmap('sum_snv16s.exome_summary',5)
dp_heatmap('sum_snv16s.genome_summary',0)
dp_heatmap('sum_snv16s.genome_summary',3)
dp_heatmap('sum_snv16s.genome_summary',5)
