D = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n = sum([int(x) for x in fields[1:]])
    D.setdefault(n, 0)
    D[n] += 1
inFile.close()
for x in D:
    print(str(x)+'\t'+str(D[x]))

print('########################')

D2 = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n = sum([int(x) for x in fields[1:]])
    D2.setdefault(n, 0)
    D2[n] += 1
inFile.close()
for x in D2:
    print(str(x)+'\t'+str(D2[x]))

from PyPlot.PyPlotClass import *
a=PyPlot('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation2.pdf')
a.single_bar([D[3],D[2],D[1]],['3-Types','2-Types','1-Type'])

a=PyPlot('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation.pdf')
a.single_bar([D2[6],D2[5],D2[4],D2[3],D2[2],D2[1]],['6-Types','5-Types','4-Types','3-Types','2-Types','1-Type'])

