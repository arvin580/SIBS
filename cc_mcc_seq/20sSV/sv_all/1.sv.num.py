Delly = {}
Invy = {}
Jumpy = {}
Duppy = {}

DELLY = []
INVY = []
JUMPY = []
DUPPY = []


inFile = open('delly.1.sv.stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    Delly[fields[0]]=len(fields[1:])
inFile.close()

DELLY=[Delly['ICC1A'],Delly['ICC2A'],Delly['ICC3A'],Delly['ICC4A'],Delly['ICC5A'],Delly['ICC6A'],Delly['ICC7A'],Delly['ICC8A'],Delly['ICC9A'],Delly['ICC10A'],Delly['CHC1A'],Delly['CHC2A'],Delly['CHC3A'],Delly['CHC4A'],Delly['CHC5A'],Delly['CHC6A'],Delly['CHC7A'],Delly['CHC8A'],Delly['CHC9A'],Delly['CHC10A']]


inFile = open('jumpy.1.sv.stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    Jumpy[fields[0]]=len(fields[1:])
inFile.close()

JUMPY=[Jumpy['ICC1A'],Jumpy['ICC2A'],Jumpy['ICC3A'],Jumpy['ICC4A'],Jumpy['ICC5A'],Jumpy['ICC6A'],Jumpy['ICC7A'],Jumpy['ICC8A'],Jumpy['ICC9A'],Jumpy['ICC10A'],Jumpy['CHC1A'],Jumpy['CHC2A'],Jumpy['CHC3A'],Jumpy['CHC4A'],Jumpy['CHC5A'],Jumpy['CHC6A'],Jumpy['CHC7A'],Jumpy['CHC8A'],Jumpy['CHC9A'],Jumpy['CHC10A']]

inFile = open('invy.1.sv.stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    Invy[fields[0]]=len(fields[1:])
inFile.close()

INVY=[Invy['ICC1A'],Invy['ICC2A'],Invy['ICC3A'],Invy['ICC4A'],Invy['ICC5A'],Invy['ICC6A'],Invy['ICC7A'],Invy['ICC8A'],Invy['ICC9A'],Invy['ICC10A'],Invy['CHC1A'],Invy['CHC2A'],Invy['CHC3A'],Invy['CHC4A'],Invy['CHC5A'],Invy['CHC6A'],Invy['CHC7A'],Invy['CHC8A'],Invy['CHC9A'],Invy['CHC10A']]

inFile = open('duppy.1.sv.stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    Duppy[fields[0]]=len(fields[1:])
inFile.close()

DUPPY=[Duppy['ICC1A'],Duppy['ICC2A'],Duppy['ICC3A'],Duppy['ICC4A'],Duppy['ICC5A'],Duppy['ICC6A'],Duppy['ICC7A'],Duppy['ICC8A'],Duppy['ICC9A'],Duppy['ICC10A'],Duppy['CHC1A'],Duppy['CHC2A'],Duppy['CHC3A'],Duppy['CHC4A'],Duppy['CHC5A'],Duppy['CHC6A'],Duppy['CHC7A'],Duppy['CHC8A'],Duppy['CHC9A'],Duppy['CHC10A']]

print(JUMPY)
print(DELLY)
print(INVY)
print(DUPPY)




from PyPlot.PyPlotClass import *
pp=PyPlot('sv.number.pdf')
#pp.multi_bar_vertical(Data,legTitle=['Tumor','Normal'],xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],legX=0.85, legY=0.98)
pp.single_bar_multi_bar_vertical_sv(DELLY,[DUPPY,INVY,JUMPY],xLabel=['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],legTitle=['Deletion','Duplication','Inversion','Translocation'])
