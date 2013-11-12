import os
DIR_First = 'output-First'

DIR = 'output'
ouFile = open('Peptides-Identified-Second', 'w')
D = {}
Fs = os.listdir(DIR)
for F in Fs:
    if F[-4:] == '.fdr':
        inFile = open(DIR + os.sep + F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            protein = fields[1]
            peptide = fields[3]
            if protein.find('REVERSE') == -1:
                if protein.find('VARIATION') != -1:
                    D.setdefault(peptide, [])
                    D[peptide].append(protein)
        inFile.close()

for k in D:
    ouFile.write('>' + '+++'.join(set(D[k])) + '\n')
    ouFile.write(k + '\n')

ouFile.close()
