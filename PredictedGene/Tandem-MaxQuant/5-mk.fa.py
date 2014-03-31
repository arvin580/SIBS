inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation')
ouFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation.fa', 'w')
num = 0
for line in inFile:
    num += 1
    ouFile.write('>pep'+str(num)+'\n')
    ouFile.write(line)
inFile.close()
ouFile.close()
