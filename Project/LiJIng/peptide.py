inFile = open('cell_peptide.fasta')
ouFile = open('cell_peptide.fa', 'w')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        ouFile.write(line1)
        ouFile.write(line2.lstrip('>'))
    else:
        break
inFile.close()
ouFile.close()
