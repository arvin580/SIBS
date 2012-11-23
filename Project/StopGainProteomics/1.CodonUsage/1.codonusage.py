inFile = open('CodonUsage')
D = dict()
for line  in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[1]
inFile.close()

stops = []
for k in D:
    if D[k] == '*':
        stops.append(k)

D2 = {}
D2['A'] = ['T', 'C', 'G']
D2['T'] = ['A', 'C', 'G']
D2['C'] = ['A', 'T', 'G']
D2['G'] = ['A', 'T', 'C']

for codon in stops:
    for i,item in enumerate(codon):
        if i == 0:
            for x in D2[item]:
                print(x+codon[1]+codon[2])
        if i == 1:
            for x in D2[item]:
                print(codon[0]+x+codon[2])
        if i == 2:
            for x in D2[item]:
                print(codon[0]+codon[1]+x)



