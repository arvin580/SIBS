D = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n = sum([int(x) for x in fields[1:]])
    D.setdefault(n, [])
    D[n].append(fields[0])
inFile.close()
for x in D:
    print(str(x)+'\t'+str(len(D[x])))

print('########################')

D2 = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n = sum([int(x) for x in fields[1:]])
    D2.setdefault(n, [])
    D2[n].append(fields[0]) 
inFile.close()
for x in D2:
    print(str(x)+'\t'+str(len(D2[x])))

print('####################')
print('\n'.join(D[6]))

def plot():
    from PyPlot.PyPlotClass import *
    a=PyPlot('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation.pdf')
    a.single_bar([len(D[6]),len(D[5]),len(D[4]),len(D[3]),len(D[2]),len(D[1])],['6-Types','5-Types','4-Types','3-Types','2-Types','1-Type'])

    a=PyPlot('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation2.pdf')
    a.single_bar([len(D2[3]),len(D2[2]),len(D2[1])],['3-Types','2-Types','1-Type'])

#plot()

