inFile = open('tandem.peptides')
ouFile1 = open('tandem.peptides.is_stopgain_not_uniprot', 'w')
ouFile2 = open('tandem.peptides.is_stopgain_is_uniprot', 'w')
ouFile3 = open('tandem.peptides.not_stopgain_is_uniprot', 'w')
ouFile4 = open('tandem.peptides.not_stopgain_not_uniprot', 'w')
ouFile5 = open('tandem.peptides.is_reverse','w')
for line in inFile:

    if line.find('REVERSE')==-1:
        if line.find('StopGain')!=-1 and line.find('Uniprot')==-1:
            ouFile1.write(line)
        elif line.find('StopGain')==-1 and line.find('Uniprot')==-1:
            ouFile4.write(line)
        elif line.find('StopGain')!=-1 and line.find('Uniprot')!=-1:
            ouFile2.write(line)
        elif line.find('StopGain')==-1 and line.find('Uniprot')!=-1:
            ouFile3.write(line)
    else:
        ouFile5.write(line)

inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()
ouFile5.close()
