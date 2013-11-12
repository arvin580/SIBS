import os
Spec = {}
inFile = open('Peptides-Identified-First-Spec')
for line in inFile:
    line = line.strip()
    Spec[line] = 1
inFile.close()
    

DIR = 'output'
ouFile = open('Peptides-Identified-Second-unSpec', 'w')
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
            sc = fields[0]
            if sc not in Spec:
                if protein.find('REVERSE') == -1:
                    if protein.find('VARIATION') != -1:
                        D.setdefault(peptide, [])
                        D[peptide].append(protein + '&&&' + sc)
        inFile.close()

for k in D:
    ouFile.write('>' + '+++'.join(set(D[k]))+ '\n')
    ouFile.write(k + '\n')

ouFile.close()
