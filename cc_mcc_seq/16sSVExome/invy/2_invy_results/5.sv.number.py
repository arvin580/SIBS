D = dict()
inFile = open('1.sv.stat')
for line in inFile:
    line = line.strip()
    fields =line.split('\t')
    D[fields[0]] = len(fields[1:])
inFile.close()

for key in D :
    print(key)
    print(D[key])

Data=[[D['ICC4A'],D['ICC5A'],D['ICC9A'],D['ICC10A'],D['CHC5A'],D['CHC6A'],D['CHC7A'],D['CHC10A']],[D['ICC4B'],D['ICC5B'],D['ICC9B'],D['ICC10B'],D['CHC5B'],D['CHC6B'],D['CHC7B'],D['CHC10B']]]


from PyPlot.PyPlotClass import *
pp=PyPlot('delly.number.pdf')
pp.multi_bar_vertical(Data,legTitle=['Tumor','Normal'],xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],legX=0.85, legY=0.98)

