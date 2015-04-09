### python 5.sv.number.py  *.repeat

import sys
D = dict()
D2 = dict()

for inF in sys.argv[1:]:
    if inF.find('is.repeat') != -1:
        sample = inF.split('.')[0]
        D[sample] = 0
        inFile = open(inF)
        for line in inFile:
            D[sample] += 1
        inFile.close()
    elif inF.find('not.repeat') != -1:
        sample = inF.split('.')[0]
        D2[sample] = 0
        inFile = open(inF)
        for line in inFile:
            D2[sample] += 1
        inFile.close()


for key in D :
    print(key)
    print(D[key])
for key in D2 :
    print(key)
    print(D2[key])

D['ICC5B']=0
D2['ICC5B']=0

Data=[[D['ICC4A'],D['ICC4B'],D['ICC5A'],D['ICC5B'],D['ICC9A'],D['ICC9B'],D['ICC10A'],D['ICC10B'],D['CHC5A'],D['CHC5B'],D['CHC6A'],D['CHC6B'],D['CHC7A'],D['CHC7B'],D['CHC10A'],D['CHC10B']],[D2['ICC4A'],D2['ICC4B'],D2['ICC5A'],D2['ICC5B'],D2['ICC9A'],D2['ICC9B'],D2['ICC10A'],D2['ICC10B'],D2['CHC5A'],D2['CHC5B'],D2['CHC6A'],D2['CHC6B'],D2['CHC7A'],D2['CHC7B'],D2['CHC10A'],D2['CHC10B']]]

from PyPlot.PyPlotClass import *
pp=PyPlot('paired.trans.repeat.number.pdf')
pp.multi_bar_vertical_sv_number(Data,legTitle=['in repeat region','not in repeat region'],xLabel=['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],legX=0.85, legY=0.98)
