inFile = open('potential_fusion.txt')
D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()
    if line1:
        fields = line1.split()
        D.setdefault(fields[0], 0)
        D[fields[0]]+=1
    else:
        break
inFile.close()
for k in D:
    print(k)
    print(D[k])

D['ICC4A']=D['sample_C4A']
D['ICC4B']=D['sample_C4B']
D['ICC5A']=D['sample_C5A']
D['ICC5B']=D['sample_C5B']
D['ICC9A']=D['sample_C9A']
D['ICC9B']=D['sample_C9B']
D['ICC10A']=D['sample_C10A']
D['ICC10B']=D['sample_C10B']
D['CHC5A']=D['sample_M5A']
D['CHC5B']=D['sample_M5B']
D['CHC6A']=D['sample_M6A']
D['CHC6B']=D['sample_M6B']
D['CHC7A']=D['sample_M7A']
D['CHC7B']=D['sample_M7B']
D['CHC10A']=D['sample_M10A']
D['CHC10B']=D['sample_M10B']

Data=[[D['ICC4A'],D['ICC5A'],D['ICC9A'],D['ICC10A'],D['CHC5A'],D['CHC6A'],D['CHC7A'],D['CHC10A']],[D['ICC4B'],D['ICC5B'],D['ICC9B'],D['ICC10B'],D['CHC5B'],D['CHC6B'],D['CHC7B'],D['CHC10B']]]


from PyPlot.PyPlotClass import *
pp=PyPlot('RNAseq.number.pdf')
pp.multi_bar_vertical(Data,legTitle=['Tumor','Normal'],xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],legX=0.98, legY=0.98)
