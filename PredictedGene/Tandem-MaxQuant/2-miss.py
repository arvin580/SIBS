inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New')
ouFile1 = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss', 'w')
ouFile2 = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-Miss', 'w')

for line in inFile:
    fields = line.split('\t')
    pep = fields[0]
    if pep[0:-1].find('K')==-1 and pep[0:-1].find('R')==-1: 
        ouFile1.write(line)
    else:
        ouFile2.write(line)
ouFile1.close()
ouFile2.close()
inFile.close()
