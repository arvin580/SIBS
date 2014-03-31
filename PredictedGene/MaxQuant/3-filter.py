D = {}
inFile = open('../Homo_sapiens.GRCh37.75.pep.all.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()

inFile = open('../human_uniprot_sprot_2014_03_10.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()

inFile = open('HeLa-Peptide-PREDICTED')
ouFile1 = open('HeLa-Peptide-Predicted-MaxQuant-pep-Known', 'w')
ouFile2 = open('HeLa-Peptide-Predicted-MaxQuant-pep-New', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[2]
    flag = 0
    for k in D:
        if pep in D[k]:
            ouFile1.write(line + '\t' + k + '\t' + D[k] + '\n')
            flag = 1
    if flag == 0:
        ouFile2.write('\t'.join(fields[2:]) + '\n')
inFile.close()

ouFile1.close()
ouFile2.close()
