inFile = open('CodonUsage')
ouFile = open('CodonUsage.acid2', 'w')
D = dict()
for line  in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[1]
inFile.close()

stops = []
for k in D:
    if D[k] == 'K' or D[k]=='R':
        stops.append(k)

D2 = {}
D2['A'] = ['T', 'C', 'G']
D2['T'] = ['A', 'C', 'G']
D2['C'] = ['A', 'T', 'G']
D2['G'] = ['A', 'T', 'C']


D3 = {}
D4 = {}
for codon in stops:
    for i,item in enumerate(codon):
        if i == 0:
            for x in D2[item]:
                D3[x+codon[1]+codon[2]]=1
        if i == 1:
            for x in D2[item]:
                D3[codon[0]+x+codon[2]]=1
        if i == 2:
            for x in D2[item]:
                D3[codon[0]+codon[1]+x]=1

for k in D3:
    if k in D:
        D4[D[k]]=1

for k in D4:
    ouFile.write(k + '\n')





