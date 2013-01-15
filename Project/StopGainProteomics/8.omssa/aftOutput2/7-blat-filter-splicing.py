inFile = open('dna_protein_out1.anno')
con = inFile.read()
inFile.close()

inFile = open('3-stopgain-protein-unique2-filtered.blated.filtered3')
ouFile = open('3-stopgain-protein-unique2-filtered.blated.filtered3.splicing','w')
ouFile2 = open('3-stopgain-protein-unique2-filtered.blated.filtered3.splicing.not','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0].split(':')[1]
    if con.find(pep)!=-1:
        ouFile.write(line+'\n')
    else:
        ouFile2.write(line+'\n')

inFile.close()
ouFile.close()
ouFile2.close()
