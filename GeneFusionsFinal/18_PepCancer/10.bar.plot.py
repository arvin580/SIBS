from PyPlot.PyPlotClass import *

ADC=[]
SCC=[]
Normal=[]
sym=[]
inFile=open('Tandem.Omssa.FDR.pep.genefusions.splicing.final.pos.3.3.spec2.num.omssa')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ADC.append(int(fields[2]))
    SCC.append(int(fields[3]))
    Normal.append(int(fields[4]))
    sym.append(fields[1])

inFile.close()


pp=PyPlot('Omssa.Pep.Distribution.ADC.SCC.Normal.pdf')
pp.multi_bar_vertical_xlael_vertical([ADC,SCC,Normal],sym,legTitle=['ADC','SCC','Normal'])



