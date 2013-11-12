import os
DIR = 'output-second'
ouFile = open('Peptides-Identified-Second', 'w')
D = {}
Fs = os.listdir(DIR)
for F in Fs:
    #if F[-4:] == '.fdr':
    if F[-4:] == '.txt':
        inFile = open(DIR + os.sep + F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if len(fields) > 4:
                protein = fields[1]
                peptide = fields[4]
                if protein.find('REVERSE') == -1 and peptide.find(':') == -1:
                    D.setdefault(peptide, [])
                    D[peptide].append(protein)
        inFile.close()

for k in D:
#    ouFile.write('>' + '\t'.join(set(D[k])) + '\n')
    ouFile.write(k + '\n')

ouFile.close()
