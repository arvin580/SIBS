from PyPlot.PyPlotClass import *

def box_plot(iFile,xLabel) :
    pp=PyPlot()
    inFile=open(iFile)
    head=inFile.readline()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        pp.filename=iFile+'.'+fields[0]+'.pdf'
        group1=[int(x) for x in fields[-8:-4]]
        group2=[int(x) for x in fields[-4:]]
        pp.box_plot([group1,group2],[xLabel[0]+':'+fields[0],xLabel[1]+':'+fields[0]])

    inFile.close()


box_plot('SNV.genome.somatic.distribution',['ICC','CHC'])
