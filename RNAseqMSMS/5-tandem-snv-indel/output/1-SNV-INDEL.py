inFile = open('snv-indel.peptides')
ouFile = open('snv-indel.peptides.filtered','w')
for line in inFile:
    line = line.strip()
    if line.find('SNV:')!=-1 and line.find('ENSP')==-1:
        ouFile.write(line+'\n')
inFile.close()
ouFile.close()
