from PyPlot.PyPlotClass import *

a=PyPlot('genefusions.pdf')
Tandem=[]
Omssa=[]
inFile=open('Tandem.FDR.pep.genefusions.final.pos.3.3')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Tandem.append(fields[0])
inFile.close()

inFile=open('Omssa.FDR.pep.genefusions.final.pos.3.3')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Omssa.append(fields[0])
inFile.close()

a.venn_diagram([Tandem,Omssa],'x!tandem','omssa')


a=PyPlot('splicing.pdf')
Tandem=[]
Omssa=[]
inFile=open('Tandem.FDR.pep.splicing.final.pos.3.3')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Tandem.append(fields[0])
inFile.close()

inFile=open('Omssa.FDR.pep.splicing.final.pos.3.3')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Omssa.append(fields[0])
inFile.close()

a.venn_diagram([Tandem,Omssa],'x!tandem','omssa')

a=PyPlot('annotated.pdf')
Tandem=[]
Omssa=[]
inFile=open('Tandem.FDR.pep.annotated.final')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Tandem.append(fields[0])
inFile.close()

inFile=open('Omssa.FDR.pep.annotated.final')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    Omssa.append(fields[0])
inFile.close()

a.venn_diagram([Tandem,Omssa],'x!tandem','omssa')
